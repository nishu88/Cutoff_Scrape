import re


with open('data.txt','r',encoding='utf-8') as f:
    x=f.read().encode('unicode-escape').decode('utf-8')


#\d\d/\d\d/\d\d
#\+\d\d\s\d{5}\s\d{5}    
x=re.split('\s(pm|am)\s-\s(\+\d\d\s\d{5}\s\d{5}|\w+\s\w+):',x)

for i in x:
##    print(i)
##    print("**************************************************************")
    if "cutoff" in i.lower() or "cut off" in i.lower() or "cgpa" in i.lower() :
        print(i.replace("\\n",' \n '))
        print("**************************************************************")
        
                
       
#print(x)
##x=x.replace("\n", "  ").replace("\n", "  ").replace("\n", " ").replace("\n", " ")
##
##print(x)
##ans=re.findall(r"CGPA"  ,x)
##
##
##print(ans)
##print("**************************************************************")
