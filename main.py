# python3
import sys
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    # return (left + right) in ["()", "[]", "{}"]
    # print("INSIDE THE FUNCTION:")
    lef = left.char
    righ = right.char
    # print("LEFT: ", type , "  RIGHT: ", c)
    if (lef == '[' and righ == ']'):
      return True
    if (lef == '{' and righ == '}'):
      return True
    if (lef == '(' and righ == ')'):
      return True
    return False


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i+1))
            # pass

        if next in ")]}":
            if(not opening_brackets_stack or not are_matching(opening_brackets_stack[len(opening_brackets_stack)-1], Bracket(next,i+1))):
                # print(i+1)
                return i+1
                # sys.exit(0)
            opening_brackets_stack.pop()
            # pass
    return opening_brackets_stack


def main():
    firstInput = input()
    # if(firstInput=='I'):
    if "I" in firstInput:
            text = input()
            mismatch = find_mismatch(text)
            # Printing answer, write your code here
            if(not mismatch):    
                print("Success")
            else:
                print(mismatch)
        


if __name__ == "__main__":
    main()
