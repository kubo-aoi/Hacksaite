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
for row in rows:
    good = "<img src='./Goods_Photo/"+row[1]+"' width='160'height='90' alt='検索'/>"
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
<button type="submit" onclick="multipleaction('./top_page.cgi')" alt="topに戻る"><img src= "./button/サイトロゴComBuy.png" width="320"height="100"></button>
<input type="search" name="search" placeholder="キーワードを入力">
<button type="submit" onclick="multipleaction('./top_page.cgi')"><img src="./button/検索ボタン.png" width="50"height="30" alt="検索" /></button> 
<button type="button" onclick="multipleaction('./login.php')"><img src="./button/横長ログイン.png" width="100"height="30" alt="送信" /></button>
<button type="button" onclick="multipleaction('./register.php')"><img src="./button/新規登録.png" width="50"height="50" alt="新規登録" /></button>
<button type="button" onclick="multipleaction('./top_page.cgi')"><img src="./button/購入履歴.png" width="50"height="50" alt="購入履歴" /></button>
<button type="button" onclick="multipleaction('./top_page.cgi')"><img src="./button/出品する.png" width="50"height="50" alt="出品する" /></button>
<button type="button" onclick="multipleaction('./purchase_confirmation.php')"><img src="./button/買い物かご.png" width="50"height="50" alt="カート" /></button>
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
<p>イスだよ</p>
<nobr>%s</nobr>
<nobr>%s</nobr>
<nobr>%s</nobr>
<nobr>%s</nobr>
<nobr>%s</nobr>
<nobr>%s</nobr>
<nobr>%s</nobr>
<nobr>%s</nobr>
<nobr>%s</nobr>
</body>
</html>
    '''%(goods_list[0],goods_list[1],goods_list[2],goods_list[3],goods_list[4],goods_list[5],goods_list[6],goods_list[7],goods_list[8],goods_list[9])
print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))

