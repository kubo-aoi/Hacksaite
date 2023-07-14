<!-- register.php -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>新規登録</title>
    <a href="top_page.cgi"><h1>
    <img src= "ボタン/ボタン/サイトロゴComBuy.png" width="320"height="100">
    </h1></a>
    <style>
        body {
            background:linear-gradient(180deg, #000000 0%, #000000 25%, #fffaf0 25%, #fffaf0 100%);
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

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            color: #555;
        }

        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            border-radius: 3px;
            border: 1px solid #ccc;
        }

        input[type="submit"] {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            color: #fff;
            background-color: #007bff;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #0069d9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>新規登録</h1>
        <form method="POST" action="register_process.php">
            <div class="form-group">
                <label for="userid">ユーザーID:</label>
                <input type="text" id="userid" name="userid" required>
            </div>
            <div class="form-group">
                <label for="pass">パスワード:</label>
                <input type="password" id="pass" name="pass" required>
            </div>
            <input type="submit" value="登録">
        </form>
    </div>
</body>
</html>

