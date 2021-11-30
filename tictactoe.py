game = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

over = 0

while over == 0:

    player1 = input("player 1, where do you want to go? - type it in the format [row] [column]")
    while True:
        try:
            if game[int(player1[0])-1][int(player1[-1])-1] == 0:
                game[int(player1[0])-1][int(player1[-1])-1] = 1
                break
            else:
                print("not a valid option")
        except:
            print("error")
    player2 = input("player 2, where do you want to go? - type it in the format [row] [column]")
    while True:
        try:
            if game[int(player2[0])-1][int(player2[-1])-1] == 0:
                game[int(player2[0])-1][int(player2[-1])-1] = 2
                break
            else:
                print("not a valid option")
        except:
            print("error")

    print("this is the board:")
    print(f"""{game[0]}
    {game[1]}
    {game[2]}""")



    for x in range(0,2):
        if game[x][0] == game[x][1] == game[x][2]:
            print(f'player {game[x][0]} wins')
            over = 1
    for x in range(0,2):
        if game[0][x] == game[1][x] == game[2][x]:
            print(f'player {game[0][x]} wins')
            over = 1

    if game[0][0] == game[1][1] == game[2][2]:
            print(f'player {game[0][0]} wins')
            over = 1
    if game[2][0] == game[1][1] == game[0][2]:
            print(f'player {game[1][1]} wins')
            over = 1

    if over == 1:
        print("thanks for playing")