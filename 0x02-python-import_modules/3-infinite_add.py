#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = len(argv) - 1
    sum = 0

    if args == 0:
        print ("0")
    else:
        if args > 0:
            for idx in range(1, args + 1):
                sum = sum + int(argv[idx])
            print("{:d}".format(sum))
