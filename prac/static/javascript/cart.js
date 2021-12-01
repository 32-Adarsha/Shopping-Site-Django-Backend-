$('.addsubtract').click(function(){
    id = $(this).val()
    data=$(this).html()
    htmlclass= '.qntcnt'+id
    test = $(htmlclass).html()
    
    if(test === "Quantity 1" & data ==="-"){
        var r = confirm("Do you wish to delete form cart ")
        if (r==true){
            $.ajax({
                url:'/qntcng/',
                type:"GET",
                data :{
                    'id': id,
                    'data':data,
                },
                success:function(response){
                    if(response ==='delete'){
                        window.location.reload()
                    }else{
                        $(htmlclass).html('Quantity '+response)
                    }
                }
            })
        }
    }
    else {$.ajax({
        url:'/qntcng/',
        type:"GET",
        data :{
            'id': id,
            'data':data,
        },
        success:function(response){
            if(response ==='delete'){
                window.location.reload()
            }else{
                $(htmlclass).html('Quantity '+response)
            }
        }
    })
}})