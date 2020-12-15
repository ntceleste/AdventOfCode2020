# Python3 program to print Nth 
# term of Van Eck's sequence 
MAX = 3000
turns = [0, 3, 6]
sequence = turns + [0] * (MAX + 1)


# Utility function to compute 
# Van Eck's sequence 
def vanEckSequence():

    # Initialize sequence array 
#    for i in range(MAX):
#        sequence[i] = 0

    # Loop to generate sequence 
    for i in range(MAX):

        # Check if sequence[i] has occured 
        # previousely or is new to sequence 
        for j in range(i - 1, -1, -1):
            if (sequence[j] == sequence[i]):

                # If occurrence found 
                # then the next term will be 
                # how far back this last term 
                # occured previousely 
                sequence[i + 1] = i - j
                break


# Utility function to return 
# Nth term of sequence 
def getNthTerm(n):

    return sequence[n]


# Driver code 
if __name__ == "__main__":

    # Pre-compute Van Eck's sequence 
    vanEckSequence()

    n = 6

    # Print nth term of the sequence 
    print(getNthTerm(n))

    n = 2020

    # Print nth term of the sequence 
    print(getNthTerm(n))

# This code is contributed by kanugargng 

