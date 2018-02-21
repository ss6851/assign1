<?php
	session_start();
?>
<!DOCTYPE html>
<html>
<link rel="stylesheet" type="text/css" href="stylesheet.css">
<body>

<h1> Web Audit Assignment One </h1>

<h2> Welcome to Our Web Server <?php if($_SESSION['login']==true){ echo $_SESSION['username']; } ?></h2> 
<br><br>
<p>If you wish to update your information in our database, please click the button below.</p>
<form action="update.html">
	<input type="submit" value="Update">
</form>

<br><br>
<p> If you wish to search for other users, click on the button below.</p>
<form action="search.html">
	<input type="submit" value="Search">
</form>

<br><br>
<p> To log out, please click the button below.</p>
<form action="logout.php">
	<input type="submit" value="Logout">
</form>
</body>
</html>
