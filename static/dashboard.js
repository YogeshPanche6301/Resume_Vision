const circle = document.querySelector(".progress");

const score = Number(circle.dataset.score);

const radius = 85;

const circumference = 2 * Math.PI * radius;

circle.style.strokeDasharray = circumference;

circle.style.strokeDashoffset = circumference;

const offset = circumference - (score / 100) * circumference;

setTimeout(() => {

    circle.style.strokeDashoffset = offset;

},300);

let current=0;

const number=document.getElementById("scoreNumber");

const timer=setInterval(()=>{

    current++;

    number.innerHTML=current+"%";

    if(current>=score){

        clearInterval(timer);

    }

},20);