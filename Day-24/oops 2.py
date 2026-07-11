'''class Instagram:
    def __init__(self):
        self._post = []
    @property
    def accesspost(self):
        return self._post
    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)

dinesh = Instagram()

print(dinesh.accesspost)
dinesh.accesspost = 'class and object'
print(dinesh.accesspost)
'''
'''
class whatsappv1:
    def message(self):
        print("You can send messages to people")

class whatsappv2(whatsappv1):
    def calls(self):
        print("You can do video/audio calls")

dinesh = whatsappv1()
print("v1 - Dinesh")
dinesh.message()


naresh = whatsappv2()
print("v2 - Naresh")
naresh.message()
naresh.calls()
'''
'''
class whatsappv1:
    def message(self):
        print("You can send messages to people")

class whatsappv2:
    def calls(self):
        print("You can do video/audio calls")

class whatsappv3:
    def media(self):
        print("You can share photos/videos")

class whatsappv4(whatsappv1,whatsappv2,whatsappv3):
    def status(self):
        print("You can share status-[24 hours]")

dinesh = whatsappv4()
print("v4 - Dinesh")
dinesh.message()
dinesh.calls()
dinesh.media()
dinesh.status()
'''
'''
class whatsappv1:
    def message(self):
        print("You can send messages to people")

class whatsappv2(whatsappv1):
    def calls(self):
        print("You can do video/audio calls")

class whatsappv3(whatsappv2):
    def media(self):
        print("You can share photos/videos")

class whatsappv4(whatsappv3):
    def status(self):
        print("You can share status-[24 hours]")

dinesh = whatsappv4()
print("v4 - Dinesh")
dinesh.message()
dinesh.calls()
dinesh.media()
dinesh.status()
'''
'''
class whatsappv1:
    def message(self):
        print("You can send messages to people")
class whatsappv2(whatsappv1):
    def emojis(self):
        print("You can send message with emojis to people")
class whatsappv3(whatsappv1):
    def stickers(self):
        print("You can send message with sticker to people")

sathwika = whatsappv2()
print("v2- sathwika")
sathwika.message()
sathwika.emojis()
'''
'''
class whatsappv1:
    def message(self):
        print("You can send messages to people")
class whatsappv2(whatsappv1):
    def emojis(self):
        print("You can send message with emojis to people")
class whatsappv3(whatsappv1):
    def stickers(self):
        print("You can send message with sticker to people")
class whatsappv4(whatsappv3,whatsappv2):
    def gif(self):
        print("You can send messages with stickers to people")

sathwika = whatsappv4()
print("v4- sathwika")
sathwika.message()
sathwika.emojis()
sathwika.stickers()
sathwika.gif()
'''
'''
class wpv1:
    def status(self):
        print("You can upload images/videos")
class wpv2(wpv1):
    def status(self):
        super().status()
        print("You can upload images/videos")
class wpv3(wpv2):
    def status(self):
        super().status()
        print("You can like and reshare")

sathwika = wpv3()
sathwika.status()
'''
'''
class wpv1:
    def status(self):
        print("You can upload images/videos")
class wpv2:
    def status(self):
        print("You can react and reply")
class wpv3(wpv2,wpv1):
    def status(self):
        wpv1.status(self)
        wpv2.status(self)
        print("you can like and reshare")
sathwika = wpv3()
sathwika.status()
'''
