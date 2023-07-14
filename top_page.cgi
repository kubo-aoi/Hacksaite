#!/usr/bin/python3
import cgi

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
<input type="search" name="search" placeholder="キーワードを入力">
<button type="submit" onclick="multipleaction('./top_page.cgi')">検索</button> 
<button type="button" onclick="multipleaction('./login.php')">ログイン</button>
<button type="button" onclick="multipleaction('./register.php')">新規登録</button>
<button type="button" onclick="multipleaction('./top_page.cgi')">検索履歴</button>
<button type="button" onclick="multipleaction('./top_page.cgi')">トップに戻る</button>
<button type="button" onclick="multipleaction('./top_page.cgi')">出品</button>
<button type="button" onclick="multipleaction('./top_page.cgi')">カート</button>
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
