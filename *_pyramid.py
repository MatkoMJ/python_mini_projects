def pyramid_scheme(x):
    one=1
    i=0
    for i in range(x):
        space=" "*x
        minus=one-1
        row1=space+"*"*one
        row2="*"*minus
        print(row1+row2)
        one=one+1
        x=x-1

pyramid_scheme(4)


#output should be: 
     *
    ***
   *****
  *******
 *********
