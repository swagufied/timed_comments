var tab_url;
$('form').on('submit', function(event){
  console.log('submitting form')
  event.preventDefault();
  var url = $(this).attr('action');
  var formdata = new FormData($(this)[0]);
  formdata.append('tab_url', tab_url);

  $.ajax({
    url: url,
    data: formdata,
    type: 'POST',
  	processData: false,
    contentType: false,
    success: function(response){
      console.log('ajax success? = ' + response.status);

			if (response.form_errors){
				var errors = response.form_errors
				for (var k in errors){
					name = '.' + k + "-errors";
					$(name).text(errors[k][0]);
				}
			}
    },
    error: function(xhr){
      console.log('ajax failed')
        var err = xhr.responseText;
        console.log(err)
    }
  });
});

jQuery(function(){
  console.log('popup html loaded')
  chrome.tabs.query({ 'active': true, 'lastFocusedWindow':true}, function (tabs) {
    tab_url = tabs[0].url;
    $('.live-comment-target').html(tab_url)
  });
});
//
//
// $('form').on('submit', function(event){
//   event.preventDefault();
//   var url = $(this).attr('action');
//   var data = {};
//   $(this).find('input').each(function(){
//     console.log($(this).attr('name'));
//     console.log($(this).val());
//     data[$(this).attr('name')] = $(this).val();
//   })
//   console.log(data);
//   var formdata = new FormData($(this)[0]);
//
//
//   chrome.runtime.sendMessage({'method': "submitTimedComment", "url": url, "data":data}, function(response) {
//     console.log(response)
//     console.log('msg sent')
//   });
// });
