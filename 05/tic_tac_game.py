from exceptions import InvalidInputError, NotNumberError, OutOfRangeError, TakenCellError


class TicTacGame:
    def __init__(self):
        self.__board = list(range(1, 10))

    def show_board(self):
        for i in range(3):
            print(self.__board[0 + i * 3], ' ',
                  self.__board[1 + i * 3], ' ',
                  self.__board[2 + i * 3])

    def validate_input(self, player_token):
        print(f'Where will we put {player_token}?')
        try:
            player_answer = int(input())
        except ValueError as err:
            raise NotNumberError(
                'Please, enter the number.') from err

        if player_answer < 1 or 9 < player_answer:
            raise OutOfRangeError(
                'Please, enter the number from 1 to 9.')

        if str(self.__board[player_answer - 1]) in 'XO':
            raise TakenCellError('This cell is already taken.')

        self.__board[player_answer - 1] = player_token

    def check_winner(self):
        winner_coords = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                         (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for winner_coord in winner_coords:
            if self.__board[winner_coord[0]] == \
                    self.__board[winner_coord[1]] == \
                    self.__board[winner_coord[2]]:
                return self.__board[winner_coord[0]]
        return None

    def start_game(self, first='X'):
        second = '0' if first == 'X' else 'X'

        counter = 0
        while True:
            self.show_board()

            while True:
                try:
                    self.validate_input(first if counter % 2 == 0 else second)
                    break
                except InvalidInputError as err:
                    print(f"Invalid input. {err}")
                    continue

            counter += 1
            if counter > 4:
                winner = self.check_winner()
                if winner:
                    self.show_board()
                    print(winner, 'win!')
                    break

            if counter == 9:
                self.show_board()
                print('Draw!')
                break


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
