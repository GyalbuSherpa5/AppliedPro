from datetime import date

customer_name = input("Enter your name ")
address = input("Enter your address ")
unit = int(input("Enter your total unit "))

print(f"""
Sunway Int'l Electricity Bill System
        Maitidevi,Kathmandu
                    Date: {date.today()}
----------------------------------------
                      Address: {address}
""")

print(f"Customer name : {customer_name}")
print(f"Consumed Unit : {unit}")


def bill(n):
    if n <= 100:
        return None

    elif 100 < n <= 200:
        return deduct(n) * 5

    else:
        first = deduct(n)
        return deduct(first) * 10 + 100 * 5


def deduct(n):
    return n - 100


final_payment = bill(unit)


def discount(unit, final_payment):
    if unit <= 500:
        return 0
    else:
        dis = unit - 500
        dis = dis * 10
        return (10 / 100) * dis


discount = discount(unit, final_payment)
print(f"""
Total amount to pay : {final_payment}
Total discount given : {discount}
Total amount after discount : {final_payment - discount}
""")

print(f"""
{customer_name}, the customer of sunway Int'l,
Electricity billing system has to pay total
amount {final_payment - discount} got Rs.{discount} discount
""")
