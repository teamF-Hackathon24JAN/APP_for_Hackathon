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

      friendlist.addEventListener('click', (e) => {
      // Flaskから受け取ったJSONデータをJavaScriptオブジェクトに変換

      // list_data = {{ input_from_python | tojson }};
      const value1 = e.target.getAttribute('data-value1');
      const value2 = e.target.getAttribute('data-value2');
      const value3 = e.target.getAttribute('data-value3');
      document.getElementById('value1').textContent = value1;
      document.getElementById('value2').textContent = value2;
      document.getElementById('value3').src = value3;

      document.getElementById('modal_friend').style.display = 'block';
    });
});

const search = document.getElementById('search');

search.addEventListener('click',() => {
  const modal_delete = document.getElementById("modal_friendAdd");
  modal_delete.style.display = 'none';
  const modal_friend = document.getElementById('modal_friend');
  modal_friend.style.display = 'block';
})

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

const leftbutton = document.querySelector('#lefticon');
const rightbutton = document.querySelector('#righticon');
const channelscontainer = document.querySelector('#channel-boxes');

leftbutton.addEventListener('click', () => {
        // containerを左方向に100pxスクロールさせる
    channelscontainer.scrollBy({top: 0, left:-100, behavior: 'smooth' });
});

rightbutton.addEventListener('click', () => {
    // channelscontainerを右方向に100pxスクロールさせる
    channelscontainer.scrollBy({top: 0, left:100, behavior: 'smooth' });
});

const friendaddmodal = document.getElementById('friendAdd');

friendaddmodal.addEventListener('click',() => {
    const modalfriadd = document.getElementById('modal_friendAdd');
    modalfriadd.style.display = "block";
})

const home_channels_edit = document.getElementById('home_channels_add');

home_channels_edit.addEventListener('click', () => {
  const modal_home_channels_edit = document.getElementById('modal_home_channels_add');
  modal_home_channels_edit.style.display = 'block'
}) 
  
  // モーダルを閉じる（クローズボタン）イベントリスナーの追加
  document.querySelectorAll(".modal_content_header_close").forEach(function(element) {
    element.addEventListener('click', function() {
      let modalId = this.getAttribute("data-modal");
      document.getElementById(modalId).style.display = "none";
    });
  });

  const ChannnelAddButton = document.getElementById('channnel_add_button');

  
  // モーダルの外側をクリックした時に閉じるイベントリスナーの追加
  window.addEventListener('click', function(event) {
    if (event.target.classList.contains("modal")) {
      event.target.style.display = "none";
    }
  });

  const page = '/chatpage/' + 1;
  const channelnumber = 'channel_' + 1
  const channel_vars = document.getElementById(channelnumber);
