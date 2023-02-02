#import pprint

customer_dictionary = {}


def initial_display():
    heading = '''
            Sunway College Bhatbhateni System
                  Maitidevi,Kathmandu    
    '''
    return heading


def initial_info():
    print(initial_display())
    total_keys = int(input("Enter the number of customers: "))
    for key in range(1, total_keys + 1):
        cusName = input(f"Enter name of the customer[{key}]: ")
        cusAddress = input(f"Enter address of customer[{key}]: ")
        cusEmail = input(f"Enter email of customer[{key}]: ")
        item = int(input(f"Enter the quantity of item[{key}]: "))
        itemDictionary, totalPrice = getItem(item)
        discountAmt, netAmt = dis(totalPrice)
        customer_dictionary["Customer " + str(key)] = {
            "About": {"Customer_name": cusName, "Customer_address": cusAddress, "Customer_email": cusEmail},
            "Item_Detail": itemDictionary, "Regular_Price": totalPrice, "Discount": discountAmt, "Net_Price": netAmt}


def getItem(num):
    total_price = 0
    item_dictionary = {}
    for j in range(num):
        itemName = input(f"Enter the name of item [{j + 1}]: ")
        unit = int(input(f"Enter Number of item [{j + 1}] : "))
        cost = int(input(f"Enter price of item [{j + 1}] : "))
        print()
        totalCost = unit * cost
        total_price += totalCost

        item_dictionary["Item" + str(j + 1)] = {"item name": itemName, "No. of item": unit, "price": cost,
                                                "sub_total": totalCost}

    return item_dictionary, total_price


def dis(totalPrice):
    discount = 0

    if totalPrice <= 5000:
        discount += totalPrice * 0.05
    elif totalPrice <= 7000:
        discount += (5000 * 0.05) + (totalPrice - 5000) * 0.08
    elif totalPrice <= 10000:
        discount += (5000 * 0.05) + (2000 * 0.08) + (totalPrice - 7000) * 0.10
    else:
        discount += (5000 * 0.05) + (2000 * 0.08) + (3000 * 0.10) + (totalPrice - 10000) * 0.15

    netAmount = totalPrice - discount
    return discount, netAmount


def finalDisplay():
    print(initial_display())
    for i in range(len(customer_dictionary)):
        print("-----------------------------------------------------------------------------")
        print(f"""
Customer Name : {customer_dictionary["Customer " + str(i + 1)]['About']['Customer_name']}
Customer Address : {customer_dictionary["Customer " + str(i + 1)]['About']['Customer_address']}
Customer Email : {customer_dictionary["Customer " + str(i + 1)]['About']['Customer_email']}
""")
        print("{:<20} {:>10} {:>15} {:>15}".format("Item Name", "Item Price", "Item Quantity", "Total Price"))
        for j in range(len(customer_dictionary["Customer " + str(i + 1)]['Item_Detail'])):
            print("{:<20} {:>10} {:>15} {:>15}".format(
                customer_dictionary["Customer " + str(i + 1)]['Item_Detail']["Item" + str(j + 1)]['item name'],
                customer_dictionary["Customer " + str(i + 1)]['Item_Detail']["Item" + str(j + 1)]['price'],
                customer_dictionary["Customer " + str(i + 1)]['Item_Detail']["Item" + str(j + 1)]['No. of item'],
                customer_dictionary["Customer " + str(i + 1)]['Item_Detail']["Item" + str(j + 1)]['sub_total'],
            ))

        print("Regular Price: ", customer_dictionary["Customer " + str(i + 1)]['Regular_Price'])
        print("Discount: ", customer_dictionary["Customer " + str(i + 1)]['Discount'])
        print("Net Total: ", customer_dictionary["Customer " + str(i + 1)]['Net_Price'])
        print("-----------------------------------------------------------------------------")


def print_bill():
    filename = "Bill.txt"
    for i in range(len(customer_dictionary)):
        head = initial_display()
        with open(filename, 'a') as f:
            f.write(head)
            f.write(f"""
Customer Name : {customer_dictionary["Customer " + str(i + 1)]['About']['Customer_name']}
Customer Address : {customer_dictionary["Customer " + str(i + 1)]['About']['Customer_address']}
Customer Email : {customer_dictionary["Customer " + str(i + 1)]['About']['Customer_email']}

""")
            f.write("{:<20} {:>10} {:>15} {:>15}\n".format("Item Name", "Item Price", "Item Quantity", "Total Price"))
            for j in range(len(customer_dictionary["Customer " + str(i + 1)]['Item_Detail'])):
                f.write("{:<20} {:>10} {:>15} {:>15}\n".format(
                    customer_dictionary["Customer " + str(i + 1)]['Item_Detail']["Item" + str(j + 1)]['item name'],
                    customer_dictionary["Customer " + str(i + 1)]['Item_Detail']["Item" + str(j + 1)]['price'],
                    customer_dictionary["Customer " + str(i + 1)]['Item_Detail']["Item" + str(j + 1)]['No. of item'],
                    customer_dictionary["Customer " + str(i + 1)]['Item_Detail']["Item" + str(j + 1)]['sub_total'],
                ))

            f.write(f"""
            
Regular Price: {customer_dictionary["Customer " + str(i + 1)]['Regular_Price']}
Discount: {customer_dictionary["Customer " + str(i + 1)]['Discount']}
Net Total: {customer_dictionary["Customer " + str(i + 1)]['Net_Price']}
-----------------------------------------------------------------------------""")

    print("Bills generated and saved successfully.")

initial_info()
finalDisplay()
print_bill()
