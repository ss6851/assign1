<?php
$host="localhost"; // Host name
$username="root"; // Mysql username
$password="singh"; // Mysql password
$db_name="test"; // Database name
$tbl_name="reg_user"; // Table name

// Connect to server and select databse.
$conn = mysqli_connect($host , $username, $password, $db_name) or die("Failed connection");
?>
