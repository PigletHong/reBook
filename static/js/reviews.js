// same with JQuery $(document).ready()
document.addEventListener("DOMContentLoaded", function(event) { 
  show_reviews();
});

function show_reviews() {
  $.ajax({
    type: 'GET',
    url: '/api/review',
    data: {},
    success: function (response) {
      const reviews = response['reviews'];

      for(let i=0; i<reviews.length; i++){
        const bookImg = reviews[i]['bookInfo']['img'];
        const bookTitle = reviews[i]['bookInfo']['title'];
        const id = reviews[i]['_id'];
        const content = reviews[i]['content'];
        const pubDate = reviews[i]['pubDate'];
        const userId = "신원";
        // const tag = reviews[i]['tag'];
        // const userId = reviews[i]['userId'];
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
                <p class="review-author">${userId}</p>
              <div>
            </div>
          </div>
        `
        $('.reviews').append(temp_html);
      }
      }
    },
  );
}
