import requests
import sys

url =  "https://rest.coincap.io/v3/assets/bitcoin?apiKey=eeef5d5453b68054dd0c77d68a93ba7a82b55ae056082681ffc33b9e00fe1f3b"
response = requests.get(url)
price_btc = float(response.json()["data"]["priceUsd"])

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:

    usd = float(sys.argv[1])
    if usd <= 0:
        sys.exit("Invalid number")

    print(f"${price_btc*usd:,.4f}")

except ValueError:
    sys.exit("Command-line argument is not a number")


