document.addEventListener('DOMContentLoaded', () => {
    let count = 3;
    const timerEl = document.getElementById('timer');

    timerEl.textContent = count;

    const interval = setInterval(() => {
        count--;
        if (count >= 0) {
            timerEl.textContent = count;
        }
        if (count < 0) {
            clearInterval(interval);
            window.location.href = 'https://whotfusests.github.io/bfthon/';
        }
    }, 1000);
});