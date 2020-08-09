import requests
access_key = '532d5495682ef1c9f006cadef3c91941'
ip = input ('enter IP address : ')
url = 'http://api.ipstack.com/{}?access_key={}'.format(ip,access_key)
response = requests.get(url)
geodata = response.json()
country_name = geodata['country_name']
country_code = geodata['country_code']
print( ' Country code of the provided IP address:{} is {}  which represents the country {}'.format(ip,country_code,country_name))
