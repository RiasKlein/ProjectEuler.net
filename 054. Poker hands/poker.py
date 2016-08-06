#################################################################################
#
#	poker.py
#
#	Project Euler Problem 54
#	Poker hands
#
#	In the card game poker, a hand consists of five cards and are ranked, from 
#	lowest to highest, in the following way:
#		High Card
#		One Pair
#		Two Pair
#		Three of a Kind
#		Straight
#		Flush
#		Full House
#		Four of a Kind
#		Straight Flush
#		Royal Flush
#
#	The cards are valued in the order:
#		2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace
#
#	If two players have the same ranked hands then the rank made up of the 
#	highest value wins; for example, a pair of eights beats a pair of fives 
#	(see example 1 below). But if two ranks tie, for example, both players have 
#	a pair of queens, then highest cards in each hand are compared 
#	(see example 4 below); if the highest cards tie then the next highest cards 
#	are compared, and so on.
#
#	Consider the following 5 hands dealt to two players:
#	Hand 	Player 1 			Player 2			Winner
#	1 		5H 5C 6S 7S KD 		2C 3S 8S 8D TD 		Player 2
#	2 		5D 8C 9S JS AC 		2C 5C 7D 8S QH 		Player 1
#	3 		2D 9C AS AH AC 		3D 6D 7D TD QD 		Player 2
#	4 		4D 6S 9H QH QC 		3D 6D 7H QD QS 		Player 1
#	5 		2H 2D 4C 4D 4S 		3C 3D 3S 9S 9D 		Player 1
#
#	The attached file contains one-thousand random hands dealt to two players.
#	Each line of the file contains 10 cards, the first five are player 1's
#	and the second 5 are player 2's. 
#
#	How many hands does Player 1 win?
#
#	Program by Shunman Tse
#	
#################################################################################

filename = 'p054_example.txt'
#filename = 'p054_poker.txt'

def read_hands( filename ):
	hands = []

	rfile = open (filename, 'r')

	while True:
		line = rfile.readline()
		if not line: 
			rfile.close()
			return hands

		if line != '\n':
			line = line.strip('\n')
			line = line.split (' ')
			hands.append(line)

def main():
	# Read in our sets of 10 cards to be evaluated 
	hands = read_hands (filename)
	
	














main()