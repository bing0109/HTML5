s=0;
step=window.innerWidth/100;

function start(){
	t=setInterval(function(){
	
	s-=step;
	if(s<-(window.innerWidth*4)){
		s=0;
	}
	console.log(s);
	if(Math.floor(s-3*step)%window.innerWidth==0||Math.ceil(s-3*step)%window.innerWidth==0){
		clearInterval(t);
		setTimeout(function(){
			start();
		},2000);
	}
	document.getElementById("inner").style.left=s+"px";
	
	
	},100);
}
start();


