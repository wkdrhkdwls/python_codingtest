function solution(array, n) {
    array.sort((a,b)=>a-b)
    Narr=[]
    let a=0
    let b=0
    for(let i=0; i<array.length; i++){
        Narr.push(Math.abs(n-array[i]))
        a = Math.min(...Narr);
        b = Narr.indexOf(a)
    }
    return array[b]
}
