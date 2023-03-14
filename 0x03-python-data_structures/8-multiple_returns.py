#!/usr/bin/python3
def multiple_returns(sentence):
    slen = 0
    if len(sentence) == 0:
        return (0, None)
    for i in (sentence):
        slen += 1
    tuple = (slen, sentence[0])
    return (tuple)
