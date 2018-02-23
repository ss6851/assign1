<?php
require('db_connect.php');
$host="localhost"; // Host name
$username="root"; // Mysql username
$password="singh"; // Mysql password
$db_name="test"; // Database name
$tbl_name="reg_user"; // Table name

$newUsername="";
$newEmail="";
$newFirstName="";
$newLastName="";
$newPassword="";

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
                        $newUsername = $test[1];
                }
                else if($test[0]=='password:')
                {
                        $newPassword = $test[1];
                }
		else if($test[0]=='firstname:')
                {
                        $newFirstName = $test[1];
                }
		else if($test[0]=='lastname:')
                {
                        $newLastName = $test[1];
                }
		else if($test[0]=='email:')
                {
                        $newEmail = $test[1];
                }
        }
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
//Query to add user
$sql = "INSERT INTO $tbl_name (username, first_name, last_name, email, password) VALUES ('$newUsername','$newFirstName','$newLastName', '$newEmail', '$newPassword')";
//Does the actual query
$result = mysqli_query($conn, $sql);
//Validates the success of the user addition
if($result)
{
header("location:site.html");
} 
else
{       
	echo '<script type="text/javascript">alert(\'FAILED REGISTRATION\')</script>';
        exit;
}
?>

