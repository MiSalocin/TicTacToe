import os

alone = False
turn = 0
p1, p2 = 'X', 'O'
the_board: list[str] = [' ' for x in range(9)]
p1w, p2w, ties = set(), set(), set()
p1w_long, p2w_long, ties_long = [], [], []
corners, middles = [0, 2, 6, 8], [1, 3, 5, 7]


def game_over():
    clear_console()
    p1w.clear()
    p2w.clear()
    ties.clear()
    p1w_long.clear()
    p2w_long.clear()
    ties_long.clear()
    pos_moves(the_board, "X" if turn == 0 else "O")
    print_board()
    global alone
    if alone:
        p1_won = "YOU WON"
        p2_won = "YOU LOSE"
    else:
        p1_won = f"PLAYER '{p1}' WON"
        p2_won = f"PLAYER '{p2}' WON"

    if winner(the_board, p1):
        print(p1_won)
        return False
    elif winner(the_board, p2):
        print(p2_won)
        return False
    elif tie(the_board):
        print("It's a TIE")
        return False
    else:
        return True


def tie(board):
    if board.count(' ') == 0:
        return True
    else:
        return False


def print_board():
    print(f'  {the_board[0]} | {the_board[1]} | {the_board[2]}')
    print(f'-------------')
    print(f'  {the_board[3]} | {the_board[4]} | {the_board[5]}')
    print(f'-------------')
    print(f'  {the_board[6]} | {the_board[7]} | {the_board[8]}')
    print()
    print(
        f"There are {len(ties) + len(p1w) + len(p2w)} possibilities, where in {len(p1w)} the {p1} wins, "
        f"in {len(p2w)} the {p2} wins and {len(ties)} ends with an tie")
    print(
        f"There are {len(ties_long) + len(p1w_long) + len(p2w_long)} possibilities, where in {len(p1w_long)} the {p1}"
        f" wins, in {len(p2w_long)} the {p2} wins and {len(ties_long)} ends with an tie")


def winner(board, letter):
    return (board[0] == letter and board[1] == letter and board[2] == letter) or \
           (board[3] == letter and board[4] == letter and board[5] == letter) or \
           (board[6] == letter and board[7] == letter and board[8] == letter) or \
           (board[0] == letter and board[3] == letter and board[6] == letter) or \
           (board[1] == letter and board[4] == letter and board[7] == letter) or \
           (board[2] == letter and board[5] == letter and board[8] == letter) or \
           (board[0] == letter and board[4] == letter and board[8] == letter) or \
           (board[2] == letter and board[4] == letter and board[6] == letter)


def move(pos, board):
    if board[pos] != ' ':
        return False
    else:
        return True


def player_move(letter):
    while True:
        try:
            pos = int(input(f"\nSelect where to put an '{letter}' (1-9): ")) - 1
            if move(pos, the_board):
                the_board[pos] = letter
                break
            else:
                print("Occupied space, try again")
        except ValueError:
            print("Please, input an valid move")
        except IndexError:
            print("The value must be from 1 to 9")


def computer_move():
    global p2, p1
    possibilities = []
    num_corners = 0
    for x in range(9):
        if the_board[x] == ' ':
            possibilities.append(x)
    for x in corners:
        if the_board[x] == ' ':
            num_corners += 1

    # Avoid opponent win and try to win
    for x in [p2, p1]:
        for y in possibilities:
            the_board[y] = x
            if winner(the_board, x):
                the_board[y] = p2
                return
            the_board[y] = ' '

    if p2 == 'O':
        # if available, fill the middle
        if the_board[4] == ' ':
            the_board[4] = p2
            return

        # If a corner is occupied by a player, put it in an opposite corner
        if the_board[0] == p1 and the_board[8] == ' ':
            the_board[8] = p2
            return
        if the_board[2] == p1 and the_board[6] == ' ':
            the_board[6] = p2
            return
        if the_board[6] == p1 and the_board[2] == ' ':
            the_board[2] = p2
            return
        if the_board[8] == p1 and the_board[0] == ' ':
            the_board[0] = p2
            return

        # if two corners are occupied by the person, put it in an non corner space
        if the_board[6] == p1 and the_board[2] == p1 or the_board[8] == p1 and the_board[0] == p1:
            for x in middles:
                if the_board[x] == ' ':
                    the_board[x] = p2
                    return

        # if there's an available corner, put it in there
        for x in corners:
            if the_board[x] == ' ':
                the_board[x] = p2
                return

    else:

        # If the opponent fill one of the middles, fill the middle
        for x in middles:
            if the_board[x] == p1 and the_board[4] == ' ' and num_corners > 2:
                the_board[4] = p2
                return

        # If a corner is occupied, put it in an opposite corner
        for x in [p1, p2]:
            if the_board[0] == x and the_board[8] == ' ':
                the_board[8] = p2
                return
            if the_board[2] == x and the_board[6] == ' ':
                the_board[6] = p2
                return
            if the_board[6] == x and the_board[2] == ' ':
                the_board[2] = p2
                return
            if the_board[8] == x and the_board[0] == ' ':
                the_board[0] = p2
                return

        for x in corners:
            if the_board[x] == ' ' and the_board[x-1] != p1:
                the_board[x] = p2
                return

    # fill any other space
    the_board[possibilities[0]] = p2


def replay():
    global alone, the_board, p1, p2, turn
    global p1w, p2w, ties
    char = input("Wanna play? (Y, N): ")
    if char.upper() == 'N':
        return False
    for pos in range(9):
        the_board[pos] = ' '
    clear_console()
    while True:
        char = str(input("Wanna be an 'X' or 'O': ").upper())
        if char == 'O':
            p1 = 'O'
            p2 = 'X'
            turn = 1
            break
        elif char == 'X':
            p1 = 'X'
            p2 = 'O'
            turn = 0
            break
        else:
            clear_console()
            print("Choose an valid letter")
    clear_console()
    while True:
        i = str(input("Against (B)ot or (H)uman: "))
        if i.upper().startswith('H'):
            alone = False
            break
        elif i.upper().startswith('B'):
            alone = True
            break
        else:
            clear_console()
            print("Input 'H' or 'B'")
    return True


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def pos_moves(board, movement):
    if winner(board, p1):
        p1w.add(tuple(board))
        p1w_long.append(board)
    elif winner(board, p2):
        p2w.add(tuple(board))
        p2w_long.append(board)
    elif tie(board):
        ties.add(tuple(board))
        ties_long.append(board)
    else:
        for i in range(9):
            if board[i] == " ":
                board[i] = movement
                pos_moves(board, 'X' if movement == 'O' else 'O')
                board[i] = " "


clear_console()
while replay():
    while game_over():
        if turn == 0:
            player_move(p1)
            turn = 1
        else:
            if alone:
                computer_move()
            else:
                player_move(p2)
            turn = 0
clear_console()
