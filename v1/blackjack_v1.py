import random

#deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#number_of_decks = 4

# define function to define the cards

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
number_of_decks = 4
cards = deck * number_of_decks

# define the cards

#cards = cards_define_function()

##print(cards)

# define function remove card
def remove_card(string):
    return cards.remove(string)

#define card for drawing from deck
def draw_card():
    extra_card = random.choice(cards)
    remove_card(extra_card)
    return extra_card





def one_hand():
	#print '++++++++++++'
	dealer=[]
	player=[]

	player.append(draw_card())
	dealer.append(draw_card())    
	    

	player.append(draw_card())
	dealer.append(draw_card())

	player_sum=sum(player)
	dealer_face_up=dealer[1]
	dealer_sum=sum(dealer)
	#print(player_sum)
	#print(dealer_face_up)


	if(dealer_face_up >=2 and dealer_face_up <=6):
		if(dealer_face_up== 2 or dealer_face_up== 3):
			while(player_sum <=13):
					player.append(draw_card())
					player_sum=sum(player)
			#print player_sum
			#print(player)
			#print '====='
		
			while(dealer_sum<17):
				dealer.append(draw_card()) 
				dealer_sum=sum(dealer)
			#print dealer_sum
			#print dealer
			if(player_sum >21):
				#print 'Player Bust. Dealer wins!'
				return(0)
			if(dealer_sum>21):
				#print 'Dealer Bust. Player Wins!'
				return(2)
			else:
				if(player_sum > dealer_sum):
					#print 'Player has more than dealer. Player wins!'
					return(2)
				elif (player_sum < dealer_sum):
					#print 'Dealer has more than player. Dealer wins!'
					return(0)
				elif (player_sum== dealer_sum):
					#print 'Push!'
					return(1)

		else:
			while(player_sum <=12):
					player.append(draw_card())
					player_sum=sum(player)
			#print player_sum
			#print(player)
			#print '====='
		
			while(dealer_sum<17):
				dealer.append(draw_card()) 
				dealer_sum=sum(dealer)
			#print dealer_sum
			#print dealer
			if(player_sum >21):
				#print 'Player Bust. Dealer wins!'
				return(0)
			if(dealer_sum>21):
				#print 'Dealer Bust. Player Wins!'
				return(2)
			else:
				if(player_sum > dealer_sum):
					#print 'Player has more than dealer. Player wins!'
					return(2)
				elif (player_sum < dealer_sum):
					#print 'Dealer has more than player. Dealer wins!'
					return(0)
				elif (player_sum== dealer_sum):
					#print 'Push!'
					return(1)
	elif(dealer_face_up >=7):
		while(player_sum<17):
			player.append(draw_card()) 
			player_sum=sum(player)
		while(dealer_sum<17):
			dealer.append(draw_card()) 
			dealer_sum=sum(dealer)

		#print player_sum
		#print(player)
		#print '====='
		#print dealer_sum
		#print dealer
		if(player_sum >21):
			#print 'Player Bust. Dealer wins!'
			return(0)
		if(dealer_sum>21):
			#print 'Dealer Bust. Player Wins!'
			return(2)
		else:
			if(player_sum > dealer_sum):
				#print 'Player has more than dealer. Player wins!'
				return(2)
			elif (player_sum < dealer_sum):
				#print 'Dealer has more than player. Dealer wins!'
				return(0)
			elif (player_sum == dealer_sum):
				#print 'Push!'
				return(1)

	

w=open('money.txt','w')
for j in range(1,100000):
	wins=0
	losses=0
	draws=0
	money=1000
        deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        number_of_decks = 4
        cards = deck * number_of_decks
	for i in range(1,50):
            if(len(cards) < 26):
                deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
		number_of_decks = 4
		cards = deck * number_of_decks
            outcome=one_hand()
            if(outcome ==2):
                wins+=1
                money=money+10
            elif(outcome==1):
                draws+=1
            elif(outcome==0):
                losses+=1
                money-=10




	#print wins
	#print losses
	#print draws
	#print wins+losses+draws
	print(money)
	w.write(str(money))
	w.write(',\n')

w.close()
