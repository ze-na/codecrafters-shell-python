import sys
import os

BUILDINS = ["exit", "echo", "type"]
PATH = os.environ.get("PATH", "")
PATHSEP = os.pathsep


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit":
            break
        elif command.startswith("echo "):
            print(command[5:])
        elif command.startswith("type "):
            cmd = command[5:]
            if cmd in BUILDINS:
                print(f"{cmd} is a shell builtin")
            elif PATH:
                for dir in PATH.split(os.pathsep):
                    full_path = os.path.join(dir, cmd)
                    print(full_path)
                    while True:
                        input()
                    if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        print(f"{cmd} is {full_path}")
                        break
                else:
                    print(f"{cmd}: not found")
            else:
                print(f"{cmd}: not found")
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
