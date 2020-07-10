import requests
response = requests.get('http://www.omdbapi.com?apikey=72bc447a&t=the+social+network').json()
print(response['Title'])
