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

const setting_profile = document.getElementById('setting_profile');

setting_profile.addEventListener('click',() => {
    const modal_setting_profile = document.getElementById('modal_setting_profile');
    modal_setting_profile.style.display = 'block'
})

const setting_delete = document.getElementById('setting_delete');

setting_delete.addEventListener('click', () => {
    const modal_setting_delete = document.getElementById('modal_setting_delete');
    modal_setting_delete.style.display = 'block'
})


//定型分の編集モーダルの表示
const onephrase_edit_els = document.querySelectorAll('.material-symbols-outlined.edit');

onephrase_edit_els.forEach(el => {
    el.addEventListener('click', ( ) => {
        document.getElementById('modal_setting_onephrase_edit').style.display = 'block';
    });
});


//定型分の削除モーダルの表示
const onephrase_delete_els = document.querySelectorAll('.material-symbols-outlined.delete');

onephrase_delete_els.forEach(el => {
    el.addEventListener('click', ( ) => {
        document.getElementById('modal_setting_onephrase_delete').style.display = 'block';
    });
});


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