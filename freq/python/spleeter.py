from os import system

def run_spleeter(filename):
    spleeter_command = f"spleeter separate -i {filename} -o spleeter-output"

    cmd_command = f'cmd /c {spleeter_command}'

    system(cmd_command)