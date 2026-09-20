# Question 1 (c) (ii)
# Nested if version of the library loan-period code.
# Produces exactly the same result as the original if/elif/else chain
# for every combination of category and fines_owed.

loan_days = 0                     # default for every other case

if category == "staff":
    if fines_owed == 0:
        loan_days = 21
    else:
        if fines_owed > 0:
            loan_days = 7
else:
    if category == "student":
        if fines_owed == 0:
            loan_days = 14

print("Loan period (days):", loan_days)
