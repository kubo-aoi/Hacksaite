<!-- register_card.php -->
<?php
// クレジットカード情報を取得
$cardNumber = $_POST['card_number'];
$expirationDate = $_POST['expiration_date'];
$securityCode = $_POST['security_code'];

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
    echo '<a href="top_page.cgi">戻る</a>';
    exit;
}
$userid = $user['id'];

// クレジットカード情報を検索
$sql = $pdo->prepare("SELECT * FROM credit_cards WHERE userid = :userid");
$sql->bindValue(':userid', $userid, PDO::PARAM_STR);
$sql->execute();
$existingCard = $sql->fetch(PDO::FETCH_ASSOC);

// クレジットカード情報の登録または更新
if ($existingCard) {
    // すでにクレジットカードが登録されている場合は変更する処理を追加
    echo '<h1>クレジットカード情報変更</h1>';
    echo '<form action="register_card.php" method="post">';
    echo '    <label for="card_number">カード番号</label>';
    echo '    <input type="text" id="card_number" name="card_number" value="' . $existingCard['card_number'] . '" required><br>';
    echo '    <label for="expiration_date">有効期限</label>';
    echo '    <input type="text" id="expiration_date" name="expiration_date" value="' . $existingCard['expiration_date'] . '" required><br>';
    echo '    <label for="security_code">セキュリティコード</label>';
    echo '    <input type="text" id="security_code" name="security_code" value="' . $existingCard['security_code'] . '" required><br>';
    echo '    <input type="submit" value="変更">';
    echo '</form>';

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        // クレジットカード情報の変更を処理
        $updateSql = "UPDATE credit_cards SET card_number = :card_number, expiration_date = :expiration_date, security_code = :security_code WHERE userid = :userid";
        $stmt = $pdo->prepare($updateSql);
        $stmt->bindValue(':card_number', $cardNumber, PDO::PARAM_STR);
        $stmt->bindValue(':expiration_date', $expirationDate, PDO::PARAM_STR);
        $stmt->bindValue(':security_code', $securityCode, PDO::PARAM_STR);
        $stmt->bindValue(':userid', $userid, PDO::PARAM_INT);
        $stmt->execute();

        echo '<h1>クレジットカード情報変更完了</h1>';
        echo '<div>クレジットカード情報が変更されました。</div>';
        echo '<a href="top_page.cgi">戻る</a>';
    }
} else {
    // クレジットカードが登録されていない場合は新規登録する処理を追加
    echo '<h1>クレジットカード登録</h1>';
    echo '<form action="register_card.php" method="post">';
    echo '    <label for="card_number">カード番号</label>';
    echo '    <input type="text" id="card_number" name="card_number" required><br>';
    echo '    <label for="expiration_date">有効期限</label>';
    echo '    <input type="text" id="expiration_date" name="expiration_date" required><br>';
    echo '    <label for="security_code">セキュリティコード</label>';
    echo '    <input type="text" id="security_code" name="security_code" required><br>';
    echo '    <input type="submit" value="登録">';
    echo '</form>';

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        // クレジットカード情報の登録を処理
        $insertSql = "INSERT INTO credit_cards (userid, card_number, expiration_date, security_code) VALUES (:userid, :card_number, :expiration_date, :security_code)";
        $stmt = $pdo->prepare($insertSql);
        $stmt->bindValue(':userid', $userid, PDO::PARAM_STR);
        $stmt->bindValue(':card_number', $cardNumber, PDO::PARAM_STR);
        $stmt->bindValue(':expiration_date', $expirationDate, PDO::PARAM_STR);
        $stmt->bindValue(':security_code', $securityCode, PDO::PARAM_STR);
        $stmt->execute();

        echo '<h1>クレジットカード登録完了</h1>';
        echo '<div>クレジットカード情報が登録されました。</div>';
        echo '<a href="top_page.cgi">戻る</a>';
    }
}
?>
