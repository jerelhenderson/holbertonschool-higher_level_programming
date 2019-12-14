#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = len(argv) - 1

    if args is 0:
        print("{:d} arguments.".format(args))
    elif args is 1:
        print("{:d} argument:".format(args))
        print("{:d}: {:s}".format(args, argv[1]))
    elif args > 1:
        print("{:d} arguments:".format(args))
        for idx in range(1, args + 1):
            print("{:d}: {:s}".format(idx, argv[idx]))
            idx = idx + 1
