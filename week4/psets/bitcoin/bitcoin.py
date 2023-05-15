import json
import requests
import sys


def main():
    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
        except:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")

    # print(n)

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    o = response.json()
    # for x in o["bpi"]["USD"]:
    #     print(x)
    # print(json.dumps(r.json(), indent=2))

    price = float(o["bpi"]["USD"]["rate_float"])

    amount = n * price

    print(f"${amount:,.4f}")
    # print(o["bpi"]["USD"]["rate_float"])


main()