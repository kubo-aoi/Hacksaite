<!-- credit_card.php -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>クレジットカード登録</title>
    <link rel="stylesheet" type="text/css" href="credit_card.css"/>
    <h1><img src= "./button/ComBuy.png" width="320" heighr ="100"></h1>
    <style>
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

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
        }

        .form-group input[type="text"],
        .form-group input[type="number"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .form-group input[type="submit"] {
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            border: none;
            color: white;
            border-radius: 5px;
            cursor: pointer;
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
        <h1>クレジットカード登録</h1>
        <form action="credit_card_process.php" method="post">
            <div class="form-group">
                <label for="card_number">カード番号</label>
                <input type="text" pattern="\d{16}" id="card_number" name="card_number" required>
            </div>
            <div class="form-group">
                <label for="expiration_date">有効期限</label>
                <input type="text" pattern="\d{2}/\d{2}" id="expiration_date" name="expiration_date" required>
            </div>
            <div class="form-group">
                <label for="security_code">セキュリティコード</label>
                <input type="number" pattern="\d{3}"id="security_code" name="security_code" required>
            </div>
            <input type="submit" value="登録">
        </form>
        <a class="back-link" href="top_page.cgi">戻る</a>
    </div>
</body>
</html>

