function solution(s){
    let count=0;
    for(let i=0, count=0; i<s.length; i++){
        if(s[i]==='('){
            count++;
        }else if(s[i] === ')'){
            count--;
        }
        
        if(count <0){
            return false;
        }
        if(i === s.length -1){
            return count==0 ? true : false;
        }
    }
    return true;
}