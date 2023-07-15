<!-- top_page.php -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>トップページ</title>
</head>
<body>
    <?php
    // ログインしているユーザ情報を取得
    $username = $_COOKIE['userid'];
    // データベースに接続しクレジットカード情報を取得
    $pdo = new PDO("mysql:host=localhost;dbname=CreditCardData;charset=utf8", "user1", "passwordA1!");
    $sql = $pdo->prepare("SELECT * FROM credit_cards WHERE username = :username");
    $sql->bindValue(':username', $username, PDO::PARAM_STR);
    $sql->execute();
    $creditCard = $sql->fetch(PDO::FETCH_ASSOC);

    if ($creditCard) {
        // クレジットカード情報が登録されている場合
        echo '<h1>クレジット情報</h1>';
        echo '<div>カード番号: ' . $creditCard['card_number'] . '</div>';
        echo '<div>有効期限: ' . $creditCard['expiration_date'] . '</div>';
        echo '<div>セキュリティコード: ' . $creditCard['security_code'] . '</div>';
        echo '<a href="edit_card.php">変更する</a>';
    } else {
        // クレジットカード情報が登録されていない場合
        echo '<h1>クレジット情報</h1>';
        echo '<div>クレジットカード情報は登録されていません。</div>';
        echo '<a href="credit_card.php">クレジットカード登録</a>';
    }
    ?>
</body>
</html>

