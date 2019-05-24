class Game:
    def __init__(self):
        # you want self.board to be the data representation of your board
        # just the data that the board contains (empty spaces, and player tokens)

                                        # board = Game()
                                        # print(board) should look like:
        self.board = [['1','2','3'],    #   1|2|3
                      ['4','5','O'],    #   4|5|O
                      ['X','8','9']]    #   X|8|9


    def __repr__(self):
        # repr is just the string representation of your board
        # you want it to show the state of your board at any given time
        # i.e. you want to work with the property self.board

        # any presentational stuff (such as '|' and seperating by whitespace/newlines)
        # should happen in __repr__ instead of in your self.board property
        ret = ''
        for row in self.board:
            ret += '|'.join(row) + '\n'
        return ret



game = Game()
print(game)
Collapse
