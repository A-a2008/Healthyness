const startingMinutes = 15;
let time = startingMinutes * 60;

const countdownEl = document.getElementById('countdown');

setInterval(updateCountdown, 1000);

function updateCountdown() {
    const minutes = Math.floor(time / 60);
    let seconds = time % 60;

    seconds = seconds < 10 ? '0' + seconds : seconds;

    countdownEl.innerHTML = '${minutes}:${seconds}';
    time--;
}

location.replace("http://127.0.0.1:8000/inner_mind/done/")
