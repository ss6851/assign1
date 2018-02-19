<?php
require('db_connect.php');

if(isset($_POST['username']))
{
	$searchUsername = $_POST['username'];
	$searchUsername = stripslashes($searchUsername);
	$searchUsername = mysqli_real_escape_string($conn, $searchUsername);
}

$sql = "SELECT username,first_name,last_name,email from reg_user where username='$searchUsername'";

$result = mysqli_query($conn, $sql);

if($result->num_rows > 0)
{
	while($r = mysqli_fetch_assoc($result))
	{
		echo "Username: " . $r['username']. "-Name: " . $r['first_name'] . " " . $r['last_name'] . " " . $r['email'] . "<br>";
	}
}
else
{
	echo "No Results Found";
}
