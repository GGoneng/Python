import cgi, cgitb
import sys, codecs
import os
from MinModule2 import *
import pickle
import pandas as pd

SCRIPT_MODE = True
cgitb.enable()

def showHTML(msg):
    print("Content-Type: text/html; charset=utf-8")

    print(f"""
        
        <!DOCTYPE html>
        <html lang="ko">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>웹은 어려웡</title>
        """+
        """
        <style>

            body {
                background-color:rgb(246, 251, 255)
            }

            header {
                height:20vh;
                padding-top:3vh;
                font-size : 25px;
                font-weight: bold;
                background-color:rgba(190, 224, 254, 0.575);
                text-align: center;
                border: 1px solid rgb(191, 194, 197);
            }

            nav {
                display:flex;
                padding-left:8vh;
                justify-content:space-between;
                height:5vh;
                width:90vw;
            }

            nav div {
                flex-grow:1;
                display:flex;
                padding: 10px;
                background-color:rgba(190, 224, 254, 0.575);
                justify-content: center;
                align-items: center;
                border: 1px solid rgb(191, 194, 197);
                width: 40vw;
                text-align: center;
           
            }
            
            a {
                color: rgb(46, 36, 36, 0.6);
                font-size: 15px;
                text-decoration: none;
                font-weight: bold;
            }

            a:visited {
                color : rgba(46, 36, 36, 0.6)
            }

            a:hover {
                color: rgba(46, 36, 36, 0.6)
            }

            a:active {
                color: rgba(46, 36, 36, 0.317)
            }

            section {
                display: flex;
                padding-top:8vh;
                padding-left: 8vh;
                justify-content:space-between;
                width: 90vw;
            }

            section div {
                flex-grow: 1;
                padding: 10px;
                justify-content: center;
                align-items: center;
                border: 1px solid rgb(191, 194, 197);
                width: 40vw;
                text-align: center;
            }

            ul {
                font-size: 20px;
                margin-right: 30px;
                text-align: center;
                list-style-type: none;
            }

            li {
                padding-top: 20px;
                padding-bottom: 20px;
            }

            form {
                margin-top: 30px;
                width: 40vw;
                margin-left: 30vw;
                padding-bottom: 20px;
                border: 1px solid rgb(191, 194, 197);
                justify-content: center;
                align-items: center;
                text-align: center;
            }

            .form_inner {
                display: flex;
                justify-content: center;
                align-items: center;
            }

            input[type="text"] {
                height:30vh;
                width:20vw;
                padding:10px;
            }

            input[type="submit"] {
                width:20vw;
                height:30px;
                background-color: rgb(236, 232, 255, 0.6);
                font-weight: bold;
            }

            #result {
                display:flex;
                width:50vw;
                height:10vh;
                margin-top: 50px;
                margin-left: 25vw;
                background-color: rgba(190, 224, 254, 0.575);
                justify-content: center;
                align-items: center;
                border: 1px solid rgb(191, 194, 197);
                font-size: 25px;
            }

        </style>
    </head>
    """)
    print(f"""
    <body>
        <header>
            <h1>순환/호흡기 질환 분석 모델</h1>
        </header>
        <form>
            <div class='form_inner'>
                <ul>
                    <li><input type='text' name='words' placeholder='텍스트를 입력해주세요' value={words}></li>
                </ul>
            </div>
            <div id=submit><input type='submit' value='제출'></div>
        </form>
        <div id='result'>{msg}</div>     
    </body>
    </html>
""")
    
model_names = ['min_model.pth']
model_paths = []

def custom_analyzer(x):
    return x

if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

if SCRIPT_MODE:
    for mod in model_names:
        model_paths.append(os.path.dirname(__file__)+ '/models/'+mod) # 웹상에서는 절대경로만
else:
    for mod in model_names:
        model_paths.append('./models/'+mod) 

form = cgi.FieldStorage()


if 'words' not in form:
    msg = "<p>텍스트가 입력 되지 않았습니다.</p>"
    words = ''

else:
    msg = ""

    words = form.getvalue('words', default = "")

    
    if not ('' == words):
        preprocessed_sentence = min_preprocessing_text(words)
        result = min_predict_value(preprocessed_sentence, model_paths[0])

        if result.item() == 0:
            msg = "<p>이 질환은 순환/호흡기 질환이 아닙니다.</p>"
        elif result.item() == 1:
            msg = '<p>이 질환은 순환/호흡기 질환입니다.</p>'
    else:
        msg = "개 빡치네"

showHTML(msg)