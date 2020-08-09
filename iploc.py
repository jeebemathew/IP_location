import requests
access_key = '532d5495682ef1c9f006cadef3c91941'
ip = input ('enter IP address : ')
url = 'http://api.ipstack.com/{}?access_key={}'.format(ip,access_key)
response = requests.get(url)
geodata = response.json()
print(geodata['country_name'])
