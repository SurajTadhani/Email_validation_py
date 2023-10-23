# Email validation using string function

email =input("Enter Your Email : ")
k=0
j=0
d=0
error =0


if len(email) >=6:
    if email[0].isalpha():
        if ('@' in email) and (email.count('@') == 1):
            if(email[-4]== '.') ^ (email[-3] == '.'):
               for i in email:
                   if i==i.isspace():
                       k=1
                   elif i.isalpha():
                       if i==i.upper():
                           j=1
                   elif i.isdigit():
                       continue
                   elif i=='_' or i=='.' or i=='@':
                       continue

                   else:
                       d=1
               if k==1 or j==1 or d==1:
                   print("Wrong Email -- Please remove white spaces or please confirm signs or please confirm don't write first latter of alpha")

               else:
                   print("Yes This Email is right!")
            else:
                print("Wrong Email -- not right using of .in and .com on your email address")

        else:
            print("Wrong Email -- Not use @ sign or more than useing of @ sign")
    else:
        print("Wrong Email - not use of first character of alpha")

else:
    print("Wrong Email -- the character is less than 6")



