string=int(input())
rev_string=str(string)
rev=rev_string[::-1]
if(rev_string==rev):
    print(0)
else:
    print(1)