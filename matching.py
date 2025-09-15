# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: BRACE MATCHER
#
# NAME: Ryan Nelson        FIXME
# ASSIGNMENT:   Project 2: Stacks & Queues

from Stack import Stack

# Returns True if the braces match,
# & False otherwise

def matcher(str):
    stack = Stack([])
    for ch in str:
        if ch in "(,{,[":
            stack.push(ch)
        elif ch in ")":
            if not stack or stack.pop() != "(":
                return False
        elif ch in "]":
            if not stack or stack.pop() != "[":
                return False
        elif ch in "}":
            if not stack or stack.pop() != "{":
                return False
    if not stack.is_empty():
        return False
    return True

def main():
    print("matcher: ", matcher("[()]"))
    print(matcher("( ( a )"))
    print(matcher("a[b]{"))
    print(matcher("({)}"))
    print(matcher("map(ke(a(4)))(b((v)))"))
    print(matcher("{ }"))
    print(matcher("map(ke(a(4)))(b((v)))"))
    print(matcher("map{key[a(4)]}{b([v])}"))
# Don't run main on import
if __name__ == "__main__":
    main()