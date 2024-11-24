import random 

def pickaball():
    balls = ['Red','Blue','Green']

    result = random.choice(balls)

    pro = balls.count('Red')/len(balls)
    print("Probability of picking Red Ball is:", pro)

    if result == 'Red':
        return 'Red is sus'
    else:
        return 'Bad luck'
    
print(pickaball())