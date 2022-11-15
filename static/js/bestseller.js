let temp_html = `<div class="col">
                        <div class="card h-100">
                            <img src="${img}"
                                 class="card-img-top">
                            <div class="card-body">
                                <h5 class="card-title">${title}</h5>
                                <p class="card-author">${author}</p>
                                <p class="card-desc">{{data.desc}}</p>
                                <p class="card-price">{{data.price}}</p>
                            </div>
                        </div>
                        </div>`
$('#cards-box').append(temp_html)

