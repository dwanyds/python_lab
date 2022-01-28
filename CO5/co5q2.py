fr=open("hello.txt","r")
fw=open("new.txt","w")
s=fr.readlines()
for i in range(0,len(s)):
    if(i%2==0):
        fw.write(s[i])
fw.close()
for i in s:
    print(i)
print("\n**************odd lines***********\n")
fr2=open("new.txt","r")
for i in fr2.readlines():
    print(i)
fr2.close()
fr.close()
    
               

    
