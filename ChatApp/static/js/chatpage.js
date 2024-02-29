// IDがheader_nameの要素を取得
const header_home = document.getElementById('header_home');

// IDがheader_homeの要素をクリックしたとき
header_home.addEventListener('click',() => {
  // /homeに遷移する
  window.location.href = '/home'
})

// IDがheader_settingの要素を取得
const header_setting = document.getElementById('header_setting');

// IDがheader_settingの要素をクリックしたとき
header_setting.addEventListener('click',( ) => {
  // /settingに遷移する
  window.location.href = '/setting'
})

// IDがheader_signoutの要素を取得
const header_signout = document.getElementById('header_signout');

// IDがheader_signoutの要素をクリックしたとき
header_signout.addEventListener('click',() => {
  // サインアウトし、/loginに遷移する
  window.location.href = '/login'
})

// classに.listとついている要素を複数取得
const friendlists = document.querySelectorAll('.list');

friendlists.forEach((friendlist,i) =>{
    friendlist.style.opacity = '0';

    const keyframes = {
        opacity: [0,1],
        translate:['-30px','0px']
    };
    const options = {
        duration:300,
        delay: i * 100,
        fill:'forwards'
    };
    friendlist.animate(keyframes,options);
    
    friendlist.addEventListener('click', () => {
      document.getElementById('modal_friend').style.display = 'block';
    });
});

const friendaddmodal = document.getElementById('friendAdd');

friendaddmodal.addEventListener('click',() => {
    const modalfriadd = document.getElementById('modal_friendAdd');
    modalfriadd.style.display = "block";
});

// const friendscontainer = document.querySelector('#friends-scrollcontainer');

// const upbutton = document.querySelector('#upicon');
// const downbutton = document.querySelector('#downicon');


// upbutton.addEventListener('click', () => {
//     // containerを上方向に50pxスクロールさせる
//     friendscontainer.scrollBy({top: -50, behavior: 'smooth' });
// });

// downbutton.addEventListener('click', () => {
//       // containerを下方向に50pxスクロールさせる
//       friendscontainer.scrollBy({top: 50, behavior: 'smooth' });
// });

window.addEventListener('DOMContentLoaded',( ) => {
    const scrollmessage = document.getElementById("messagearea");
  // 要素内の最下部にスクロール
  scrollmessage.scrollTop = scrollmessage.scrollHeight;
})

const chatpage_fixedphrases = document.getElementById('chatpage_fixedphrases');

chatpage_fixedphrases.addEventListener('click', () => {
  const modal_chatpage_fixedphrases = document.getElementById('modal_chatpage_fixedphrases');
  modal_chatpage_fixedphrases.style.display = 'block';
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

  const select_phrases = document.querySelectorALL('.modal_content_body_box_fixedphrase');

  select_phrases.forEach((select_phrase) => {
    select_phrase.addEventListener('dbclick',(e) => {
      const messageInput = document.getElementById('messageInput');
      messageInput.value = e.target.textContent;
    });
  });
