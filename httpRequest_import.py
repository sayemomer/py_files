from urllib.request import urlopen,Request

response = urlopen(Request('http://google.com'))

print(response.read())
response.close()
