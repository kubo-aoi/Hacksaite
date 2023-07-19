<!-- login_main.php -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>ログイン結果</title>
    <a href="top_page.cgi"><h1>
    <img src= "./button/ComBuy.png" width="320"height="100">
    </h1></a>
    <style>
        body {
            background:linear-gradient(180deg, #000000 0%, #000000 27%, #fffaf0 27%, #fffaf0 100%);
            background-repeat:no-repeat;
            font-family: Arial, sans-serif;
            background-color:#fffaf0;
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

        .error-message {
            color: #ff0000;
            text-align: center;
            margin-bottom: 20px;
        }

        .success-message {
            color: #00cc00;
            text-align: center;
            margin-bottom: 20px;
        }

        .back-link {
            display: block;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <?php
        // フォームからの値をそれぞれ変数に代入
        $user = $_POST['userid'];
        $password = $_POST['pass'];
        // SQLの準備（接続先、DB名、DBログインユーザ名、パスワード・・・・）
        $pdo = new PDO("mysql:host=localhost;dbname=ShopData;charset=utf8", "user1", "passwordA1!", [PDO::ATTR_ERRMODE => PDO::ERRMODE_WARNING]);
        $sql = $pdo->prepare("SELECT * FROM userinfo WHERE userid = :userid AND password = :pass");
        // SQL文への値の設定
        $sql->bindValue(':userid', $user, PDO::PARAM_STR);
        $sql->bindValue(':pass', $password, PDO::PARAM_STR);
        // SQL文の実行
        $sql->execute();
        // 結果の取得
        $result = $sql->fetchAll();
        if (!$result) {
            echo '<h1>ログイン結果</h1><br>';
            echo '<div class="error-message">ログインに失敗しました．</div>';
            echo '<a class="back-link" href="login.php">戻る</a>';
        } else {
            foreach ($result as $loop) {
                echo '<h1>ログイン結果</h1>';
                echo '<div class="success-message">ログインに成功しました</div>';
                echo '<div>' . $loop['userid'] . 'さん、こんにちは</div>';

                // クッキーにユーザ情報を保存
                setcookie('userid', $loop['userid'], time() + 3600, '/'); // 1時間有効なクッキー
                setcookie('pass', $loop['pass'], time() + 3600, '/');
                
                echo '<a class="back-link" href="top_page.cgi">トップページへ</a>';
                echo '<a class="back-link" href="login.php">ログアウト</a>';
                echo '<a class="back-link" href="credit_card.php">クレジットカード登録</a>';
            }
        }
        ?>
    </div>
</body>
</html>

