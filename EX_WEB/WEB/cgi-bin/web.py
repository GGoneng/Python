import cgi, cgitb
import sys, codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

cgitb.enable()

def showHTML():
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

            strong {
                font-size: 25px;
            }

            ul {
                font-size: 20px;
                margin-right: 30px;
                text-align: left;
            }

            li {
                padding-top: 20px;
                padding-bottom: 20px;
            }
        </style>
    </head>
    """)
    print(f"""
    <body>
        <header>
            <h1>모델 연결 웹</h1>
        </header>

        <section>
            <div id="ml">
                <strong>전복 나이 분석 모델<hr></strong>
                <ul>
                    <li>모델 : DecisionTreeRegression</li>
                    <li>Feature : 전복 특성 3가지</li>
                    <li>Target : 전복의 나이</li>        
                </ul>
            </div>
            <div id="dl">
                <strong>아마존 리뷰 감정 분석 모델<hr></strong>
                <ul>
                    <li>모델 : Custom ANN Model</li>
                    <li>Feature : 영어 리뷰 문장</li>
                    <li>Target : 긍/부정</li>
                </ul>
            </div>
            <div id="cv">
                <strong>고양이과 동물 분류 모델<hr></strong>
                <ul>
                    <li>모델 : Custom Model (convnext_tiny)</li>
                    <li>Feature : 고양이과 동물 사진</li>
                    <li>Target : 동물 종류 분류</li>
                </ul>
            </div>
            <div id="nlp">
                <strong>질병 종류 분류 모델<hr></strong>
                <ul>
                    <li>모델 : LSTM Custom Model</li>
                    <li>Feature : 약학정보원 크롤링 데이터</li>
                    <li>Target : 질병 분류</li>
                </ul>
            </div>
        </section>
        <nav>
            <div>
                <img src = "../data/homepage.png" style="width:20px;
                height:20px";>
                <a href="./ml_web.py">
                    &ensp;홈페이지 바로가기
                </a>
            </div>
            <div>
                <img src = "../data/homepage.png" style="width:20px;
                height:20px";>
                <a href="./dl_web.py">
                    &ensp;홈페이지 바로가기
                </a>
            </div>
            <div>
                <img src = "../data/homepage.png" style="width:20px;
                height:20px";>
                <a href="./webClassifieranimals.py">
                    &ensp;홈페이지 바로가기
                </a>
            </div>
            <div>
                <img src = "../data/homepage.png"; style="width:20px; height:20px";>
                <a href="./nlp_web.py">&ensp;홈페이지 바로가기</a>
            </div>
        </nav>
    </body>
    </html>
        """)
    
showHTML()