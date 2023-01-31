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



//BOUNCING BALL


/*

let Ball = document.querySelector('div');
let Window_Height = window.innerHeight;
window.onresize = function(){Window_Height = window.innerHeight};
let Style_Tag= document.querySelector('style');
Ball.style.animationName = "Bouncing"
let Height = window.innerHeight;
Style_Tag.innerHTML = `
@keyframes Bouncing {
    from {top: 0px;
    background-color:rgb(87, 4, 87);
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    font-size: 43px;
}
    to {top: ${Height-142}px ;
    background-color : rgb(141, 23, 196);
}
  }`
window.onresize = function(){
    Height = window.innerHeight;
    Style_Tag.innerHTML = `
    @keyframes Bouncing {
        from {top: 0px;
        background-color:rgb(87, 4, 87);
        font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
        font-size: 43px;
    }
        to {top: ${Height-142}px ;
        background-color : rgb(141, 23, 196);
    }
      }
    `
}


*/



/*

In onresize :
when we assign a value to a variable dynamically then the value can't be taken outside the onresize function


Example:
<body>
    <div>
      Here is the Div tag
    </div>
       <script>
        let Change = 0;
        window.onresize = function(){
        Change = 121;}
        document.querySelector('div').innerHTML = Change;
       </script>

       Here When the window dimensions changes then "Change" value is not passed below statements that means it doesn't updates the value of varaiable "Change"
       It only Changes within the resize function thats it 


*/
/*
//Line Animation]
let a = document.querySelector('.one');
fetch('practise.json')
    .then(res => res.json())
    .then(value => a.innerHTML = `Rs. ${value.price}`)*/
/*
function res(){
    fetch('https://api.coindesk.com/v1/bpi/currentprice.json')
    .then(response => response.json())
    .then(price => console.log(price.data.bpi.USD.rate_float))
      setInterval(getBtcPrice, 10000) }
*/
/*

CRYPTO

let a = document.querySelector('.BTC');
let b = document.querySelector('.ETC');
let c = document.querySelector('.USDT');
let d = document.querySelector('.BNB');
let e = document.querySelector('.USDC');
let f = document.querySelector('.XRP');
let g = document.querySelector('.BUSD');

function call() {
    //fetch("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    fetch("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD")
    .then(res => res.json())
    .then(data => a.innerHTML = data.USD);
    fetch("https://min-api.cryptocompare.com/data/price?fsym=ETC&tsyms=USD")
    .then(res => res.json())
    .then(data => b.innerHTML = data.USD);
    fetch("https://min-api.cryptocompare.com/data/price?fsym=USDT&tsyms=USD")
    .then(res => res.json())
    .then(data => c.innerHTML = data.USD);
    fetch("https://min-api.cryptocompare.com/data/price?fsym=BNB&tsyms=USD")
    .then(res => res.json())
    .then(data => d.innerHTML = data.USD);
    fetch("https://min-api.cryptocompare.com/data/price?fsym=USDC&tsyms=USD")
    .then(res => res.json())
    .then(data => e.innerHTML = data.USD);
    fetch("https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD")
    .then(res => res.json())
    .then(data => f.innerHTML = data.USD);
    fetch("https://min-api.cryptocompare.com/data/price?fsym=BUSD&tsyms=USD")
    .then(res => res.json())
    .then(data => g.innerHTML = data.USD);

}
setInterval(() => {
    call();
},5000);
*/
/*
let x = document.querySelector('section')
for (let i = 10;i <= 56;i++){
    if(i !== 39){
        x.innerHTML +=`<div onclick="hero(22A81A06${i})"><img src="https://sves.org.in/Ecap/StudentPhotos/22A81A06${i}.jpg"><p>22A81A06${i}</p></div>`
    }
}
function hero(a)
{
    console.log(a)
}*/

