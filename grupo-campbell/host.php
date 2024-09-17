<?php
// Se define los dominios {public,private}
$dir = "/grupo-campbell";
$protocol = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off' || $_SERVER['SERVER_PORT'] == 443) ? "https://" : "http://";
$host = $_SERVER['HTTP_HOST'];
$domain = $protocol . $host . $dir;
define('CURL', $domain); // Cambia esto por tu dominio real si es necesario
define('APP_NAME', 'Notas Hospitalización');
define('LOGIN_NAME', 'Portal - Iniciar sesión');
