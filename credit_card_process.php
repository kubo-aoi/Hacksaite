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
$cardnumber = $_POST['cardnumber'];
$expiration = $_POST['expiration'];
$cvv = $_POST['cvv'];

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
    $userid = $_SESSION['userid'];

    // クレジットカード情報の登録
    $sql = "INSERT INTO credit_cards (userid, cardnumber, expiration, cvv) VALUES (:userid, :cardnumber, :expiration, :cvv)";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':userid', $userid, PDO::PARAM_INT);
    $stmt->bindParam(':cardnumber', $cardnumber, PDO::PARAM_STR);
    $stmt->bindParam(':expiration', $expiration, PDO::PARAM_STR);
    $stmt->bindParam(':cvv', $cvv, PDO::PARAM_STR);
    $stmt->execute();

    // 成功メッセージを表示
    echo "クレジットカード情報が正常に登録されました。";
    echo '<a href="address_registration.php">住所登録画面へ</a><br><br>';
    echo '<a href="login.cgi">戻る</a>';

} catch (PDOException $e) {
    // エラーメッセージを表示
    echo "クレジットカード情報の登録中にエラーが発生しました。";
    echo $e->getMessage();
    echo '<a href="credit_card.php">クレジット登録画面に戻る</a><br><br>';
    echo '<a href="address_registration.php">住所登録画面へ</a>';
}
?>

