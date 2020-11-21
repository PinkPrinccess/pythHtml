let arr = [2, 5, 6, 19, 55];

let res = arr.map(function(elem) {
	return Math.sqrt(elem)
});

console.log(res);


let mah = ['окно','бочка', 'консоль', 'солдат', 'кот'];

res1 = mah.map(function(elem) {
	return elem + '!'
});
	
console.log(res1);


let str = ['камень','фонарь', 'платформа', 'аниме', 'экран'];

res2 = str.map(function(elem) {
	return elem.split('').reverse().join('')
});

console.log(res2);


let arr2 = ['87', '156', '712'];

let res3 = arr2.map(function(elem) {
	return elem.split('')
});

console.log(res3);


let arr3 = [1, 5, 9, 1, 4];

let res4 = arr3.map(function(elem, index) {
	return elem * index;
});

console.log(res4); 