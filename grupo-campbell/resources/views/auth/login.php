<?php
require __DIR__ . '../../../../host.php';
session_start();
if (isset($_SESSION['loggedin']) && $_SESSION['loggedin'] === true) {
    header('Location: medical-note'); // Redirige a la página principal o a donde desees
    exit;
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="public/src/img/icon-julaje.ico" type="image/x-icon">
    <title><?php echo LOGIN_NAME ?></title>
    <link rel="canonical" href="<?php echo CURL; ?>/login">
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap">
    <!-- Style Bootstrap -->
    <link rel="stylesheet" href="https://getbootstrap.com/docs/5.3/dist/css/bootstrap.min.css">
    <!-- Icon Bootstrap -->
    <link rel="stylesheet" href="https://icons.getbootstrap.com/assets/font/bootstrap-icons.min.css">
    <!-- Icon - Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css">
    <!-- SweetAlert -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@11/dist/sweetalert2.min.css">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
        }
    </style>
</head>

<body>
    <div class="container-fluid">
        <div class="row">
            <div class="col-12 col-sm-12 col-md-12 col-lg-6 m-auto mt-1 mt-sm-1 mt-md-4 mt-lg-4 mt-xl-4 mt-xxl-5">
                <div class="card shadow bg-body-tertiary">
                    <form class="card-body needs-validation" action="signin" method="POST" autocomplete="off" novalidate>
                        <div class="px-lg-5 py-3">
                            <div class="text-center mb-3">
                                <img src="public/src/img/logo-vallesalud.png" alt="" class="rounded-circl img-thumbnai p-4">
                                <h1>ACCESO USUARIOS</h1>
                                <small class="d-block text-muted fw-semibold mt-2">
                                    "Las credenciales que debes ingresar son las mismas que las de Esclapio."
                                </small>
                                <!-- <img alt="logo.png" width="250px" src="https://creatorexport.zoho.com/file/admin2844/intranet/Sede_Report/2888687000026985022/Foto/image-download/MWKH7E4EG58YPWhbtkh76AW3ysy1C25zvZX6SXjZrVtEREfDCAWahqamBsRPPJgQM4rSpp3aweVKn82DrAX7aCAm9vvJ2swC7Cdk?filepath=/1623191703026_LOG_ValleSalud.png"> -->
                            </div>

                            <div class="form-floating mb-3">
                                <input type="text" class="form-control" id="username" name="username" pattern="([a-z]+|[a-z]+\.{1}[a-z]+)" maxlength="100" required placeholder="Usuario" value="demo.vallesalud">
                                <label for="username"><i class="bi bi-person-fill"></i> Usuario</label>
                                <!-- <small class="d-block text-muted mt-2">
                                    Por favor, ingrese su nombre de usuario.
                                </small> -->
                            </div>

                            <div class="form-floating mb-3">
                                <input type="password" class="form-control" id="password" name="password" required placeholder="Contraseña" value="12345">
                                <label for="password"><i class="bi bi-person-fill-lock"></i> Contraseña</label>
                            </div>

                            <div class="form-floating mb-3">
                                <select class="form-select" id="server" name="server" required></select>
                                <label for="vs_id_type">Conexión</label>
                            </div>

                            <div class="text-center">
                                <input type="submit" class="btn btn-lg btn-info text-light fw-light rounded-5" style="background-color: #3481C4;" value="Ingresar">
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11/dist/sweetalert2.all.min.js"></script>
    <script src="https://getbootstrap.com/docs/5.3/assets/js/validate-forms.js"></script>
    <script src="public/js/server.js"></script>
    <script src="public/js/data.js"></script>
    <script src="public/js/web.js"></script>
    <?php
    if (isset($_SESSION['error'])) {
        echo '<script>const Toast = Swal.mixin({toast: true,position: "top-end",showConfirmButton: false,timer: 6000,timerProgressBar: true,didOpen: (toast) => {toast.onmouseenter = Swal.stopTimer;toast.onmouseleave = Swal.resumeTimer;}});Toast.fire({icon: "error",title: "'.$_SESSION['error'].'"});</script>';
    }
    ?>
</body>

</html>