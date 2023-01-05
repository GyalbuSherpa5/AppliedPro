def initialDis():
    print(f"""
        Sunway Temperature Record Management System
                    Kathmandu Nepal
                    11 April 2022
""")


days = []
temp = []


def inputTemperature():
    noOfDays = int(input("How many days to record?"))
    print(f"Please enter {noOfDays} days temperature readings")
    for i in range(noOfDays):
        num = int(input(f"Temperature day [{i + 1}] = "))
        days.append(num)


def categoryCheck(days):
    cold = 0
    mid = 0
    hot = 0
    for i in days:
        if i > 85:
            temp.append("very hot")
            hot += 1
        elif 60 < i < 85:
            temp.append("Pleasent day")
            mid += 1
        else:
            temp.append("Very cold")
            cold += 1
    return cold, mid, hot


def calculationTemperature(days):
    sum = 0
    for i in days:
        sum += i

    length = len(days)

    average = sum / length

    return average


def finalDisplay():
    initialDis()
    inputTemperature()
    categoryCheck(days)
    print("Daily Temperature Report")

    for j, k in zip(days, temp):
        print(f"Temperature day[{len(days)}] = {j} {k}")

    print(calculationTemperature(days))


finalDisplay()


