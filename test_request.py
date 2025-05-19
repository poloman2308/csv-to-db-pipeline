import requests

response = requests.post(
    "http://127.0.0.1:5000/load",
    json={"csv_path": "data/customers.csv", "table_name": "raw_customers"}
)

print(response.status_code)
print(response.json())
