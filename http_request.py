import requests

# Replace this URL with the one provided by ngrok
url = 'http://127.0.0.1:5000/ask'  # Use your actual ngrok URL

# Create the payload with the question
payload = {
    'question': 'What is the capital of France?'
}

# Send the POST request
response = requests.post(url, json=payload)

# Print the response from the server
print(response.status_code)  # Print the HTTP status code
print(response.json())       # Print the JSON response from the server
