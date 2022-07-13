const form = document.getElementById('form');
const txtUser = document.getElementById('txtUser');
const txtEmail = document.getElementById('txtEmail');
const txtPassword = document.getElementById('txtPassword');
const txtPassword2 = document.getElementById('txtPassword2');
const txtNombre = document.getElementById('txtNombre');
const txtApellidos = document.getElementById('txtApellidos');
const txtRut = document.getElementById('txtRut');
const txtDv = document.getElementById('txtDv');
const txtDireccion = document.getElementById('txtDireccion');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    checkInputs();
});

function checkInputs() {
    const userValue = txtUser.value.trim();
    const emailValue = txtEmail.value.trim();
    const passwordValue = txtPassword.value.trim();
    const password2Value = txtPassword2.value.trim();
    const nombreValue = txtNombre.value.trim();
    const apellidosValue = txtApellidos.value.trim();
    const rutValue = txtRut.value.trim();
    const dvValue = txtDv.value.trim();
    const direccionValue = txtDireccion.value.trim();

    if (userValue === '') {
        setErrorFor(txtUser, 'El usuario es requerido');
    } else {
        setSuccessFor(txtUser);
    }

    if (emailValue === '') {
        setErrorFor(txtEmail, 'El email es requerido');
    } else if (!isEmail(emailValue)) {
        setErrorFor(txtEmail, 'El email no es valido');
    } else {
        setSuccessFor(txtEmail);
    }

    if (passwordValue === '') {
        setErrorFor(txtPassword, 'La contraseña es requerida');
    } else if (passwordValue.length < 6) {
        setErrorFor(txtPassword, 'La contraseña debe tener al menos 6 caracteres');
    } else {
        setSuccessFor(txtPassword);
    }

    if (password2Value === '') {
        setErrorFor(txtPassword2, 'La contraseña es requerida');
    } else if (password2Value.length < 6) {
        setErrorFor(txtPassword2, 'La contraseña debe tener al menos 6 caracteres');
    } else if (passwordValue !== password2Value) {
        setErrorFor(txtPassword2, 'Las contraseñas no coinciden');
    } else {
        setSuccessFor(txtPassword2);
    }

    if (nombreValue === '') {  
        setErrorFor(txtNombre, 'El nombre es requerido');
    } else {
        setSuccessFor(txtNombre);
    }

    if (apellidosValue === '') {  
        setErrorFor(txtApellidos, 'El apellido es requerido');
    } else {
        setSuccessFor(txtApellidos);
    }

    if (rutValue === '') {   
        setErrorFor(txtRut, 'El rut es requerido');
    } else if (!isRut(rutValue)) {
        setErrorFor(txtRut, 'El rut no es valido');
    } else {
        setSuccessFor(txtRut);
    }

    if (dvValue === '') {  
        setErrorFor(txtDv, 'El dv es requerido');
    } else if (!isDv(dvValue)) {
        setErrorFor(txtDv, 'El dv no es valido');
    } else {
        setSuccessFor(txtDv);
    } 

    if (direccionValue === '') { 
        setErrorFor(txtDireccion, 'La direccion es requerida');
    } else {
        setSuccessFor(txtDireccion);
    }
}

function setErrorFor(input, message) {
    const formControl = input.parentElement;
    const small = formControl.querySelector('small');
    formControl.className = 'form-control error';
    small.innerText = message;
}

function setSuccessFor(input) {
    const formControl = input.parentElement;
    formControl.className = 'form-control success';
}