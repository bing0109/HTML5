s=0;

t=null;
aa=null;

function start(){
	
	t=setInterval(function(){
		if(aa!=null){
			clearTimeout(aa);
			aa=null;
		}
	
		step=Math.floor(window.innerWidth/100);
		s-=step;
		if(s<-(window.innerWidth*4)){
			s=0;
		}
		
		
		if(Math.abs(s)%window.innerWidth<step&&Math.abs(s)%window.innerWidth>=0){
			clearInterval(t);
			l=-(((Math.abs(s)/innerWidth)*innerWidth)-3*Math.floor(Math.abs(s)/innerWidth)*step);
			document.getElementById("inner").style.left=l+"px";
			s-=3*Math.floor(Math.abs(s)/innerWidth)*step;
			aa=setTimeout(function(){
				start();
			},2000);
		}else{
			document.getElementById("inner").style.left=s+"px";
		}

		
	
	
	},100);
}
start();

