# Question 1 (d)
# Corrected version of the classify_number() function.
# Three faults were removed:
#   1. missing colon after the function header
#   2. missing colon after the if condition
#   3. assignment (=) used instead of comparison (==)
# A fourth fault, the missing closing bracket on the final print() call,
# is also corrected below.

def classify_number(n):
    if n > 0:
        return "Positive"
    elif n == 0:
        return "Zero"
    else:
        return "Negative"

print(classify_number(-5))        # prints: Negative
