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
      console.log(friendlist.dataset.id)
      friend_name = document.getElementById('fname')
      friend_phrase = document.getElementById('fphrase')
      friend_name.textContent = friendlist.dataset.id
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


// const upbutton = document.querySelector('#upicon');
// const downbutton = document.querySelector('#downicon');
// const friendscontainer = document.querySelector('#friends-scrollcontainer');

const leftbutton = document.querySelector('#lefticon');
const rightbutton = document.querySelector('#righticon');
const channelscontainer = document.querySelector('#channel-boxes');

// upbutton.addEventListener('click', () => {
//     // containerを上方向に50pxスクロールさせる
//     friendscontainer.scrollBy({top: -50, behavior: 'smooth' });
// });

// downbutton.addEventListener('click', () => {
//       // containerを下方向に50pxスクロールさせる
//       friendscontainer.scrollBy({top: 50, behavior: 'smooth' });
// });

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

  // const channel_Vars = document.querySelectorAll('._channels-var');
  // channel_Vars.forEach(channel_var => {
  //   channel_var.addEventListener('click',() => {
  //     window.location.href = '/chatpage';
  //   });
  // });

    // channel_vars.addEventListener('click',( ) => {
    //   let 
    // window.location.href = '/chatpage';
    // });



// document.querySelectorAll('.tab').forEach((tab) => {
//   tab.addEventListener('click', function() {
//     const target = this.getAttribute('data-tab');
    
//     // 以前のアクティブなタブの内容を非表示にする
//     document.querySelectorAll('.content').forEach((content) => {
//       content.style.display = 'none';
//     });

//     // クリックされたタブに関連するコンテンツを表示
//     document.getElementById(target).style.display = 'block';

//     // 以前のアクティブなタブのスタイルをリセット
//     document.querySelectorAll('.tab').forEach((tab) => {
//       tab.classList.remove('active');
//     });

//     // クリックされたタブのスタイルをアクティブに
//     this.classList.add('active');
//   });
// });