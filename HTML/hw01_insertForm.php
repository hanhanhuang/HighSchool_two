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

	<body>
		<div class="container-fluid">
			<div class="row mt-1">
				<div class="col-md-8 offset-md-2">
					<div class="card">
						<div class="card-header bg-primary text-white text-center">
							<h2 class="text-center">新增學生資料作業</h2>
						</div>
						<div class="card-body">
							<form action="hw01_insert.php" method="post">
								座號：<input type="text" name="seatNo"><br>
								姓名：<input type="text" name="studentName"><br>
								國文：<input type="text" name="chinese"><br>
								英文：<input type="text" name="english"><br>
								數學：<input type="text" name="math"><br>
								專一：<input type="text" name="pro1"><br>
								專二：<input type="text" name="pro2"><br>
								<button class="btn btn-primary" type="submit">送出</button>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>