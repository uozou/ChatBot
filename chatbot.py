import requests
from pyChatGPT import ChatGPT
import time

session_token = ''
api = ChatGPT(session_token)

#message = 
url = ("https://api.telegram.org/bot435:xxx")
#url_msg = 'https://api.telegram.org/bot435:xxx/sendMessage?chat_id=-543&text="{}"'.format(message)

api.reset_conversation()
def read_msg(offset):
  parameter = { "offset" : offset}
  resp = requests.get(url + "/getUpdates", data= parameter)
  data = resp.json()

  print(offset)
  for result in data["result"]:
    t = "text"
    Print(result)
    if t in result["message"]:
      resp = api.send_message(result["message"]["text"])
      print(resp['message'])
    
      parameters ={"chat_id" : "-543", "text" : resp['message']}
      respo = requests.get(url + "/sendMessage", data= parameters)
      time.sleep(2)
    else :
      continue
      time.sleep(1)


  if data["result"]:
    return data["result"][-1]["update_id"] + 1
  



offset = 555
while True:

  offset = read_msg(offset)
  time.sleep(1)
