var server_url = 'http://localhost:5000/get-timed-comments';


chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
  if (message.method == "determineHost") {
    var validHosts = ['gogoanime', 'crunchyroll'];
    var hostName = getHostName(sender.url)
    console.log(getHostName(sender.url))
    if (validHosts.indexOf(hostName) > -1){
      console.log('host is valid')
      sendResponse({'host':hostName})
    } else {
      console.log('host is not valid')
      sendResponse({})
    }
    return true
  } else if (message.method == "getTimedComments"){
      console.log('getting timed comments')
         tab_url = sender.url;
         $.ajax({
           url: server_url,
           data: {'url': tab_url},
           type:'GET',
           success: function(response){
             console.log(response)
             console.log(response.success)
             if (response.success){
               console.log(response.success)
               console.log(response.timed_comments);
               sendResponse({timed_comments:response.timed_comments})
             } else {
               console.log('cant connect')
             }

           },
           error: function(xhr, status, error) {
             console.log('retrive comments failed')

           }
         });

      return true;

    }

});

function getHostName(url) {
    var match = url.match(/:\/\/(www[0-9]?\.)?(.[^/:]+)/i);
    if (match != null && match.length > 2 && typeof match[2] === 'string' && match[2].length > 0) {
      split_match = match[2].split('.');
      return split_match[0];
    // return match[2];
    }
    else {
        return null;
    }
}

// chrome.tabs.onUpdated.addListener(function(tabid, info, tab) {
//   console.log(tabid)
//   console.log(tab)
//     console.log(info);
// });
