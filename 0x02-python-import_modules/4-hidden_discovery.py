#!/usr/bin/python3
import hidden_4


if __name__ in "__main__":
    dir = dir(hidden_4)
    i = 0

    for i in range(len(dir)):
        if dir[i][0] == '_' and dir[i][1] == '_':
            continue
        print(dir[i])
