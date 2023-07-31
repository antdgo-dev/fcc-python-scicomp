# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator

# For public execution and test
# https://replit.com/@ToniG4/boilerplate-probability-calculator


import copy
import random

class Hat :

    def __init__(self, **kwargs) :

        self.contents = []
        self._contents_dict = {}

        for ball, n_balls in kwargs.items() :

            i = 0
            while i < n_balls :
                self.contents.append(ball)
                self._contents_dict[ball] = n_balls
                i += 1
    

    def draw(self, n_balls) :

        drawn_balls = []

        # Draw all balls
        if n_balls >= len(self.contents) :

            drawn_balls = copy.deepcopy(self.contents)
            self.contents = []
        
        # Draw a number of balls by selecting the "contents" indexes randomly
        else :

            contents_indexes = []
            i = 0
            while i < len(self.contents) :
                contents_indexes.append(i)
                i += 1
            
            ball_indexes = random.sample(contents_indexes, n_balls)
            ball_indexes.sort(reverse = True) # to start picking balls from the end

            for idx in ball_indexes :
                drawn_balls.append(self.contents[idx])
                del self.contents[idx]
            
        return drawn_balls


    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments) :

    m = 0 # the number of successful experiments

    i = 0
    while i < num_experiments :
        
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)   
        
        # Put the balls in a dictionary
        drawn_balls = {}
        for ball in balls :

            try :
                if drawn_balls[ball] : drawn_balls[ball] += 1
            
            except :
                drawn_balls[ball] = 1
        
        # Compare the drawn balls with the "expected_balls" (r: result of the experiment)
        for ball, count in expected_balls.items() :
            
            try :
                if drawn_balls[ball] and drawn_balls[ball] >= count : r = True
                else :
                    r = False
                    break
            
            except :
                r = False
                break
        
        if r : m += 1 # count of successful experiments

        i += 1


    return m/num_experiments


# Example execution and tests

#hat1 = Hat(yellow=3, blue=2, green=6)
#hat2 = Hat(red=5, orange=4)
#hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

#print(hat1.contents)
#print(hat2.contents)
#print(hat3.contents)

#hat = Hat(red=5,blue=2)
#print(hat.contents)
#print(hat.draw(3))
#print(hat.contents)
#print(len(hat.contents))


hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print(probability)


hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
print(probability)


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={"red":2,"green":1}, num_balls_drawn=5, num_experiments=2000)
print(probability)
