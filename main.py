class Grandparents:
    sped = 1
    sick = 'heart disease'
    height = 150
class Parents(Grandparents):
    height = 175
    speed = 5
class Child(Parents):
    speed = 8
    def __init__(self):
        print(self.sick)
        print(self.height)
        print(self.speed)
max_roma_pavlo = Child()
#lesson6
import requests
help(requests)
rq = requests
print("For mother",requests.__cake__)
print(rq.__name__)
print(rq.__url__ )
print(type(3))
ls = []
for i in dir(ls):
    print(i)
print(dir(ls))