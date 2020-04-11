# -*- coding: utf-8 -*-

import os
import pandas as pd
BASE = (os.path.dirname(os.path.realpath(__file__)))

data = pd.read_csv(BASE + "/../../assets/csv/hero.csv")

def __notification__(text):
    ui = """
    <a id="btn_toast" class="btn btn-info invisible" onclick="toastr.info('{}');"></a>
         """.format(text)
    return ui



def generate_ui(text):

    with open(BASE + "/top.html","r") as file:
        top=file.read()
    
    with open(BASE + "/bottom.html","r") as file:
        bottom=file.read()
    
    
    with open(BASE + "/index.html","w+") as file:
        file.write(top)
        file.write(__notification__(text))
        file.write(bottom)

#generate_ui("dude, buy teleport !")