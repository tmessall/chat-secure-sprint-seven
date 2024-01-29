import json
import urllib
import base64
import requests

# The IP address should be the address of the machine where the server is running.
server_url = 'http://127.0.0.1:6969/nao?image_data=%s'

# Here, we're sending a simple dictionary as data.
data_to_send = {
    'key1': 'value1',
    'key2': 'value2'
}


#Convert the dictionary to a JSON string before sending.
#json_data = json.dumps(data_to_send)

# Create the request object with the server URL and the JSON data as the body.
#req = urllib.Request(server_url, json_data, headers={'Content-Type': 'application/json'})

req = requests.post(url=server_url, json={'image_data':data_to_send})

print(req.status_code)
# Make the POST request and get the response.
#response = urllib.urlopen(req)

# Read the response
#response_text = response.read()

# Print the response text (or perform any other necessary actions)
#print(response_text)