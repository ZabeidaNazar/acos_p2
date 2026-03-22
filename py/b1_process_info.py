import os
import subprocess

pid = os.getpid()
ppid = os.getppid()

print(f"PID: {pid}")
print(f"PPID: {ppid}")

ps_command = ["ps", "-o", "pid,ppid,stat,ni,comm", "-p", str(pid)]

subprocess.run(ps_command)
