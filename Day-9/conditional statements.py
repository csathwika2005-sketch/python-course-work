s='java progaming'
if 'java' in s:
    print('java found')
if s[0]=='j':
    print('string is starting with p')


data=('sdf','123')
username,password = input("enter the user name and password:").split()
if data ==(username,password):
    print("login succesful")
else:
    print("wrong password")


n=int(input("Enter the num:"))
if n>0:
    print("+ve")
elif n<0:
    print("-ve")
else:
    print("0")


products={
    'laptop':0,
    'mouse':5,
    'charger':44,
    'books':3
}
product= input("enter the product:")
if product in products:
    if products[product]!=0:
        print(f"you can buy {product}!!")
    else:
        print(f"{product}out of stock")
else:
    print(f"{product}is not available")
