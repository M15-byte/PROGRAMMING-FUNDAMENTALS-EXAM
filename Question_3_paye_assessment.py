# Question 3
# PAYE (Pay As You Earn) assessment program.
# Built from four functions with one responsibility each:
#   (a) get_tax_rate()     - rate lookup for a monthly gross income
#   (b) enter_employees()  - validated input of names and incomes
#   (c) display_payroll()  - the PAYE table, totals and band count
#   (d) main()             - control, guarded by __name__


def get_tax_rate(income):
    """Return the PAYE rate for a monthly gross income as a decimal
    (e.g. 0.10)."""
    # Validation: a negative income is not a valid monthly income
    if income < 0:
        raise ValueError("Income cannot be negative")

    if income <= 235000:              # 0 to 235,000: tax-free
        rate = 0.0
    elif income <= 335000:            # 235,001 to 335,000: low income band
        rate = 0.10
    elif income <= 410000:            # 335,001 to 410,000: middle income band
        rate = 0.20
    else:                             # above 410,000: high income band
        rate = 0.30
    return rate


def enter_employees():
    """Collect every employee's name and validated gross monthly income."""
    names = []
    incomes = []
    count = int(input("Enter the number of employees: "))
    while len(names) < count:
        name = input(f"Name of employee {len(names) + 1}: ")
        income = -1
        while income < 0:                       # repeat until valid
            try:
                income = float(input(f"Gross monthly income of {name} (UGX): "))
            except ValueError:
                print("Enter the income as a number.")
                continue
            if income < 0:
                print("Income cannot be negative. Try again.")
        names.append(name)
        incomes.append(income)
    return names, incomes


def display_payroll(names, incomes):
    """Print the PAYE table, the totals and the size of the tax-free band."""
    total_tax = 0
    tax_free = 0
    print(f"{'Name':<18}{'Gross (UGX)':>14}{'Rate':>7}{'Tax (UGX)':>14}")
    print("-" * 53)
    for name, income in zip(names, incomes):
        rate = get_tax_rate(income)
        tax = income * rate
        total_tax += tax
        if rate == 0:
            tax_free += 1
        print(f"{name:<18}{income:>14,.0f}{rate:>7.0%}{tax:>14,.0f}")
    print("-" * 53)
    print(f"Total tax collected: UGX {total_tax:,.0f}")
    print(f"Highest income: UGX {max(incomes):,.0f}")
    print(f"Lowest income: UGX {min(incomes):,.0f}")
    print(f"Employees in the tax-free band: {tax_free}")


def main():
    """Run the PAYE assessment."""
    names, incomes = enter_employees()
    display_payroll(names, incomes)


if __name__ == '__main__':
    main()
