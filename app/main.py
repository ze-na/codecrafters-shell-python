import sys
import os
import subprocess

commands = {
    "exit": lambda line: sys.exit(0),
    "echo": lambda line: print(line[5:]),
    "type": lambda line: print(f"{args} is a shell builtin")
    if (args := "".join(line.split()[1:])) in commands
    else find_type(line[5:])
}

def run_external(line):
    input = line.split()
    program = input[0]
    found, program_path = program_found(program)
    program_composition = "./" + program
    # program_composition = "./" + program_path
    
    # program_composition = input.append(program_path)
    if found:
        # for arg in input[1:]:    
        #     program_composition = program_composition + " " + arg
        # os.subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)
     #   print(f"pprogram_compostition: {program_composition}")    
        subprocess.run(program + input[1:], capture_output=True)
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
            # print(f"{program} is {program_path}")
            return True, program_path
    else: 
        return False, program_path
        # print(f"{program}: not found")

def find_type(program):
    found, program_path = program_found(program)
    if found:
        print(f"{program} is {program_path}")
    else:
        print(f"{program}: not found")
        
    # directories = get_path_directories()

    # for directory_path in directories:
    #     program_path = os.path.join(directory_path, program)
        
    #     if os.path.exists(program_path) and os.access(program_path, os.X_OK):
    #         print(f"{program} is {program_path}")
    #         return
    # else: 
    #     print(f"{program}: not found")
        

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
            # sys.stderr.write(f"{line}: command not found\n")


if __name__ == "__main__":
    main()