import requests
print(requests.__version__)
r = requests.get('http://www.google.com')
print(r)
sc = requests.get('https://raw.githubusercontent.com/Matheus-Du/cmput404-lab1/main/req.py')
print(sc.text)