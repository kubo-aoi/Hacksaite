#!/usr/bin/python3
import cgi
import MySQLdb
import os
from http import cookies
import random, string

cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE',''))

try:

	userid = cookie["userid"].value+"さん"

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

cursor.execute("select * from Goods")

rows = cursor.fetchall()
goods_list = []
goods_name = []
for row in rows:
    good = "<a href='"+row[3]+"'><img src='./Goods_Photo/"+row[1]+"' width='180'height='150' alt='検索'/></a>"
    goods_list.append(good)
    goods_name.append(row[2])
len_goodslist=len(goods_list)
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
    <button type="button" onclick="multipleaction('./purchase_confirmation.php')"><img src="./button/cart.png" width="50"height="50" alt="カート" /></button>
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
    <button type="button" onclick="multipleaction('./top_page.cgi')"><img src="./button/rireki.png" width="50"height="50" alt="購入履歴" /></button>
    <button type="button" onclick="multipleaction('./Exhibit.cgi')"><img src="./button/syuppin.png" width="50"height="50" alt="出品する" /></button>
    <button type="button" onclick="multipleaction('./purchase_confirmation.php')"><img src="./button/cart.png" width="50"height="50" alt="カート" /></button>
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
<img src="./Goods_Photo/cushion.png" width="300"height="230" alt="クッション" />
<a href='./cushion_cart.cgi'><img src='./button/add.png' width='50'height='50' alt='カートに追加'/></a>
<nobr><a href='./cushion_cart.cgi'>カートに追加</a></nobr>
<br>商品名:クッション</br>
<br>値段:500円</br>
<br>配送業者:佐川</br>
<br>お届け日数:6日</br>
</body>
</html>
    '''
print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))

