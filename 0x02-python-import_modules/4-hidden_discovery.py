#!/usr/bin/python3
import hidden_4 as p
def main():
    name = dir(p)
    for n in name:
        if name[0] == "__":
            return
        else:
            print(n)
