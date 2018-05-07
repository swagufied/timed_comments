// debugger;

function updateTimedComments(){
  var currentTime = String(parseInt(eimeerTimedCommentVideo.currentTime()));

  if (currentTime && currentTime in eimeerTimedComments && eimeerTimedComments[currentTime].length >= 1){
    console.log('rendering comments')
    renderTimedComments(eimeerTimedComments[currentTime][0], currentTime);
  }
}


function renderTimedComments(comment, currentTime){
  var displayedComments = $('div.eimeer-timed-comment-box');

  if ($(displayedComments).length > 0){
    displayedComments.each(function(){
      $(this).remove();
    });
  }

  var commentBox = onScreenCommentBox(comment, currentTime);
  $(commentBox).insertBefore($('#' + eimeerVideoID));
  setTimeout(function(){
    $(commentBox).fadeOut(1000, function(){
      $(this).remove();
      });
    }, 3000);
}

function renderProgressBox(videoDuration){
  console.log('duration: ' + videoDuration)

}

function onScreenCommentBox(comment, currentTime){
  return  $([
  "<div class='eimeer-timed-comment-box eimeer-overlay'>",
  "<div class='eimeer-timed-comment-information-line'>",
  "<div class='eimeer-timed-comment-username'>",
  comment['username'],
  "</div>",
  "<div class='eimeer-timed-comment-time'>",
  prettifyTime(currentTime),
  "</div>",
  "</div>",
  "<div class=eimeer-timed-comment-content>",
  comment['content'],
  "</div>",
  "</div>"
].join("\n"));
}

function prettifyTime(time) {
  time = parseInt(time);
  minutes = parseInt(time/60);
  seconds = ("0" + time%60).slice(-2);

  return String(minutes + ':' + seconds);
}
