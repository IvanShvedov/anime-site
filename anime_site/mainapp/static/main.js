btns = document.querySelectorAll('.episode');
player = document.querySelector('.anime-player')
btns.forEach(btn => {
    btn.addEventListener('click', function(){
        changeEpisode(btn.getAttribute('data'), btn);
    })
});

function disableAll() {
    btns.forEach(btn => {
        btn.setAttribute('state', 'disable');
    })
}

function changeEpisode(url, btn) {
    player.setAttribute('src', url);
    disableAll();
    btn.setAttribute('state', 'active')
}