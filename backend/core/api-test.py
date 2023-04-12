import requests

email = 'admin@admin.com'
password = 'pa22w0rd'

data = []
response = requests.get('http://127.0.0.1:8000/api/location')
data = response.json()

print(data)
    