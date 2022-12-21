# Code by Gyalbu Sherpa
import os

file_Name = "output.txt"
list_Of_Staff_Info = []


def staff_Info():
    global staff_no
    staff_no = int(input("Please enter the number of staff you wanted you provide data:"))
    for i in range(staff_no):
        tempList = []
        flag = True
        print(f"Enter for the {i + 1} Staff Information ")
        staff_Name = (input(f"Enter Staff Name [{i + 1}]"))
        staff_Address = input(f"Enter Address [{i + 1}]")
        staff_Pan = input(f"Enter Pan No [{i + 1}]")
        fiscal_Year = input(f"Enter FY [{i + 1}]")
        while flag:
            married_Status = input(f"Enter ‘Y’ for Married and ‘N’ for Unmarried Status [{i + 1}]").upper()
            if married_Status == 'Y' or married_Status == 'N':
                flag = False
        staff_Income = int(input(f"Enter Staff per month income [Rs.] [{i + 1}]"))
        tempList.append(staff_Name)
        tempList.append(staff_Address)
        tempList.append(staff_Pan)
        tempList.append(fiscal_Year)
        tempList.append(married_Status)
        tempList.append(staff_Income)
        list_Of_Staff_Info.append(tempList)


def calculate_Tax_Of_Staff(married_status, income):
    if married_status == 'Y':
        tax, taxSlab = calculate_Tax_Of_Staff_Married(income)
    else:
        tax, taxSlab = calculate_Tax_Of_Staff_Unmarried(income)
    return tax, taxSlab


def calculate_Tax_Of_Staff_Married(income):
    tax = 0
    tax_Slab = ""
    if income <= 450000:
        tax += 0.01 * income
        tax_Slab += "1%"
    elif 450000 < income <= 550000:
        tax += 450000 * 0.01 + (income - 450000) * 0.1
        tax_Slab += "10%"
    elif 450000 < income <= 650000:
        tax += 450000 * 0.01 + 100000 * 0.1 + (income - 550000) * 0.2
        tax_Slab += "20%"
    elif 450000 < income <= 1000000:
        tax += 450000 * 0.01 + 100000 * 0.1 + 100000 * 0.2 + (income - 650000) * 0.3
        tax_Slab += "30%"
    elif income > 2000000:
        tax += 450000 * 0.01 + 100000 * 0.1 + 100000 * 0.2 + 0.3 * 1350000 + (income - 2000000) * 0.36
        tax_Slab += "36%"
    else:
        tax += 450000 * 0.01 + 100000 * 0.1 + 100000 * 0.2 + (income - 650000) * 0.3
        tax_Slab += "30%"
    return tax, tax_Slab


def calculate_Tax_Of_Staff_Unmarried(income):
    tax = 0
    tax_Slab = ""
    if income <= 400000:
        tax += 0.01 * income
        tax_Slab += "1%"
    elif 400000 < income <= 500000:
        tax += 400000 * 0.01 + (income - 400000) * 0.1
        tax_Slab += "10%"
    elif 400000 < income <= 600000:
        tax += 400000 * 0.01 + 100000 * 0.1 + (income - 500000) * 0.2
        tax_Slab += "20%"
    elif 400000 < income <= 1000000:
        tax += 400000 * 0.01 + 100000 * 0.1 + 100000 * 0.2 + (income - 600000) * 0.3
        tax_Slab += "30%"
    elif income > 2000000:
        tax += 400000 * 0.01 + 100000 * 0.1 + 100000 * 0.2 + 0.3 * 1300000 + (income - 2000000) * 0.36
        tax_Slab += "36%"
    else:
        tax += 400000 * 0.01 + 100000 * 0.1 + 100000 * 0.2 + (income - 600000) * 0.3
        tax_Slab += "30%"
    return tax, tax_Slab


def display_Staff_Info():
    for i in range(staff_no):
        head = display_Static_Info()
        tax, taxSlab = calculate_Tax_Of_Staff(list_Of_Staff_Info[i][4], list_Of_Staff_Info[i][5])
        body = f"""Staff Name: {list_Of_Staff_Info[i][0]}                        Address:{list_Of_Staff_Info[i][1]}
PAN No: {list_Of_Staff_Info[i][2]}              FY:{list_Of_Staff_Info[i][3]}             Married Status={list_Of_Staff_Info[i][4]}

Staff {list_Of_Staff_Info[i][0]} with PAN {list_Of_Staff_Info[i][2]} fall under {taxSlab} Tax slab 
{list_Of_Staff_Info[i][0]} (PAN {list_Of_Staff_Info[i][2]}) to pay tax to government is [Rs.]={tax}
    """
        print(head)
        print(body)
        if not os.path.exists(file_Name):
            with open(file_Name, "w") as fileWriter:
                fileWriter.write(head)
                fileWriter.write(body)
        else:
            with open(file_Name, "a") as fileWriter:
                fileWriter.write(head)
                fileWriter.write(body)


def display_Static_Info():
    temp = f"""          
            Sunway College Account Department
                Maitidevi, Kathmandu
                     Welcome to
            Salary & Tax Calculate System(STCS)
"""
    return temp


staff_Info()
display_Staff_Info()
