function load() {
    let slug = document.querySelector('.anime-slug').value
    let url = '/comments?slug=' + slug
    fetch(url)
        .then(response => response.json())
        .then(data => {
            // commentRender(JSON.parse(data).reverse())
            commentRender(data.reverse())
        })
}

function commentRender(data) {
    document.querySelector('.comments').innerHTML = ''
    let comments = document.querySelector('.comments')
    data.map((item)=>{
        let li = document.createElement('li')
        li.classList.add('list-group-item')
        li.innerHTML = `<h6>${item.user}</h6><p>${item.comment}</p>`
        comments.append(li)
    })
}

document.querySelector('.fetch').addEventListener('click', (e)=>{
    e.preventDefault()
    var csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value
    let anime = document.querySelector(".anime-slug").value
    let comment = document.querySelector("[name=comment]").value
    let url = '/comments'
    let body = {
        'comment': comment,
        'anime': anime
    }
    fetch(url, {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {
            'X-CSRFToken': csrftoken
        },
        credentials: 'include'
    })
    .then(()=>{
        load()
    })
    document.querySelector("[name=comment]").value = null
})


window.onload = load()