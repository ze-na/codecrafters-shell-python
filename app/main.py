import sys

commands = {
    "exit": lambda line: sys.exit(0),
    "echo": lambda line: print(line[5:]),
    "type": lambda line: print(f"{args} is a shell builtin")
    if (args := "".join(line.split()[1:])) in commands
    else print(f"{args}: not found"),
}


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