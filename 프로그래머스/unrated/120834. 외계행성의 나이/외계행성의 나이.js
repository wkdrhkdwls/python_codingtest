function solution(age) {
   
    let res =""
    let arrayAge=String(age).split("").map(Number)
    for(let i=0; i<arrayAge.length; i++){
        res+= String.fromCharCode(arrayAge[i]+97)
    }
    return res
}