import requests

response = requests.get("https://api.example.com/students")

if response.status_code == 200:
    print("API Working Fine")
else:
    print("Error in API")
