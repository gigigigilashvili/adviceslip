import requests
import json
from win10toast import ToastNotifier

response = requests.get(f'https://api.adviceslip.com/advice')
print(response)
print(response.headers)
print(response.status_code)
result = response.json()
print(result)
text = response.text
print(json.dumps(result, indent=4))
with open('advice.json', 'w') as file:
    file.write(response.text)
    json.dump(result, file, indent=4)
s = text.split(" ")
for i in range(len(s)):
    l = s[5::1]
print(l)
toaster = ToastNotifier()
toaster.show_toast('advice', l, duration=3)
