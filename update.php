<?php
require('db_connect.php');

if(isset($_POST['username']) && isset($_POST['password']))
{
	$newUsername = $_POST['username'];
	$newEmail = $_POST['email'];
	$newFirstName = $_POST['firstname'];
	$newLastName = $_POST['lastname'];
	$newPassword = $_POST['password'];
}

//Cleanses data to prevent SQL injection
$newUsername = stripslashes($newUsername);
$newUsername = mysqli_real_escape_string($conn, $newUsername);
$newEmail = stripslashes($newEmail);
$newEmail = mysqli_real_escape_string($conn, $newEmail);
$newFirstName = stripslashes($newFirstName);
$newFirstName = mysqli_real_escape_string($conn, $newFirstName);
$newLastName = stripslashes($newLastName);
$newLastName = mysqli_real_escape_string($conn, $newLastName);
$newPassword = stripslashes($newPassword);
$newPassword = mysqli_real_escape_string($conn, $newPassword);

$sql = "UPDATE reg_user SET username='$newUsername', first_name='$newFirstName', last_name='$newLastName', email='$newEmail', password='$newPassword' where username='$newUsername'";

$result = mysqli_query($conn, $sql);

print_r($result);
if($result->num_rows > 0)
{
	//header("location:successLG.php");
} 
else
{
	//echo '<script type="text/javascript">alert(\'FAILED UPDATE\')</script>';
        //exit;
}
?>

