# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: GENERATE BINARY NUMBER STRINGS
#
# NAME:  Ryan Nelson       FIXME
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue

# generate & return a queue of binary number strings from 1 to N
# front of queue begins @ '1', returns empty Queue otherwise

def generate_binary_numbers(N):
    numbers1 = Queue([])
    numbers = Queue([])
    numbers1.enq("1")
    for _ in range(N):
        current = numbers1.deq()
        numbers.enq(current)
        numbers1.enq(current + "0")
        numbers1.enq(current + "1")
    return numbers


def main():
    generate_binary_numbers(2).print()
    generate_binary_numbers(3).print()
    generate_binary_numbers(6).print()


# Don't run main on import
if __name__ == "__main__":
    main()