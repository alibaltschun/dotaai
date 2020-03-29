import easygui
import boto3
import artificial_assistent, spectator_server, spectator_client

def __check_user__():
    username = easygui.enterbox("insert your email address")
    
    ACCESS_KEY = "AKIAVSRG2BELW4TOFMP5"
    SECRET_KEY = "7Y+a4lBfgbnDkq1bAmEBwk8tYxLc39HQ65Qay+r9"
    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
    )
    
    dynamodb = session.resource('dynamodb', 
                              region_name='ap-southeast-1',)
    
    table = dynamodb.Table("dotaai_dev")
    
    res =  table.get_item(
        Key={'id':username})
    if 'Item' in res:
        return username, True
    else :
        return username, False

def menu():
    msg = "Choose program"
    choices = ["Artificial assitent","spectator map client","spectator map server"]
    reply = easygui.buttonbox(msg, choices=choices)
    return reply

if __name__ == "__main__":
    username, exist = __check_user__()
    if exist:
        program = menu()
        if program == "Artificial assitent":
            artificial_assistent.main()
        elif program == "spectator map client":
            endpoint = spectator_client.setup(username)
            if endpoint is not None:
                spectator_client.main(endpoint)
            else:
                easygui.msgbox("please start your spectator server".format(username))
        elif program == "spectator map server":
            err = spectator_server.setup(username)
            if err is None:
                spectator_server.main()
            else:
                easygui.msgbox(err)
    else:
        easygui.msgbox("User {} is not registered".format(username))