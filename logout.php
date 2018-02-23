<?php
session_start();
$_SESSION['username']="cl0002";
echo $_SESSION['username'];
echo "\n";
if(isset($_SESSION['username']))
{
	echo "logout\n";
	$_SESSION['username']="";
	session_destroy();
	echo $_SESSION['username'];
}
header("location:site.html");
?>
