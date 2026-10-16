def get_amount(message):
    """Get a valid non-negative amount from the user."""
    while True:
        try:
            amount = float(input(message))
            if amount < 0:
                print("Amount cannot be negative. Try again.")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number.")


def calculate_salary():
    print("=" * 40)
    print("       EMPLOYEE SALARY CALCULATOR")
    print("=" * 40)

    # Employee details
    employee_id = input("Enter Employee ID: ")
    employee_name = input("Enter Employee Name: ")

    # Salary components
    basic_salary = get_amount("Enter Basic Monthly Salary: ₹")
    hra = get_amount("Enter House Rent Allowance (HRA): ₹")
    other_allowances = get_amount("Enter Other Allowances: ₹")
    bonus = get_amount("Enter Bonus: ₹")

    # Deduction rates
    pf_rate = get_amount("Enter PF Deduction Rate (%): ")
    tax_rate = get_amount("Enter Income Tax Rate (%): ")

    if pf_rate > 100 or tax_rate > 100:
        print("Error: Deduction rates cannot exceed 100%.")
        return

    # Salary calculations
    gross_salary = (
        basic_salary + hra + other_allowances + bonus
    )

    pf_deduction = basic_salary * pf_rate / 100
    tax_deduction = gross_salary * tax_rate / 100

    total_deductions = pf_deduction + tax_deduction
    net_salary = gross_salary - total_deductions

    # Display salary slip
    print("\n" + "=" * 40)
    print("             SALARY SLIP")
    print("=" * 40)

    print(f"Employee ID   : {employee_id}")
    print(f"Employee Name : {employee_name}")

    print("-" * 40)
    print("EARNINGS")
    print("-" * 40)
    print(f"Basic Salary      : ₹{basic_salary:,.2f}")
    print(f"HRA               : ₹{hra:,.2f}")
    print(f"Other Allowances  : ₹{other_allowances:,.2f}")
    print(f"Bonus             : ₹{bonus:,.2f}")

    print("-" * 40)
    print(f"Gross Salary      : ₹{gross_salary:,.2f}")

    print("\nDEDUCTIONS")
    print("-" * 40)
    print(f"PF Deduction      : ₹{pf_deduction:,.2f}")
    print(f"Income Tax        : ₹{tax_deduction:,.2f}")
    print(f"Total Deductions  : ₹{total_deductions:,.2f}")

    print("=" * 40)
    print(f"NET MONTHLY SALARY: ₹{net_salary:,.2f}")
    print("=" * 40)

    print(f"Annual Net Salary : ₹{net_salary * 12:,.2f}")


# Run the calculator
calculate_salary()
