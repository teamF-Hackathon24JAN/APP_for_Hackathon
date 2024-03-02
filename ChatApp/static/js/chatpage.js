// IDがheader_nameの要素を取得
const header_home = document.getElementById("header_home");

// IDがheader_homeの要素をクリックしたとき
header_home.addEventListener("click", () => {
  // /homeに遷移する
  window.location.href = "/home";
});

// IDがheader_settingの要素を取得
const header_setting = document.getElementById("header_setting");

// IDがheader_settingの要素をクリックしたとき
header_setting.addEventListener("click", () => {
  // /settingに遷移する
  window.location.href = "/setting";
});

// IDがheader_signoutの要素を取得
const header_signout = document.getElementById("header_signout");

// IDがheader_signoutの要素をクリックしたとき
header_signout.addEventListener("click", () => {
  // サインアウトし、/loginに遷移する
  window.location.href = "/login";
});

// classに.listとついている要素を複数取得
const friendlists = document.querySelectorAll(".list");

friendlists.forEach((friendlist, i) => {
  friendlist.style.opacity = "0";

  const keyframes = {
    opacity: [0, 1],
    translate: ["-30px", "0px"],
  };
  const options = {
    duration: 300,
    delay: i * 100,
    fill: "forwards",
  };
  friendlist.animate(keyframes, options);

  friendlist.addEventListener("click", (e) => {
    const value1 = e.target.getAttribute('data-value1');
    const value2 = e.target.getAttribute('data-value2');
    const value3 = e.target.getAttribute('data-value3');
    document.getElementById('value1').textContent = value1;
    document.getElementById('value2').textContent = value2;
    document.getElementById('value3').src = value3;
    document.getElementById("modal_friend").style.display = "block";
  });
});

const friendaddmodal = document.getElementById("friendAdd");

friendaddmodal.addEventListener("click", () => {
  const modalfriadd = document.getElementById("modal_friendAdd");
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


const channel_edit = document.getElementById('channel_edit');

channel_edit.addEventListener('click', ( ) => {
  const modal_channel_edit = document.getElementById('modal_channel_edit');
  modal_channel_edit.style.display = 'block';
});

window.addEventListener("DOMContentLoaded", () => {
  const scrollmessage = document.getElementById("messagearea");
  // 要素内の最下部にスクロール
  scrollmessage.scrollTop = scrollmessage.scrollHeight;
});

const chatpage_fixedphrases = document.getElementById("chatpage_fixedphrases");

chatpage_fixedphrases.addEventListener("click", () => {
  const modal_chatpage_fixedphrases = document.getElementById(
    "modal_chatpage_fixedphrases");
  modal_chatpage_fixedphrases.style.display = "block";
});

// モーダルを閉じる（クローズボタン）イベントリスナーの追加
document
  .querySelectorAll(".modal_content_header_close")
  .forEach(function (element) {
    element.addEventListener("click", function () {
      let modalId = this.getAttribute("data-modal");
      document.getElementById(modalId).style.display = "none";
    });
  });

// モーダルの外側をクリックした時に閉じるイベントリスナーの追加
window.addEventListener("click", function (event) {
  if (event.target.classList.contains("modal")) {
    event.target.style.display = "none";
  }
});

const select_phrases = document.querySelectorAll(
  ".modal_content_body_box_fixedphrase"
);

select_phrases.forEach((select_phrase) => {
  select_phrase.addEventListener("dblclick", (e) => {
    const messageInput = document.getElementById("messageInput");
    messageInput.value = e.target.textContent;
    modal_chatpage_fixedphrases = document.getElementById(
      "modal_chatpage_fixedphrases"
    );
    modal_chatpage_fixedphrases.style.display = "none";
  });
});

select_phrases.forEach(selected_phrase => {
  selected_phrase.addEventListener('click', (e) => {
    select_phrases.forEach(phrase => {
      if (phrase !== e.target) {
        phrase.classList.remove('clicked');
      }
    });
    e.target.classList.add('clicked');
    e.stopPropagation();
  });
});
