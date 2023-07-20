<!-- address_registration.php -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>住所登録画面</title>
</head>
<body>
    <h1>住所登録</h1>
    <form action="address_process.php" method="post">
        <input type="hidden" name="userid" value="<?php echo $_COOKIE['userid']; ?>">
        <label for="yuubinbangou">郵便番号：</label>
        <input type="text" id="yuubinbangou" name="yuubinbangou" required><br>

        <label for="todouhuken">都道府県：</label>
        <input type="text" id="todouhuken" name="todouhuken" required><br>

        <label for="sikutyouson">市区町村：</label>
        <input type="text" id="sikutyouson" name="sikutyouson" required><br>

        <label for="banchi">番地：</label>
        <input type="text" id="banchi" name="banchi" required><br>

        <input type="submit" value="登録">
    </form>
</body>
</html>

