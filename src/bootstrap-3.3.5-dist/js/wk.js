function image_upload(){
	window.alert('アラートの表示');
	var gazo_full = document.getElementById("image_up").value;
	var file_name = GetFileName(gazo_full);

	window.alert(file_name)
}

function GetFileName(file_url){
   file_url = file_url.substring(file_url.lastIndexOf("\\")+1,file_url.length)
   //拡張子も取り除く場合は以下のコメントアウト解除
   //file_url = file_url.substring(0,file_url.indexOf("."));
   return file_url;
}

