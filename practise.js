/*let bharath="great";
function add(a,b){
    return a**b;
};

// Array
let Array = [];
Array.push("Bharath");
Array.push("Madhan");


//Object
let Object = {
    FirstName : " Madhan ",
    lastName  : " Panja "
};
document.write(add(3,2)+ " " + Array + " " + Object.FirstName);*/
/* Calcultor */ 
/*
const FirstNumber = document.querySelector('h1');
const Click = n => FirstNumber.append(n);
const SecondNumber = document.querySelector('h4');

function Clear() {
    FirstNumber.innerHTML = '';
    SecondNumber.innerHTML = '';
}

const Calculate = () => {
    if(FirstNumber.innerHTML == ''){
        FirstNumber.innerHTML = 0;
        let a = parseFloat(FirstNumber.innerHTML);
        let b = parseFloat(SecondNumber.innerHTML);
        let see = SecondNumber.innerHTML.includes('+');
        SecondNumber.innerHTML = '';
        if(see){
            FirstNumber.innerHTML = a + b;
        }
    }
    else {
        let a = parseFloat(FirstNumber.innerHTML);
        let b = parseFloat(SecondNumber.innerHTML);
        let plus = SecondNumber.innerHTML.includes('+');
        let sub = SecondNumber.innerHTML.includes('-');
        let div = SecondNumber.innerHTML.includes('/');
        let multi = SecondNumber.innerHTML.includes('*');
        switch(FirstNumber.innerHTML !== '' ){
            case plus:
                FirstNumber.innerHTML = a + b;
                break
            case sub:
                FirstNumber.innerHTML = b - a;
                break
            case div:
                FirstNumber.innerHTML = b /a;
                break
            case multi:
                FirstNumber.innerHTML = a * b;
                break
            default:
                break
        }
        SecondNumber.innerHTML = '';
    }
}
const Operand = (n) => {
    if(FirstNumber.innerText.includes(n) && SecondNumber.innerText.includes(n) ){
         return
    }
    else{
         FirstNumber.append(n);
         SecondNumber.innerHTML = FirstNumber.innerHTML;
         FirstNumber.innerHTML = '';
    }
}
const mouse = document.getElementById('mouse');
const mouse1 = document.getElementById('mouse1');
const mouse2 = document.getElementById('mouse2');
const mouse3 = document.getElementById('mouse3');
setTimeout(console.log(window.innerHeight+ " " + window.innerWidth),1)
window.onmousemove = e => {
    const x = e.clientX,
          y = e.clientY;
    mouse.style.bottom = `${Math.random()*y}px`
    mouse1.style.bottom = `${Math.random()*y}px`
    mouse2.style.bottom = `${Math.random()*y}px`
    mouse3.style.bottom = `${Math.random()*y}px`
    mouse.style.margin = `${x , y , y , y}px`,mouse1.style.margin = `${x , y , y , y}px`,mouse2.style.margin = `${x , y , y , y}px`,mouse3.style.margin = `${x , y , y , y}px`
}

if(1 == 1){
        var Name = "Madhan"
        console.log("It is inside the block level component i.e if  while \n" + Name) 
}
console.log("Call Name variable outside the if \n" + Name)

if(1 == 1){
    let Madhan = 1
}
console.log(Madhan)

x = 1
function Resloved(){
    y = 1 
    if(1 === 1){
         z = 1
        console.log(y)
        console.log(x)
    }
    console.log(z)
}
Resloved() */
/* Generator Function */
/*function* generate(){
    yield 1;
    yield 2;
    return 3;
}
let generator = generate();
let one = generator.next();
let two = generator.next();
let three = generator.next();
alert(JSON.stringify(one));
alert(JSON.stringify(two));
alert(JSON.stringify(three));
*/

let Ball = document.querySelector('div');
let Window_Height = window.innerHeight;
let Style_Tag= document.querySelector('style');
if(Ball.style.margin == !Window_Height){
    Style_Tag.innerHTML = `
    @keyframes Bouncing {
        from {top: 0px;
        background-color:rgb(87, 4, 87);
        font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
        font-size: 43px;
    }
        to {top: ${Window_Height-142}px ;
        background-color : rgb(141, 23, 196);
    }
      }
    `
    Ball.style.animationName = "Bouncing"
}