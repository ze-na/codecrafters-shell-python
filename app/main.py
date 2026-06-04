import sys
import os

commands = {
    "exit": lambda line: sys.exit(0),
    "echo": lambda line: print(line[5:]),
    "type": lambda line: print(f"{args} is a shell builtin")
    if (args := "".join(line.split()[1:])) in commands
    else find_dir(line[5:])
}

def get_path_directories():
    directories = os.environ['PATH'].split(os.pathsep)
    return directories

def find_dir(program):
    directories = get_path_directories

    for directory_path in directories:
        program_path = os.path.join(directory_path, program)
        
        if os.path.exists(program_path) and os.access(program_path, os.X_OK):
            print(f"{program} is {program_path}")
            return
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
            sys.stderr.write(f"{line}: command not found\n")


if __name__ == "__main__":
    main()