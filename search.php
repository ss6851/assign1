<html>
<link rel="stylesheet" type="text/css" href="stylesheet.css">
<body>

<h1> Web Audit Assignment One </h1>

<br>
<h2> Search Results </h2>
<br>

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
                        $searchUsername = $test[1];
                }
        }
}
echo $searchUsername;
if($searchUsername)
{
	$searchUsername = stripslashes($searchUsername);
	$searchUsername = mysqli_real_escape_string($conn, $searchUsername);
}

$sql = "SELECT username,first_name,last_name,email from reg_user where username='$searchUsername'";

$result = mysqli_query($conn, $sql);


if($result->num_rows > 0)
{
	while($r = mysqli_fetch_assoc($result))
	{
		echo "<p>Username: " . $r['username']. "</p><br><p>Name: " . $r['first_name'] . " " . $r['last_name'] . "</p><br><p>Email " . $r['email'] . "</p><br>";
	}
}
else
{
	echo '<script type="text/javascript">alert(\'NO RESULTS\')</script>';
        exit;
}
?>

<br><br>
<p> For a new search, please click the button below.</p>
<form action="search.html">
        <input type="submit" value="Search">
</form>

</body>
</html>

