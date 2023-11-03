function solution(my_string) {
    My_string = [...my_string]
    for(let i=0; i<My_string.length; i++){
        if(My_string[i] == My_string[i].toUpperCase()){
            My_string[i] = My_string[i].toLowerCase()
        }else{
            My_string[i] = My_string[i].toUpperCase()
        }
    }
    return My_string.join("")
}