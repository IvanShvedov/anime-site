let radios = document.querySelectorAll('.btn-check')
radios.forEach(radio =>{
    radio.addEventListener('change', function(){
        let grade = radio.id.slice(-1)
        var csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value
        let anime = document.querySelector(".anime-slug").value
        let url = '/grades'
        let body = {
            'grade': grade,
            'anime': anime
        }
        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(body)
        })
    })
})

window.onload = function() {
    let slug = document.querySelector('.anime-slug').value
    let url = '/grades'
    fetch(url+'?slug='+slug)
    .then(response => response.json())
    .then(data => {
        selector = '#btnradio' + data.grade
        document.querySelector(selector).checked = true
    })
}