<?php
$access_token = "eyJzZXJ2ZXIiOiIxOTIuMTY4LjEyLjI1MSIsInNlcnZlck5hbWUiOiJWYWxsZSBTYWx1ZCJ9";

session_start();

// default users
$users = [["username" => "demo.vallesalud", "password" => "123456", "server" => "192.168.12.251"], ["username" => "juan.madrid", "password" => "159951", "server" => "192.168.12.251"], ["username" => "julian.guzman", "password" => "1020", "server" => "192.168.23.251"], ["username" => "yolanda.bravo", "password" => "2030", "server" => "192.168.16.251"]];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $d_connection = "192.168.12.251";
    $username = $_POST['username'];
    $password = $_POST['password'];
    $server = $_POST['server'];
    $error = 'Incorrect user name or password.';
    foreach ($users as $user) {
        if ($username === $user['username'] && $password === $user['password']) {
            //
            if ($d_connection === $server) {
                $_SESSION['loggedin'] = true;
                $_SESSION['username'] = $username;
                header('Location: medical-note');
                exit;
            } else {
                $error = 'Wrong server connection';
            }
        }
    }
    $_SESSION['error'] = $error;
    header("Location: login?access_token={$access_token}");
    exit;
}
