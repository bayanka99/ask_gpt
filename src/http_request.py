import requests


url = 'http://localhost:5000/ask'


payload = {
    'question': 'what is your name?'
}


response = requests.post(url, json=payload)


print(response.status_code)  # print the status code
print(response.json())       # Print the response from the server
