import numpy as np
#basic bag contents - [1,1,1,1,2,3,3,0,0,00]
def bag_war(reps = 5000):

    small_bag_wins = 0
    big_bag_wins = 0
    ties = 0

    for i in range(reps):    
    #Small Bag   
        
        small_bag_score = 0
        small_bag_supporters = 5
        small_bag_madness = 0
        original_small_bag_values = [2,3,3,0,0,99,0]
        small_bag_values = original_small_bag_values
        small_bag_audit = []
        for i in range(small_bag_supporters-1):
            
            small_bag_pull = np.random.choice(small_bag_values)
        
            if small_bag_pull == 0:
            
                small_bag_supporters -= 1
                small_bag_madness += 1
            elif small_bag_pull == 99:
                small_bag_pull == 0
                small_bag_supporters -= 2
                small_bag_madness +=1
            else:
                small_bag_score += small_bag_pull
            if small_bag_madness == 4:
                small_bag_values == original_small_bag_values
            if small_bag_supporters <= 0:
                small_bag_pull == -100    

            small_bag_values.remove(small_bag_pull)
            small_bag_audit.append(small_bag_pull) 
        print("Small Bag Score is " + str(small_bag_score) + " From Tokens: " + str(small_bag_audit) + " Final Madness " + str(small_bag_madness) + " Supporters: " + str(small_bag_supporters))

    #Big Bag
        
        big_bag_score = 0
        big_bag_supporters = 5
        big_bag_madness = 0
        big_bag_audit = []
        original_big_bag_values = [1,1,1,1,2,3,3,0,0,99,0]
        big_bag_values = original_big_bag_values

        for i in range(big_bag_supporters-1):
            
            big_bag_pull = np.random.choice(big_bag_values)

            if big_bag_pull == 0:
                
                big_bag_supporters -= 1
                big_bag_madness += 1
            elif big_bag_pull == 99:
                big_bag_pull == 0
                big_bag_supporters -= 2
                big_bag_madness +=1
            else:
                big_bag_score += big_bag_pull
            if big_bag_madness == 4:
                big_bag_values == original_big_bag_values
            if big_bag_supporters <= 0:
                big_bag_pull == -100    
            big_bag_values.remove(big_bag_pull)  
            big_bag_audit.append(big_bag_pull)
        print("Big Bag Score is " + str(big_bag_score) + " From Tokens: " + str(big_bag_audit) + " Final Madness " + str(big_bag_madness) + " Supporters: " + str(big_bag_supporters))

        if small_bag_score > big_bag_score:
            small_bag_wins += 1 
    
        if big_bag_score > small_bag_score:
            big_bag_wins += 1

        if big_bag_score == small_bag_score:
            ties +=1
    print("Small Bag Wins: " + str(small_bag_wins))
    print("Big Bag Wins: " + str(big_bag_wins))
    print("Ties: " + str(ties))
bag_war()

            

