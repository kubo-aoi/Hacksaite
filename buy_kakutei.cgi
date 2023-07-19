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
        sql = "insert into `buy` (`User_id`, `goods_name`,`goods_site`,`price`) VALUES('"+userid+"','"+row[1]+"','"+row[2]+"',"+str(row[3])+");"
        cursor.execute(sql)
        connection.commit()
connection.close()


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

sql = "delete from cart where User_id ='"+userid+"';"
cursor.execute(sql)
connection.commit()
connection.close()
print("Content-Type: text/html\n")
if userid == "please_login":
    htmlText = '''
    <!DOCTYPE html>

    <html lang="ja">
    <head>
    <meta charset="utf-8">
    <title>ComBuy</title>
    <style type="text/css">
    <!--
    h1 { color:green }
    strong { color: blue; font-size: large }
    em { font-style: Italic }
    -->
    button {
        width: auto;
        padding:0;
        margin:0;
        background:none;
        border:0;
        font-size:0;
        line-height:0;
        overflow:visible;
        cursor:pointer;
    }
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
    <button type="submit" onclick="multipleaction('./top_page.cgi')" alt="topに戻る"><img src= "./button/ComBuy.png" width="320"height="100"></button>
    <h1>%s</h1>
    <input type="search" name="search" placeholder="キーワードを入力">
    <button type="submit" onclick="multipleaction('./top_page.cgi')"><img src="./button/search_button.png" width="50"height="30" alt="検索" /></button> 
    <button type="button" onclick="multipleaction('./login.php')"><img src="./button/login.png" width="100"height="30" alt="送信" /></button>
    <button type="button" onclick="multipleaction('./register.php')"><img src="./button/sign_up.png" width="50"height="50" alt="新規登録" /></button>
    <button type="button" onclick="multipleaction('./top_page.cgi')"><img src="./button/rireki.png" width="50"height="50" alt="購入履歴" /></button>
    <button type="button" onclick="multipleaction('./Exhibit.cgi')"><img src="./button/syuppin.png" width="50"height="50" alt="出品する" /></button>
    <button type="button" onclick="multipleaction('./cart.cgi')"><img src="./button/cart.png" width="50"height="50" alt="カート" /></button>
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
    <style type="text/css">
    <!--
    h1 { color:green }
    strong { color: red; font-size: large }
    em { font-style: Italic }
    -->
    button {
        width: auto;
        padding:0;
        margin:0;
        background:none;
        border:0;
        font-size:0;
        line-height:0;
        overflow:visible;
        cursor:pointer;
    }
    label {
        font-family: sans-serif;
        font-size: 1rem;
        padding-right: 10px;
    }   

    select {
        font-size: 0.9rem;
        padding: 2px 5px;
    }

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
    <button type="submit" onclick="multipleaction('./top_page.cgi')" alt="topに戻る"><img src= "./button/ComBuy.png" width="320"height="100"></button>
    <h1>%sさん</h1>
    <input type="search" name="search" placeholder="キーワードを入力">
    <button type="submit" onclick="multipleaction('./top_page.cgi')"><img src="./button/search_button.png" width="50"height="30" alt="検索" /></button> 
    <button type="button" onclick="multipleaction('./top_page.cgi')"><img src="./button/rireki.png" width="50"height="50" alt="購入履歴" /></button>
    <button type="button" onclick="multipleaction('./Exhibit.cgi')"><img src="./button/syuppin.png" width="50"height="50" alt="出品する" /></button>
    <button type="button" onclick="multipleaction('./cart.cgi')"><img src="./button/cart.png" width="50"height="50" alt="カート" /></button>
    </form>
    </body>
    
    </html>
    '''%(userid)

print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))


form = cgi.FieldStorage()
htmlText = '''
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>Python Form</title>
</head>
<body>
<strong>購入が確定しました。</strontg>
<br><a href="./top_page.cgi">トップへ戻る</a></br>
</body>
</html>
    '''%()
print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))

