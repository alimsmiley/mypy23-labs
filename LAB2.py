# Check if value is of correct type.

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Input is not a valid number. Please try again.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Input is not a valid integer. Please try again.")

# Function to calculate sequences.

def ArithmeticSequence(a1, d, n):
    return n/2 * (2 * a1 + (n-1) * d)

def GeometricSequence(g1, q, n):
    if q == 1:
        return g1 * n
    else:
        return g1 * (1 - q ** n) / (1 - q)

# Get variable from user.

print("\nData for the arithmetic sequence.\n")
a1 = get_float_input("Start value for arithmetic sequence: ")
d = get_float_input("Interval for arithmetic sequence: ")

print("\nData for the geometric sequence.\n")
g1 = get_float_input("Start value for geometric sequence: ")
q = get_float_input("Interval for geometric sequence: ")

print("\nAmount of terms in the sequence.\n")
n =  get_int_input("Amount of values in the sequences: ")

# Print which result has a higher value or if they are equal.

arithmetic_sequence_sum = ArithmeticSequence(a1, d, n)
geometric_sequence_sum = GeometricSequence(g1, q, n)

if arithmetic_sequence_sum > geometric_sequence_sum:
    print("\nThe arithmetic sequence has a higher value.", arithmetic_sequence_sum, "\n")
elif geometric_sequence_sum > arithmetic_sequence_sum:
    print("\nThe geometric sequence has a higher value.", geometric_sequence_sum, "\n")
else:
    print("\nThe values are equal.\n")

""" Code gotten from ChatGPT to understand how to check if the input value is the right type
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Input is not a valid number. Please try again.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Input is not a valid integer. Please try again.")

# Get user input for the variables
a1 = get_float_input("Start value for arithmetic sequence: ")
d = get_float_input("Interval for arithmetic sequence: ")
g1 = get_float_input("Start value for geometric sequence: ")
b = get_float_input("Interval for geometric sequence: ")
n = get_int_input("Amount of values in the sequences: ")

# Now you have valid float and integer values in the variables

"""
