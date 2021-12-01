$('.addtocart').click(function(){
    var b = $(this).val()
    console.log(b)
    $.ajax({
        type:"GET",
        url:'/addtocart/',
        data:{
            'data':b
        },
        success:function(response){
            $('.cart-count').html(response);
        }

    })})