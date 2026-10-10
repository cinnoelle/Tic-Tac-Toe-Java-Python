# Lab 10 - Tic Tac Toe
# Name: Sara
# Making a tic tac toe game for 2 people to play

def build_board():
    #create an empty list
    num_list = []
    #for i in range 9 (0-8)
    for i in range(9):
        #append i+1 so that it goes from 1-9 instead
        num_list.append(i+1)

    #print(num_list)
    #return the list of nums
    return num_list


def display_board(board_list):
    
    #create the board w/ every number, and print dashed lines between
    print(board_list[0], "|", board_list[1], "|", board_list[2])
    print("----------")
    print(board_list[3], "|", board_list[4], "|", board_list[5])
    print("----------")
    print(board_list[6], "|", board_list[7], "|", board_list[8])


#board = list of board, spot = where user is placing tile
def is_legal(board, spot):
    #print("board", board)
    #print("spot", spot)

    #if spot is out of range, return false
    if spot > 9 or spot < 1:
        print("Out of range. Pick a number 1 - 9.")
        return False
    
    #if spot is already covered by x or o
    if board[spot-1] == "x" or board[spot-1] == "o":
        print("Already covered, pick again.")
        return False

    #else in range, return true
    return True
        

def fill_spot(board, spot, char): 

    
    #print("Board:", board)
    #print("Spot:",spot)

    #whatever the spot is, -1 because it will always be one back
    board[spot-1] = char
    #return as true
    return True



    
    

def is_game_won(board):

    #create all possible win combos based on placement (starts at 0)
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            #diagonals
            (0,4,8),(2,4,6)]
    
    for one, two, three in wins:
        #all three spots need to be one of the orders
        if board[one] == board[two] == board[three]:
            return True
    #is only false when no combos are true (not in else statement)
    return False
    

def is_game_over(board,num_plays):
    #game is won when someone wins or all spots r full
    #if game is won by someone
    if is_game_won(board):
        return True
    
    #if all squares are full
    if num_plays == 9:
        return True

    #else return false
    return False



def play_game():
    #method to play, execute all functions, add play again feature

    play_again = "Y"


    while play_again.upper() == "Y":
        #make new boards each game
        #set board to build board
        board = build_board()
        #counter for number of plays
        num_plays = 0
        #set winners to none for checker
        winner = None

        #calling display board
        display_board(board)

        

        while not is_game_over(board, num_plays):
            

            #Player 1 (X) goes first
            spot = int(input("Player 1, where would you like to put X?: "))

            #if the spot is able to be used, it is used
            if is_legal(board,spot):
                fill_spot(board, spot, "x")
                #add up the num of plays, for when it gets to the max amt
                num_plays = num_plays + 1
                #move this from main to here
                display_board(board)

                #if x wins
                if is_game_won(board):
                    #winner is x
                    winner = "Player 1 (X)"
                    #leave loop if over 9 plays
                    break

            #if games over, don't ask o for input again
            if is_game_over(board, num_plays):
                break


            #Player 2 (O) goes first
            spot = int(input("Player 2, where would you like to put O?: "))

            #if the spot is able to be used, it is used
            if is_legal(board,spot):
                #if is legal: do this
                fill_spot(board, spot, "o")
                #add up the num of plays, for when it gets to the max amt
                num_plays = num_plays + 1
                #move this from main to here
                display_board(board)

                #if o wins
                if is_game_won(board):
                    #winner is O
                    winner = "Player 2 (O)"
                    #leave loop if over 9 plays
                    break

        #if there is a winner print which player won
        #if winner exists
        if winner:
            print (f"{winner} wins!")
        #print else for if there's a tie
        else:
            print("It's a tie!")

        #input for user to play again
        play_again = input("To play again, type 'Y': ")

        
        






def main():
    ## MOVED TO PLAY_GAME
    # list = build_board()
    # display_board(list) 
    # user_input = play_game()
    

    #call play_game
    play_game()

    


main()
