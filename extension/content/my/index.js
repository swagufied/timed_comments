jQuery(function(){
  chrome.runtime.sendMessage({'method': 'determineHost'}, function(response) {
    console.log('init jquery function')
    if (response.host){
      detectVideo(determineVideoSelector(response.host));
      getTimedComments();
      timedCommentSetup();
    }
  });
});


//for gogoanime testing
$('iframe').on('load', function(){
  if (!this.id){
    console.log(this)
    // contents = $(this).contents();
    // console.log(contents)
    var contentDoc = this.contentDocument || this.contentWindow.document;
    var iTarget = contentDoc.querySelectorAll('video');
    console.log(iTarget)
    // contentDoc.postMessage({''}, "*")
  }

})
