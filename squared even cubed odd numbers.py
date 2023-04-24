# Bernido, Charles David P. | BSCPE 1-5
# Object Oriented Programming | Assignment 4 - Problem 4
# This program reads a text file that contains a set of numbers. Then, the even and odd numbers will be obtained from the text file. 
# The extracted even numbers will be squared and the odd numbers will be cubed. The result will be transferred to separate files.

# open integers.txt (read), double.txt(write), triple.txt(write)
with open("integers.txt", 'r') as input_file, open("double.txt", 'w') as output_even,  open("triple.txt", 'w') as output_odd:
    
    # read integers.txt line by line
    for line in input_file:
        """"""
        # convert each line from integers.txt into integer
        # if the extracted number is even
            # extracted number will be squared
            # squared even numbers will be written to double.txt
        # else if the extracted number is odd
            # extracted number will be tripled
            # cubed odd numbers will be written to double.txt