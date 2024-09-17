const file = "grupo-campbell/";
const optionEmpty = "<option value='' selected >- Seleccione -</option>";
const maximoTextarea = 5;
let sweetData = {};
if (path == `${file}login`) {
    const selectServer = document.querySelector("#server");
    selectServer.innerHTML = optionEmpty;
    connections().forEach(row => {
        const opc = document.createElement('option');
        opc.text = `${row.name}`;
        opc.value = `${row.ipAddress}`;
        selectServer.add(opc);
    });
    if (params['size'] > 0) {
        const access_token = params.get("access_token");
        const decodeAccess = JSON.parse(decodeBase64(access_token));
        Object.keys(decodeAccess).forEach(function (key) {
            const element = document.querySelector(`select[name='${key}']`);
            if (element != null) {
                element.value = decodeAccess[key];
            }
        });
    }
    else {
        Swal.fire({
            icon: "warning",
            title: "ADVERTENCIA",
            text: "Esperando el parámetro \"access_token\" por URL",
            confirmButtonText: "De acuerdo",
            allowEscapeKey: false,
            allowOutsideClick: false,
            customClass: {
                confirmButton: "btn  btn-warning text-dark rounded-0"
            }
        });
    }
}
else {
    const selectEmpresa = document.querySelector("#empresa");
    selectEmpresa.innerHTML = optionEmpty;
    companies().forEach(row => {
        const opc = document.createElement('option');
        opc.text = `${row.name}`;
        opc.value = `${row.prefix}`;
        selectEmpresa.add(opc);
    });

    if (path == `${file}medical-note`) {
        const btnCaso = document.querySelector("#buscar_caso")
        btnCaso.addEventListener('click', function (evt) {
            const element = this;
            const parentElement = this.closest('.input-group');
            const caso = parentElement.children[0].value;
            const empresa = document.querySelector("#empresa").value;
            //
            if (empresa.trim() === '' || empresa.trim().length === 0) {
                sweetData.icon = "warning";
                sweetData.text = "Por favor, seleccionar una empresa.";
                showToast(sweetData);
            }
            else if (caso.trim() === '' || caso.trim().length === 0) {
                sweetData.icon = "warning";
                sweetData.text = "Por favor, ingrese un número de caso.";
                showToast(sweetData);
            }
            else {
                console.log(caso);
            }
        });
    }
}

const fieldsValidate = document.querySelectorAll('[data-validate]');
fieldsValidate.forEach(field => {
    const validationType = field.getAttribute('data-validate').toLowerCase().trim();
    const value = field.value.trim();
    if (validationType === 'numeric') {
        field.addEventListener('keypress', valueNumber);
    }
    if (validationType === 'text') {
        field.addEventListener('keypress', valueLetters);
    }
});

const btnValidate = document.querySelectorAll('[data-btn-validate]');
btnValidate.forEach(btn => {
    const validationType = btn.getAttribute('data-btn-validate').toLowerCase().trim();
    if (validationType === 'btn-ia') {
        btn.addEventListener('click', function (evt) {
            const medicalNote = document.querySelector("textarea[name=nota_medica]").value;
            if (medicalNote.trim() === '' || medicalNote.trim().length === 0) {
                sweetData.icon = "warning";
                sweetData.title = "ERROR AL ANALIZAR";
                sweetData.text = "Antes de utilizar la IA, asegúrate de haber ingresado algo en el campo <b>'Nota MIC'</b>.";
                showToast(sweetData);
            }
            else {
                const validatorIA = document.querySelector("textarea[name=ia_notaMedica]");
                // validatorIA.value = `Se encontraron los siguientes errores en la nota médica:\nLesion => Lesión\nbrzo => brazo\nizq => izquierdo\ntruam => trauma`; // Simulación de analisis
                // sweetData.icon = "success";
                // sweetData.title = "ANALIZADO";
                // sweetData.text = "IA ha analizado la nota MEDICA.";
                // showToast(sweetData);
                // //
                analyzeNote(validatorIA.value);
            }
        });
    }
    if (validationType === 'microphone') {
        btn.addEventListener('click', function (evt) {
            sweetData.icon = "info";
            sweetData.title = "CONCEDER PERMISO";
            sweetData.text = "Debes dar clic en permitir <b>'Micrófono'</b>";
            showToast(sweetData);
        });
    }
});

//
/*!
 * Color mode toggler for Bootstrap's docs (https://getbootstrap.com/)
 * Copyright 2011-2024 The Bootstrap Authors
 * Licensed under the Creative Commons Attribution 3.0 Unported License.
 */

(() => {
    'use strict'

    const getStoredTheme = () => localStorage.getItem('theme')
    const setStoredTheme = theme => localStorage.setItem('theme', theme)

    const getPreferredTheme = () => {
        const storedTheme = getStoredTheme()
        if (storedTheme) {
            return storedTheme
        }

        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
    }

    const setTheme = theme => {
        if (theme === 'auto') {
            document.documentElement.setAttribute('data-bs-theme', (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'))
        } else {
            document.documentElement.setAttribute('data-bs-theme', theme)
        }
    }

    setTheme(getPreferredTheme())

    const showActiveTheme = (theme, focus = false) => {
        const themeSwitcher = document.querySelector('#bd-theme')

        if (!themeSwitcher) {
            return
        }

        const themeSwitcherText = document.querySelector('#bd-theme-text')
        const activeThemeIcon = document.querySelector('.theme-icon-active use')
        const btnToActive = document.querySelector(`[data-bs-theme-value="${theme}"]`)
        const svgOfActiveBtn = btnToActive.querySelector('svg use').getAttribute('href')
        console.log(svgOfActiveBtn)
        
        document.querySelectorAll('[data-bs-theme-value]').forEach(element => {
            element.classList.remove('active')
            element.setAttribute('aria-pressed', 'false')
        })

        btnToActive.classList.add('active')
        btnToActive.setAttribute('aria-pressed', 'true')
        activeThemeIcon.setAttribute('href', svgOfActiveBtn)
        const themeSwitcherLabel = `${themeSwitcherText.textContent} (${btnToActive.dataset.bsThemeValue})`
        themeSwitcher.setAttribute('aria-label', themeSwitcherLabel)

        if (focus) {
            themeSwitcher.focus()
        }
    }

    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
        const storedTheme = getStoredTheme()
        if (storedTheme !== 'light' && storedTheme !== 'dark') {
            setTheme(getPreferredTheme())
        }
    })

    window.addEventListener('DOMContentLoaded', () => {
        showActiveTheme(getPreferredTheme())

        document.querySelectorAll('[data-bs-theme-value]')
            .forEach(toggle => {
                toggle.addEventListener('click', () => {
                    const theme = toggle.getAttribute('data-bs-theme-value')
                    setStoredTheme(theme)
                    setTheme(theme)
                    showActiveTheme(theme, true)
                })
            })
    })
})()

