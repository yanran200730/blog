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

function Father(name,friends){
  this.name = name;
  this.friends = friends;
}
Father.prototype.money = "100k $";
Father.prototype.getName = function(){
  console.log(this.name);
};

function Son(name,age){
  // 继承父类的属性
  Father.call(this,name,['aaa','bbb']);
  
  this.age = age;
}

// 继承父类原型中的属性和方法
Son.prototype = new Father();
Son.prototype.constructor = Son;

Son.prototype.getAge = function(){
  console.log(this.age);
};

var s1 = new Son('son1',12);
s1.friends.push('ccc');
console.log(s1.friends);  // ["aaa", "bbb", "ccc"]
console.log(s1.money);    // 100k $
s1.getName();             // son1
s1.getAge();              // 12

var s2 = new Son('son2',24);
console.log(s2.friends);  // ["aaa", "bbb"]
console.log(s2.money);    // 100k $
s2.getName();             // son2
s2.getAge();              // 24
