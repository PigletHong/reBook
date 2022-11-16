    {% if msg %}
        alert("{{ msg }}")
    {% endif %}

    function login() {
        $.ajax({
            type: "POST",
            url: "/api/login",
            data: {id_give: $('#userId').val(), pw_give: $('#userPwd').val()},
            success: function (response) {
                if (response['result'] == 'success') {
                    $.cookie('mytoken', response['token']);

                    alert('로그인 완료!')
                    window.location.href = '/'
                } else {
                    alert(response['msg'])
                }
            }
        })
    }