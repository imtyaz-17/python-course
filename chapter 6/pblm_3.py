str1 = 'Buy me a coffee'
str2 = 'like'
str3= 'subscribe'
str4 = 'click'

comment = input("Enter your comment: ")
if(str1 in comment or str2 in comment or str3 in comment or str4 in comment):
    print("Spam detected!")
else:
    print("No spam detected.")