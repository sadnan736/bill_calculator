print("Welcome to the Bill Calcutator!")


def bill_calc():
    try:
        bill = float(input("What was the total bill? ৳"))
        persons = bill_split()
        tip = tip_calc()

        per_person_pay = (bill + (bill * tip / 100)) / persons
        per_person_pay = round(per_person_pay, 2)

        print(f"Each person should pay: ৳{per_person_pay}")

    except ValueError:
        print("Please Input a valid Value")
        bill_calc()


def bill_split():
    tot_p = (input("How many people will split the bill? "))
    tot_p = 1 if tot_p == '' else int(tot_p)

    return tot_p

def tip_calc():
    i_tip = (input("How much tip would you like to give? Standard is 15% "))
    i_tip = 25 if i_tip == '' else float(i_tip)

    return i_tip


bill_calc()

