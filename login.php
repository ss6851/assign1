<?php
//require('db_connect.php');
$host="localhost"; // Host name
$username="root"; // Mysql username
$password="singh"; // Mysql password
$db_name="test"; // Database name
$tbl_name="reg_user"; // Table name

$conn = mysqli_connect($host , $username, $password, $db_name) or die("Failed connection");
// username and password sent from form
$file = fopen("post_input.txt", "r");
if($file)
{
	while(($line = fgets($file)) !== false)
	{
		$line = trim($line, "\n");
		$test = explode(" ",$line);
		if($test[0]=='username:')
		{
			$myusername = $test[1];

		}
		else if($test[0]=='password:')
		{
			$mypassword = $test[1];

		}
	}
}


// To protect MySQL injection (more detail about MySQL injection)
$myusername = stripslashes($myusername);
$mypassword = stripslashes($mypassword);
$myusername = mysqli_real_escape_string($conn, $myusername);
$mypassword = mysqli_real_escape_string($conn, $mypassword);

$sql="SELECT * FROM $tbl_name WHERE username='$myusername' and password='$mypassword'";
$result=mysqli_query($conn, $sql);

// Mysql_num_row is counting table row
$count=mysqli_num_rows($result);

// If result matched $myusername and $mypassword, table row must be 1 row

if($count==1){
	echo "It works\n";
	$_SESSION['login']=true;
	// Register $myusername and redirects to successful login in page"
	$_SESSION['username'] = $myusername;
	echo $_SESSION['username'];
	echo "<script>window.location.replace('/site.html');</script>";
}
else {
	//echo "FAILED LOGIN";
	echo "<script>alert(\'FAILED LOGIN\');</script>";
    exit;
}
?>
