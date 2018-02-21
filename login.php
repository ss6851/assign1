<html>
<?php
session_start();
require('db_connect.php');
// username and password sent from form
$myusername=$_POST['username'];
$mypassword=$_POST['password'];

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
	$_SESSION['login']=true;
	// Register $myusername and redirects to successful login in page"
	$_SESSION['username'] = $myusername;
	header("location:successLG.php");
}
else {

	echo '<script type="text/javascript">alert(\'FAILED LOGIN\')</script>';
        exit;
}
?>
</html>
