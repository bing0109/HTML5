k=0;
t=setInterval(function(){
	k-=1;
	if(k<-30){
		k=0;
	}
	document.getElementById("liebiao").style.top=k+"px";
	
},100);
function addclass(){
	document.getElementById("xiala").className="ishide";
}
function removeclass(){
	
	document.getElementById("xiala").className="ishow";
	e.stopPropagation();
}
function preventclass(){
	e.stopPropagation();
}