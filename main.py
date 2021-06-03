import random

player = 'X'
computer = 'O'
the_board: list[str] = [' ' for x in range(9)]


def winner():
    global alone
    if alone:
        if is_winner(the_board, player):
            print("YOU WON")
            return False
        elif is_winner(the_board, computer):
            print("YOU LOSE")
            return False
        elif is_full():
            print("It's a TIE")
            return False
    else:
        if is_winner(the_board, player):
            print(f"PLAYER {player} WON")
            return False
        elif is_winner(the_board, computer):
            print(f"PLAYER {the_board, computer} WON")
            return False
        elif is_full():
            print("It's a TIE")
            return False
    return True


def is_full():
    if the_board.count(' ') == 0:
        return True
    else:
        return False


def print_board():
    print(f'---------------')
    print(f'| {the_board[0]} || {the_board[1]} || {the_board[2]} |')
    print(f'---------------')
    print(f'| {the_board[3]} || {the_board[4]} || {the_board[5]} |')
    print(f'---------------')
    print(f'| {the_board[6]} || {the_board[7]} || {the_board[8]} |')
    print(f'---------------')


def is_winner(bo, le):
    return (bo[0] == le and bo[1] == le and bo[2] == le) or \
           (bo[3] == le and bo[4] == le and bo[5] == le) or \
           (bo[6] == le and bo[7] == le and bo[8] == le) or \
           (bo[0] == le and bo[3] == le and bo[6] == le) or \
           (bo[1] == le and bo[4] == le and bo[7] == le) or \
           (bo[2] == le and bo[5] == le and bo[8] == le) or \
           (bo[0] == le and bo[4] == le and bo[8] == le) or \
           (bo[2] == le and bo[4] == le and bo[6] == le)


def move(pos, board):
    if board[pos] != ' ':
        return False
    else:
        return True


def player_move():
    run = True
    while run:
        try:
            pos = int(input(f"\nSelect where to put an '{player}' (1-9): ")) - 1
            if move(pos, the_board):
                the_board[pos] = player
                run = False
            else:
                print("Invalid move, try again")
        except:
            print("Please, input an valid move")


def player2_move():
    run = True
    while run:
        try:
            pos = int(input(f"\nSelect where to put an '{computer}' (1-9): ")) - 1
            if move(pos, the_board):
                the_board[pos] = computer
                run = False
            else:
                print("Invalid move, try again")
        except:
            print("Please, input an valid move")


def choose_letter():
    global player, computer
    print("Wanna be an 'X' or 'O'")
    while True:
        char = input().upper()
        if char == 'O':
            player = 'O'
            computer = 'X'
            break
        elif char == 'X':
            player = 'X'
            computer = 'O'
            break
        else:
            print("Choose an valid letter")


def computer_move():
    """
    Is there an win-move?
    is there an lose-move
    is any corner available?
    is the center available?
    random move
    """
    global computer, player
    pos_moves = [x for x, y in enumerate(the_board) if y == ' ']
    copy = the_board
    done = True
    for pos in pos_moves:
        copy[pos] = computer
        if is_winner(copy, computer):
            the_board[pos] = computer
            done = False
            break
        copy[pos] = ' '
    if done:
        for pos in pos_moves:
            copy[pos] = player
            if is_winner(copy, player):
                the_board[pos] = computer
                done = False
                break
            copy[pos] = ' '
    if done:
        if 0 in pos_moves:
            the_board[0] = computer
            done = False
        elif 2 in pos_moves:
            the_board[2] = computer
            done = False
        elif 6 in pos_moves:
            the_board[6] = computer
            done = False
        elif 8 in pos_moves:
            the_board[8] = computer
            done = False
        elif 5 in pos_moves:
            the_board[5] = computer
            done = False
    if done:
        the_board[pos_moves[0]] = computer


def are_u_alone():
    print("Against (B)ot or (H)uman: ")
    while True:
        p2 = input()
        if p2.upper().startswith('H'):
            return False
        elif p2.upper().startswith('B'):
            return True
        else:
            print("Input 'H' or 'B'")


def replay():
    char = input("Wanna play? (Y, N) ")
    if char.upper() == 'Y':
        return True
    elif char.upper() == 'N':
        return False
    else:
        return True


while replay():
    the_board: list[str] = [' ' for x in range(9)]
    choose_letter()
    global alone
    turn = random.randint(0, 1)
    if are_u_alone():
        alone = True
    else:
        alone = False
    while not is_full() and winner():
        print_board()
        if turn == 0:
            player_move()
            turn = 1
        else:
            if alone:
                computer_move()
            else:
                player2_move()
            turn = 0
