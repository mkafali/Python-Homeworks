9#Blackjack game. Using functions, lists, dictionaries, sets, break, continue etc. did not allowed. So, I create this program with really simple things.
from random import randint
user_score = 1000
round = 0
print("Welcome to the game")
ask = ""
while ask != "y" and ask != "n":
    ask = input("Do you want to play(y/n): ")
while ask == "y":
        dealers_score = 2000 - user_score
        take_card_condition = True #user's taking card condition
        dealers_process_condition = True # dealer's process condition
        if user_score == 0:
            print("You do not have enough money")
            ask = "n"
        elif dealers_score == 0:
            print("You get the game")
            ask = "n"
        else:     
            sacrifice = int(input("Enter sacrifice which is less than " + str(min(user_score,dealers_score)) +  " and bigger than 0: "))
            if sacrifice <= min(user_score,dealers_score) and 0 < sacrifice:
                users_hand = ""
                dealers_hand = ""
                users_ace = 0
                users_sum = 0
                dealers_ace = 0
                dealers_sum = 0
                round += 1
                print("#"*10 + "\nRound: " + str(round) + "\nYour Score: " + str(user_score) + "\nDealers score: " + str(dealers_score) + "\n" + "#"*10)
                dealers_mock_hand = "?-" #it will be shown to user until dealer takes new card
                for i in range(2): #give 2 card to each dealer and user
                    card = min(10,randint(1,13)) #user's card
                    users_hand += ("-"*i + str(card))
                    if card == 1:
                        users_ace += 1
                    users_sum += card
                    card = min(10,randint(1,13)) #dealer's card
                    dealers_hand += "-"*i +str(card)  
                    dealers_mock_hand += str(card)*(i//1)
                    if card == 1:
                        dealers_ace += 1
                    dealers_sum += card  
                if users_ace > 0:
                    print("Your hand: " + users_hand + " total(" + str(users_sum + 10) + ")"+ "\nDealer's hand: " + dealers_mock_hand)     
                else:
                    print("Your hand: " + users_hand + " total(" + str(users_sum) + ")"+ "\nDealer's hand: " + dealers_mock_hand)
                if sacrifice*2 <= min(user_score,dealers_score): #do you want to double it?
                        double_it = ""
                        while double_it != "y" and double_it != "n":
                            double_it = input("Do you want take 1 card and make sacrifice double(y/n): ")
                        if double_it == "y":
                            take_card_condition = False #do not execute the loop that provides taking 1 card, without doubling the bet
                            sacrifice *= 2
                            card = min(10,randint(1,13)) #user's card
                            users_hand += "-" + str(card)  
                            print("\nUsers new card : " + str(card))
                            if card == 1:
                                users_ace += 1
                            users_sum += card
                            if users_sum > 21:
                                if dealers_ace > 0:
                                    dealers_sum += 10
                                print("Your hand: " + users_hand + " total(" + str(users_sum) + ")" + "\nDealer's hand: " + dealers_hand +" total(" + str(dealers_sum) + ")"+"\nYou lost")
                                dealers_process_condition = False # do not execute the loop thats related to dealer's process
                                user_score -= sacrifice                
                else:
                    print("You cannot make your bet double")
                while take_card_condition: #take card without doubling the bet
                    take_card = ""
                    while take_card != "y" and take_card != "n":
                        take_card = input("Do you want to take card(y/n): ")
                    if take_card == "y":
                            card = min(10,randint(1,13)) #user's card
                            users_hand += "-" + str(card) 
                            print("\nUsers new card: " + str(card))
                            if card == 1:
                                users_ace += 1
                            users_sum += card
                            if users_sum > 21:
                                if dealers_ace > 0:
                                    dealers_sum += 10
                                print("Your hand: " + users_hand + " total(" + str(users_sum) + ")" + "\nDealer's hand: " + dealers_hand + 
                                      " total(" + str(dealers_sum) + ")"+ "\nYou lost")
                                take_card_condition = False # do not ask do you want to take card
                                dealers_process_condition = False # do not execute dealer's process
                                user_score -= sacrifice
                            else:
                                if users_ace > 0 and users_sum + 10 <= 21:
                                    print("Your hand: " + users_hand + " total(" + str(users_sum + 10) + ")" +  "\nDealer's hand: " + dealers_mock_hand)
                                else:
                                    print("Your hand: " + users_hand + " total(" + str(users_sum) + ")" +  "\nDealer's hand: " + dealers_mock_hand)
                    else:
                        take_card_condition = False # do not ask do you want to take card
                if users_ace > 0: #final version of user's cards sum
                        if users_sum + 10 <= 21:
                            users_sum += 10
                dealers_net_sum = dealers_sum #dealers_net_sum will be ace controlled version of dealers_sum
                while dealers_process_condition:
                    dealers_net_sum = dealers_sum # calculate user's cards sum
                    if dealers_ace > 0:
                        if dealers_sum + 10 <= 21:
                            dealers_net_sum = dealers_sum + 10
                    print("\nYour hand: " + users_hand + " total(" + str(users_sum) + ")" +  "\nDealer's hand: " + dealers_hand + " total(" + str(dealers_net_sum) + ")")
                    if dealers_sum > 21:
                        print("\nYou won")
                        user_score += sacrifice
                        dealers_process_condition = False #do not execute dealer's process 
                    elif dealers_net_sum < users_sum:
                        card = min(10,randint(1,13)) #delaer's card
                        dealers_hand += "-" + str(card)
                        if card == 1:
                            dealers_ace += 1
                        dealers_sum += card
                        print("\nDelaer's new card : " + str(card))
                    elif dealers_net_sum > users_sum:
                        print("\nYou lost")
                        user_score -= sacrifice
                        dealers_process_condition = False # do not execute dealer's process
                    else:
                        print("\nDraw")
                        dealers_process_condition = False # do not execute dealer's process
                ask = ""
                while ask != "y" and ask != "n":
                    ask = input("Do you want to play(y/n): ")
            else:
                print("Enter valid amount")
                        
                