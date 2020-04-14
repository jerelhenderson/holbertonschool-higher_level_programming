#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = len(argv) - 1
    i = 1

    if args == 1:
        print ("{} argument:".format(args))
        print ("{}: {}".format(args, argv[args]))
    if args == 0:
        print ("{} arguments.".format(args))
    if args > 1:
            print ("{} arguments:".format(args))
            while i < args + 1:
                print ("{}: {}".format(i, argv[i]))
                i = i + 1
