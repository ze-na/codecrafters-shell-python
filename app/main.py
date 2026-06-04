import sys
import os

commands = {
    "exit": lambda line: sys.exit(0),
    "echo": lambda line: print(line[5:]),
    "type": lambda line: print(f"{args} is a shell builtin")
    if (args := "".join(line.split()[1:])) in commands
    else find_dir(line[5:]) #print(f"{args}: not found") 
}

def find_dir(program):
    #todo: remember the path to get to program.
    #program_path = os.pathsep
    #look through path from left to right to find program
    PATH = os.environ['PATH']
    # print(f"test, PATH = {PATH}")
    directories = PATH.split(os.pathsep) # split with path separater
    
    # for x in directories:
    #     print(f"test, directories = {x}")
        
    # if (program in directories): # check if program is in PATH and #execute permission boolean
    #     print(f"test, program = {program} programPath = {programPATH}")
    for directory_path in directories:
        # if (x == program):
        #     break
        program_path = os.path.join(directory_path, program)
        
      #  program_path = program_path + os.pathsep + directoryPath
      #  program_path = os.path.join(programPATH, directory_path)
    
        if os.path.exists(program_path) and os.access(program_path, os.X_OK):
            print(f"{program} is {program_path}")
            exit()
        # else:
        #     print(f"{program}: not found")
        #     exit()
    else: 
        # print(f"test, program = {program} flop ")
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