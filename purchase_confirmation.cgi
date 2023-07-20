#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import cgi

def main():
    # ヘッダーの出力
    print("Content-type: text/html; charset=UTF-8\n")

    # カートの商品情報を仮想的に作成（実際はデータベースから取得する必要があります）
    cart_items = [
        {'product_name': '商品A', 'price': 1000, 'quantity': 2},
        {'product_name': '商品B', 'price': 500, 'quantity': 3},
        {'product_name': '商品C', 'price': 1500, 'quantity': 1}
    ]

    # HTMLの出力
    print("<!DOCTYPE html>")
    print("<html>")
    print("<head>")
    print("<meta charset='UTF-8'>")
    print("<title>購入確認ページ</title>")
    print("</head>")
    print("<body>")
    print("<h1>購入確認ページ（カートの内容表示）</h1>")
    
    if cart_items:
        print("<h2>購入内容の確認</h2>")
        print("<table>")
        print("<tr><th>商品名</th><th>価格</th><th>数量</th></tr>")
        for item in cart_items:
            print("<tr>")
            print("<td>{}</td>".format(item['product_name']))
            print("<td>{}</td>".format(item['price']))
            print("<td>{}</td>".format(item['quantity']))
            print("</tr>")
        print("</table>")
    else:
        print("<h2>カートが空です</h2>")
    
    print("<form action='purchase_complete.cgi' method='post'>")
    # その他のフォーム項目（配送先入力など）を追加
    print("<input type='submit' value='購入確定'>")
    print("</form>")
    print("</body>")
    print("</html>")

if __name__ == '__main__':
    try:
        main()
    except:
        # エラー処理
        print("Content-type: text/html; charset=UTF-8\n")
        print("<h1>エラーが発生しました</h1>")

