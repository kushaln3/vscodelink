import requests
from pyngrok import ngrok
import time


def Ngrok_Url():
    ngrok_connect = ngrok.connect(8080)
    print(f"\nNgrok Tunnel Address is {ngrok_connect.public_url}\n\n")
    return(ngrok_connect.public_url)

def Check_Website_Up(ngrokUrl):
    resCode = requests.get(ngrokUrl).status_code
    if resCode == 200:
        print("Site is up and working :).")
        return("working")
    elif resCode == 404:
        print("Site is Down :(")
        return("not working")


while True:
    ngrokUrl = Ngrok_Url()
    while True:
        status = Check_Website_Up(ngrokUrl)
        if status == "not working":
            break
        time.sleep(10)
        print(time.localtime())
