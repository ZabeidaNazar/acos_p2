import os
import sys


print(f"[Основний процес] Основний PID: {os.getpid()}")

pid = os.fork()

if pid == 0:
    print(f"[Дочірній процес] Дочірній процес PID: {os.getpid()}")
    
    os.execl("/bin/bash", "bash", "-lc", "echo '[Дочірній процес] Дочірній процес працює...'; exit 7")
    
    print("Не вдалося змінити дочірній процес")
    sys.exit(1)

else:
    print(f"Основний процес чекає на завершення дочірнього процесу з PID: {pid}...")
    
    child_pid, status = os.waitpid(pid, 0)
    
    if os.WIFEXITED(status):
        exit_code = os.WEXITSTATUS(status)
        print(f"[Основний процес] Дочірній процес з PID: {child_pid} завершився з кодом: {exit_code}")
    elif os.WIFSIGNALED(status):
        # Процес був убитий сигналом (наприклад, SIGKILL)
        signal_num = os.WTERMSIG(status)
        print(f"[Основний процес] Дочірній процес був примусово завершений сигналом: {signal_num}")
