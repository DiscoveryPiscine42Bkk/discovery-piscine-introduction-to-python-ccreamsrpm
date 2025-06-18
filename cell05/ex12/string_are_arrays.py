import sys

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    conbined = ''.join(args)
    z_chars = [char for char in conbined if char == 'z']
    if len(z_chars) == 0:
        print("none")
    else:
        print(''.join(z_chars))