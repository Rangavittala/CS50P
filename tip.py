def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    print(dollars)
    percent = percent_to_float(input("What percentage would you like to tip? "))
    print(percent)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    d = d[1:]


    return float(d)


def percent_to_float(p):
    # TODO
    p = p[:-1]
    p = float(p)/100
    return (p)


main()