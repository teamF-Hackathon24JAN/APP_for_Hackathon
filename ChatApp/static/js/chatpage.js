const header_home = document.getElementById('header_home');

header_home.addEventListener('click',() => {
  window.location.href = '/home'
})

const header_setting = document.getElementById('header_setting');

header_setting.addEventListener('click',( ) => {
  window.location.href = '/setting'
})

const header_signout = document.getElementById('header_signout');

header_signout.addEventListener('click',() => {
  window.location.href = '/login'
})


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

const friendscontainer = document.querySelector('#friends-scrollcontainer');

const upbutton = document.querySelector('#upicon');
const downbutton = document.querySelector('#downicon');


upbutton.addEventListener('click', () => {
    // containerを上方向に50pxスクロールさせる
    friendscontainer.scrollBy({top: -50, behavior: 'smooth' });
});

downbutton.addEventListener('click', () => {
      // containerを下方向に50pxスクロールさせる
      friendscontainer.scrollBy({top: 50, behavior: 'smooth' });
});

window.addEventListener('DOMContentLoaded',( ) => {
    const scrollmessage = document.getElementById("messagearea");
  // 要素内の最下部にスクロール
  scrollmessage.scrollTop = scrollmessage.scrollHeight;
})



const friendAddmodal = document.getElementById('friendAdd');

friendAddmodal.addEventListener('click',() => {
    const modalfriadd = document.getElementById('modal_friendAdd');
    modalfriadd.style.display = "block";
})
  
  // モーダルを閉じる（クローズボタン）イベントリスナーの追加
  document.querySelectorAll(".modal_content_header_close").forEach(function(element) {
    element.addEventListener('click', function() {
      let modalId = this.getAttribute("data-modal");
      document.getElementById(modalId).style.display = "none";
    });
  })
  
  // モーダルの外側をクリックした時に閉じるイベントリスナーの追加
  window.addEventListener('click', function(event) {
    if (event.target.classList.contains("modal")) {
      event.target.style.display = "none";
    }
  });
