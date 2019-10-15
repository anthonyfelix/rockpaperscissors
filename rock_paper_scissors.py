import os, time, random



class Game:
    num_players:None
    state:None
    loan_amount = 0
    loan_games = 0
    loan = False

class Player:
    name = None
    choice = None
    wallet = 10000
    bet    = None

def check_choice(this_player):
    try:
        choice = this_player.choice[0]
        if choice != 'R' and choice != 'P' and choice != 'S':
            redo_choice(this_player)
    except:
        redo_choice(this_player)

def redo_choice(player):  
    print(player.name + ', you must enter Rock, Paper or Scissors')
    player.choice = input('Please remake your choice:')
    player.choice = player.choice.upper()
    check_choice(player)

def next_game():
    try:
        if player_1.wallet == 0 and game.state == "Human vs Machine":
            offer_loan()
        if game.loan and game.loan_games > 4 and game.loan_games % 5 == 0:
            os.system('cls||clear')
            print('So about that loan...')
            if game.loan_amount > 0 and game.loan_games > 0:
                time.sleep(1)
                game.loan_amount = int(game.loan_amount * 1.09)
                print('With 10% interest, you owe $' + str(game.loan_amount))
                response = input('Are you ready to pay up? (Y/N) : ')
                pay_loan_low(response)
        player_1.choice = input(player_1.name + ", what is your choice: ")
        player_1.choice_word = player_1.choice
        os.system('cls||clear')
        player_1.bet = input('How much would you like to wager? (Current Bankroll:' + str(player_1.wallet) +'):')
        validate_user_bet(player_1)
        if game.state == 'Human vs Human':
            player_2.choice = input(player_2.name + ", what is your choice: ")
            player_2.choice = player_2.choice.upper()
        else:
            player_2.choice = random.choice(rps)
        player_1.choice = player_1.choice.upper()
        player_1.choice = player_1.choice[0]
        finish_game()
    except:
        print("Sorry, something went wrong, try again")
        next_game()

def pay_loan_low(response):
    response = response.upper()
    if response == 'Y' or response == 'YES':
        payment = input("Great, how much do you want to pay? (You have $" + str(player_1.wallet) + " and you owe $"+ str(game.loan_amount) +")" )
        validate_payment(payment)
    elif response == 'N' or response == 'No':
        print('I get it, times are tough...')
        time.sleep(1)
        print('But I am giving you a late fee of $1000')
        game.loan_amount += 1000
    else:
        response = input("I don't understand what you are trying to say but I am going to take it as disrespect, can you pay today? (Y/N) :")
        pay_loan_low(response)


def validate_payment(payment):
    try:
        payment = int(payment)
        if payment < player_1.wallet and payment < game.loan_amount:
            player_1.wallet -= payment
            game.loan_amount -= payment
            print('Okay, you paid $' + str(payment) + " and you owe $" +  str(game.loan_amount))
            print("I'll be back, but let's play again!")
        elif payment < player_1.wallet and payment == game.loan_amount:
            player_1.wallet -= game.loan_amount
            game.loan_amount = 0
            game.loan = False
            game.loan_games = 0
        elif payment > player_1.wallet:
            payment = input("Sorry, I don't do IOU's, how much CASH can you give me? : ")
            validate_payment(payment)
        elif payment > game.loan_amount and player_1.wallet >= game.loan_amount:
            player_1.wallet -= game.loan_amount
            game.loan_amount = 0
            game.loan = False
            game.loan_games = 0
    except:
        payment = input('Make sure you are using just numbers, try again:')
        validate_payment(payment)

        
def finish_game():
    check_choice(player_1)
    check_choice(player_2)
    for word in rps:
        print(word)
        time.sleep(.6)
    print('Shoot!')
    print('And the winner is...')
    time.sleep(1.4)
    print("*******************************************")
    print('')
    find_winner(player_1,player_2)
    print('')
    print("*******************************************")
    print(player_1.name + " chose " + display_choice(player_1.choice))
    print(player_2.name + " chose " + display_choice(player_2.choice))
    if game.state == "Human vs Machine":
        print("Current Bankroll: " + str(player_1.wallet))
    next_game()

def find_winner(plr1, plr2):
    plr1_choice = player_1.choice[0]
    plr2_choice = player_2.choice[0]
    if plr1_choice == plr2_choice:
        print("Nobody, It's a draw!")
    elif plr1_choice == "R":
        if plr2_choice == "S":
            print(plr1.name)
            if game.state == "Human vs Machine":
                payout_bets(player_1.wallet,player_1.bet, "Human")
                if game.loan:
                    game.loan_games += 1
        else:
            print(plr2.name)
            if game.state == "Human vs Machine":
                payout_bets(player_1.wallet,player_1.bet, "Computer")
                if game.loan:
                    game.loan_games += 1
    elif plr1_choice == "S":
        if plr2_choice == "R":
            print(plr2.name)
            if game.state == "Human vs Machine":
                payout_bets(player_1.wallet, player_1.bet, "Computer")
                if game.loan:
                    game.loan_games += 1
        else:
            print(plr1.name)
            if game.state == "Human vs Machine":
                payout_bets(player_1.wallet,player_1.bet, "Human")
                if game.loan:
                    game.loan_games += 1
    elif plr1_choice == "P":
        if plr2_choice == "R":
            print(plr1.name)
            if game.state == "Human vs Machine":
                payout_bets(player_1.wallet,player_1.bet, "Human")
                if game.loan:
                    game.loan_games += 1
        else:
            print(plr2.name)
            if game.state == "Human vs Machine":
                payout_bets(player_1.wallet,player_1.bet, "Computer")
                if game.loan:
                    game.loan_games += 1

def payout_bets(current_bankroll, bet, winner):
    if winner == 'Human':
        player_1.wallet = current_bankroll + int(bet)
    else:
        player_1.wallet = current_bankroll - int(bet)

def create_players():
    try:
        player_1.name = input('Player 1, what is your name: ')
        player_1.choice = input(player_1.name + ", what is your choice (R/P/S) : ")
        player_1.choice[0]
        player_1.choice_word = player_1.choice

        os.system('cls||clear')

        if int(game.num_players) > 1:
            game.state = 'Human vs Human'
            player_2.name = input('Player 2, what is your name: ')
            player_2.choice = input(player_2.name + ", what is your choice: ")
            player_2.choice_word = player_2.choice
            player_2.choice = player_2.choice.upper()
        else:
            game.state = 'Human vs Machine'
            player_1.bet = input('How much would you like to wager? (Current Bankroll:' + str(player_1.wallet) +'):')
            validate_user_bet(player_1)
            player_2.name= "The computer"
            player_2.choice = random.choice(rps)
            print(player_1.name + ", you are playing the computer, good luck!")
        player_1.choice = player_1.choice.upper()
        player_1.choice = player_1.choice[0]
    except:
        print("Sorry something went wrong, let's try again")
        create_players()

def validate_user_count(count):
    if count.isdigit() and int(count) <= 2 and int(count) > 0:
        create_players()
    else: 
        game.num_players = input('How many players are there? (make sure it is either 1 or 2)')
        validate_user_count(game.num_players)

def validate_user_bet(player):
    try: 
        int(player.bet)
        if int(player.bet) > player.wallet:
            player.bet = input("That bet was too high, bet again (you have $"+str(player_1.wallet) + ") :")
            validate_user_bet(player)
    except:
        player.bet = input('Please make sure your bet is a number, try again: ')
        validate_user_bet(player)


def offer_loan():
    response = input('You are out of money, would you like to borrow $5000? (Y/N)')
    response = response.upper()
    if response == 'Y':
        game.loan = True
        game.loan_amount += 5000
        player_1.wallet = 5000
        os.system('cls||clear')
        print("Okay, but I am gonna need that back...")
    

def display_choice(choice):
    if choice[0] == 'R':
        return "ROCK"
    elif choice[0] == 'S':
        return "SCISSORS"
    elif choice[0] == "P":
        return "PAPER"
 
rps = ["ROCK", "PAPER", "SCISSORS"]
pc_rps = ["R", "P", "S"]

player_1 = Player()
player_2 = Player()
game = Game()

game.num_players = input('How many players are there?')
validate_user_count(game.num_players)
finish_game()

