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
	
	$subject="seatNo";
	$updown="ASC";
	Switch($_GET[value]){
		case seatNo:
			$subject="seatNo";
			$updown="ASC";
			break;
		case chinese:
			$subject="chinese";
			$updown="DESC";
			break;
		case english:
			$subject="english";
			$updown="DESC";
			break;			
		case math:
			$subject="math";
			$updown="DESC";
			break;
		case pro1:
			$subject="pro1";
			$updown="DESC";	
			break;
		case pro2:
			$subject="pro2";
			$updown="DESC";
			break;
		case total:
			$subject="total";
			$updown="DESC";
			break;
	}

	// 設定 SQL 指令
	$sql = "SELECT *, "
				."(chinese + english + math + pro1 + pro2) AS total, "
				."(chinese + english + math + pro1 + pro2) / 5 AS average "
				."FROM scoreTable WHERE 1 ORDER BY ".$subject." ".$updown.";";
	
	// 輸入 SQL 指令
	$statement = $dbConnection->prepare($sql);
	// 執行 SQL 指令
	$statement->execute();
	// 取出查詢結果
	$result = $statement->get_result();
	?>
	

	<body>
		<div class="container-fluid">
			<div class="row mt-1">
				<div class="col-md-8 offset-md-2">
					<div class="card">
						<div class="card-header bg-primary text-white text-center">
							<h2 class="text-center">scoreTable 中的資料</h2>
							<p>修改資料</p>
						</div>
						<div class="card-body">
							<table class="table table-bordered table-hover">
								<thead>
									
									<tr>
										<th><a href="hw01.php?value=seatNo">座號</a></th>
										<th>姓名</th>
										<th><a href="hw01.php?value=chinese">國文</a></th>
										<th><a href="hw01.php?value=english">英文</a></th>
										<th><a href="hw01.php?value=math">數學</a></th>
										<th><a href="hw01.php?value=pro1">專一</a></th>
										<th><a href="hw01.php?value=pro2">專二</a></th>
										<th><a href="hw01.php?value=total">總分</a></th>
										<th>平均</th>
										<th>操作區</th>
									</tr>
									
								</thead>
								<tbody>
									<?php
									while ($student = $result->fetch_assoc()) {
									?>
									<tr>
										<td><?php echo $student['seatNo'];?></td>
										<td><?php echo $student['studentName'];?></td>
										<?php $Chinese=$student['chinese'];
											  if($Chinese<60) echo "<td style=\"color:red\">$Chinese</td>";
												else echo "<td>$Chinese</td>";?>
										<?php $English=$student['english'];
											  if($English<60) echo "<td style=\"color:red\">$English</td>";
												else echo "<td>$English</td>";?>
										<?php $Math=$student['math'];
											  if($Math<60) echo "<td style=\"color:red\">$Math</td>";
												else echo "<td>$Math</td>";?>
										<?php $Pro1=$student['pro1'];
											  if($Pro1<60) echo "<td style=\"color:red\">$Pro1</td>";
												else echo "<td>$Pro1</td>";?>
										<?php $Pro2=$student['pro2'];
											  if($Pro2<60) echo "<td style=\"color:red\">$Pro2</td>";
												else echo "<td>$Pro2</td>";?>
										<td><?php echo $student['total'];?></td>
										<?php $Average=$student['average'];
											  if($Average<60) echo "<td style=\"color:red\">$Average</td>";
												else echo "<td>$Average</td>";?>
										<td><a href="hw01_updateForm.php?seatNo=<?php echo $student['seatNo'];?>">修改/編輯</a>
											<a href="hw01_delete.php?seatNo=<?php echo $student['seatNo'];?>">刪除</a></td>
									</tr>
									<?php
									}
									?>
								</tbody>
								<form action="hw01_insertForm.php" method="post">
									<button class="btn btn-primary" type="submit">新增學生</button>
								</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>