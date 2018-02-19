<?php
session_start();
if(!$_SESSION["myusername"]){
header("main_login.php");
}
?>

<table width="300" border="0" align="center" cellpadding="0" cellspacing="1" bgcolor="#CCCCCC">
	<tr>
	<form name="logout" method="get" action="logout.php">
	<td>
	<td><input="submit" name="Logout" value="Logout"></td>
	</td>
	</form>
	</tr>
</table>
