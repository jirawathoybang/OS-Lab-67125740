# fork_zombie.py
import os
import time
import sys

def main():
    print(f"[Parent] My PID is {os.getpid()}")
    print("[Parent] Forking a child process...")

    pid = os.fork()

    if pid > 0:
        print(f"[Parent] Created Child with PID {pid}.")
        print("[Parent] I am doing heavy ML work and forgot to call os.wait()...")
        print("[Parent] Open another terminal and run: htop (Look for 'Z' status)")
        time.sleep(60)
        print("[Parent] Waking up and exiting.")

    elif pid == 0:
        print(f"[Child] My PID is {os.getpid()}. I am finishing my task quickly!")
        sys.exit(0)

if __name__ == "__main__":
    main()