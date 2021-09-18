import requests

url = "http://localhost/api"

res = requests.get(url, params={'text': "I'm going to be converted !"})
print(res.text)

res = requests.get(url, params={'morse': ".. .----. --   -. --- .--   .-   ... - .-. .. -. --.   -.-.--"})
print(res.text)

res = requests.get(url, params={'text': "Is there a difference ?", 'morse': ".. ...   - .... . .-. .   .-   -.. .. ..-. ..-. . .-. . -. -.-. .   ..--.."})
print(res.text)
