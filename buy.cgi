#!/usr/bin/python3
import cgi
import MySQLdb
import os
from http import cookies
import random, string

cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE',''))

try:

	userid = cookie["userid"].value

except KeyError:

	userid = 'please_login'

connection = MySQLdb.connect(

    host='localhost',

    user='user1',

    passwd='passwordA1!',

    db='ShopData',

    charset='utf8'

)

cursor = connection.cursor()

cursor.execute("select * from cart")

rows = cursor.fetchall()
cart_list = str()
cart_num = 0
sum_money = 0
for row in rows:
    if row[0]==userid:
        cart = "<br><a href='"+row[2]+"'>"+row[1]+str(row[3])+"円</a></br>"
        cart_list+=cart
        sum_money += row[3]
        cart_num += 1
connection.close()
print("Content-Type: text/html\n")
if userid == "please_login":
    htmlText = '''
    <!DOCTYPE html>

    <html lang="ja">
    <head>
    <meta charset="utf-8">
    <title>ComBuy</title>
    <link rel="stylesheet" type="text/css" href="buy.css"/>
    <!--
    h1 { color:green }
    strong { color: blue; font-size: large }
    em { font-style: Italic }
    -->
    
    </style>
    
    </head>
    
    <body>
    <!-- ボタンの宛先を指定するjavascript -->
    <script>
    function multipleaction(u){
    var f = document.querySelector("form");
    var a = f.setAttribute("action", u);
    document.querySelector("form").submit();
    }
    </script>

    <form id="mainform">
    <div class="logo"><button type="submit" onclick="multipleaction('./top_page.cgi')" alt="topに戻る"><img src= "./button/ComBuy.png" width="320"height="100"></button></div>
    <h1>%s</h1>
    <input type="search" name="search" placeholder="キーワードを入力">
    <button type="submit" onclick="multipleaction('./top_page.cgi')"><img src="./button/search_button.png" width="50"height="30" alt="検索" /></button> 
    <div class="btn"><button type="button" onclick="multipleaction('./login.php')"><img src="./button/login.png" width="70"height="70" alt="送信" /></button>
    <button type="button" onclick="multipleaction('./register.php')"><img src="./button/sign_up.png" width="70"height="70" alt="新規登録" /></button>
    <button type="button" onclick="multipleaction('./rireki.cgi')"><img src="./button/rireki.png" width="70"height="70" alt="購入履歴" /></button>
    <button type="button" onclick="multipleaction('./Exhibit.cgi')"><img src="./button/syuppin.png" width="70"height="70" alt="出品する" /></button>
    <button type="button" onclick="multipleaction('./cart.cgi')"><img src="./button/cart.png" width="70"height="70" alt="カート" /></button></div>
    </form>
    </body>
    
    </html>
    '''%(userid)
else:
    htmlText = '''
    <!DOCTYPE html>

    <html lang="ja">
    <head>
    <meta charset="utf-8">
    <title>ComBuy</title>
    <link rel="stylesheet" type="text/css" href="buy.css"/>
    <!--
    h1 { color:green }
    strong { color: red; font-size: large }
    em { font-style: Italic }
    -->
  

    </style>
    </head>
    
    <body>
    <!-- ボタンの宛先を指定するjavascript -->
    <script>
    function multipleaction(u){
    var f = document.querySelector("form");
    var a = f.setAttribute("action", u);
    document.querySelector("form").submit();
    }
    </script>

    <form id="mainform">
    <div class="logo"><button type="submit" onclick="multipleaction('./top_page.cgi')" alt="topに戻る"><img src= "./button/ComBuy.png" width="320"height="100"></button></div>
    <h1>%sさん</h1>
    <input type="search" name="search" placeholder="キーワードを入力">
    <button type="submit" onclick="multipleaction('./top_page.cgi')"><img src="./button/search_button.png" width="50"height="30" alt="検索" /></button> 
    <div class="btn"><button type="button" onclick="multipleaction('./rireki.cgi')"><img src="./button/rireki.png" width="70"height="70" alt="購入履歴" /></button>
    <button type="button" onclick="multipleaction('./Exhibit.cgi')"><img src="./button/syuppin.png" width="70"height="70" alt="出品する" /></button>
    <button type="button" onclick="multipleaction('./cart.cgi')"><img src="./button/cart.png" width="70"height="70" alt="カート" /></button></div>
    </form>
    </body>
    
    </html>
    '''%(userid)

print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))

connection = MySQLdb.connect(

    host='localhost',

    user='user1',

    passwd='passwordA1!',

    db='ShopData',

    charset='utf8'

)

cursor = connection.cursor()

cursor.execute("select * from credit_cards")

rows = cursor.fetchall()
credit_num = str()
for row in rows:
    if row[1]==userid:
        credit_num = row[2]
connection.close()


form = cgi.FieldStorage()
htmlText = '''
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>Python Form</title>
</head>
<body>
<br>カートの中身:%s件</br>
%s
<br><strong>合計金額:%s円</strong></br>
<label for="pet-select">支払い方法を選択:</label>
<select id="pet-select">
    <option value="">--支払い方法を選択してください--</option>
    <option value="dog">コンビニ支払い</option>
    <option value="cat">クレジットカード:%s</option>
</select>
<br><a href="./buy_kakutei.cgi">購入確定</a></br>
</body>
</html>
    '''%(cart_num,cart_list,sum_money,credit_num)
print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))


