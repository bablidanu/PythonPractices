def is_symmetric(s):
    lenght = len(s)
    mid = lenght // 2
    if lenght % 2==0:
        return s[:mid] == s[mid:]
    else :
        return s[: mid ] == s [mid +1:]
    

s = "vmava"   # Example


if is_symmetric(s):
    print("Given string is symmetrical")
else :
    print("Given string is not symmetrical")


