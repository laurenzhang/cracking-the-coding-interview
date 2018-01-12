#!/usr/bin/env python3

"""
    balanced_brackets.py: Determine whether a string of brackets is balanced.
    View full prompt here:
    https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem
"""

def is_matched(expression):
    brackets = {
        '{': '}',
        '[': ']',
        '(': ')'
    }

    stack = []
    for bracket in list(expression):
        if bracket in brackets.keys():
            stack.append(bracket)
        elif bracket in brackets.values():
            if not stack:
                # There are no elements left in stack to match 'bracket'
                return False
            elif bracket != brackets[stack.pop()]:
                return False
        else:
            # String contains non-bracket characters
            return False

    if not stack:
        return True


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
