from datetime import datetime
a=datetime.now()
m=a.strftime("%d-%b-%y(%H:%M:%S)  =  ")
def date():
    import datetime
    return datetime.now()
k=True
j=True
print("Helth management system for performing thes following operations.: \n1.create new entry for food or exercise.\n2.Read your helth report.\n")
while(k):   
    try:
        a=int(input("Chose the following: \n1-Lokesh  \n2-kunal\n"))
        b=int(input("Comfirm your selection.:\n1-New entry. \n2-Retrieve data.\n"))
    except:
        print("sorry, i did not understand that\n")
        continue
    while(j):
        if a==1:
            if b==1:
                try:
                    ab=int(input("new entry for:- \n1-food\n2-exercise\n"))
                except :
                    print("sorry, i did not understand that\n")
                if ab==1:
                    c=str(input("enter what you eat today: \n"))
                    f=open("Lokesh_dite.txt","a")
                    f.write(m)
                    f.write(c+"   ")
                    f.write("\n")
                    f.close()
                    s=str(input("are you whant to write more data: (y/n) \n"))
                    if s=="y":
                        j=True
                    else:
                        j=False
                        k=False
                elif ab==2:
                    c=str(input("enter what you exercise today: \n"))
                    f=open("Lokesh_exercise.txt","a")
                    f.write(m)
                    f.write(c+"   ")
                    f.close()
                    s=str(input("are you whant to write more data: (y/n) \n"))
                    if s=="y":
                        j=True
                    else:
                        j=False
                        k=False
                else:
                    break  
            elif b==2:
                f=open("Lokesh_dite.txt","r")
                l=f.readlines()
                f.close()
                print(l)
                f=open("Lokesh_exercise.txt","r")
                l=f.readlines()
                f.close()
                print(l)
                j=False
                k=False
            else:
                break
        elif a==2:
            if b==1:
                try:
                    ab=int(input("new entry for:- \n1-food\n2-exercise\n"))
                except:
                    print("sorry, i did not understand that\n")
                if ab==1:
                    c=str(input("enter what you eat today: \n"))
                    f=open("kunal_dite.txt","a")
                    f.write(m)
                    f.write(c+"   ")
                    f.write("\n")
                    f.close()
                    s=str(input("are you whant to write more data: (y/n) \n"))
                    if s=="y":
                        j=True
                    else:
                        j=False
                        k=False
                elif ab==2:
                    c=str(input("enter what you exercise today: \n"))
                    f=open("kunal_exercise.txt","a")
                    f.write(m)
                    f.write(c+"   ")
                    f.close()
                    s=str(input("are you whant to write more data: (y/n) \n"))
                    if s=="y":
                        j=True
                    else:
                        j=False
                        k=False
                else:
                    break  
            elif b==2:
                f=open("kunal_dite.txt","r")
                l=f.readline()
                f.close()
                f=open("kunal_exercise.txt","r")
                l=f.readlines()
                f.close()
                print(l)
                print(l)
                j=False
                k=False
            else:
                break
            
    
        
