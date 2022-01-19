import requests

response = requests.get("http://192.168.25.44:5000/echo_call/godsaehan")

# /id/post/

response = response.text
print(response)

