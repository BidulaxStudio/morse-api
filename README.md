# More API
A Flask API who converts morse to text and text to morse

### Creation :
- Created by Bidulman
- Work with Python 3+
- Uses Flask API

### Usage :
Download the repository with git :
```
git clone https://github.com/BidulaxStudio/morse-api/
```
Configure `run.py` and start the project with `python3 run.py` !

### Examples :
```
import requests

url = "http://localhost/api"

res = requests.get(url, params={'text': "I'm going to be converted !"})
print(res.text)

res = requests.get(url, params={'morse': ".. .----. --   -. --- .--   .-   ... - .-. .. -. --.   -.-.--"})
print(res.text)

res = requests.get(url, params={'text': "Is there a difference ?", 'morse': ".. ...   - .... . .-. .   .-   -.. .. ..-. ..-. . .-. . -. -.-. .   ..--.."})
print(res.text)
```

And... That's all for today !