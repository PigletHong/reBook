// same with JQuery $(document).ready()
document.addEventListener("DOMContentLoaded", function(event) {
  const params = new URLSearchParams(window.location.search);
  const type = params.get('type');
  const query = params.get('query');
  // query가 있을 경우
  if(type && query){
    search_reviews(type, query);
  }else {
    // 없을 경우
    get_reviews();
  }
});

function get_reviews() {
  $.ajax({
    type: 'GET',
    url: '/api/review',
    data: {},
    success: function (response) {
        show_reviews(response);
      }
    },
  );
}

function search_reviews(type, query) {
  $.ajax({
    type: 'GET',
    url: `/api/review?type=${type}&query=${query}`,
    data: {},
    success: function (response) {
        show_reviews(response);
      }
    },
  );
}

function show_reviews(res) {
  const reviews = res['reviews'];

  for(let i=0; i<reviews.length; i++){
    const bookImg = reviews[i]['bookInfo']['img'];
    const bookTitle = reviews[i]['bookInfo']['title'];
    const id = reviews[i]['_id'];
    const content = reviews[i]['content'];
    const pubDate = reviews[i]['pubDate'];
    const username = reviews[i]['username'];
    // const tag = reviews[i]['tag'];
    const temp_html = `
      <div class="review-card" id="${id}">
        <img
          class="review-img"
          src="${bookImg}"
        />
        <div class="text-area">
          <h3 class="review-title">${bookTitle}</h3>
          <p class="review-desc">
            ${content}
          </p>
          <div class="detail-info">
            <p class="review-createdBy">${pubDate}</p>
            <p class="review-author">${username}</p>
          <div>
        </div>
      </div>
    `
    $('.reviews').append(temp_html);
  }
}
