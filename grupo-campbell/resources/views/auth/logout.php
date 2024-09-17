<?php
$access_token = "eyJzZXJ2ZXIiOiIxOTIuMTY4LjEyLjI1MSIsInNlcnZlck5hbWUiOiJWYWxsZSBTYWx1ZCJ9";
session_start();
session_unset(); // Destruye todas las variables de sesión
session_destroy(); // Destruye la sesión
header("Location: login?access_token={$access_token}");
exit;
?>
