import sys
import shutil


def main():
    builtin = ["echo", "exit", "type"]

    while True:
        sys.stdout.write("$ ")

        command: str = input()
        if command == "exit":
            break

        elif command.startswith("echo "):
            print(command.removeprefix("echo "))

        elif command.startswith("type "):
            bic: str = command.removeprefix("type ")
            if bic in builtin:
                print(f"{bic} is a shell builtin")
            elif shutil.which(bic):
                print(f"{bic} is {shutil.which(bic)}")
            else:
                print(f"{bic}: not found")

        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()