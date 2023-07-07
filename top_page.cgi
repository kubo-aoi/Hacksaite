#!/usr/bin/python3
import cgi

print("Content-Type: text/html\n")

htmlText = '''
<!DOCTYPE html>

<html lang="ja">
<head>
<meta charset="utf-8">
<title>トップページ</title>
<style type="text/css">
<!--
h1 { color:green }
strong { color: blue; font-size: large }
em { font-style: Italic }
-->
</style>
</head>
<body>
<span style = "white-apace:norap;">
<h1>メルカリのパクリ</h1>
<form action="./top_page.cgi" method="post">
<input type="search" name="search" placeholder="キーワードを入力">
<input type="submit" name="submit" value="検索">
</span>
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
