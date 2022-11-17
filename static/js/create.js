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

function writeBtnHandler() {
  const bookUrl = document.querySelector('.book-url').value;
  const bookContent = document.querySelector('.book-content').value;

  // 예외 처리
  if(bookUrl.includes('product.kyobobook.co.kr/detail/') && bookContent && selected ){
    // user id 값 추가 필요
    $.ajax({
      type: 'POST',
      url: '/api/review',
      data: {
        url_give: bookUrl,
        content_give: bookContent,
        tag_give: selected,
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