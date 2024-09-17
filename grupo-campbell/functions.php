<?php
$dir = 'resources/views';
function loadView($viewName)
{
    global $dir;
    $file = __DIR__ . "/{$dir}/{$viewName}.php";
    if (file_exists($file)) {
        return $file;
    } else {
        return false;
    }
}
