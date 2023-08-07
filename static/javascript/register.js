let firstname = document.forms['form']['firstname'];
let lastname = document.forms['form']['lastname'];
let email = document.forms['form']['email'];
let username = document.forms['form']['username'];
let password = document.forms['form']['password'];
let confirm_password = document.forms['form']['confirm_password'];

let firstname_error = document.getElementById('firstname_error');
let lastname_error = document.getElementById('lastname_error');
let email_error = document.getElementById('email_error');
let username_error = document.getElementById('username_error');
let password_error = document.getElementById('password_error');
let c_password_error = document.getElementById('confirm_password_error');

firstname.addEventListener('textInput', firstname_Verify);
lastname.addEventListener('textInput', lastname_Verify);
email.addEventListener('textInput', email_Verify);
username.addEventListener('textInput', name_Verify);
password.addEventListener('textInput', password_Verify);
confirm_password.addEventListener('textInput', c_password_Verify);

function validateRegister() {

  if (firstname.value.length < 4) {
    firstname.style.border = "1px solid red";
    firstname_error.innerHTML = "Please fill your First Name";
    firstname_error.style.color = "red"
    firstname.focus();
    return false;
  }

  if (lastname.value.length < 4) {
    lastname.style.border = "1px solid red";
    lastname_error.innerHTML = "Please fill your Last Name";
    lastname_error.style.color = "red"
    lastname.focus();
    return false;
  }

  if (email.value.length < 4) {
    email.style.border = "1px solid red";
    email_error.innerHTML = "Please fill your Email";
    email_error.style.color = "red"
    email.focus();
    return false;
  }

  if (username.value.length < 4) {
    username.style.border = "1px solid red";
    username_error.innerHTML = "Please fill your User Name";
    username_error.style.color = "red"
    username.focus();
    return false;
  }

  if (password.value.length < 4) {
    password.style.border = "1px solid red";
    password_error.innerHTML = "Please fill your Password";
    password_error.style.color = "red"
    password.focus();
    return false;
  }

  if (confirm_password.value.length < 4) {
    confirm_password.style.border = "1px solid red";
    c_password_error.innerHTML = "Please check your Password";
    c_password_error.style.color = "red"
    confirm_password.focus();
    return false;
  }

  

}

function firstname_Verify() {
    if (firstname.value.length >= 6) {
      firstname.style.border = "1px solid green ";
      firstname_error.style.display = 'none';
      return true;
    }
  }

function lastname_Verify() {
    if (lastname.value.length >= 6) {
      lastname.style.border = "1px solid green ";
      lastname_error.style.display = 'none';
      return true;
    }
  }

function name_Verify() {
  if (username.value.length >= 6) {
    username.style.border = "1px solid green ";
    username_error.style.display = 'none';
    return true;
  }
}

function email_Verify() {
    if (email.value.length >= 6) {
      email.style.border = "1px solid green ";
      email_error.style.display = 'none';
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

function c_password_Verify() {
    if (confirm_password.value.length >= 3) {
      confirm_password.style.border = "1px solid green ";
      c_password_error.style.display = 'none';
      return true;
    }
  }