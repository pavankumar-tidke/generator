console.log('auth32');


// Toggle between the signup and login view
$('.signup-section').hide()
$('.login-link').click( (e) => {
    $('.login-section').show();
    $('.signup-section').hide();
}) ;
$('.signup-link').click( (e) => {
    $('.login-section').hide();
    $('.signup-section').show();
}) ;


// Account create action
$('.signup-submit').click( (e) => {

    $.ajax({
        type: "POST",
        url: `authenticateUser/`,
        dataType: "json",
        data: {
            name: $("input[name='name']").val(),
            username: $("input[name='username']").val(),
            email: $("input[name='email']").val(),
            password: $("input[name='password']").val(),
            operation: 'signup',
        },
        success: (data) => {
           
          console.log((data.error) ? data :  data.errorMsg);
          
        },
        error: (xhr, status, error) => {
          console.log(error, status);
        },
      });
});


// login action
$('.login-submit').click( (e) => {

  $.ajax({
    type: "POST",
    url: `authenticateUser/`,
    dataType: "json",
    data: { 
        username: $("input[name='loginUsername']").val(), 
        password: $("input[name='loginPassword']").val(),
        operation: 'login',
    },
    success: (res) => { 
      // window.location.href = res.data.redirect_url
      console.log(res);  
      
    },
    error: (xhr, status, error) => {
      console.log(error, status);
    },
  });
});


// if the success response will come from the request then this will call
// const SuccessAuthResponse('')