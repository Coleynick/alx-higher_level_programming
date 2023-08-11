#!/usr/bin/python3
import hidden_4 as p


def main():
    name = dir(p)
    for n in name:
        if n[:2] == "__":
            continue
        else:
            print(n)


if __name__ == "__main__":
    main()
