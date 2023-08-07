let username = document.forms['form']['username'];
let password = document.forms['form']['password'];

let name_error = document.getElementById('name_error')
let password_error = document.getElementById('password_error')

username.addEventListener('textInput', name_Verify);
password.addEventListener('textInput', password_Verify);

function validateLogin() {
  if (username.value.length < 4) {
    username.style.border = "1px solid red";
    name_error.innerHTML = "Please fill your User Name";
    name_error.style.color = "red"
    username.focus();
    return false;
  }

  if (password.value.length < 3) {
    password.style.border = "1px solid red";
    password_error.innerHTML = "Please fill your Password";
    password_error.style.color = "red"
    password.focus();
    return false;
  }

}

function name_Verify() {
  if (username.value.length >= 4) {
    username.style.border = "1px solid green ";
    name_error.style.display = 'none';
    return true;
  }
}

function password_Verify() {
  if (password.value.length >= 3) {
    password.style.border = "1px solid green ";
    password_error.style.display = 'none';
    return true;
  }
}