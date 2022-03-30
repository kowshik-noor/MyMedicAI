$(document).ready(function(){
    $('#navbar-toggler').click(function(){
        $('.navbar-collapse').slideToggle(400);
    });

    $(window).scroll(function(){
        let pos = $(window).scrollTop();
        if(pos >= 100){
            $('.navbar').addClass('cng-navbar');
        }
        else{
            $('.navbar').removeClass('cng-navbar');
        }
        // console.log(pos);
    });
});
