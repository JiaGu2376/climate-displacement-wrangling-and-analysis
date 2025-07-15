import requests
import json

url = "https://helix-tools-api.idmcdb.org/external-api/gidd/disasters/?client_id=3UR82XDHOPEU6S6J&end_year=2022&format=json&limit=15000&start_year=1990"  # replace with actual URL
response = requests.get(url)

if response.status_code == 200:
    with open("GIDDImport.json", "w") as file:
        json.dump(response.json(), file, indent=4)
    print("Data saved to GIDDImport.json")
else:
    print("Failed to fetch data:", response.status_code)
