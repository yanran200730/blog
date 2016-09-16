window.onload = function(){
	var botton = document.getElementById('button').getElementsByTagName('span'),
		form   = document.getElementsByTagName('form');

		for (var i=0;i<botton.length;i++){
			botton[i].index = i;
			botton[i].onclick = function(){
			for (var j=0;j<botton.length;j++){
				form[j].style.display = 'none';
				botton[j].className = 'none';
			}
			form[this.index].style.display = 'block';
			this.className = 'botton_sytle';
		}
	}
}

