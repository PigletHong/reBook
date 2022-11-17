        function logout() {
            $.removeCookie('mytoken');
            alert("로그아웃 완료!")
            window.location.href = '/'
        }
