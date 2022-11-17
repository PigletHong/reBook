
function join() {
    $.ajax({
        type: "POST",
        url: "/api/join",
        data: {
            id_give: $('#userId').val(),
            pw_give: $('#userPwd').val(),
            name_give: $('#userName').val()
        },
        success: function (response) {
            if (response['result'] == 'success') {
                alert('회원가입이 완료되었습니다.')
                window.location.href = '/login'
            } else {
                alert(response['msg'])
            }
        }
    })
}