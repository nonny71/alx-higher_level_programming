#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len_of_args = len(argv)
     sum = 0
     for i in range(1, len_of_args):
         sum += int(argv[i])
    print(sum)
