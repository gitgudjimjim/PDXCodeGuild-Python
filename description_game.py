# description_game.py

chosen_word = input("choose a word that both players agree on >")
max_len = input("how many associating words will you say? >")
max_len = int(max_len)
player_one_words = []
player_two_words = []
for player in [player_one_words, player_two_words]
    while len(player) < max_len:
        player.append(input(f"what word do you associate with {chosen_word}?"))
    os.system('clear') #on windows, you might need os.system('cls')
player_one_words.sort()
player_two_words.sort()
print(player_one_words)
print(player_two_words)
if player_one_words == player_two_words:
    print("win!")
