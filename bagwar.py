import numpy as np

def bag_war(reps = 200):

    small_bag_wins = 0
    big_bag_wins = 0
    ties = 0

    for i in range(reps):    
    #Small Bag   
        
        small_bag_score = 0
        small_bag_supporters = 4
        small_bag_madness = 0
        original_small_bag_values = [3,3,3,00,0,0]
        small_bag_values = original_small_bag_values
        small_bag_audit = []
        while small_bag_supporters > 1 and small_bag_madness < 4:
            
            small_bag_pull = np.random.choice(small_bag_values)
        
            if small_bag_pull == 0:
            
                small_bag_supporters -= 1
                small_bag_madness += 1
            
            elif small_bag_pull == 00:
            
                small_bag_supporters -= 2
                small_bag_madness +=1
            elif small_bag_madness == 4:
                print("Small Bag Bust!")
            small_bag_score += small_bag_pull
            small_bag_values.remove(small_bag_pull)
            small_bag_audit.append(small_bag_pull) 
        print("Small Bag Score is " + str(small_bag_score) + " From Tokens: " + str(small_bag_audit) + " Final Madness " + str(small_bag_madness) + " Supporters: " + str(small_bag_supporters))

    #Big Bag
        
        big_bag_score = 0
        big_bag_supporters = 4
        big_bag_madness = 0
        big_bag_audit = []
        original_big_bag_values = [1,1,1,3,3,3,0,00,0]
        big_bag_values = original_big_bag_values

        while big_bag_supporters > 1 and big_bag_madness < 4:
            
            big_bag_pull = np.random.choice(big_bag_values)

            if big_bag_pull == 0:
                
                big_bag_supporters -= 1
                big_bag_madness += 1
            
            elif big_bag_pull == 00:
            
                big_bag_supporters -= 2
                big_bag_madness +=1
            elif big_bag_madness == 4:
                print("Big Bag Bust!")
            big_bag_score += big_bag_pull
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

            

