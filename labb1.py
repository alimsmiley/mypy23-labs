# 2023/09/08 Laboration 1 av: Emanuel Moberg, Alim Esmaili, Carl frimert.

# Get variable from user

a1 = float(input("Start value for arithmetic sequence: "))
d = float(input("Interval for arithmetic sequence: "))
n = int(input("Amount of values in arithmetic sequence: "))

# Function to calculate the sequence

def arithmetic_sequence(a1, d, n):
    """The function for the sum of the arithmetic sequence with starting value a1, difference d, and interval n"""
    return n/2 * (2 * a1 + (n-1) * d)

# Print the result

arithmetic_sequence_result = arithmetic_sequence(a1, d, n)
print(f"This is the result of the arithmetic sequence {arithmetic_sequence_result}")

g1 = float(input("Start value for geometric sequence: "))
b = float(input("Interval for geometric sequence: "))
m = int(input("Amount of values in geometric sequence: "))

# Function to calculate the sequence

def geometric_sequence(g1, b, m):
    """The function for the sum of the geometric sequence with starting value g1, difference b, and interval m"""
    if b == 1:
        return b * n
    else:
        return g1 * (1 - b ** m) / (1 - b)

# Print the result

geometic_sequence_result = geometric_sequence(g1, b, m)
print(f"This is the result of the geometric sequence {geometic_sequence_result}")

