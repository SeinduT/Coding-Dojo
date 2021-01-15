//1///
var results = [];
function array() {
    for (i=0; i<=255; i++) {
        results.push (i);
    }
}
array();
console.log (results);

//2//
function sum() {
    var result = 0;
    for (var i=0; i<=1000; i++){
        if (i % 2 == 0){
            result = result + i;
        }
    }
    return result;
}
console.log (sum());

//3//
function sum() {
    var result = 0;
    for (var i=1; i<=5000; i+=2){
        if (i % 2 == 1){
            result = result + i;
            console.log(i);
        }
    }
    return result;
}
console.log (sum());

//4//
function iterate(numArr) {
    var sum = 0;
    for (var i = 0; i < numArr.length; i++) {
        sum = sum + numArr[i];
    }
    return sum;
}
console.log (iterate([1,2,5]));

//5//
function findMax(arr) {
    var max = arr [0];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}
console.log (findMax([-3,3,5,7]));

//6//
function findAvg (arr) {
    var sum =0;
    var avg = 0;
    for (var i = 0; i < arr.length; i++) {
        sum = sum + arr[i];
    }
    avg = sum / arr.length;
    return avg;
}
console.log (findAvg([1,3,5,7,20]));

//7//
function arrOdd () {
    var odd = [];
    for (var i = 0; i <= 50; i++) {
        if (i % 2 != 0) {
            odd.push (i);
        }
    }
    return odd;
}
console.log (arrOdd());

//8//
function greaterY (arr) {
    var y = 3;
    greater = [];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > y) {
            greater.push (arr[i]);
        }
    }
    return greater.length;
}
console.log (greaterY([1,3,5,7]));

//9//
function squares (arr) {
    var newValues = [];
    for (var i = 0; i < arr.length; i++) {
        arr[i] = arr[i] * arr[i];
        newValues.push (arr[i]);
    }
    return newValues;
}
console.log (squares([1,5,10,-2]));

//10//
function noNegative (arr) {
    var newArr = [];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] < 0) {
            arr[i] = 0;
            newArr.push (arr[i]);
        }
        else {
            newArr.push (arr[i]);
        }
    }
    return newArr;
}
console.log (noNegative([1,5,10,-2]));

//11//
function maxMinAvg (arr) {
    var newArr = [];
    var max = arr [0];
    var min = arr [0];
    var sum = 0;
    var avg = 0;
    for (var i = 0; i < arr.length; i++) {
        sum = sum + arr[i];
        avg = sum / arr.length;
        if (arr[i] > max) {
            max = arr[i];
        }
        else if (arr[i] < min) {
            min = arr[i];
        }
    }
    newArr.push (max);
    newArr.push (min);
    newArr.push (avg);
    return newArr;
}
console.log (maxMinAvg([1,5,10,-2]));

//12//
function swap (arr) {
    var temp = arr[0];
    var i = arr.length -1;
        arr[0] = arr[i];
        arr[i] = temp;
    return arr;
}
console.log (swap([1,5,10,-2]));

//13//
function stringNum (arr) {
    newArr = [];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] < 0) {
            newArr.push ("Dojo");
        }
        else {
            newArr.push (arr[i]);
        }
    }
    return newArr;
}
console.log (stringNum([-1,-3,2]));