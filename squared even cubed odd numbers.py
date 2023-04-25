# Bernido, Charles David P. | BSCPE 1-5
# Object Oriented Programming | Assignment 4 - Problem 4
# This program reads a text file that contains a set of numbers. Then, the even and odd numbers will be obtained from the text file. 
# The extracted even numbers will be squared and the odd numbers will be cubed. The result will be transferred to separate files.

# request for user input
def user_input():
    # open integers.txt (write)
    with open("integers.txt", 'w') as input_file1:  
        # while loop
        while True:
            try:
                # user input
                user_input = input("Enter a Number:  ")
                
                # if input is integer
                if user_input.strip().isnumeric():
                    # user input will be written to numbers.txt
                    input_file1.write(str(user_input) + '\n')
                    continue
                    """
                


                    """
            except:
                """
                """

def main():
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
                
            # else if the obtained integer is odd
            elif obtained_integer % 2 == 1:
                # obtained integer will be cubed
                cubed_odd = obtained_integer ** 3

                # cubed odd numbers will be written to double.txt
                output_cubed.write(str(cubed_odd)+ "\n")

user_input()
main()
