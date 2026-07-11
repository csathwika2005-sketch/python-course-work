  '''class Flipkart:
        discount = 10
        product = ['laptop','phone','mouse','charger']

        @classmethod
        def showProducts(cls):
            print(cls.product)

        def login(self,username,password):
            self.username = username
            self.password = password
            print(f'welcome to the flipkart {self.username}')

        @staticmethod
        def banner():
            print("10% discount is going on flipkart, shop now!")


sathwika = Flipkart()
sathwika.login('sathwika','sathwika@2005')
sathwika.banner()
sathwika.showProducts()

Flipkart.showProducts()
Flipkart.banner()
'''
'''
class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.followers = []
        print(f'Welcome to instagram, {self.username}')

vamsi = Instagram('vamsi','vamsi@2005')
'''
'''
class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.followers = []
    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password = newpassword

vamsi = Instagram('vamsi','vamsi@2005')
print("Before username:",vamsi.username)
vamsi.username = 'praneeth'
print("After username:",vamsi.username)
print("Before password:",vamsi.getpassword())
vamsi.setpassword('praneeth@123')
print("After password:",vamsi.getpassword())
'''
