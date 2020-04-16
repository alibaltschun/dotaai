# -*- coding: utf-8 -*-

import os
import pandas as pd
BASE = (os.path.dirname(os.path.realpath(__file__)))

data = pd.read_csv(BASE + "/../assets/csv/hero.csv")


def __notification__(arr_texts):
    ui = ""
    for i in range(len(arr_texts)):
        ui += """
    <a id="btn_toast{}" class="btn btn-info invisible" onclick="toastr.info('{}');"></a>
         """.format(i, arr_texts[i])
    return ui


def __js_notif__(index):
    top = """
        setTimeout("CallButton""" + str(index) + """()",""" + str(500 * (index+1)) + """)
            function CallButton""" + str(index) + """(){
            """

    mid = """
                document.getElementById("btn_toast{}").click();""".format(
                    index)

    bottom = """

        }"""

    return top + mid + bottom


def __js__(arr_texts):
    js_notif = ""
    for i in range(len(arr_texts)):
        js_notif += __js_notif__(i)

    top = """<script type="text/javascript"> """

    bottom = """
        async function checkUpdate()
        {
            const response = await fetch('http://localhost:5000/html_update');
            const res = await response.json()
            // res = "0"
            console.log("x")
            if( res == "1"){
                location.reload();
            }else{
                setTimeout(() => {
                    checkUpdate()
                }, 1000);
            }
        }
        checkUpdate();

    </script>
    """

    return top + js_notif + bottom


def generate_ui(text):

    with open(BASE + "/utils/head.html", "r") as file:
        head = file.read()

    with open(BASE + "/utils/style_gameplay.html", "r") as file:
        style = file.read()

    with open(BASE + "/utils/close_head_open_body.html", "r") as file:
        head_body = file.read()

    # with open(BASE + "/utils/js_gameplay_notif.html", "r") as file:
    #     js_notif = file.read()

    with open(BASE + "/utils/js.html", "r") as file:
        js = file.read()

    with open(BASE + "/utils/bottom.html", "r") as file:
        bottom = file.read()

    with open(BASE + "/index.html", "w+") as file:
        file.write(head)
        file.write(style)
        file.write(head_body)
        file.write(__notification__(text))
        file.write(js)
        file.write(__js__(text))
        file.write(bottom)


generate_ui(["Dude, buy teleport", "test", "fu"])
