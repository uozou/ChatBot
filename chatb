import requests
from pyChatGPT import ChatGPT
import time

session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..RDbVU12oVwaVTAIo.rsvbrs6jzC5wCu_dRB2lGwKZtrNC_cXOZRUiC-m9nMcOB3YQyWk3YuTmcn9qLsON4vzK305UG7F6_TTCBox8PBqTl_wfB_aQ7MFV5KSAJQBYfebd6eefHsHOxXZLj2lzs-gv0tpXkalobQ2kyR1XWPigJdiJKTung9dXHX6iFiIci4uKgXWX26Pn17LilzuW5dvtHFkU48McytmEmMCIdas88Z5YxNSqoeKsieM7UEODd_xmB09Ljd98I47SpFfTBGrC2fZ_i3ImULmH_NkS8NE4tL6t4zLhvp7X2Vz0QbJEWDMJKVDUp2RVDkuWUTY0ydf2rn6_962J2nPRog7Qm4uuF8M-bD1bRzVJfU4m6Vq9-DqtKwr12ZWIHVg8l3XniFoI0VaillGOjSKsWq3Hf0HGViQ-eMBfcsPXhUQOGdNEd68IjGVJOUTw5ERUDuZChNKck6sPWF7reSBOAmFjyWkI-LBjyYgiCb7QRvzyphtDNP7yeQJRnGx3gm1s0_HQJBxpAwtdsQQLoBN9uC5JWJBwYcy5AHcLX7_rcIFn3HdV99aQleMWcrD2Zmfahk2DNNrEGzAOj2M8tGkyKF2BYNr6F0xejxBt1KbgwuoQvdcgLlzHTuYAt1ZjGFXb5pMO40w_Dgv-FNMAHeFmb5nkrOZOn_hejvOHUKA-ouVoLQ4Oe55aZWAqCCq5UPXn_M8toqziBIotzIYvHmswyY1SHurZL9yv1cQWRuVRNniogn2K3GVRyme0Pobyq9vp9VYl3c5cwkjN9dMoMGDR2fXCOy7gqULqvV2AmGvm2mqu2ukWxaLNfafNAgOuAAet5zttX7GWMdKZrz23JNsctN-L2p7lExzYk4_lWk4Oa6XrX0q0uLbDYT2WK5MMEN5PT_3M2IAQlzSEJdUF-PcB-VRvwrzFsYAGbFtE_Ci8XPuH7CX2JJSU2ytuEFJDANXJobmGv3NaAxqF_2FEcMDfaDeYv8-PpRQHDD2gBI6flBq-CssP0126zhVqf-lZ4jlPFBeewm5qa1BBe7li7C5ZZ5T-NmgDyKHxf3GQshbHgYZSIMyQS6SlGmq2svV2M_UTVE5iIvjL3umWIDM8YxESGRHdFk-S3lp6GmRoByrxc-_CwQUnMN-ZP3pHVdWzSIFKTya3pMKu_MoV920GPEUTRthUp1-mA3zKvd0eRXWwyHLAptUZ4Uh-KfDifJIkULPvEtF3iU1zE9oEvKZFdz-5zX3wIjECZ2dFbcLiLyMwJtyuaEfm7FhbvlJmRKqvbhy76Fh-zA9U-KXSLSbolw4YhbVgP7SUZkmH3Z1EWyI8J_2hO4maPKls_4HbhKorW84E2M5zrGwFPGl2InKhMRKgWeeOO_5QQt01MYyalLqH7EPhMNJdAQN0g3akTw6TDy1V02jS-oq2ssLGskrKh4k2rmTe8RwrThnuPDWMqhzgBBvas1ikWsAL0jSKC0Ugb0bSdyFH_gXe1VutotuC7UdslyMwpzYvx0n12sNV2-u-asGGZGK9BedVzZ7PnS22HpMYAilR-3zcyuGdlWm5ZMLgm1a15b639kO76QBT_ugmfjI-87rPpBgMjOsmXIOOm5YHwcdngqD1KUDeDgFBwrbCYTroFAumvfd7xx9P7HTWGs9WM_EIyoLIPqUZBUJinwf6JZPGUgeePqFsZzvfCCtxPS_AA0OrxIapM_Fzr22dtiF_fkHPo_Jo9Lo9dH2G8XZSIusskMciYTCWneJQ4nu0UrPswEO4tRMS4Qq6m06SeT2OzPzsIqC8WCfiFkDoe-20zlF_eGeH1luhkT2Ggmi4e-z-mffl7OyL0GjhWdlyZEh5CduPvJPymecyTXl8KCSr4MPV5F10myf8OOqeNUL7NJt66kdBtFAh3zejYnmTVt1oPzqroUbrtv2MA1ZuVPoNlyoLn21Pi0CDRp27NaHPYwTsT2coBfWaTg9CPm6Oq5EA3ekCHiuVDuLuxbecVvlcGdIw2aOpfi0Kah5zffe_54SRsaCg_rr_28HIi6Nmk3NnmfiUIi6b0-SbLQwhY6zWvs_8h6oOQ3VRB28v8NQXtU10QzaC-2qCbIfEJzIArrYXayetpaQwKqFEDtWEEBDKSL3QdXfVqR-bEzKICY-GGZSC1FMH-9ThgniqA8BkX5Zs_84xO2JIki-BQ70sCv-X91MGa_qsjjbpMCv5OR6_g1JJlg-J4Muh-0VeF4nHI4MARsk4CIIK8Jl70zHmP6Cf8VJ-EgPbsFdYrcfz2OSr3qqgc31tKfbnwO4uGjHQzKRVHX0NOy7CRexUsSYBfCHQ-bT0p6UjodUlgD-tAe0naYo1JWP5f975Co7L-3CzoTOxBF67rgiJswNkmi5l6iMIavloQlUyOVbZQw.GsOSLjscjdtji3BPpRSnWA'

api = ChatGPT(session_token)

#message = 
url = ("https://api.telegram.org/bot5873778396:AAGOiPTwqq03ABocRX74aqE0BcwZZIm9Kwk")
#url_msg = 'https://api.telegram.org/bot5873778396:AAGOiPTwqq03ABocRX74aqE0BcwZZIm9Kwk/sendMessage?chat_id=-867171943&text="{}"'.format(message)

api.reset_conversation()
def read_msg(offset):
  parameter = { "offset" : offset}
  resp = requests.get(url + "/getUpdates", data= parameter)
  data = resp.json()

  print(offset)
  for result in data["result"]:
    t = "text"
    if t in result["message"]:
      resp = api.send_message(result["message"]["text"])
      print(resp['message'])
    
      parameters ={"chat_id" : "-867171943", "text" : resp['message']}
      respo = requests.get(url + "/sendMessage", data= parameters)
      time.sleep(4)
    else :
      continue


  if data["result"]:
    return data["result"][-1]["update_id"] + 1
  



offset = 918801344
while True:

  offset = read_msg(offset)
  time.sleep(1)
