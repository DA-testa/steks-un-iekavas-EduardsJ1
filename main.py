# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i+1))
        pass
        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return i+1
            x=opening_brackets_stack.pop()
            if not are_matching(x.char,next):
                return i+1
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    return "Success"
    #pass


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
