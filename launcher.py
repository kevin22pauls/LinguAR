"""LinguAR launcher — kills any existing server on the port, starts fresh, and opens the browser."""

import os
import subprocess
import sys
import threading
import time
import webbrowser

PORT = 8000
URL = f"http://localhost:{PORT}"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VENV_PYTHON = os.path.join(SCRIPT_DIR, ".venv", "Scripts", "python.exe")
LOCK_FILE = os.path.join(SCRIPT_DIR, ".launcher.pid")

if not os.path.exists(VENV_PYTHON):
    print(f"ERROR: venv not found at {VENV_PYTHON}")
    print("Run: py -3.11 -m venv .venv && .venv\\Scripts\\pip install -r requirements.txt")
    sys.exit(1)


def kill_existing():
    """Kill previous launcher and any process on the port."""
    # Kill previous launcher process via PID file
    if os.path.exists(LOCK_FILE):
        try:
            with open(LOCK_FILE) as f:
                old_pid = f.read().strip()
            if old_pid:
                print(f"Stopping previous launcher (PID {old_pid})...")
                subprocess.run(
                    ["taskkill", "/F", "/T", "/PID", old_pid],
                    capture_output=True,
                )
        except Exception:
            pass

    # Kill anything still listening on the port
    try:
        result = subprocess.run(
            ["netstat", "-ano"],
            capture_output=True, text=True,
        )
        killed = set()
        for line in result.stdout.splitlines():
            if f":{PORT}" in line and "LISTENING" in line:
                pid = line.strip().split()[-1]
                if pid not in killed:
                    print(f"Killing process on port {PORT} (PID {pid})...")
                    subprocess.run(["taskkill", "/F", "/T", "/PID", pid], capture_output=True)
                    killed.add(pid)
    except Exception as e:
        print(f"Warning: could not check for existing processes: {e}")

    time.sleep(0.5)


def write_pid():
    """Write current PID so the next launch can kill us."""
    with open(LOCK_FILE, "w") as f:
        f.write(str(os.getpid()))


def open_browser():
    """Wait for the server to actually respond, then open the browser."""
    import urllib.request
    print("Waiting for server to start...")
    for i in range(120):
        time.sleep(2)
        try:
            urllib.request.urlopen(URL, timeout=2)
            print(f"Server ready after ~{i*2}s — opening browser.")
            webbrowser.open(URL)
            return
        except Exception:
            if i % 5 == 4:
                print(f"  Still waiting... ({i*2}s elapsed)")
    print("WARNING: server did not become ready in time, open manually:", URL)


if __name__ == "__main__":
    kill_existing()
    write_pid()
    threading.Thread(target=open_browser, daemon=True).start()
    try:
        subprocess.run(
            [VENV_PYTHON, "-m", "uvicorn", "backend.main:app", "--port", str(PORT), "--reload"],
            cwd=SCRIPT_DIR,
        )
    finally:
        # Clean up PID file on exit
        try:
            os.remove(LOCK_FILE)
        except OSError:
            pass
