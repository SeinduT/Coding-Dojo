import random
def randInt(min= 0, max= 100):
    range = max - min
    num = random.random()
    return round(num * range + min)
print(randInt())
print(randInt(max=50))
print(randInt(min=50)) 	
print(randInt(min=50, max=500))  
