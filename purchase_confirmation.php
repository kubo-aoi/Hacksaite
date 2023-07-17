<!-- purchase_confirmation.php -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>購入確認画面</title>
</head>
<body>
    <?php
    // ユーザ名からユーザIDを取得
	$pdo = new PDO("mysql:host=localhost;dbname=ShopData;charset=utf8", "user1", "passwordA1!");
	$userid = $_COOKIE['userid'];
	$sql = $pdo->prepare("SELECT id FROM userinfo WHERE userid = :userid");
	$sql->bindValue(':userid', $userid, PDO::PARAM_STR);
	$sql->execute();
	$user = $sql->fetch(PDO::FETCH_ASSOC);

	if (!$user) {
	    echo '<h1>クレジットカード登録エラー</h1>';
	    echo '<div>ユーザ情報が見つかりません。</div>';
	    echo '<a href="purchase.php">戻る</a>';
	    exit;
	}

	$userid = $user['id'];

    // データベースに接続しクレジットカード情報を取得
    $pdo = new PDO("mysql:host=localhost;dbname=ShopData;charset=utf8", "user1", "passwordA1!");
    $sql = $pdo->prepare("SELECT * FROM credit_cards WHERE userid = :userid");
    $sql->bindValue(':userid', $userid, PDO::PARAM_STR);
    $sql->execute();
    $creditCard = $sql->fetch(PDO::FETCH_ASSOC);

    if ($creditCard) {
        // クレジットカード情報が登録されている場合
        echo '<h1>クレジットカード登録情報確認</h1>';
        echo '<div>カード番号: ' . $creditCard['card_number'] . '</div>';
        echo '<div>有効期限: ' . $creditCard['expiration_date'] . '</div>';
        echo '<div>セキュリティコード: ' . $creditCard['security_code'] . '</div>';
        echo '<form action="purchase.php" method="post">';
        echo '    <input type="hidden" name="card_number" value="' . $creditCard['card_number'] . '">';
        echo '    <input type="hidden" name="expiration_date" value="' . $creditCard['expiration_date'] . '">';
        echo '    <input type="hidden" name="security_code" value="' . $creditCard['security_code'] . '">';
        echo '    <input type="submit" value="クレジットカード情報の変更">';
        echo '</form>';
        echo '<form action="purchase.php" method="post">';
        echo '    <input type="submit" value="購入手続きへ進む">';
        echo '</form>';
    } else {
        // クレジットカード情報が登録されていない場合
        echo '<h1>クレジットカード未登録</h1>';
        echo '<div>クレジットカード情報が登録されていません。</div>';
        echo '<a href="register_card.php">クレジットカード登録</a>';
        echo '<a href="purchase.php">戻る</a>';
    }
    ?>
    <h2>購入内容の確認</h2>
    <!-- 購入内容の表示 -->
    <!-- その他の表示項目やボタンを追加 -->
    
    <form action="purchase_complete.php" method="post">
        <!-- 購入に関するフォーム項目 -->
        <!-- 例: 配送先の入力フォーム、購入確定ボタンなど -->
        <input type="submit" value="購入確定">
</body>
</html>

