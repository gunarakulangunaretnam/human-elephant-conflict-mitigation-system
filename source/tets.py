import vonage

client = vonage.Client(key="2f5efac9", secret="afzYx3ojfIS32ruz")
sms = vonage.Sms(client)

responseData = sms.send_message(
    {
        "from": "Vonage APIs",
        "to": "+94740001141",
        "text": "Hello, This is Gunarakulan",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")