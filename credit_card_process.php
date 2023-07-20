<!-- credit_card_process.php -->
<?php
session_start();

// ログインしているユーザ情報を確認
if (!isset($_COOKIE['userid'])) {
    // ユーザがログインしていない場合はリダイレクトなどの処理を行う
    header("Location: login.php");
    exit;
}

// フォームからの値をそれぞれ変数に代入
$card_number = $_POST['card_number'];
$expiration_date = $_POST['expiration_date'];
$security_code = $_POST['security_code'];

// データベースへの接続情報
$host = 'localhost';
$dbname = 'ShopData';
$username = 'user1';
$password = 'passwordA1!';

try {
    // データベースへの接続
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // ログインしているユーザのIDを取得
    $userid = $_COOKIE['userid'];

    // クレジットカード情報の登録
    $sql = "INSERT INTO credit_cards (userid, card_number, expiration_date, security_code) VALUES (:userid, :card_number, :expiration_date, :security_code)";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':userid', $userid, PDO::PARAM_STR);
    $stmt->bindParam(':card_number', $card_number, PDO::PARAM_STR);
    $stmt->bindParam(':expiration_date', $expiration_date, PDO::PARAM_STR);
    $stmt->bindParam(':security_code', $security_code, PDO::PARAM_INT);
    $stmt->execute();

    // 成功メッセージを表示
    echo "クレジットカード情報が正常に登録されました。";
    echo '<a href="address_registration.php">住所登録画面へ</a><br><br>';
    echo '<a href="login.php">戻る</a>';

} catch (PDOException $e) {
    // エラーメッセージを表示
    echo "クレジットカード情報の登録中にエラーが発生しました。<br><br>";
    echo $e->getMessage();
    echo '<br><br><a href="credit_card.php">クレジット登録画面に戻る</a>';
}
?>

