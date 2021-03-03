let btn = document.querySelector('.lib')

function check() {
    let slug = document.querySelector('.anime-slug').value
    let url = '/lib?slug=' + slug 
    fetch(url)
    .then(data => {
        if (data.status == 200) {
            btn.innerHTML = 'В избранном'
            btn.removeAttribute('class')
            btn.setAttribute('class', 'btn btn-success lib')
        }
    })
}

check()

btn.addEventListener('click', (e)=>{
    e.preventDefault()
    if (btn.innerHTML == 'Добавить в избранное') {
        btn.innerHTML = 'В избранном'
        btn.removeAttribute('class')
        btn.setAttribute('class', 'btn btn-success lib')
        let url = '/lib'
        var csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value
        let slug = document.querySelector('.anime-slug').value
        let body = {
            'slug': slug
        }
        fetch(url,{
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(body)
        })
    } else if(btn.innerHTML == 'В избранном') {
        btn.innerHTML = 'Добавить в избранное'
        btn.removeAttribute('class')
        btn.setAttribute('class', 'btn btn-light lib')
        let url = '/lib'
        var csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value
        let slug = document.querySelector('.anime-slug').value
        let body = {
            'slug': slug
        }
        fetch(url,{
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(body)
        })
    }
})