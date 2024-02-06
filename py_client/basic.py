import requests

# endpoint = "http://httpbin.org/status/200"
# endpoint = "http://httpbin.org/anything"
endpoint = "http://localhost:8000/"

get_response = requests.get(endpoint)
print(get_response.text)  # print raw response
# print(get_response.json())  # print response as json
