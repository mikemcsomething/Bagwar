import numpy as np
#basic bag contents - [1,1,1,1,2,3,3,0,0,00]

small_bag = [2,3,3,0,0,99,0]
big_bag = [1,1,1,1,2,3,3,0,0,99,0]


def bag_pull(selected_bag):
    og_bag = selected_bag
    bag_audit = []
    if len(selected_bag) == 0:
        selected_bag == og_bag
    else:
        current_chip = np.random.choice(selected_bag)
        selected_bag.remove(current_chip)
        bag_audit.append(current_chip)
    
    print("Current Chip is " + str(current_chip))
bag_pull(big_bag)






def bag_war(reps = 10):

    small_bag_wins = 0
    big_bag_wins = 0
    ties = 0

    for i in range(reps):    
    #Small Bag   
        
        small_bag_score = 0
        small_bag_supporters = 5
        small_bag_madness = 0
        small_bag_audit = []
        original_small_bag_values = [2,3,3,0,0,99,0]

        small_bag_values = original_small_bag_values

        while small_bag_supporters > 1 and small_bag_score < 25:
            if len(small_bag_values) == 0:
                small_bag_values == original_small_bag_values
            else:
                small_bag_pull = np.random.choice(small_bag_values)
        
            if small_bag_pull == 0:
            
                small_bag_supporters -= 1
                small_bag_madness += 1

            elif small_bag_pull == 99:
                small_bag_supporters -= 2
                small_bag_madness +=1

            else:
                if small_bag_supporters == 0:
                    small_bag_score -=100
                    break
                elif small_bag_madness == 4:
                    small_bag_values == original_small_bag_values
                    small_bag_madness -= 4
                else:
                    small_bag_score += small_bag_pull
                  

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

        while big_bag_supporters > 1 and big_bag_score < 25:
            if len(big_bag_values) == 0:
                big_bag_values == original_big_bag_values
            else:
                big_bag_pull = np.random.choice(big_bag_values)

            if big_bag_pull == 0:
                
                big_bag_supporters -= 1
                big_bag_madness += 1

            elif big_bag_pull == 99:
                big_bag_supporters -= 2
                big_bag_madness += 1
                
            else:
                big_bag_score += big_bag_pull

            if big_bag_madness == 4:
                big_bag_values == original_big_bag_values
                big_bag_madness -= 4  
            if big_bag_supporters <= 0:
                big_bag_score == -100

            big_bag_values.remove(big_bag_pull)  
            big_bag_audit.append(big_bag_pull)
        print("Big Bag Score is " + str(big_bag_score) + " From Tokens: " + str(big_bag_audit) + " Final Madness " + str(big_bag_madness) + " Supporters: " + str(big_bag_supporters))

        if small_bag_score and big_bag_score <= 0:
            ties +=1
            print("Tie")
        elif small_bag_score > big_bag_score :
            small_bag_wins += 1 
            print("Small Bag Wins")
        elif big_bag_score > small_bag_score:
            big_bag_wins += 1
            print("Big Bag Wins")
        elif big_bag_score == small_bag_score:
            ties +=1
            print("Tie")

    print("Small Bag Wins: " + str(small_bag_wins))
    print("Big Bag Wins: " + str(big_bag_wins))
    print("Ties: " + str(ties))
bag_war()



            
