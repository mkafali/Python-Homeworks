#simply note: I did not use lists and it's methods, break and continue expressions as well. Also I did not do iteration on string by using for loop.
#Because we have learned loops and strings but if I am not wrong we did not discuss about are strings iterable data type or not.
#So, I did not do iteration on string by using for loop. Also, since using break and continue expressions are not allowed, I used another method which
#determined default condition of loops before the loop's initial line. At the end of the loop I changed the condition when I needed to. 
#In my program there are too many loops but the most confusing ones are main_condition and loops that reside in main_condition loop
#Basically main_condition method provides execute loops reside in main_condition loop as condition5 several times
#As you see, the loops reside in main_condition loop are be presented in with same indentation, because I used this loops as function that we have not learned yet.
#When I need one of them I change some of thems condition and do my process in related loop. Then a left from that loop
#For example first condition3 works and it starts game with deploying 2 cards each of us. Then it's condition had changed because I do not want to keeps it running without my permisson
#Since computer executes codes line by line, if I want to execute a loop that below of the loop that I am executing, I deactivate the loops which between them
#If I want to execute a loop that above that above of the loop that I am executing, I deactivate the loops which under the current loop and above the target loop. I am able to do that
#thanks to main_loop loop



from random import randint
user_score = 1000
dealers_score = 1000
round = 0

condition1 = True #game will continue or not
print("Welcome to the game! ")
while condition1:
    if user_score == 0:
        print("you dont have enough money")
        condition1 = False
    elif dealers_score == 0:
        print("you get the game")
        condition1 = False
    else:
        ask = input("Do you wanna play(y/n): ")
        if ask == "n":
            print("your score: " + str(user_score) + "\nGood Bye!")
            condition1 = False
        elif ask == "y":
            round += 1
            print("#"*10 + "\nRound " + str(round) + "\nCurrent User Point: " + str(user_score) + "\nCurrent Dealar Point: " + str(dealers_score) + "\n" + "#"*10)
            m = 0
            user_hand = ""
            user_hand_sum = 0 #since ace's value is not constant, first I add up cards except ace
            users_net_sum = 0 #in there I get absolute value of my hand. I mean it is user_hand_sum + ace's value
            user_ace_amount = 0 #how many ace I have
            dealers_hand = ""
            dealers_hand_mock = "?-" #at the begining of the game I have to show only 1 card of the dealers. This variable is just exists for print one of the dealer's card 
            dealers_hand_sum = 0 #same as the user_hand_sum
            dealers_net_sum = 0 #same as the user_net_sum
            dealers_ace_amount = 0 #same as the user_ace_amount
            condition_for_sacrifice = True #is sacrifice valid? 
            while condition_for_sacrifice:
                sacrifice = int(input("enter your sacrifice which is less than " + str(min(user_score,dealers_score)) + ": "))
                if sacrifice <= min(user_score,dealers_score):
                    condition_for_sacrifice = False
                    dealer_take_card_cond = False#this is the condition of the loop that provides take card for dealer
                    control_num = 1 #it is control value which controls that loop starts the loop2, condition2 or condition5 or condition 5
                    main_cond = True#this is my main loop's condition after answered 
                    condition2 = False#this is the condition of the loop that provides me take a card
                    condition3 = True#this is the condition of the loop that starts the game by deploying 2 cards each of us. it's value is True so that loop will executes defaultly
                    condition4 = True#this is the condition of the loop that asks me am I gonna make the sacrifice double. it's value is True so that loop will executes defaultly
                    condition5 = False#this is the condition of the loop that asks me am I gonna take card
                    condition6 = False#this is the condition of the loop that related with dealer's process
                    while main_cond:
                        while condition2:
                            card = min(10,randint(1,13))
                            if card != 1:
                                user_hand_sum += card                
                            else:
                                user_ace_amount += 1
                            user_hand += ("-" + str(card))
                            print("your hand = " + user_hand + "\ndelaer hand: " + dealers_hand_mock)
                            if user_ace_amount != 0:
                                temp_sum = (user_ace_amount-1)*1 + user_hand_sum
                                if temp_sum + 11 > 21:
                                    users_net_sum = temp_sum + 1
                                else:
                                    users_net_sum = temp_sum + 11
                            else:
                                users_net_sum = user_hand_sum
                            if users_net_sum > 21:
                                print("your hand = " + user_hand + "\ndelaer hand: " + dealers_hand)
                                print("you lost!")
                                main_cond = False
                                
                                condition5 = False
                                condition6 = False
                                user_score -= sacrifice
                                dealers_score += sacrifice
                            else:
                                if control_num == 5:
                                    condition5 = True
                                elif control_num == 4:   
                                    condition6 = True
                            condition2 = False



                        while condition3:
                            for i in range(2):
                                card = min(10,randint(1,13))
                                if card != 1:
                                    user_hand_sum += card                
                                else:
                                    user_ace_amount += 1
                                user_hand += ("-"*(i%2) + str(card))

                            for i in range(2):
                                card = min(10,randint(1,13))
                                if card != 1:
                                    dealers_hand_sum += card                
                                else:
                                    dealers_ace_amount += 1
                                dealers_hand += ("-"*(i%2) + str(card))
                                dealers_hand_mock += (str(card)*i)

                            if user_ace_amount != 0:
                                temp_sum = (user_ace_amount-1)*1 + user_hand_sum
                                if temp_sum + 11 > 21:
                                    users_net_sum = temp_sum + 1
                                else:
                                    users_net_sum = temp_sum + 11
                            else:
                                users_net_sum = user_hand_sum

                            if dealers_ace_amount != 0:
                                temp_sum = (dealers_ace_amount-1)*1 + dealers_hand_sum
                                if temp_sum + 11 > 21:
                                    dealers_net_sum = temp_sum + 1
                                else:
                                    dealers_net_sum = temp_sum + 11
                            else:
                                dealers_net_sum = dealers_hand_sum

                            if users_net_sum == 21 or dealers_net_sum == 21:
                                condition4 = False
                                main_cond = False
                                if dealers_net_sum == 21 and users_net_sum == 21:
                                    print("your hand = " + user_hand + "\ndelaer hand: " + dealers_hand + "\ndraw")
                                elif users_net_sum == 21 and dealers_net_sum != 21:
                                    print("your hand = " + user_hand + "\ndelaer hand: " + dealers_hand + "\nyou won")
                                    user_score += sacrifice
                                    dealers_score -= sacrifice
                                else:
                                    print("your hand = " + user_hand + "\ndelaer hand: " + dealers_hand + "\nyou lost")
                                    user_score -= sacrifice
                                    dealers_score += sacrifice

                                    
                            else:
                                print("your hand = " + user_hand + "\ndelaer hand: " + dealers_hand_mock)
                            condition3 = False
                        
                        while condition4:
                            if sacrifice*2 > min(user_score,dealers_score):
                                condition4 = False
                                condition5 = True
                            else:
                                double_it = input("Do you want to to take 1 card and make your sacrifice double: ")
                                if double_it == "n":
                            
                                    condition4 = False
                                    condition5 = True
                                elif double_it == "y":
                                    condition4 = False
                                    condition2 = True
                                    control_num = 4
                                    sacrifice *= 2
                                else:
                                    print("Enter valid letter")

                        while condition5:
                            take_card = input("Do you want to take card? ")
                            if take_card == "y":
                                condition2 = True
                                condition5 = False
                                control_num = 5
                            elif take_card == "n":
                        
                                condition5 = False
                                condition6 = True

                            else:
                                print("Enter valid letter")

                        while dealer_take_card_cond:
                            card = min(10,randint(1,13))
                            if card != 1:
                                dealers_hand_sum += card                
                            else:
                                dealers_ace_amount += 1
                            dealers_hand += ("-" + str(card))
                            print("your hand = " + user_hand + "\ndelaer hand: " + dealers_hand)
                            if dealers_ace_amount != 0:
                                temp_sum = (dealers_ace_amount-1)*1 + dealers_hand_sum
                                if temp_sum + 11 > 21:
                                    dealers_net_sum = temp_sum + 1
                                else:
                                    dealers_net_sum = temp_sum + 11
                            else:
                                dealers_net_sum = dealers_hand_sum
                            if dealers_net_sum > users_net_sum and dealers_net_sum <= 21:
                                print("you lost")
                                condition6 = False
                                main_cond = False
                                user_score -= sacrifice
                                dealers_score += sacrifice
                                
                            elif dealers_net_sum > 21:
                                print("you won")
                                condition6 = False
                                main_cond = False
                                user_score += sacrifice
                                dealers_score -= sacrifice
                            
                            else:
                                condition6 = True


                            dealer_take_card_cond = False
                            

                        while condition6:
                            if m == 0:
                                print("your hand = " + user_hand + "\ndealer's hand: " + dealers_hand)
                                m = 1
                                
                            
                            if dealers_net_sum < users_net_sum:
                                dealer_take_card_cond = True

                            elif dealers_net_sum == users_net_sum:
                                
                                print("draw")
                                condition6 = False
                                main_cond = False


                            else:
                                
                                print("you lost")

                                main_cond = False
                                user_score -= sacrifice
                                dealers_score += sacrifice

                            condition6 = False
                            

                else:
                    print("Enter valid amount")#invalid sacrifice amount


        else:
            print("Enter valid letter")#wrong attempt for the question do you wanna play









            