// this is in jquery, but should probably change to React.js

$("form[name='signup_form']").submit(function(e){

    var $form = $(this);
    var $error = $form.find('.error');
    var data = $form.serialize();

    $.ajax({
        url: "/user/signup",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
          window.location.href = "/dashboard/";
        },
        error: function(resp) {
        //   This doesnt work in Brave browser, but does in Firefox/Chrome/Edge
          $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });

    e.preventDefault();
});

$("form[name='login_form']").submit(function(e){

    var $form = $(this);
    var $error = $form.find('.error');
    var data = $form.serialize();

    $.ajax({
        url: "/user/login",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
          window.location.href = "/dashboard/";
        },
        error: function(resp) {
        //   This doesnt work in Brave browser, but does in Firefox/Chrome/Edge
          $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });

    e.preventDefault();
});