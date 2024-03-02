const header_home = document.getElementById('header_home');

header_home.addEventListener('click',() => {
  window.location.href = '/home'
})

const header_signout = document.getElementById('header_signout');

header_signout.addEventListener('click',() => {
  window.location.href = '/login'
})

const setting_picture = document.getElementById('setting_picture');

setting_picture.addEventListener('click', ( ) => {
  const modal_setting_picture = document.getElementById('modal_setting_picture');
  modal_setting_picture.style.display = 'block';
});


const setting_name = document.getElementById('setting_name');

setting_name.addEventListener('click', () => {
    const modal_setting_name = document.getElementById('modal_setting_name');
    modal_setting_name.style.display = 'block'
})

const setting_onephrase = document.getElementById('setting_onephrase');

setting_onephrase.addEventListener('click', (e) => {
  const phraseText = e.target.textContent;

      // モーダルのinput要素を取得
      var modalInput = document.querySelector('.modal_set_onephrase');

      // 取得したテキストをモーダルのinputのvalueにセット
      modalInput.value = phraseText;

  const modal_setting_onephrase = document.getElementById('modal_setting_onephrase');
  modal_setting_onephrase.style.display = 'block';
})

const setting_mailaddress = document.getElementById('setting_mailaddress');

setting_mailaddress.addEventListener('click', (e) => {
  var phraseText = e.target.textContent;

      // モーダルのinput要素を取得
      var modalInput = document.querySelector('.modal_set_mailaddress');

      // 取得したテキストをモーダルのinputのvalueにセット
      modalInput.value = phraseText;


  const modal_setting_onephrase = document.getElementById('modal_setting_mailaddress');
  modal_setting_onephrase.style.display = 'block';
})

const setting_password = document.getElementById('setting_password');

setting_password.addEventListener('click', () => {

  const modal_setting_onephrase = document.getElementById('modal_setting_password');
  modal_setting_onephrase.style.display = 'block';
})


  // モーダルを閉じる（クローズボタン）イベントリスナーの追加
  document.querySelectorAll(".modal_content_header_close").forEach(function(element) {
    element.addEventListener('click', function() {
      let modalId = this.getAttribute("data-modal");
      document.getElementById(modalId).style.display = "none";
    });
  });
  
  // モーダルの外側をクリックした時に閉じるイベントリスナーの追加
  window.addEventListener('click', function(event) {
    if (event.target.classList.contains("modal")) {
      event.target.style.display = "none";
    }
  });