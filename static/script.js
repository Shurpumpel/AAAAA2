function validateForm() 
{
//validate name
var flag=false;
var name = $('input[name="name"]').val();
  nameReg = /^[A-z][a-z]+$/ 
var name1 = name[0].toUpperCase()+name.slice(1);
$('input[name="name"]').val(name1);
if (((name.length <= 1) || (name.length >= 26)) || (!nameReg.test(name)))
{
  flag = true;
	console.log('Enter correct name');
}
//validate lastname
var lastname = $('input[name="lastname"]').val();
  lastnameReg = /^[A-z][a-z]+$/
var lastname1 = lastname[0].toUpperCase() + lastname.slice(1);
$('input[name="lastname"]').val(lastname1);
if (((lastname.length <= 1) || (lastname.length >= 26)) || (!lastnameReg.test(lastname)))
{
  flag = true;
	console.log('Enter correct lastname');
}
//validate email
var email = $('input[name="email"]').val(),
	emailReg = /^([\w-.]+@[\w-]+[.]+[\w-]{2,4})?$/;
if((!emailReg.test(email) || email == '') && (email !=""))
{
  flag = true;
	console.log('Enter correct email');
}
//validate password
var password = $('input[name="password"]').val(),
	passwordReg = /^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[\w]+/
if ((!passwordReg.test(password)))
{
  flag = true;
  console.log('Enter strong password');  
}
if ((password.length <= 7))
{
  flag = true;
  console.log('Enter correct password');
  
}
//confirm password
var conf_password = $('input[name="conf-password"]').val();
if ((!(conf_password == password)))
{
  flag = true;
	console.log('Different passwords');
}
if (flag)
{
  alert("uncorrect input");
  return false;
}
}

function SendRequest()
{
  var game = {
    name : $('input[name="name"]').val(),
    description : $('input[name="description"]').val(),
    release_date : $('input[name="release_date"]').val(),
    rating : $('input[name="rating"]').val(),
  };
  var jsongame =JSON.stringify(game); 
  $.ajax ({
    type: "POST",
    dataType: 'json',
    url: '/',
    data: jsongame,
  });
  return false;
} 



