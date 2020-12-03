let arr = [1,-5,10,324,5,13,19];

let res = arr.filter(function(elem,index){
    if (elem*index < 30){return true;}
    else{return false;}
});

console.log(res);