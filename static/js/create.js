// same with JQuery $(document).ready()
document.addEventListener("DOMContentLoaded", function(event) {
  token_valid();
});

let selected;

function calcTextareaHeight(e) {
  e.style.height = 'auto'
  e.style.height = `${e.scrollHeight}px`
}

function tagBtnHandler(e) {
  const targetClass = e.target.getAttribute('class');
  const targetSubject = e.target.getAttribute('id');

  // 선택되지 않았으면
  if(targetClass.indexOf('selected') === -1){
    if(selected){
      const _selected = document.getElementById(selected);
      _selected.setAttribute('class', 'tag-btn');
    }

    e.target.setAttribute('class', targetClass + ' selected')
    selected = targetSubject;
  }
}

function getUsername() {
  let username;
  $.ajax({
    type: "GET",
    url: "/api/token",
    async: false,
    data: {},
    success: function (response) {
      username = response.name
    }
  });
  return username;
}

function token_valid() {
  $.ajax({
    type: "GET",
    url: "/api/token",
    data: {},
    success: function (response) {
      const done = response['result'] === 'success' ? true : false;
      if(!done){
        window.location.href = '/';
      }
    }
  });
}

function writeBtnHandler(event) {
  const writeBtn = event.target;
  const bookUrl = document.querySelector('.book-url').value;
  const bookContent = document.querySelector('.book-content').value;
  const username = getUsername();
  // console.log(userName);
  
  // 예외 처리
  if(bookUrl.includes('product.kyobobook.co.kr/detail/') && bookContent && selected ){
    // 한번만 눌리도록 버튼 disabled 처리
    writeBtn.setAttribute("disabled", "disalbed");
    $.ajax({
      type: 'POST',
      url: '/api/review',
      data: {
        url_give: bookUrl,
        content_give: bookContent,
        tag_give: selected,
        name_give: username
      },
      success: function (response) {
        alert(response['msg']);
        // 완료되면 리뷰 리스트 페이지로 나가기
        window.location.href = '/reviews';
      },
    });
  } else {
    alert('값을 모두 올바르게 입력해주세요')
  }
}