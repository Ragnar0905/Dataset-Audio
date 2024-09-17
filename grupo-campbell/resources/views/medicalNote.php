<div class="col-12 col-sm-12 col-md-12 col-lg-10 col-xl-10 col-xxl-10 m-auto my-5">
    <div class="card shadow bg-body-tertiary">
        <form class="card-body" method="POST" autocomplete="off">
            <div class="row">
                <div class="col-md-6">
                    <div class="form-floating mb-3">
                        <select name="empresa" id="empresa" class="form-select"></select>
                        <label for="empresa">Empresa</label>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-4">
                    <div class="input-group mb-3">
                        <input type="text" class="form-control form-control-xl" id="numeroCaso" name="numeroCaso" data-validate="numeric" required placeholder="Número de Caso">
                        <button class="btn btn-default px-4" type="button" id="buscar_caso"><i class="bi bi-search" style="font-size:22px"></i></button>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="form-floating mb-3">
                        <input type="date" class="form-control disabled" id="fecha" name="fecha" required>
                        <label for="fecha">Fecha de Atención</label>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="form-floating mb-3">
                        <input type="time" class="form-control disabled" id="hora" name="hora">
                        <label for="hora">Hora</label>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-4">
                    <div class="form-floating mb-3">
                        <input type="text" class="form-control disabled" id="documento" name="documento" required placeholder="Número de Identificación">
                        <label for="documento">Número de Identificación</label>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="form-floating mb-3">
                        <input type="text" class="form-control disabled" id="nombres" name="nombres" required placeholder="Nombres">
                        <label for="nombres">Nombres</label>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="form-floating mb-3">
                        <input type="text" class="form-control disabled" id="apellidos" name="apellidos" required placeholder="Apellidos">
                        <label for="apellidos">Apellidos</label>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-4">
                    <div class="form-floating mb-3">
                        <input type="text" class="form-control disabled" id="sexo" name="sexo" required placeholder="Sexo">
                        <label for="sexo">Sexo</label>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="form-floating mb-3">
                        <input type="text" class="form-control disabled" id="edad" name="edad" data-validate="numeric" required placeholder="Edad">
                        <label for="edad">Edad</label>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6">
                    <div class="form-floating">
                        <textarea class="form-control rsize" name="nota_medica" id="nota_medica" style="height: 150px">Lesion en el brzo izq con truam en la cabeza</textarea>
                        <label for="nota_medica">Nota MIC</label>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="form-floating mb-3">
                        <textarea class="form-control rsize disabled" name="ia_notaMedica" style="height: 150px"></textarea>
                        <label for="ia_notaMedica">Validador Nota MIC</label>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6">
                    <a href="javascript:;" class="btn btn-link" id="btn-i" data-btn-validate="btn-ia" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Analizar la Nota MIC IA">
                        <i class="fa-brands fa-searchengin icon-xl"></i>
                    </a>
                    <a href="javascript:;" class="btn btn-link text-success" data-btn-validate="microphone" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Micrófono 'Clic para hablar'">
                        <i class="fa-solid fa-microphone icon-xl"></i>
                    </a>
                    <a href="javascript:;" class="btn btn-link text-secondary" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Guardar los datos">
                        <i class="bi bi-floppy2 icon-xl"></i>
                    </a>
                </div>
            </div>
        </form>
    </div>
</div>