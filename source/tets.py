import requests

url = "https://send.lk/sms/send.php"
params = {
    "token": "1100|cJqH5b1Un4bpkkYYLu85gi9Tja5NezyZOkP7ekpm",
    "to": "0740001141",
    "from": "HECMS",
    "message": "Hello"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print("SMS sent successfully")
else:
    print("Failed to send SMS")
