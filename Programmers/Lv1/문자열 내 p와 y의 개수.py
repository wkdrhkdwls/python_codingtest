def solution(s):
    str_p = s.lower().count("p")
    str_y = s.lower().count("y")
    if str_p == str_y:
        return True
    else:
        return False
        