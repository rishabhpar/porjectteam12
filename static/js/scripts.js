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
          console.log(resp);
        //   This shit doesnt work in Brave browser, but does in Firefox/Chrome/Edge
          $error.text(resp.responseJSON.error);
          $error.removeClass("error--hidden");
        }
    });

    e.preventDefault();
});