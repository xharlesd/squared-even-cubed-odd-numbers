# Bernido, Charles David P. | BSCPE 1-5
# Object Oriented Programming | Assignment 4 - Problem 4
# This program reads a text file that contains a set of numbers. Then, the even and odd numbers will be obtained from the text file. 
# The extracted even numbers will be squared and the odd numbers will be cubed. The result will be transferred to separate files.


def user_input():
    # open integers.txt (write)
    with open("integers.txt", 'w') as input_file:  
        # while loop
        while True:
            try:
                # request for user input
                user_input = int(input("Enter a Number:  "))
                
                # if input is integer
                if user_input <= 0 or user_input >= 0:
                    # user input will be written to integers.txt
                    input_file.write(str(user_input) + '\n')
                    continue

            except:
                print("Finding the square of even numbers and the cube of odd numbers.....")
                break
  
def main():
    # open integers.txt (read), double.txt(write), triple.txt(write)
    with open("integers.txt", 'r') as input_file1, open("double.txt", 'w') as output_squared1,  open("triple.txt", 'w') as output_cubed1:
        
        # read integers.txt line by line
        for line in input_file1:
            
            # convert each line from integers.txt into integer
            obtained_integer = int(line)

            # if the obtained integer is even
            if obtained_integer % 2 == 0:
                # obtained integer will be squared
                squared_even = obtained_integer ** 2
                # squared even numbers will be written to double.txt
                output_squared1.write(str(squared_even) + "\n")
                
            # else if the obtained integer is odd
            elif obtained_integer % 2 == 1:
                # obtained integer will be cubed
                cubed_odd = obtained_integer ** 3

                # cubed odd numbers will be written to double.txt
                output_cubed1.write(str(cubed_odd) + "\n")

def output():
    # open integers.txt (read), double.txt(read), triple.txt(read)
    with open("integers.txt", 'r') as input_file2, open("double.txt", 'w') as output_squared2,  open("triple.txt", 'w') as output_cubed2:
        """"""


user_input()
main()
