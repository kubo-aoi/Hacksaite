<!-- purchase_confirm.php -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>購入確認</title>
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
        echo '<h1>購入確認</h1>';
        echo '<div>クレジットカード情報</div>';
        echo '<div>カード番号: ' . $creditCard['card_number'] . '</div>';
        echo '<div>有効期限: ' . $creditCard['expiration_date'] . '</div>';
        echo '<div>セキュリティコード: ' . $creditCard['security_code'] . '</div>';
    } else {
        // クレジットカード情報が登録されていない場合
        echo '<h1>クレジットカード情報未登録</h1>';
        echo '<div>クレジットカード情報が登録されていません。</div>';
        echo '<a href="register_card.php">クレジットカード登録へ</a>';
    }
    
    // 購入内容を表示する処理を追加
    echo '<h2>購入内容の確認</h2>';
    echo '<div>商品名: ' . $product['name'] . '</div>';
    echo '<div>価格: ' . $product['price'] . '</div>';
    // その他の購入内容表示項目を追加
    
    ?>
    
    <form action="purchase_complete.php" method="post">
        <!-- 購入に関するフォーム項目 -->
        <!-- 例: 配送先の入力フォーム、購入確定ボタンなど -->
        <input type="submit" value="購入確定">
    </form>
    
</body>
</html>

