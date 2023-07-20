<!-- address_process.php -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>ログイン結果</title>
    <a href="top_page.cgi"><h1>
    <h1><img src= "./button/ComBuy.png" width="320"height="100"></h1>
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
// データベース接続情報
$host = "localhost";
$dbname = "ShopData";
$username = "user1";
$password = "passwordA1!";

try {
    // POSTデータ取得
    $user_id = $_POST['userid']; // Cookieからuseridを取得
    $yuubinbangou = $_POST['yuubinbangou'];
    $todouhuken = $_POST['todouhuken'];
    $sikutyouson = $_POST['sikutyouson'];
    $banchi = $_POST['banchi'];

    // データベース接続
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);

    // 既に住所情報が登録されているかチェック
    $stmt_check = $pdo->prepare("SELECT COUNT(*) FROM location WHERE User_id = :user_id");
    $stmt_check->bindParam(':user_id', $user_id, PDO::PARAM_STR);
    $stmt_check->execute();
    $count = $stmt_check->fetchColumn();

    if ($count > 0) {
        // 既に住所情報が登録されている場合は更新
        $stmt_update = $pdo->prepare("UPDATE location SET yuubinbangou = :yuubinbangou, todouhuken = :todouhuken, sikutyouson = :sikutyouson, banchi = :banchi WHERE User_id = :user_id");
        $stmt_update->bindParam(':user_id', $user_id, PDO::PARAM_STR);
        $stmt_update->bindParam(':yuubinbangou', $yuubinbangou, PDO::PARAM_STR);
        $stmt_update->bindParam(':todouhuken', $todouhuken, PDO::PARAM_STR);
        $stmt_update->bindParam(':sikutyouson', $sikutyouson, PDO::PARAM_STR);
        $stmt_update->bindParam(':banchi', $banchi, PDO::PARAM_STR);

        if ($stmt_update->execute()) {
            echo '<h1>更新完了</h1>';
            echo '<div class="success-message">住所情報が更新されました。</div>';
            echo '<a class="back-link" href="top_page.cgi">戻る</a>';
        } else {
            echo '<h1>エラー</h1>';
            echo '<div class="error-message">更新に失敗しました。</div>';
            echo '<a class="back-link" href="touroku.php">戻る</a>';
        }
    } else {
        // 住所情報が登録されていない場合は新規登録
        $stmt_insert = $pdo->prepare("INSERT INTO location (User_id, yuubinbangou, todouhuken, sikutyouson, banchi) VALUES (:user_id, :yuubinbangou, :todouhuken, :sikutyouson, :banchi)");
        $stmt_insert->bindParam(':user_id', $user_id, PDO::PARAM_STR);
        $stmt_insert->bindParam(':yuubinbangou', $yuubinbangou, PDO::PARAM_STR);
        $stmt_insert->bindParam(':todouhuken', $todouhuken, PDO::PARAM_STR);
        $stmt_insert->bindParam(':sikutyouson', $sikutyouson, PDO::PARAM_STR);
        $stmt_insert->bindParam(':banchi', $banchi, PDO::PARAM_STR);

        if ($stmt_insert->execute()) {
            echo '<h1>登録完了</h1>';
            echo '<div class="success-message">住所情報が登録されました。</div>';
            echo '<a class="back-link" href="top_page.cgi">戻る</a>';
        } else {
            echo '<h1>エラー</h1>';
            echo '<div class="error-message">登録に失敗しました。</div>';
            echo '<a class="back-link" href="touroku.php">戻る</a>';
        }
    }

} catch (PDOException $e) {
    echo '<h1>エラー</h1>';
    echo '<div class="error-message">データベース接続エラー: ' . $e->getMessage() . '</div>';
    echo '<a class="back-link" href="touroku.php">戻る</a>';
}
?>
</div>
</body>
</html>

