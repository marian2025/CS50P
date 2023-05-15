def main():
    coke = 50

    while coke > 0:
        print(f"Amount Due: {coke}")
        coin = int(input("Insert coin: "))

        if coin == 5 or coin == 10 or coin == 25:
            coke = coke - coin

    if coke <= 0:
        print(f"Change Owed: {-coke}")

main()