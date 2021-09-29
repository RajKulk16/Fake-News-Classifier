// if(!!window.IntersectionObserver){
// 	let video = document.querySelector('video');
// 	let isPaused = false; /* flag for auto-pausing of the video */
// 	let observer = new IntersectionObserver((entries, observer) => {
// 		entries.forEach(entry => {
// 			if(entry.intersectionRatio!=1  && !video.paused){
// 				video.pause(); isPaused = true;
// 			}
// 			else if(isPaused) {video.play(); isPaused=false}
//
// 		});
// 	}, {threshold: 1});
// 	observer.observe(video) ;
// }


let videos = document.querySelectorAll("video");
    videos.forEach((video) => {
        // We can only control playback without insteraction if video is mute
        video.muted = true;
        // Play is a promise so we need to check we have it
        let playPromise = video.play();
        if (playPromise !== undefined) {
            playPromise.then((_) => {
                let observer = new IntersectionObserver(
                    (entries) => {
                        entries.forEach((entry) => {
                            if (
                                entry.intersectionRatio !== 1 &&
                                !video.paused
                            ) {
                                video.pause();
                            } else if (video.paused) {
                                video.play();
                            }
                        });
                    },
                    { threshold: 1 }
                );
                observer.observe(video);
            });
        }
    });

// else document.querySelector('#warning').style.display = 'block';
// const video = document.querySelector("video");
// let playState = null;
//
// const observer = new IntersectionObserver((entries) => {
//   entries.forEach((entry) => {
//     if (!entry.isIntersecting) {
//       video.pause();
//       playState = false;
//     } else {
//       video.play();
//       playState = true;
//     }
//   });
// }, {});
//
// observer.observe(video);
// const video = document.querySelector("video");
//
// const observer = new IntersectionObserver((entries) => {
//   entries.forEach((entry) => {
//     if (!entry.isIntersecting) {
//       video.pause();
//     } else {
//       video.play();
//     }
//   });
// }, {});
//
// observer.observe(video);
