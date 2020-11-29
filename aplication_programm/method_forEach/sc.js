let arr = [1, 2, 3, 4, 5];
let sum = 0;
let sum1 = 0;
let sum2 = 0;

arr.forEach(function(elem) {
	sum += elem*elem;
});

arr.forEach(function(elem) {
	sum1 += elem+elem;
});

arr.forEach(function(elem) {
	sum2 += elem-elem;
});
console.log(sum);
console.log(sum1);
console.log(sum2);

function aa(){
	cat.style.width='55px'
}