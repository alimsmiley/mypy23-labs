# Function to get a valid float input from the user
def get_float_input(prompt):
    """This function takes care of error in type, when tpe is not float, and returns error message to try again"""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Det där var inte ett flyttal. Försök igen.")

# Function to get a valid integer input from the user
def get_int_input(prompt):
    """This function takes care of input error, when the type is not an integer, and returns an error message"""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Det där var inte ett heltal. Försök igen.")

# Get variables from user for the arithmetic sequence
print("Data for the arithmetic sequence:")
a1 = get_float_input("Start value (a1): ")
d = get_float_input("Difference (d): ")
n = get_int_input("Number of terms (n): ")

# Get variables from user for the geometric sequence
print("\nData for the geometric sequence:")
g1 = get_float_input("Start value (g1): ")
q = get_float_input("Ratio (q): ")
m = get_int_input("Number of terms (m): ")

# Function to calculate the sequence
def arithmetic_sequence(a1, d, n):
    """The function for the sum of the arithmetic sequence with starting value a1, difference d, and interval n"""
    return n/2 * (2 * a1 + (n-1) * d)

def geometric_sequence(g1, q, m):
    """The function for the sum of the geometric sequence with starting value g1, difference b, and interval m"""
    if q == 1:
        return g1 * m
    else:
        return g1 * (1 - q ** m) / (1 - q)

# Calculate the sums
arithmetic_sequence_result = arithmetic_sequence(a1, d, n)
geometric_sequence_result = geometric_sequence(g1, q, m)

# Determine which sum is greater
if arithmetic_sequence_result > geometric_sequence_result:
    print("\nThe arithmetic sum is greater.")
elif geometric_sequence_result > arithmetic_sequence_result:
    print("\nThe geometric sum is greater.")
else:
    print("\nThe sums are equal.")
