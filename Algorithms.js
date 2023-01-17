/*
Ep-1

 Algorithm Basics 

-Well defined inputs and Outputs 
-Each step should be clear and unambiguous
-An Algorithm should be language independent
-It should written in such a way it can be used in different programming languages

Ep-2

Performance of an Algorithm

The absolute running time of an algorithm cannot be predicted,Since it depends on many factors
-Programming language used to implement the algorithm
-The computer the program runs on
-Other programs running at the same time 
-Quality of the operating system and many other factors...

We evalute the performance the of an algorithm in terms of its input size

They are two types
1)Time Complexity : Amount of time taken by an algorithm to run, as a function of input size
2)Space Complexity : Amo unt of memory taken by an algorithm to run, as a function of input size

By evaluating against the input size, the analysis is not only machine independent but the comparison is also more appropiate.

Ep-3 

How to represent complexity?

Asymptotic notations
-Mathematical tools to represent time and space complexity 

They are mainly #3 types of Asymptotic notations 
1) Big-O Notation (O-notation)-Worst case complexity 
2) Omega Notation (omega-Notation)-Best case complexity 
3) Theta Notation (0-NOtation)-Average case complexity



*/

// Problems 

/* // fibb

function fibb(n) {
    const set = [0,1];
    for(let i = 2 ; n > i ; i++ ){
        set[i] = set[i-1] + set[i-2];
    }
    console.log(set)
};
fibb(5)

*/

/*

// My code Factorial  program

function factorial(n){
    let num = 1;
    if(n === 0 ){console.log(1);}else{   
        while(n!==0){
        num = n*num;
        n--;
    }
    console.log(num);}
};
factorial(0);
factorial(4);
factorial(5);

*/

/*

// Youtuber's coding for factorial program

function factorial(n){
    let result = 1
    for(let i = 2 ; n >= i ; i++ ){
        result = result*i;
    }
    return result
};

*/

//Power of two