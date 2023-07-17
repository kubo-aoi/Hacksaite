#!/usr/bin/python3

import cgi
import sys
import os
import MySQLdb
from http import cookies

cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE',''))

connection = MySQLdb.connect(

	host='localhost',

	user='user1',

	passwd='passwordA1!',

	db='ShopData',

	charset='utf8'

)


try:

	userid = cookie["userid"].value

except KeyError:

	userid = 'temp'
	

if ( os.environ['REQUEST_METHOD'] == "GET"):
	htmlText = """
	<!DOCTYPE html">
		<html lang="ja">
		<head>
			<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
			<meta charset="utf-8">
			
		</head>
		<body>	
			<style>
				textarea {
				resize: None;
			}
			</style>
			<script type="text/javascript">
				msgtxt = new Array();
				msgtxt[0] = "210円";
				msgtxt[1] = "450円";
				msgtxt[2] = "750円~";
				
				msgtxt2 = new Array();
				msgtxt2[0] = "角型A4(31.2cm×22.8cm),厚さ ~3cm, 重さ1kg";
				msgtxt2[1] = "薄型 24.8cm×34cm, 厚型 25cm(縦)×20cm(横)×5cm(高さ), 重さの規定なし";
				msgtxt2[2] = "3辺 ~160cm, 重さ　~25kg";

				function selchg() {
				    x = document.f1.mailways.selectedIndex;
				    document.f1.t1.value = msgtxt[x];
				    document.f1.t2.value = msgtxt2[x];
				}

			    </script>
			<h1>新しく出品する</h1>
			<form action="./Exhibit.cgi" name = "f1" method="post" enctype="multipart/form-data">
			<input type="file" name="imgfile">
			<p>コメント</p>
			<textarea cols="30" rows="5" name="comments"></textarea><br>
			<p>商品情報</p>
			<p>商品名:</p><input type="text" name="title" required>
			<p>価格:</p><input type="number" min="300" name="price" required>
			<p> 状態：
			<select name="status">
				<option value="新品・未使用">新品・未使用</option>
				<option value="未使用に近い">未使用に近い</option>
				<option value="目立った傷なし">目立った傷なし</option>
				<option value="やや傷や汚れあり">やや傷や汚れあり</option>
				<option value="傷や汚れあり">傷や汚れあり</option>
				<option value="全体的に悪い">全体的に悪い</option>
			</select>
			<p>発送元：
			<select name="address">
				<option value="北海道">北海道</option>
				<option value="青森県">青森県</option>
				<option value="岩手県">岩手県</option>
				<option value="宮城県">宮城県</option>
				<option value="秋田県">秋田県</option>
				<option value="山形県">山形県</option>
				<option value="福島県">福島県</option>
				<option value="茨城県">茨城県</option>
				<option value="栃木県">栃木県</option>
				<option value="群馬県">群馬県</option>
				<option value="埼玉県">埼玉県</option>
				<option value="千葉県">千葉県</option>
				<option value="東京都">東京都</option>
				<option value="神奈川県">神奈川県</option>
				<option value="新潟県">新潟県</option>
				<option value="富山県">富山県</option>
				<option value="石川県">石川県</option>
				<option value="福井県">福井県</option>
				<option value="山梨県">山梨県</option>
				<option value="長野県">長野県</option>
				<option value="岐阜県">岐阜県</option>
				<option value="静岡県">静岡県</option>
				<option value="愛知県">愛知県</option>
				<option value="三重県">三重県</option>
				<option value="滋賀県">滋賀県</option>
				<option value="京都府">京都府</option>
				<option value="大阪府">大阪府</option>
				<option value="兵庫県">兵庫県</option>
				<option value="奈良県">奈良県</option>
				<option value="和歌山県">和歌山県</option>
				<option value="鳥取県">鳥取県</option>
				<option value="島根県">島根県</option>
				<option value="岡山県">岡山県</option>
				<option value="広島県">広島県</option>
				<option value="山口県">山口県</option>
				<option value="徳島県">徳島県</option>
				<option value="香川県">香川県</option>
				<option value="愛媛県">愛媛県</option>
				<option value="高知県">高知県</option>
				<option value="福岡県">福岡県</option>
				<option value="佐賀県">佐賀県</option>
				<option value="長崎県">長崎県</option>
				<option value="熊本県">熊本県</option>
				<option value="大分県">大分県</option>
				<option value="宮崎県">宮崎県</option>
				<option value="鹿児島県">鹿児島県</option>
				<option value="沖縄県">沖縄県</option>
			</select>
			</p>
			<select name="mailways" onChange="selchg()">
				<option>ポスト郵送
				<option>お手軽郵送
				<option>通常郵送
				</select>

				<TEXTAREA name="t1" rows="1" readonly></TEXTAREA>
				<br>
				<TEXTAREA name="t2" rows="3" cols = "30" readonly></TEXTAREA>
				<br>
						
			<input type="submit" value="出品する">
			</form>
		</body>
		
	"""

elif ( os.environ['REQUEST_METHOD'] == "POST" ):
	form = cgi.FieldStorage()
	comments = form.getfirst('comments')
	title = form.getfirst('title')
	price = form.getfirst('price')
	status = form.getfirst('status') 
	address = form.getvalue("address") 
	mailsways = form.getvalue("mailways") 
	
	target_dir = "./Goods_Photo/"
	fileitem = form["imgfile"]

	cursor = connection.cursor()
	
	sql    = "insert into `itemdata`(`userid`,`comments`,`title`,`prace`,`status`,`address`,`mailways`,`imgname`) values('"+userid+"','"+comments+"','"+title+"','"+price+"','"+status+"','"+address+"','"+mailsways+"','"+fileitem.filename+"');"
	cursor.execute(sql)
	
	connection.commit()        
	connection.close()
	
	filepath = os.path.join(target_dir, fileitem.filename)
	with open(filepath, "wb") as f:
		f.write(fileitem.file.read())
		f.seek(0)
	
	
	htmlText = """
	<!DOCTYPE html">
		<html lang="ja">
		<head>
			<meta charset="utf-8">
			
		</head>
		<body>
			<p>出品完了しました！</p>
			<a href='./top_page.cgi' alt = "トップページに戻る">
		</body>
		
	"""%(sql)
	
		
print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))
