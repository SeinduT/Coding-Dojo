var testArr = [6,3,5,1,2,4]
var sum = 0
var mulPos = ""
for (i = 0; i < testArr.length; i++){
    sum += testArr[i];
    console.log ("Num ", testArr[i], "Num ", sum);
}
for (i = 0; i < testArr.length; i++){
    mulPos = testArr[i] * i;
    console.log (mulPos)
}