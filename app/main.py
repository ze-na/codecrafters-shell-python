import sys
import os
import subprocess
import pathlib

commands = {
    "exit": lambda line: sys.exit(0),
    "echo": lambda line: print(line[5:]),
    "type": lambda line: print(f"{args} is a shell builtin")
    if (args := "".join(line.split()[1:])) in commands
    else find_type(line[5:]),
    "pwd": lambda line: print(f"{os.getcwd()}"),
    "cd": lambda line: change_dir(line[3:])
}

def change_dir(path):
    if (path == "~"):
        path = pathlib.Path.home()

    if (os.access(path = path, mode = os.F_OK)):
        os.chdir(path)
    else:
        print(f"cd: {path}: No such file or directory")

def run_external(line):
    input = line.split(" ")
    program = input[0]
    found, program_path = program_found(program)
    
    if found: 
        subprocess.run(input)
    else:    
        sys.stderr.write(f"{line}: command not found\n")        


def get_path_directories():
    return os.environ['PATH'].split(os.pathsep)
        
        
def program_found(program):
    directories = get_path_directories()
    
    program_path = ""

    for directory_path in directories:
        program_path = os.path.join(directory_path, program)
        
        if os.path.exists(program_path) and os.access(program_path, os.X_OK):
            return True, program_path
    else: 
        return False, program_path


def find_type(program):
    found, program_path = program_found(program)
    if found:
        print(f"{program} is {program_path}")
    else:
        print(f"{program}: not found")
        

def main():
    while True:
        sys.stdout.write("$ ")

        line = input()

        for command in commands:
            if line.startswith(command):
                commands[command](line)
                break
        else:
            run_external(line)


if __name__ == "__main__":
    main()