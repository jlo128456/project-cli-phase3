#cross platform to open second console
import os
import sys
import subprocess

def open_cli():
    if sys.platform.startswith("win"):
        subprocess.Popen('start cmd /k python library.py', shell=True)
    elif sys.platform == "darwin":
        script_path = os.path.abspath("library.py")
        os.system(f'osascript -e \'tell application "Terminal" to do script "python3 {script_path}"\'')
    else:
        # Linux/WSL: Use xterm with readable font
        subprocess.Popen(['xterm', '-fa', 'Monospace', '-fs', '14', '-e', 'python3 library.py'])

open_cli()
