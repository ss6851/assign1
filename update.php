<?php
//require('db_connect.php');
$host="localhost"; // Host name
$username="root"; // Mysql username
$password="hello"; // Mysql password
$db_name="test"; // Database name
$tbl_name="reg_user"; // Table name

$conn = mysqli_connect($host , $username, $password, $db_name) or die("Failed connection");
// username and password sent from form
$file = fopen("test.txt", "r");
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

$sql = "UPDATE reg_user SET username='$newUsername', first_name='$newFirstName', last_name='$newLastName', email='$newEmail', password='$newPassword' where username='$newUsername'";

$result = mysqli_query($conn, $sql);

print_r($result);
if($result)
{
	//header("location:successLG.php");
} 
else
{
	//echo '<script type="text/javascript">alert(\'FAILED UPDATE\')</script>';
        //exit;
}
?>

