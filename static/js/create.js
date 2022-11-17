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
  const bookContent = document.getElementsByClassName('book-content').innerHTML;
  const bookUrl = document.getElementsByClassName('book-url').innerHTML;

  console.log(bookContent, bookUrl);
  // 예외 처리
  if(!select){
  }
  // ajax call
}