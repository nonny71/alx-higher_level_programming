#!/usr/bin/python3
if __name__ =='__main__':
     import sys
     argv = sys.argv[1:]
     arg_count = len(argv)
     sum = 0
     index = 1
     while index <= arg_count:
         sum += int(sys.argv[index])
         index += 1
          print("{:d}".format(sum))
