from PIL import  ImageGrab
import os
import json
import requests
import boto3
import decimal
import time
import threading


##################### FLASK ################################

from flask import Flask, send_from_directory
from flask_ngrok import run_with_ngrok

app = Flask(__name__, static_url_path='')

run_with_ngrok(app)

STATIC = "/static"

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

def run_flask():
    app.run()
    
##################### FLASK ################################


QUALITY = 90
DELAY = 5
username = None


def __get_ngrok_url__():
    try :
        url = "http://localhost:4040/api/tunnels/"
        res = requests.get(url)
        res_unicode = res.content.decode("utf-8")
        res_json = json.loads(res_unicode)
        for i in res_json["tunnels"]:
            if i['name'] == 'command_line':
                return i['public_url']
                break
    except:
        return False
        
def __get_networth_summary__(img,quality_val=QUALITY):
    w,h = img.size
    delta = w*0.347 if w*9 > h*21 else w*0.465
    networth = img.crop((h*0.024,h*0.18,delta,h*0.59))
    
    print("save new networth summary")
    networth.save("./static/networth_summary.jpg", 'JPEG', quality=quality_val)
    
def __get_map__(img,quality_val=QUALITY):
    w,h = img.size
    the_map = img.crop((0,h-h*0.26,h*0.26,h))
    
    print("save new map image")
    the_map.save("./static/map.jpg", 'JPEG', quality=quality_val)

def __get_networth__(img,quality_val=QUALITY):
    w,h = img.size
    delta = w*0.12 if w*9 > h*21 else w*0.16
    networth = img.crop((0,h*0.11,delta,h*0.43))
    
    print("save new networth")
    networth.save("./static/networth.jpg", 'JPEG', quality=quality_val)

def __dynamodb_table__():
    try :
        ACCESS_KEY = "AKIAVSRG2BELW4TOFMP5"
        SECRET_KEY = "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"
        session = boto3.Session(
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY,
        )
        
        dynamodb = session.resource('dynamodb', 
                                  region_name='ap-southeast-1',)
        
        
        table = dynamodb.Table("dotaai_dev")
        return table
    except:
        return False

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def __check_user_exist__(table,username):
    try:
        response = table.get_item(
            Key={
                'id': username
            }
        )
        return True if "Item" in response else False
    except :
        return False

def setup(username):
    if not os.path.exists(STATIC[1:]):
        os.makedirs(STATIC[1:])
    
    
    dynamodb_table = __dynamodb_table__()
    if dynamodb_table is not False:
        response = __check_user_exist__(dynamodb_table,username)
        if response is not False:
            server_process = threading.Thread(target=run_flask)
            server_process.setDaemon(True)
            server_process.start()
            time.sleep(DELAY)
            
            ngrok_url = __get_ngrok_url__() 

            if ngrok_url is not False:
                response = dynamodb_table.update_item(
                Key={'id': username},
                UpdateExpression='SET #ts = :val1',
                ExpressionAttributeValues={
                    ":val1": ngrok_url
                    },
                ExpressionAttributeNames={
                        "#ts": "server_url"
                  })
                return None 
            else:
                return "error : please turn on your ngrok" 
        else:
            return "error : user not found" 
    else:
        return "main server error"
   
    

def main():
    while True:
        img = ImageGrab.grab()
        __get_networth__(img)
        __get_map__(img)
        time.sleep(DELAY)
    
    
#if __name__ == "__main__":
#    login_success = False
#    r,server_process = setup()
#    if r is True:
#        main()
#            
#    else:
#        ctypes.windll.user32.MessageBoxW(0, r, u"Error", 0)
