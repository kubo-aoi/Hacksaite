#!/usr/bin/python3
import cgi

print("Content-Type: text/html\n")

htmlText = '''
<!DOCTYPE html>

<html lang="ja">
<head>
<meta charset="utf-8">
<title>掲示板サンプル</title>
<style type="text/css">
<!--
h1 { color:green }
strong { color: blue; font-size: large }
em { font-style: Italic }
-->
</style>
</head>
<body>
<h1>私の掲示板</h1>
<p>ご自由に書き込んでください</p>
<form action="./bbs2.cgi" method="post">
題名:<input type="text" name="title" size="60"><br>
名前:<input type="text" name="author" size="20"><br>
本文<br>
    <textarea cols="60" rows="5" name="text"></textarea><br>
    <input type="submit" value="送信">
    <input type="reset" value="リセット">

</form>

</body>

</html>

'''
print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))

form = cgi.FieldStorage()
title = form.getfirst('title')
author = form.getfirst('author')
text = form.getfirst('text')
htmlText = '''
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>Python Form</title>
</head>
<body>
<strong>%s</strong><br>
<em>%s</em><br>
<p>%s</p>
<hr>
</body>
</html>
'''%(title, author, text)
print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))
