
print( "\033c\033[40;37m\give the file .txt reg key to show ? ")
#a=input()
backs=""
a="score.txt"
f1=open(a,"r")
b=f1.read()
f1.close()
c=b.split("\n")
for counter in range(len(c)):
    c[counter]=c[counter].strip()
    if c[counter]!="":
        ss=c[counter].split(",")
        ss[0]=ss[0].strip()
        sss=""
        if len(ss)>1:
            sss=ss[1].strip()
            xxx="000000000000"+sss
            e=len(xxx)-12
            xxx=xxx[e:]
            c[counter]=xxx+","+ss[0]
c.sort()
for counter in range(len(c)):
    c[counter]=c[counter].strip()
    if c[counter]!="":
        ss=c[counter].split(",")
        ss[0]=ss[0].strip()
        sss=""
        if len(ss)>1:
            ii=0
            sss=ss[0].strip()
            
            try:
                ii=int(sss)
                
                sss=str(ii)
                print(ss[1]+","+sss)
            except:
                u=0
