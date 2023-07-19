#!/usr/bin/python3
import dis


def print_hidden_names():
    with open('hidden_4.pyc', 'rb') as file:
        byte = file.read()

    code = dis.Bytecode(byte)
    usrdef_names = set()

    for instr in code:
        if instr.opname == 'LOAD_NAME':
            name = instr.argval
            if not name.startswith('__'):
                usrdef_names.add(name)

    for name in sorted(usrdef_names):
        print(name)


if __name__ == "__main__":
    print_hidden_names()
