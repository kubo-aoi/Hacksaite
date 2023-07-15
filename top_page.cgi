#!/usr/bin/python3
import cgi
import MySQLdb
import os
from http import cookies
import random, string

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
goods_list2 = []
for row in rows:
    good = "<img src='./商品写真and情報/商品写真_情報/"+row[1]+"' width='160'height='90' alt='検索'/>"
    goods_list.append(good)
connection.close()

print("Content-Type: text/html\n")
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

<form>
<button type="submit" onclick="multipleaction('./top_page.cgi')" alt="topに戻る"><img src= "./ボタン/ボタン/サイトロゴComBuy.png" width="320"height="100"></button>
<input type="search" name="search" placeholder="キーワードを入力">
<button type="submit" onclick="multipleaction('./top_page.cgi')"><img src="./ボタン/ボタン/検索ボタン.png" width="50"height="30" alt="検索" /></button> 
<button type="button" onclick="multipleaction('./login.php')"><img src="./ボタン/ボタン/横長ログイン.png" width="100"height="30" alt="送信" /></button>
<button type="button" onclick="multipleaction('./register.php')"><img src="./ボタン/ボタン/新規登録.png" width="50"height="50" alt="新規登録" /></button>
<button type="button" onclick="multipleaction('./top_page.cgi')"><img src="./ボタン/ボタン/購入履歴.png" width="50"height="50" alt="購入履歴" /></button>
<button type="button" onclick="multipleaction('./top_page.cgi')"><img src="./ボタン/ボタン/出品する.png" width="50"height="50" alt="出品する" /></button>
<button type="button" onclick="multipleaction('./purchase.php')"><img src="./ボタン/ボタン/買い物かご.png" width="50"height="50" alt="カート" /></button>
</form>
</body>

</html>
'''
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
<nobr>%s</nobr>
<nobr>%s</nobr>
<nobr>%s</nobr>
<nobr>%s</nobr>
</body>
</html>
    '''%(goods_list[0],goods_list[1],goods_list[2],goods_list[3])
print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))

