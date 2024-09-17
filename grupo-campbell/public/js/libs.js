function showToast(obj) {
    const icon = obj["icon"];
    const title = obj["title"];
    const txt = obj["text"];
    if(title != null || txt != null)
    {
        const Toast = Swal.mixin({
            toast: true,
            position: "top-end",
            showConfirmButton: false,
            timer: 5000,
            timerProgressBar: true,
            didOpen: (toast) => {
                toast.onmouseenter = Swal.stopTimer;
                toast.onmouseleave = Swal.resumeTimer;
            }
        });

        Toast.fire({
            icon: icon,
            title: title,
            html: txt
        });
    }
}

function valueNumber(evt) {
    // // code is the decimal ASCII representation of the pressed key.
    var code = (evt.which) ? evt.which : evt.keyCode;
    if (code >= 48 && code <= 57) { // is a number.
        return true;
    } else { // other keys.
        return evt.preventDefault();
    }
}
// Permite que los campos texte solo acepte solo letras y espacio [a-zA-Z\s]
function valueLetters(evt) {
    // // code is the decimal ASCII representation of the pressed key.
    var code = (evt.which) ? evt.which : evt.keyCode;
    if (code == 8 || code == 32 || code == 241 || code == 209) { // backspace.
        return true;
    } else if ((code >= 65 && code <= 90) || (code >= 97 && code <= 122)) { // is a letter.
        return true;
    } else { // other keys.
        return evt.preventDefault();
    }
}