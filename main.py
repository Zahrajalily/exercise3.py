#شمارش حروف اسم و فامیل
name =input("enter your name: ")
name=name.lower()
name=name.strip()  #this method delete space from first and the end of line 
name=name.replace(" ","")  #you can by this method delete all spaces
a=[]
for n in name:
    if n not in a :
     print(f"your name has{ name.count(n)} {n}" )
     a.append(n)
