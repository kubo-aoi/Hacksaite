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
    echo '<a href="purchase.php">戻る</a>';
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
    $cardId = $existingCard['card_id'];
    $updateSql = "UPDATE credit_cards SET card_number = :card_number, expiration_date = :expiration_date, security_code = :security_code WHERE card_id = :card_id";
    $stmt = $pdo->prepare($updateSql);
    $stmt->bindValue(':card_number', $cardNumber, PDO::PARAM_STR);
    $stmt->bindValue(':expiration_date', $expirationDate, PDO::PARAM_STR);
    $stmt->bindValue(':security_code', $securityCode, PDO::PARAM_STR);
    $stmt->bindValue(':card_id', $cardId, PDO::PARAM_INT);
    $stmt->execute();

    echo '<h1>クレジットカード情報変更完了</h1>';
    echo '<div>クレジットカード情報が変更されました。</div>';
    echo '<a href="purchase.php">戻る</a>';
} else {
    // クレジットカードが登録されていない場合は新規登録する処理を追加
    $insertSql = "INSERT INTO credit_cards (userid, card_number, expiration_date, security_code) VALUES (:userid, :card_number, :expiration_date, :security_code)";
    $stmt = $pdo->prepare($insertSql);
    $stmt->bindValue(':userid', $userid, PDO::PARAM_STR);
    $stmt->bindValue(':card_number', $cardNumber, PDO::PARAM_STR);
    $stmt->bindValue(':expiration_date', $expirationDate, PDO::PARAM_STR);
    $stmt->bindValue(':security_code', $securityCode, PDO::PARAM_STR);
    $stmt->execute();

    echo '<h1>クレジットカード登録完了</h1>';
    echo '<div>クレジットカード情報が登録されました。</div>';
    echo '<a href="purchase.php">戻る</a>';
}
?>

