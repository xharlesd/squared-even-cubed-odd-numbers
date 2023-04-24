# Bernido, Charles David P. | BSCPE 1-5
# Object Oriented Programming | Assignment 4 - Problem 4
# This program reads a text file that contains a set of numbers. Then, the even and odd numbers will be obtained from the text file. 
# The extracted even numbers will be squared and the odd numbers will be cubed. The result will be transferred to separate files.

# open integers.txt (read), double.txt(write), triple.txt(write)
with open("integers.txt", 'r') as input_file, open("double.txt", 'w') as output_squared,  open("triple.txt", 'w') as output_cubed:
    
    # read integers.txt line by line
    for line in input_file:
        
        # convert each line from integers.txt into integer
        obtained_integer = int(line)

        # if the obtained integer is even
        if obtained_integer % 2 == 0:
            # obtained integer will be squared
            squared_even = obtained_integer ** 2
            # squared even numbers will be written to double.txt
            output_squared.write(str(squared_even)+ "\n")
            
            """"""
            
        # else if the obtained integer is odd
            # obtained integer will be tripled
            # cubed odd numbers will be written to double.txt