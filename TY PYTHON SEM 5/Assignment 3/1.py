# Write a python program to check whether the string is Symmetrical or Palindrome
def check_sym(string):
    n=len(string)
    flag=0
    if n%2:
        mid=n//2+1
    else:
        mid= n//2
    start=0
    end= mid
    while(start <mid and end<n):
        if(string[start]== string[end]):
            start= start+1
            end= end+1
        else:
            flag=1
            break
    if flag==0:
        print("symmetrical or palindrome")
    else:
        print("not symmetrical not palindrome")

# main
s= "abcabc"
print (s)
check_sym(s)
s2= "abcdab"
print(s2)
check_sym(s2)
