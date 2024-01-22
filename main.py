import sys
import random

class rps_game():

    def validate(self, choice, choices):
        if choice in choices:
            return choice
        else:
            print("Invalid choice - please enter 'rock', 'paper', or 'scissors'")
            choice = input().lower()
            return self.validate(choice)

    
    def main(self):

        ai = False
        simulate = False

        if len(sys.argv) > 1:
            for arg in sys.argv[1:]:
                if arg == '-AI':
                    ai = True
                elif arg == '-AIAUTO':
                    simulate = True

        choices = ['rock', 'paper', 'scissors']
        matchups = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }

        print("Let's play rock, paper, scissors\n Player 1's move?")

        if not simulate:
            choice = input().lower()
            choice1 = self.validate(choice, choices)
        
            print("Player 2's move?")
            if not ai:
                choice = input().lower()
                choice2 = self.validate(choice, choices)
            else:
                choice2 = choices[random.randint(0,2)]
                print(choice2)
        else:   #simulate game
            choice1 = choices[random.randint(0,2)]
            print(choice1)
            print("Player 2's move?")
            choice2 = choices[random.randint(0,2)]
            print(choice2)

        if choice1 == choice2:
            print("Player 1 and Player 2 both played " + choice1)
        elif choice2 in matchups[choice1]:
            print("Player 1's " + choice1 + " beats Player 2's " + choice2)
        else:
            print("Player 2's " + choice2 + " beats Player 1's " + choice1)


game = rps_game()
game.main()