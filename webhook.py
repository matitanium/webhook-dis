import requests
import sys
a = input("enter webhook url: ")
webhook = a
while True: 
    b = input("enter message")
    if b == "ex":
        sys.exit()
    data = {"username": "Bot", "content": b}
    req = requests.post(webhook, json=data)
    print(req.text)