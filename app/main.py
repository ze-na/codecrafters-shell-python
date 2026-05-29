import sys
import os

commands = {
    "exit": lambda line: sys.exit(0),
    "echo": lambda line: print(line[5:]),
    "type": lambda line: print(f"{args} is a shell builtin")
    if (args := "".join(line.split()[1:])) in commands
    else findDir(line[5:]) #print(f"{args}: not found") 
}

def findDir(program):
    #look through path from left to right to find program
    PATH = os.environ['PATH']
    directories = PATH.split(os.pathsep) # split with path separater
    if (program in directories): # check if program is in PATH and #execute permission boolean
        if os.access(PATH, os.X_OK):
            print(f"{program} is {PATH}")
        else:
            print(f"{program}: not found")
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