import sys

commands = ["help", "b", "c"]

if not sys.argv[1].startswith("--"):
    print("error, unrecognized command: '" + sys.argv[1] + "'")
    exit

command_name = sys.argv[1][2:]
# print(command_name)

match command_name:
    case "help":
        print("here be help!")
        exit
