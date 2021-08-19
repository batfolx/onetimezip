import sys
import os


def usage():
    print("Usage: zip [input-file] [output-file]")


def compress(input_file, output_file):
    with open(output_file, 'w+') as f:
        f.write('1')

    os.remove(input_file)


def main():
    arguments = sys.argv
    if len(arguments) != 3:
        usage()
        return

    input_file = arguments[1]
    output_file = arguments[2]
    print('compressing file ...')
    compress(input_file, output_file)
    print('compressing finished')


main()
