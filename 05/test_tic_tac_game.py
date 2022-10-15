import sys
import unittest
from io import StringIO
from unittest import mock

from exceptions import NotNumberError, OutOfRangeError, TakenCellError
from tic_tac_game import TicTacGame


@mock.patch('sys.stdout', new=StringIO())
class TestTicTac(unittest.TestCase):

    @staticmethod
    def merge_el_by_el(lhs, rhs) -> list:
        arr = []

        if len(lhs) != len(rhs):
            return arr

        for i in range(2 * len(lhs)):
            arr.append(str(
                lhs[i // 2] if i % 2 == 0 else rhs[i // 2]))

        return arr

    def test_1_ashow_board(self):
        game = TicTacGame()

        game.show_board()
        output = sys.stdout.getvalue().strip().splitlines()

        self.assertEqual(len(output), 3)
        self.assertEqual(output[0], '1   2   3')
        self.assertEqual(output[1], '4   5   6')
        self.assertEqual(output[2], '7   8   9')

    def test_2_validate_input(self):
        game = TicTacGame()
        with mock.patch('builtins.input',
                        side_effect=['abc', '23', '1', '1', '2']):
            while True:
                try:
                    game.validate_input('X')
                    break
                except (NotNumberError, OutOfRangeError) as err:
                    print(err)
                    continue
            output = sys.stdout.getvalue().strip().splitlines()
            self.assertEqual(len(output), 8)

            # invalid input: not a number
            self.assertEqual(output[3], 'Where will we put X?')
            self.assertEqual(output[4],
                             'Please, enter the number.')

            # invalid input: out of the range
            self.assertEqual(output[5], 'Where will we put X?')
            self.assertEqual(output[6],
                             'Please, enter the number from 1 to 9.')

            # step: put X to 1
            self.assertEqual(output[7], 'Where will we put X?')
            game.show_board()
            while True:
                try:
                    game.validate_input('0')
                    break
                except TakenCellError as err:
                    print(err)
                    continue
            output = sys.stdout.getvalue().strip().splitlines()
            self.assertEqual(len(output), 14)
            self.assertEqual(output[8], 'X   2   3')
            self.assertEqual(output[9], '4   5   6')
            self.assertEqual(output[10], '7   8   9')

            # step: try to put 0 to 1
            self.assertEqual(output[11], 'Where will we put 0?')
            self.assertEqual(output[12], 'This cell is already taken.')

            # step: try to put 0 to 1
            self.assertEqual(output[13], 'Where will we put 0?')
            game.show_board()
            output = sys.stdout.getvalue().strip().splitlines()
            self.assertEqual(len(output), 17)
            self.assertEqual(output[14], 'X   0   3')
            self.assertEqual(output[15], '4   5   6')
            self.assertEqual(output[16], '7   8   9')

    def test_3_check_winner(self):
        win_steps_rows = ((1, 2, 3),
                          (4, 5, 6),
                          (7, 8, 9))
        lose_steps_rows = ((4, 5, 7),
                           (7, 8, 3),
                           (1, 2, 6))
        for player in 'X0':
            for i in range(3):
                steps = TestTicTac.merge_el_by_el(win_steps_rows[i],
                                                  lose_steps_rows[i])
                steps.pop()
                with mock.patch('builtins.input', side_effect=steps):
                    game = TicTacGame()
                    game.start_game(player)
                    output = sys.stdout.getvalue().strip().splitlines()
                    self.assertEqual(
                        output[-1], f'{player} win!')

        win_steps_cols = ((1, 4, 7),
                          (2, 5, 8),
                          (3, 6, 9))
        lose_steps_cols = ((2, 6, 8),
                           (3, 4, 9),
                           (1, 5, 7))
        for player in 'X0':
            for i in range(3):
                steps = TestTicTac.merge_el_by_el(win_steps_cols[i],
                                                  lose_steps_cols[i])
                steps.pop()
                with mock.patch('builtins.input', side_effect=steps):
                    game = TicTacGame()
                    game.start_game(player)
                    output = sys.stdout.getvalue().strip().splitlines()
                    self.assertEqual(
                        output[-1], f'{player} win!')

        win_steps_diags = ((1, 5, 9),
                           (3, 5, 7))
        lose_steps_diags = ((2, 3, 6),
                            (1, 2, 4))
        for player in 'X0':
            for i in range(2):
                steps = TestTicTac.merge_el_by_el(win_steps_diags[i],
                                                  lose_steps_diags[i])
                steps.pop()
                with mock.patch('builtins.input', side_effect=steps):
                    game = TicTacGame()
                    game.start_game(player)
                    output = sys.stdout.getvalue().strip().splitlines()
                    self.assertEqual(
                        output[-1], f'{player} win!')

        for player in 'X0':
            steps = [1, 2, 3, 4, 6, 9, 7, 5, 8]
            with mock.patch('builtins.input', side_effect=steps):
                game = TicTacGame()
                game.start_game(player)
                output = sys.stdout.getvalue().strip().splitlines()
                self.assertEqual(
                    output[-1], 'Draw!')


if __name__ == '__main__':
    unittest.main()
