function solution(num_list) {
    len = num_list.length
     num1 = num_list[len -1]
    num2 = num_list[len-2]
     num_list.push(num1 > num2 ? num1 - num2 : num1 * 2);
    return num_list
}