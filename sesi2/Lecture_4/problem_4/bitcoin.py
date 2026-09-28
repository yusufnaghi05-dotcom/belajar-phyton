import sys
import requests
import os 
api_key = os.getenv("COINCAP_API_KEY")

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
    response = requests.get(f'https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}')
    get_price = response.json()
    harga = float(get_price["data"]["priceUsd"])
    total = n * harga
    print(f"${total:,.4f}")
except ValueError:
    sys.exit("Command-line argument is not a number")
    
