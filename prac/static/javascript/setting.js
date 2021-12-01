$('#usersetting').click(function(){
    $('#general-view').css('display','none'),
    $('#usersetting-view').css('display','block')
    $('#profilepic-view').css('display','none')
    $('#password-view').css('display','none')
})

$('#general').click(function(){
    $('#general-view').css('display','block'),
    $('#usersetting-view').css('display','none')
    $('#profilepic-view').css('display','none')
    $('#password-view').css('display','none')
})

$('#profilepic').click(function(){
    $('#general-view').css('display','none'),
    $('#usersetting-view').css('display','none')
    $('#profilepic-view').css('display','block')
    $('#password-view').css('display','none')
})
$('#change_password').click(function(){
    $('#general-view').css('display','none'),
    $('#usersetting-view').css('display','none')
    $('#profilepic-view').css('display','none')
    $('#password-view').css('display','block')
})



$('#id_username').addClass('form-control')
$('#id_first_name').addClass('form-control')
$('#id_last_name').addClass('form-control')
$('#id_email').addClass('form-control')
$('#id_pic').addClass('form-control')
$('#id_company_name').addClass('form-control')
$('#id_bio').addClass('form-control')

$('#imagechange').change(function(){
    console.log('changed')
    dir = $(this).val()
    console.log(dir)
})