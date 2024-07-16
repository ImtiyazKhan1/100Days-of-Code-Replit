#From 100 Days of Code - The Complete Python Pro Bootcamp for 2021
#The rules state that rock smashes scissors, scissors cuts paper, and paper covers rock. So, rock wins over scissors, scissors win over paper and paper wins over rock. With the understanding of the rules, we can proceed to create the game.

from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E")
print()
print("Select your move (R for Rock, P for Paper or S for Scissors")

player1 = input(str("Player 1 > "))
player2 = input(str("Player 2 > "))
if player1 == "r" and player2 == "r":
  print("You both picked Rock, draw! 🪢")
elif player1 == "p" and player2 == "r":
  print("Player 1's Paper covers Player 2's, Player 1 Wins 📄")
elif player1 == "r" and player2 == "p":
  print("Player 2's Paper covers Player 1's, Player 2 Wins 📄")
elif player1 == "s" and player2 == "p":
  print("Player 1's Scissors covers Player 1's, Player 1 Wins ✂️")
elif player1 == "p" and player2 == "s":
  print("Player 2's Scissors covers Player 1's, Player 2 Wins ✂️")
elif player1 == "r" and player2 == "s":
  print("Player 1's Rock covers Player 1's, Player 1 Wins 🪨")
elif player1 == "s" and player2 == "r":
  print("Player 2's Rock covers Player 1's, Player 2 Wins 🪨")
else: 
  print("Invalid Options, Try Again")