'''class Hotstar:
    def __init__(self,name):
        self.name = name
        print(f'Hi {self.name},Welcome to the hotstar')
    def login(self):
        print("you can login")
    def dashboard(self):
        print("you can see the dashboard items")
    def search(self):
        print("you can search")
    def languages(self):
        print("you select the languages")
    def playcontrollers(self):
        print("you can pause and play the video")
    def ads(self):
        print("Ads will run")
    def movies(self):
        print("you can limited acess for movies")
    def sports(self):
        print("Limited time you can watch sports")
    def quality(self):
        print("Limited quality")
class PremiumHotstar(Hotstar):
    def __init__(self,name):
        self.name = name
        print(f'Hi {self.name},Welcome to the hotstar')
    def ads(self):
        print("Ads wont run")
    def movies(self):
        print("you can unlimited acess for movies")
    def sports(self):
        print("you can watch sports")
    def quality(self):
        print("High quality")
sathwika = Hotstar('sathwika')
sathwika.login()
sathwika.dashboard()
sathwika.search()
sathwika.languages()
sathwika.playcontrollers()
sathwika.ads()
sathwika.movies()
sathwika.sports()
sathwika.quality()


sath = PremiumHotstar('sath')
sath.login()
sath.dashboard()
sath.search()
sath.languages()
sath.playcontrollers()
sath.ads()
sath.movies()
sath.sports()
sath.quality()
'''
'''
class Number:
    def __init__(self,n):
        self.n = n
    def __add__(self,other):
        return self.n + other.n
    def __sub__(self,other):
        return self.n - other.n
    def __mul__(self,other):
        return self.n * other.n
    def __truediv__(self,other):
        return self.n / other.n
    def __eq__(self,other):
        return self.n == other.n
    def __lt__(self,other):
        return self.n < other.n
    def __gt__(self,other):
        return self.n > other.n
    def __str__(self):
        return str(self.n)
n1 = Number(10)
n2 = Number(20)

print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)

print(n1==n2)
print(n1<n2)
print(n1>n2)
print(n1,n2)
'''
