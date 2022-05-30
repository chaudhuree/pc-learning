import requests

responst = requests.get('http://www.google.com')
print(responst.status_code)
