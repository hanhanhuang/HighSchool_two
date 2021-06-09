<?php
// 建立資料庫連線 & 選擇資料庫
$dbConnection = new mysqli('localhost', 'cas27', '48230504', 'cas27');
if ($dbConnection->connect_error) die("Connection failed: " . $dbConnection->connect_errno);

// 設定資料庫轉換字元集 
$dbConnection->query("SET NAMES 'utf8'");
$dbConnection->query("SET character_set_client = utf8;");
$dbConnection->query("SET character_set_results = utf8;");

// 設定 SQL 指令
$sql = "DELETE FROM scoreTable WHERE seatNo = $_GET[seatNo];";

// 輸入 SQL 指令
$statement = $dbConnection->prepare($sql);
// 執行 SQL 指令
$statement->execute();

// 網頁轉向
header("Location: http://$_SERVER[HTTP_HOST]".dirname($_SERVER['PHP_SELF'])."/hw01.php");
?>