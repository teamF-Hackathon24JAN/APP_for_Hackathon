const lists = document.querySelectorAll('.list');

lists.forEach((list,i) =>{
    list.style.opacity = '0';

    const keyframes = {
        opacity: [0,1],
        translate:['-30px','0px']
    };
    const options = {
        duration:300,
        delay: i * 100,
        fill:'forwards'
    };
    list.animate(keyframes,options);
});


const upbutton = document.querySelector('#upicon');
const downbutton = document.querySelector('#downicon');
const friendscontainer = document.querySelector('#friends-scrollcontainer');

const leftbutton = document.querySelector('#lefticon');
const rightbutton = document.querySelector('#righticon');
const channelscontainer = document.querySelector('#channel-box');

upbutton.addEventListener('click', () => {
    // containerを上方向に50pxスクロールさせる
    friendscontainer.scrollBy({top: -50, behavior: 'smooth' });
});

downbutton.addEventListener('click', () => {
      // containerを下方向に50pxスクロールさせる
      friendscontainer.scrollBy({top: 50, behavior: 'smooth' });
});

leftbutton.addEventListener('click', () => {
        // containerを左方向に100pxスクロールさせる
    channelscontainer.scrollBy({top: 0, left:-100, behavior: 'smooth' });
});

rightbutton.addEventListener('click', () => {
    // channelscontainerを右方向に100pxスクロールさせる
    channelscontainer.scrollBy({top: 0, left:100, behavior: 'smooth' });
});


// for (i = 0 ; i <  lists.length ; i++) {
//     const keyframes = {
//         opacity: [0,1],
//         translate:['-30px','0px']
//     };
//     const options = {
//         duration:300,
//         delay: i * 100,
//         fill:'forwards'
//     };
//     lists[i].animate(keyframes,options);
// }
