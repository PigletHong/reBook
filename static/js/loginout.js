function logout() {
  $.removeCookie('mytoken');
  alert("로그아웃 완료!")
  window.location.href = '/reviews'
}


$(document).ready(function () {
  api_valid();
});


function api_valid() {
  $.ajax({
    type: "GET",
    url: "/api/token",
    data: {},
    success: function (response) {
      const done = response['result'] === 'success' ? true : false;
      let temp_html = ``
      if (done) {
        temp_html = `<img onclick="logout()" class="icon logoutIcon" src="../static/image/logoutIcon.png" />
        <h3 class="icon-slash">/</h3>
        <img onclick="location.href='/create'" class="icon writeIcon" src="../static/image/writeIcon.png" />`

      } else {
        temp_html = `<img onclick="location.href='/login'" class="icon logoutIcon" src="../static/image/loginIcon.png"/>
          <h3 class="icon-slash">/</h3>
          <img onclick="location.href='/join'" class="icon writeIcon" src="../static/image/joinIcon.png"/>`
      }
      $('#icon-box').append(temp_html)
    }
  })
}