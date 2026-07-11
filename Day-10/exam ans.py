'''data={
    "sathu":{'status':True,'python':97,'mysql':78,'flask':80},
    "prava":{'status':True,'python':87,'mysql':70,'flask':60},
    "saniya":{'status':False,'python':None,'mysql':None,'flask':None},
    "rishi":{'status':True,'python':57,'mysql':50,'flask':50}
    }
name=input()
if name in data:
              if data[name]['status']:
                       total=data[name]['python']+data[name]['mysql']+data[name]['flask']
              avg=total/3
              if avg>90:
                       print(f"congratualations{name}")
              if avg>70:
                       print(f"good{name}")
              if avg>35:
                       print(f"fail{name}")
              else:
                  print(f"{name}is not attend the exam")
else:
     print(f"{name}s data is not found")
                       
'''
'''budget=int(input("enter the budget:"))
if budget>30000:
    print("you can go for pub")
elif budget>10000:
    print("you can go for shopping")
elif budget>5000:
    print("you can go for movie")
else:
    print("take a break")
'''
hrs,mins=list(map(int,input("enter the time(HH:MM):").split(':')))
if 0 <=hrs<=23 AND 0<= mins <=59:
    
