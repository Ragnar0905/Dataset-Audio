<?php
// Incluye el archivo host
require 'host.php';
// Incluye el archivo de funciones
require 'functions.php';
// Obtiene la página solicitada (si no se especifica, por defecto es 'home')
$page = $_GET['view'] ?? '';
// Carga la vista correspondiente
$view = loadView($page);
if ($view) {
    // Incluye la plantilla principal
    include "{$dir}/layouts/app.php";
} else {
    http_response_code(404); // Establece código de respuesta HTTP 404
    include "{$dir}/404.php"; // Incluye la vista de error personalizada
    exit;
}
