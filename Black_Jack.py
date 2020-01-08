import random

class Deck:
    deck = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J','Q','K','A', '1' , '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J','Q','K', 'A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J','Q','K', 'A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J','Q','K', 'A']
      
    def hit(self):       
        #if self.play == 'h':
            x = random.choice(self.deck)
            #print(x)           
            pop_card_index = self.deck.index(x)
            self.deck.pop(pop_card_index)   
            hit_another = x           
        #if self.play == 's':
            #pass

            return hit_another
    #print(hit_another) 
    #print(deck)
    
class Players_hand:
    player_hand = []
    sum_player_previous = 0
    #hit_another='Q'
    #print(hit_another)
    
    def a_A (self):
        hit_another = 0
        Aa = input('choose A as 1 or 10?')
        if Aa == '1':
            hit_another = '1'
        if Aa == '10':
            hit_another = '10'
        return hit_another
                
    def sumPlayer(self,sum_player_previous, hit_another):    
        #if play == 'h':
            self.player_hand.append(hit_another)
            #print(player_hand)       
            switcher =  {
                '1': 1,
                '2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9,
                '10':10,
                'J': 10,
                'Q': 10,
                'K': 10,
                'A': 10,               
            }               
            sum_player_previous += switcher[hit_another] 
            return sum_player_previous
        
#call aleart
#print(sum_player)

class Computer_hand:
    computer_hand = []
    sum_computer_previous = 0
    #sum_player = 0
    #hit_another='Q'
    #print(hit_another)
    
    def a_A (self):
        list = ['1','10']
        aA = random.choice(list)
        return aA
        
    def sumComputer(self, sum_computer_previous, hit_another):
        self.computer_hand.append(hit_another)
        #print(player_hand)       
        switcher =  {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10':10,
            'J': 10,
            'Q': 10,
            'K': 10,
            'A': 10,
            }           
        sum_computer_previous += switcher[hit_another] 
        return sum_computer_previous

    #print(sum_player)
    
class Money:
    def originalAmount(self):
        Amount = int(input('Please set your original amount?(>=1000)'))
        return Amount
        
    def betAmount(self,player_bet_total):
    
        bet = int(input('Please bet?(10-50)'))
        player_bet_total += bet
        return player_bet_total
        
    def currentAmount(self,playerWin,Amount,player_bet_total):
        if playerWin == 4:
            Amount = Amount+player_bet_total
        if playerWin == 3:
            Amount = Amount-player_bet_total
        if playerWin == 0:
            pass
        return Amount
        
class Alert:
    def judge(self, play,  sum_player=0, sum_computer=0):
        if play == 's': 
            if sum_computer > 21 and sum_player > 21:
                print('Computer busts!')
                print('Player busts!')
                play = 0
                #return play 
            if sum_computer > 21 and sum_player < 21:
                print('Computer busts!')
                print('Player wins!')
                play = 4
            if sum_computer < 21 and sum_player > 21:
                print('player busts!')
                print('Computer wins!')
                play = 3            
            if sum_player < sum_computer < 21:
                print('Player losses!')
                play = 3
                #return play
            if 21 > sum_player > sum_computer:
                print ('Player wins!')
                play = 4
                #return play 
            elif sum_player == sum_computer < 21:
                print('Tie Game!')
                play = 0
            return play 

        elif play == 'h':
            if sum_computer > 21 and sum_player < 21:
                print('Computer busts!')
                play = 4
                #return play 
            if sum_computer < 21 and sum_player > 21:
                print('Player busts!')
                play = 3
            return play 

            
            
            


current_alert = Alert()
#deck1.play = 'h'
player1_money = Money()
player1_amount = player1_money.originalAmount()



while True:
    print('')
    print('')
    print('Welcome to Black Jack!')
    start=input('Ready to start? (y/n)').lower()
    
    sumP1 = 0
    sumC1 = 0
    player1_bet_total = 0
    play='h'
    
    deck1 = Deck(); #how to check whether the deck is new?
    print(deck1)
    
    player1_hand = Players_hand()  
    player1_hand.player_hand=[]
    print('player hand is: ')
    print(player1_hand.player_hand)
    

    computer1_hand = Computer_hand()
    computer1_hand.computer_hand=[]
    print('computer hand is: ')   
    print(computer1_hand.computer_hand)
    
    
    sumP1=0
    sumC1=0
    
    if start=='y':
        while play!=3 and play!=4 and play!=0:
            
            
            play = input('Hit or Stand?(h/s)') 
            if play == 'h':
                card_player1 = deck1.hit()
                print('player card is: '+card_player1)
                if card_player1=='A':
                    card_player1 = player1_hand.a_A()       
                sumP1 = player1_hand.sumPlayer(sumP1, card_player1)
                player1_bet_total = player1_money.betAmount(player1_bet_total)
                print('player1 total bet is: ')
                print(player1_bet_total)
                print('player1 sum is: ')
                print(sumP1)
                print('player hand is: ')
                print(player1_hand.player_hand)


                card_computer1 = deck1.hit()
                print('computer card is: '+card_computer1)
                if card_computer1=='A':
                    card_computer1 = computer1_hand.a_A()
                sumC1 = computer1_hand.sumComputer(sumC1, card_computer1)
                computer1_bet_total = player1_bet_total
                print('computer1 total bet is: ')
                print(computer1_bet_total)
                print('computer1 sum is: ')
                print(sumC1)
                print('computer hand is: ')
                print(computer1_hand.computer_hand)
               

                play = current_alert.judge(play, sumP1, sumC1)
                player1_amount = player1_money.currentAmount(play,player1_amount,player1_bet_total)
                print('player1 amount is: ')
                print(player1_amount)    


            if play == 's':
                card_computer1 = deck1.hit()
                if card_computer1=='A':
                    card_computer1 = computer1_hand.a_A()
                sumC1 = computer1_hand.sumComputer(sumC1, card_computer1)

                play = current_alert.judge(play, sumP1, sumC1)
                player1_amount = player1_money.currentAmount(play,player1_amount,computer1_bet_total)
                print('player1 amount is: ')
                print(player1_amount)
                
    if start =='n':
        print('Good luck! Bye for now!')
        break
    
    
    
    
