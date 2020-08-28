#!/usr/bin/python3
def multiple_returns(sentence):
    count = 0

    if sentence == "":
        return None
    for i in sentence:
        count = count + 1
    return (count, sentence[0])
