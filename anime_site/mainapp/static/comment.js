// function load() {
//     let slug = document.querySelector('.anime_slug').value
//     let url = '/comments?slug=' + slug
//     fetch(url)
//         .then((res) => {
//             return res.json()
//         })
//         .then((data) => {
//             data.forEach(el => {
//                 document.querySelector('.comments').innerHTML += el
//             })
//         })
// }

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
    console.log(body)
    fetch(url, {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {
            'X-CSRFToken': csrftoken
        },
        credentials: 'include'
    })
})


// window.onload = load()