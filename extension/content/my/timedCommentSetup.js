var eimeerVideoID = 'eimeer-timed-comment-video', eimeerTimedCommentVideo, eimeerTimedComments;



//searches for video given selector
function detectVideo(videoSelector) {
  console.log('detecting video')
  var videoPing = setInterval(function() {
    var video = $(videoSelector)[0];
    if ($(video).length > 0) {
      console.log('found video')
      console.log($(video))
      clearTimeout(videoPing);
      var videoID = $(video).attr('id');
      if (!videoID) {
        videoID = eimeerVideoID;
        $(video).attr('id', videoID);
      }

      $('#' + eimeerVideoID).onload() = function(){
        console.log('iframe loaded')
      }

      eimeerTimedCommentVideo = videojs(videoID, {}, function() {
        console.log('videojs obj created')
        var videojsObj = this;
        this.on('loadedmetadata', function() {
          console.log('metadata loaded')
          var videoDuration = parseInt(videojsObj.duration());
          renderProgressBox(videoDuration);

          setInterval(function(){
            console.log(videojsObj.currentTime())
          }, 2000)
        });
      });
    } else {
      console.log('havent found video')
    }
  }, 1000);
  setTimeout(function(){clearTimeout(videoPing);}, 20000)
}
//retrieves timed comments
function getTimedComments() {
  console.log('getting timed comments')
  var commentsPing = setInterval(function(){
    console.log('calling for comments')

    chrome.runtime.sendMessage({'method': "getTimedComments"}, function(response) {
      eimeerTimedComments = response.timed_comments;
      clearTimeout(commentsPing);
    });
  }, 10000);

  chrome.runtime.sendMessage({'method': "getTimedComments"}, function(response) {
    eimeerTimedComments = response.timed_comments;
    clearTimeout(commentsPing);
    console.log('calling for comments')
  });

  setTimeout(function(){clearTimeout(commentsPing);}, 20000);

}


//renders comments if comments are available
function timedCommentSetup(){

  var renderCommentsTimeout = setTimeout(function(){clearTimeout(setupTimedCommentsPing);}, 40000);
  var setupTimedCommentsPing = setInterval(function() {
    if (eimeerTimedComments){
      clearTimeout(renderCommentsTimeout);
      clearTimeout(setupTimedCommentsPing);
      setInterval(updateTimedComments, 1000);
    }
  }, 1000);
}



//returns selector depending on site
function determineVideoSelector(host) {
  console.log('host = ' + host)
  if (host == 'crunchyroll') {
    return 'video.video-stream';
  } else if (host.includes('gogoanime')) {
    return $('div.play-video').find('iframe');
  } else {
    return ""
  }
}
