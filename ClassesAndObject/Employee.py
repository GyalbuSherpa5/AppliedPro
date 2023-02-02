def initialInformation():
    n = int(input("enter the number of staff: "))
    staff_data = {}

    for i in range(n):
        staff_data[i+1] = {}

        staff_data[i+1]['name'] = input(f"Enter the name of staff[{i+1}]")
        staff_data[i+1]['address'] = input(f"Enter the address of staff[{i+1}]")
        staff_data[i+1]['email'] = input(f"Enter the email of staff[{i+1}]")
        monthly_income = int(input(f"Enter the monthly income of staff[{i+1}]"))
        staff_data[i+1]['Annual_income'] = monthly_income*12

    print(staff_data)


initialInformation()