<!-- purchase.php -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>購入画面</title>
    <a href="top_page.cgi"><h1>
    <img src= "ボタン/ボタン/サイトロゴComBuy.png" width="320"height="100">
    </h1></a>
    <style>
        body {
            background-color: #f2f2f2;
            font-family: Arial, sans-serif;
        }

        .container {
            max-width: 400px;
            margin: 0 auto;
            padding: 40px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
            margin-top: 0;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
        }

        .form-group input[type="text"],
        .form-group input[type="number"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .form-group input[type="submit"] {
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            border: none;
            color: white;
            border-radius: 5px;
            cursor: pointer;
        }

        .back-link {
            display: block;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <?php
    // ログインしているユーザ情報を取得
    $userid = $_COOKIE['userid'];
    // データベースに接続しクレジットカード情報を取得
    $pdo = new PDO("mysql:host=localhost;dbname=ShopData;charset=utf8", "user1", "passwordA1!");
    $sql = $pdo->prepare("SELECT * FROM credit_cards WHERE userid = :userid");
    $sql->bindValue(':userid', $userid, PDO::PARAM_STR);
    $sql->execute();
    $creditCard = $sql->fetch(PDO::FETCH_ASSOC);

    if ($creditCard) {
        // クレジットカード情報が登録されている場合
        echo '<h1>購入画面</h1>';
        echo '<div>クレジットカード情報</div>';
        echo '<div>カード番号: ' . $creditCard['card_number'] . '</div>';
        echo '<div>有効期限: ' . $creditCard['expiration_date'] . '</div>';
        echo '<div>セキュリティコード: ' . $creditCard['security_code'] . '</div>';
    } else {
        // クレジットカード情報が登録されていない場合
        echo '<h1>クレジットカード情報の入力</h1>';
        echo '<form action="register_card.php" method="post">';
        echo '    <label for="card_number">カード番号</label>';
        echo '    <input type="text" id="card_number" name="card_number" required><br>';
        echo '    <label for="expiration_date">有効期限</label>';
        echo '    <input type="text" id="expiration_date" name="expiration_date" required><br>';
        echo '    <label for="security_code">セキュリティコード</label>';
        echo '    <input type="text" id="security_code" name="security_code" required><br>';
        echo '    <input type="submit" value="登録">';
        echo '</form>';
    }
    ?>
</body>
</html>

