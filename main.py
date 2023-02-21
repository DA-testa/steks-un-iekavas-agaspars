# python3
import sys
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    # return (left + right) in ["()", "[]", "{}"]
    # print("INSIDE THE FUNCTION:")
    type = left.char
    c = right.char
    # print("LEFT: ", type , "  RIGHT: ", c)
    if (type == '[' and c == ']'):
      return True
    if (type == '{' and c == '}'):
      return True
    if (type == '(' and c == ')'):
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
    text = input()
    mismatch = find_mismatch(text)
    opening_brackets_stack=find_mismatch(text)
    # print("PRINTING FROM MAIN:", opening_brackets_stack)
    # Printing answer, write your code here
    if(not mismatch):    
        if(not opening_brackets_stack):
            print("Success")
        else:
            try:
                print(opening_brackets_stack[len(opening_brackets_stack)-1].position)
            except:
                sys.exit(0)
    else:
        print(mismatch)
        


if __name__ == "__main__":
    main()
