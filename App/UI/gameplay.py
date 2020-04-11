# -*- coding: utf-8 -*-

import os
import pandas as pd
BASE = (os.path.dirname(os.path.realpath(__file__)))

data = pd.read_csv(BASE + "/../assets/csv/hero.csv")

def __notification__(text):
    ui = """
    <a id="btn_toast" class="btn btn-info invisible" onclick="toastr.info('{}');"></a>
         """.format(text)
    return ui

def generate_ui(text=""):

    with open(BASE + "/utils/head.html","r") as file:
        head=file.read()
    
    with open(BASE + "/utils/style_gameplay.html","r") as file:
        style=file.read()
    
    with open(BASE + "/utils/close_head_open_body.html","r") as file:
        head_body=file.read()
    
    with open(BASE + "/utils/js_gameplay_notif.html","r") as file:
        js_notif=file.read()
    
    with open(BASE + "/utils/js_gameplay_blank.html","r") as file:
        js=file.read()
    
    with open(BASE + "/utils/bottom.html","r") as file:
        bottom=file.read()
    
    with open(BASE + "/index.html","w+") as file:
        file.write(head)
        file.write(style)
        file.write(head_body)
        file.write(__notification__(text))
        if text:
            file.write(js_notif)
        else:
            file.write(js)
        file.write(bottom)

generate_ui("c")