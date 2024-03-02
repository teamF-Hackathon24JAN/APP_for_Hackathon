const loginbutton = document.getElementById('login_button');

// ログインページで鍵のボタンを押すとホームに遷移する
loginbutton.addEventListener('click',() => {
    window.location.href = '/home'
})