<!-- register_process.php -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>新規登録結果</title>
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

        // 既存ユーザーのチェック
        $sql = $pdo->prepare("SELECT * FROM userinfo WHERE userid = :userid");
        $sql->bindValue(':userid', $user, PDO::PARAM_STR);
        $sql->execute();
        $result = $sql->fetchAll();

        if ($result) {
            echo '<h1>新規登録結果</h1>';
            echo '<div class="error-message">既に存在するユーザーIDです．</div>';
            echo '<a class="back-link" href="register.php">戻る</a>';
        } else {
            // 新規ユーザーの登録
            $sql = $pdo->prepare("INSERT INTO userinfo (userid, password) VALUES (:userid, :pass)");
            $sql->bindValue(':userid', $user, PDO::PARAM_STR);
            $sql->bindValue(':pass', $password, PDO::PARAM_STR);
            $sql->execute();

            echo '<h1>新規登録結果</h1>';
            echo '<div class="success-message">新規登録が完了しました．</div>';
            echo '<a class="back-link" href="login.php">ログイン</a>';
        }
        ?>
    </div>
</body>
</html>

