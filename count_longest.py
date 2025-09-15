# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: COUNT THE LONGEST SUBSEQUENCE
#
# NAME:  Ryan Nelson       FIXME
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue

# count longest sequence of duplicates in a queue
# can destroy the queue & make it empty
def count_longest(q):
    if q.is_empty():
        return 0
    count = 1
    len = 0
    last_char = q.deq()
    while not q.is_empty():
        for char in q.deq():
            if char == last_char:
                count += 1
            else:
                if count > len:
                    len = count
                last_char = char
                count = 1
    if count > len:
        len = count
    return len




def main():
    print("out 2:", count_longest(Queue([l for l in "hello"])))
    print("out 5:", count_longest(Queue([l for l in "m" * 5])))
    print("out 3:", count_longest(Queue([l for l in "heee" ])))
    print("out 4:", count_longest(Queue([l for l in "oooohheeee"])))
    print("out 0:", count_longest(Queue([ ])))
    print("out 1:", count_longest(Queue([l for l in "m"])))
# Don't run main on import
if __name__ == "__main__":
    main()