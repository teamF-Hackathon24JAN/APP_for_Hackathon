const header_home = document.getElementById('header_home');

header_home.addEventListener('click',() => {
  window.location.href = '/home'
})

const header_signout = document.getElementById('header_signout');

header_signout.addEventListener('click',() => {
  window.location.href = '/login'
})


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
  // const phraseText = e.target.textContent;

      // モーダルのinput要素を取得
      // const modalInput = document.querySelector('.modal_set_password');

      // 取得したテキストをモーダルのinputのvalueにセット
      // modalInput.value = phraseText;

  const modal_setting_onephrase = document.getElementById('modal_setting_password');
  modal_setting_onephrase.style.display = 'block';
})

// const setting_profile = document.getElementById('setting_profile');

// setting_profile.addEventListener('click',() => {
//     const modal_setting_profile = document.getElementById('modal_setting_profile');
//     modal_setting_profile.style.display = 'block'
// })

const setting_delete = document.getElementById('setting_delete');

setting_delete.addEventListener('click', () => {
    const modal_setting_delete = document.getElementById('modal_setting_delete');
    modal_setting_delete.style.display = 'block'
})


//定型分の編集モーダルの表示
const fixedphrase_edit_els = document.querySelectorAll('.material-symbols-outlined.edit');

fixedphrase_edit_els.forEach(el => {
    el.addEventListener('click', (e) => {

      const phraseText = e.target.parentNode.querySelector('.phrase').textContent;

      // モーダルのinput要素を取得
      const modalInput = document.querySelector('.modal_content_body_editInput');

      // 取得したテキストをモーダルのinputのvalueにセット
      modalInput.value = phraseText;

        document.getElementById('modal_setting_onephrase_edit').style.display = 'block';
    });
});


//定型分の削除モーダルの表示
// const fixedphrase_delete_els = document.querySelectorAll('.material-symbols-outlined.delete');
// 
// fixedphrase_delete_els.forEach(el => {
//     el.addEventListener('click', (e) => {
//       const phraseText = e.target.closest('.setting_main_rightside_fixedphrases_phrase')
//                                .querySelector('.phrase').textContent;
//         
//         // モーダル内の<span>にテキストを設定
//         document.querySelector('#modal_setting_onephrase_delete .modal_content_body span').textContent = phraseText;
// 
//         document.getElementById('modal_setting_onephrase_delete').style.display = 'block';
//     });
// });


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