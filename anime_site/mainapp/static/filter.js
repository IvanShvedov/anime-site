function getGenres() {
    let ul = document.querySelector('.dropdown-menu')
    fetch('/genres')
    .then(data => {
        let body = JSON.parse(data)
        body.map((item) => {
            let li = document.createElement('li')
                li.innerHTML = `<a class="dropdown-item"`
        })
    })
}