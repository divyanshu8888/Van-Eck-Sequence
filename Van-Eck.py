
MAX = 100
sequence = [0] * (MAX + 1)
 
# Utility function to compute
# Van Eck's sequence
def vanEckSequence() :
 
    # Initialize sequence array
    for i in range(MAX) :
        sequence[i] = 0
 
    # Loop to generate sequence
    for i in range(MAX) :
         
        # Check if sequence[i] has occurred
        # previously or is new to sequence
        for j in range(i - 1 , -1, -1) :
            if (sequence[j] == sequence[i]) :
 
                # If occurrence found
                # then the next term will be
                # how far back this last term
                # occurred previously
                sequence[i + 1] = i - j
                break
 
# Utility function to return
# Nth term of sequence
def getNthTerm() :
 
    print( sequence)
 
# Driver code
    # Pre-compute Van Eck's sequence
vanEckSequence()
 
    # Print nth term of the sequence
getNthTerm()
