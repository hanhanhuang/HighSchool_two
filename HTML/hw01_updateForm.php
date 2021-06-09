<!DOCTYPE html>

<html lang="en">
	<head>
		<title>甲班 27 黃韋翰 14-1</title>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>		
	</head>
	
<?php
	// 建立資料庫連線 & 選擇資料庫
	$dbConnection = new mysqli('localhost', 'cas27', '48230504', 'cas27');
	if ($dbConnection->connect_error) die("Connection failed: " . $dbConnection->connect_errno);
	
	// 設定資料庫轉換字元集 
	$dbConnection->query("SET NAMES 'utf8'");
	$dbConnection->query("SET character_set_client = utf8;");
	$dbConnection->query("SET character_set_results = utf8;");
	
	// 設定 SQL 指令
	$sql = "SELECT * FROM scoreTable WHERE seatNo='$_GET[seatNo]';";

	// 輸入 SQL 指令
	$statement = $dbConnection->prepare($sql);
	// 執行 SQL 指令
	$statement->execute();
	// 取出查詢結果
	$result = $statement->get_result();
	$student = $result->fetch_assoc();
	?>
	
	<body>
		<div class="container-fluid">
			<div class="row mt-1">
				<div class="col-md-8 offset-md-2">
					<div class="card">
						<div class="card-header bg-primary text-white text-center">
							<h2 class="text-center">修改學生資料作業</h2>
						</div>
						<div class="card-body">
							<form action="hw01_update.php" method="post">
								<!-- 將唯一鍵值--座號以隱藏變數的方式傳遞到下一網頁。-->
								<input type="hidden" name="seatNo" value="<?php echo $student['seatNo']?>"><br>
								
								姓名：<input type="text" name="studentName" value="<?php echo $student['studentName']?>"><br>
								國文：<input type="text" name="chinese" value="<?php echo $student['chinese']?>"><br>
								英文：<input type="text" name="english" value="<?php echo $student['english']?>"><br>
								數學：<input type="text" name="math" value="<?php echo $student['math']?>"><br>
								專一：<input type="text" name="pro1" value="<?php echo $student['pro1']?>"><br>
								專二：<input type="text" name="pro2" value="<?php echo $student['pro2']?>"><br>
								<button class="btn btn-primary" type="submit">送出</button>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>