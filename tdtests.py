# Name:         Amani Arora
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Tile Driver
# Term:         Spring 2021

import unittest

import tiledriver
from tiledriver import PuzzleState as PS  # only allowed use of from ... import


class TestMakeAdjacent(unittest.TestCase):

    def test_make_adjacent_1(self):
        state = PS((3, 2, 1, 0), "")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((3, 0, 1, 2), "J"), PS((3, 2, 0, 1), "L")])

    def test_make_adjacent_2(self):
        state = PS((1, 2, 3, 0), "")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((1, 0, 3, 2), "J"), PS((1, 2, 0, 3), "L")])

    def test_make_adjacent_3(self):
        state = PS((0, 2, 3, 1), "")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((3, 2, 0, 1), "K"), PS((2, 0, 3, 1), "H")])

    def test_make_adjacent_4(self):
        state = PS((4, 0, 2, 3, 1, 5, 6, 7, 8), "")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((4, 1, 2, 3, 0, 5, 6, 7, 8), "K"),
                          PS((4, 2, 0, 3, 1, 5, 6, 7, 8), "H"),
                          PS((0, 4, 2, 3, 1, 5, 6, 7, 8), "L")])

    def test_make_adjacent_5(self):
        state = PS((3, 7, 6, 8, 0, 1, 4, 2, 5), "K")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((3, 7, 6, 8, 2, 1, 4, 0, 5), "KK"),
                          PS((3, 7, 6, 8, 1, 0, 4, 2, 5), "KH"),
                          PS((3, 7, 6, 0, 8, 1, 4, 2, 5), "KL")])

class TestSwap(unittest.TestCase):

    def test_swap_1(self):
        lst = [1, 2, 3, 4]
        swapped = [1, 3, 2, 4]
        self.assertEqual(tiledriver.swap(lst, 1, 2),
                         swapped)

    def test_swap_2(self):
        lst = [1, 3, 2, 4]
        swapped = [4, 3, 2, 1]
        self.assertEqual(tiledriver.swap(lst, 0, 3),
                         swapped)

    def test_swap_3(self):
        lst = [4, 5]
        swapped = [5, 4]
        self.assertEqual(tiledriver.swap(lst, 0, 1),
                         swapped)

    def test_swap_4(self):
        lst = [8, 8, 6, 3, 5]
        swapped = [3, 8, 6, 8, 5]
        self.assertEqual(tiledriver.swap(lst, 0, 3),
                         swapped)

    def test_swap_5(self):
        lst = [3, 2, 1]
        swapped = [3, 1, 2]
        self.assertEqual(tiledriver.swap(lst, 1, 2),
                         swapped)

class TestNewEntry(unittest.TestCase):

    def test_new_entry_1(self):
        self.assertEqual(tiledriver.new_entry([2, 1, 0, 3], "K", 0, 2, ""),
                         PS((0, 1, 2, 3), "K"))

    def test_new_entry_2(self):
        self.assertEqual(tiledriver.new_entry([2, 1, 0, 3], "J", 0, 2, ""),
                         PS((0, 1, 2, 3), "J"))

    def test_new_entry_3(self):
        self.assertEqual(tiledriver.new_entry([2, 1, 0, 3], "H", 0, 2, ""),
                         PS((0, 1, 2, 3), "H"))

    def test_new_entry_4(self):
        self.assertEqual(tiledriver.new_entry([2, 1, 0, 3], "I", 0, 2, ""),
                         PS((0, 1, 2, 3), "I"))

    def test_new_entry_5(self):
        self.assertEqual(tiledriver.new_entry([2, 1, 0, 3], "L", 0, 2, ""),
                         PS((0, 1, 2, 3), "L"))

class TestValid(unittest.TestCase):

    def test_valid_1(self):
        directions = [2, 1, 0, 3]
        index = 1
        blank = 3
        width = 2
        total_tiles = 4
        self.assertEqual(tiledriver.valid(directions,
                                index, blank, width, total_tiles), True)

    def test_valid_2(self):
        directions = [2, 1, 0, 3]
        index = 1
        blank = 5
        width = 2
        total_tiles = 4
        self.assertEqual(tiledriver.valid(directions,
                             index, blank, width, total_tiles), True)

    def test_valid_3(self):
        directions = [2, 1, 0, 3]
        index = 1
        blank = 1
        width = 2
        total_tiles = 4
        self.assertEqual(tiledriver.valid(directions,
                             index, blank, width, total_tiles), True)

    def test_valid_4(self):
        directions = [2, 1, 0, 3]
        index = 1
        blank = 3
        width = 3
        total_tiles = 4
        self.assertEqual(tiledriver.valid(directions,
                            index, blank, width, total_tiles), False)

    def test_valid_5(self):
        directions = [2, 1, 0, 3]
        index = 2
        blank = 3
        width = 2
        total_tiles = 4
        self.assertEqual(tiledriver.valid(directions,
                               index, blank, width, total_tiles), False)

class TestNonOpposing(unittest.TestCase):

    def test_non_opposing_1(self):
        index = 0
        path = 'KL'
        self.assertEqual(tiledriver.non_opposing(index, path), True)

    def test_non_opposing_2(self):
        index = 0
        path = 'K'
        self.assertEqual(tiledriver.non_opposing(index, path), True)

    def test_non_opposing_3(self):
        index = 0
        path = ''
        self.assertEqual(tiledriver.non_opposing(index, path), True)

    def test_non_opposing_4(self):
        index = 1
        path = 'KL'
        self.assertEqual(tiledriver.non_opposing(index, path), True)

    def test_non_opposing_5(self):
        index = 2
        path = 'KL'
        self.assertEqual(tiledriver.non_opposing(index, path), False)






class TestIsSolvable(unittest.TestCase):

    def test_is_solvable_1(self):
        self.assertTrue(tiledriver.is_solvable((3, 2, 1, 0)))

    def test_is_solvable_2(self):
        self.assertFalse(tiledriver.is_solvable((0, 2, 1, 3)))

    def test_is_solvable_3(self):
        self.assertFalse(tiledriver.is_solvable((2, 0, 1, 3)))

    def test_is_solvable_4(self):
        self.assertFalse(tiledriver.is_solvable((0, 8, 5, 3)))

    def test_is_solvable_5(self):
        self.assertTrue(tiledriver.is_solvable((3, 0, 1, 2, 4, 6, 8, 7, 5)))

class TestMergeSortStarter(unittest.TestCase):

    def test_merge_sort_starter_1(self):
        new = [3, 2, 1, 0]
        length = len(new)
        self.assertEqual(tiledriver.merge_sort_starter(new, length), 6)

    def test_merge_sort_starter_2(self):
        new = [5, 3, 1, 4]
        length = len(new)
        self.assertEqual(tiledriver.merge_sort_starter(new, length), 4)

    def test_merge_sort_starter_3(self):
        new = [6, 4, 2, 1]
        length = len(new)
        self.assertEqual(tiledriver.merge_sort_starter(new, length), 6)

    def test_merge_sort_starter_4(self):
        new = [8, 9, 6, 4]
        length = len(new)
        self.assertEqual(tiledriver.merge_sort_starter(new, length), 5)

    def test_merge_sort_starter_5(self):
        new = [4, 5, 6, 7]
        length = len(new)
        self.assertEqual(tiledriver.merge_sort_starter(new, length), 0)

class TestMergeSort(unittest.TestCase):

    def test_merge_sort_1(self):
        new = [2, 4, 5, 7]
        length = len(new)
        hold = [0] * length
        self.assertEqual(tiledriver.merge_sort(new, hold, 0, length - 1), 0)

    def test_merge_sort_2(self):
        new = [2, 8, 5, 7]
        length = len(new)
        hold = [0] * length
        self.assertEqual(tiledriver.merge_sort(new, hold, 0, length - 1), 2)

    def test_merge_sort_3(self):
        new = [2, 3, 5, 7]
        length = len(new)
        hold = [0] * length
        self.assertEqual(tiledriver.merge_sort(new, hold, 0, length - 1), 0)

    def test_merge_sort_4(self):
        new = [2, 9, 5, 7]
        length = len(new)
        hold = [0] * length
        self.assertEqual(tiledriver.merge_sort(new, hold, 0, length - 1), 2)

    def test_merge_sort_5(self):
        new = [2, 6, 5, 7]
        length = len(new)
        hold = [0] * length
        self.assertEqual(tiledriver.merge_sort(new, hold, 0, length - 1), 1)

class TestMerge(unittest.TestCase):

    def test_merge_1(self):
        new = [2, 4, 5, 7]
        length = len(new)
        hold = [0] * length
        left = 0
        mid = 2
        right = 3
        self.assertEqual(tiledriver.merge(new, hold, left, mid, right), 0)

    def test_merge_2(self):
        new = [2, 4, 5, 8]
        length = len(new)
        hold = [0] * length
        left = 0
        mid = 2
        right = 3
        self.assertEqual(tiledriver.merge(new, hold, left, mid, right), 0)

    def test_merge_3(self):
        new = [2, 4, 6, 7]
        length = len(new)
        hold = [0] * length
        left = 0
        mid = 2
        right = 3
        self.assertEqual(tiledriver.merge(new, hold, left, mid, right), 0)

    def test_merge_4(self):
        new = [2, 3, 5, 7]
        length = len(new)
        hold = [0] * length
        left = 0
        mid = 2
        right = 3
        self.assertEqual(tiledriver.merge(new, hold, left, mid, right), 0)

    def test_merge_5(self):
        new = [1, 4, 5, 7]
        length = len(new)
        hold = [0] * length
        left = 0
        mid = 2
        right = 3
        self.assertEqual(tiledriver.merge(new, hold, left, mid, right), 0)



class TestSolvePuzzle(unittest.TestCase):

    def test_solve_puzzle_1(self):
        self.assertEqual(tiledriver.solve_puzzle((3, 2, 1, 0)), "JLKHJL")

    def test_solve_puzzle_2(self):
        self.assertEqual(tiledriver.solve_puzzle((0, 1, 2, 3)), "")

    def test_solve_puzzle_3(self):
        self.assertEqual(tiledriver.solve_puzzle((2, 1, 3, 0)), "LJ")

    def test_solve_puzzle_4(self):
        self.assertEqual(tiledriver.solve_puzzle((1, 4, 2, 3, 0,
                                        5, 6, 7, 8)), "JL")

    def test_solve_puzzle_5(self):
        self.assertEqual(tiledriver.solve_puzzle((1, 0, 2, 3,
                                        4, 5, 6, 7, 8)), "L")


class TestUniformCostSearch(unittest.TestCase):

    def test_uniform_cost_search_1(self):
        start = PS((3, 2, 0, 1), "")
        endgoal = (0, 1, 2, 3)
        self.assertEqual(tiledriver.uniform_cost_search(start,
                                            endgoal, explored=[]),
                         "JHKLJ")

    def test_uniform_cost_search_2(self):
        start = PS((2, 1, 0, 3), "")
        endgoal = (0, 1, 2, 3)
        self.assertEqual(tiledriver.uniform_cost_search(start,
                                    endgoal, explored=[]),
                                        "J")

    def test_uniform_cost_search_3(self):
        start = PS((0, 1, 2, 3, 4, 5, 6, 7, 8), "")
        endgoal = (0, 1, 2, 3, 4, 5, 6, 7, 8)
        self.assertEqual(tiledriver.uniform_cost_search(start,
                                    endgoal, explored=[]), "")

    def test_uniform_cost_search_4(self):
        start = PS((1, 0, 2, 3, 4, 5, 6, 7, 8), "")
        endgoal = (0, 1, 2, 3, 4, 5, 6, 7, 8)
        self.assertEqual(tiledriver.uniform_cost_search(start,
                                    endgoal, explored=[]), "L")

    def test_uniform_cost_search_5(self):
        start = PS((1, 4, 2, 3, 0, 5, 6, 7, 8), "")
        endgoal = (0, 1, 2, 3, 4, 5, 6, 7, 8)
        self.assertEqual(tiledriver.uniform_cost_search(start,
                                            endgoal, explored=[]), "JL")


class TestInsertionSort(unittest.TestCase):

    def test_insertion_sort_1(self):
        lst = [1, 2, 4, 3]
        sorted_lst = [1, 2, 3, 4]
        self.assertEqual(tiledriver.insertion_sort(lst), sorted_lst)

    def test_insertion_sort_2(self):
        lst = [1, 2, 4, 3]
        sorted_lst = [1, 2, 3, 4]
        self.assertEqual(tiledriver.insertion_sort(lst), sorted_lst)

    def test_insertion_sort_3(self):
        lst = [6, 2, 4, 3]
        sorted_lst = [2, 3, 4, 6]
        self.assertEqual(tiledriver.insertion_sort(lst), sorted_lst)

    def test_insertion_sort_4(self):
        lst = [1, 9, 4, 8]
        sorted_lst = [1, 4, 8, 9]
        self.assertEqual(tiledriver.insertion_sort(lst), sorted_lst)

    def test_insertion_sort_5(self):
        lst = [1]
        sorted_lst = [1]
        self.assertEqual(tiledriver.insertion_sort(lst), sorted_lst)

    def test_insertion_sort_6(self):
        lst = []
        sorted_lst = []
        self.assertEqual(tiledriver.insertion_sort(lst), sorted_lst)

class TestInExplored(unittest.TestCase):

    def test_in_explored_1(self):
        explored = [PS((0, 2, 3, 1), 'JK')]
        move = PS((2, 0, 3, 1), 'JKL')
        self.assertEqual(tiledriver.in_explored(move, explored), False)

    def test_in_explored_2(self):
        explored = [PS((0, 2, 3, 1), 'JK')]
        move = PS((2, 0, 6, 1), 'JKL')
        self.assertEqual(tiledriver.in_explored(move, explored), False)

    def test_in_explored_3(self):
        explored = [PS((0, 2, 3, 1), 'JK')]
        move = PS((2, 0, 7, 1), 'JKL')
        self.assertEqual(tiledriver.in_explored(move, explored), False)

    def test_in_explored_4(self):
        explored = [PS((0, 2, 3, 1), 'JK')]
        move = PS((2, 0, 8, 1), 'JKL')
        self.assertEqual(tiledriver.in_explored(move, explored), False)

    def test_in_explored_5(self):
        explored = [PS((0, 2, 3, 1), 'JK')]
        move = PS((2, 0, 9, 1), 'JKL')
        self.assertEqual(tiledriver.in_explored(move, explored), False)

class TestQueueProcessing(unittest.TestCase):

    def test_queue_processing_1(self):
        queue = [PS((0, 2, 3, 1), 'JK')]
        move = PS((2, 0, 3, 1), 'JKL')
        self.assertEqual(tiledriver.queue_processing(queue, move),
                         queue)

    def test_queue_processing_2(self):
        queue = [PS((0, 2, 3, 1), 'JK')]
        move = PS((2, 0, 7, 1), 'JKL')
        self.assertEqual(tiledriver.queue_processing(queue, move),
                         queue)

    def test_queue_processing_3(self):
        queue = [PS((0, 2, 3, 1), 'JK')]
        move = PS((2, 0, 8, 1), 'JKL')
        self.assertEqual(tiledriver.queue_processing(queue, move),
                         queue)

    def test_queue_processing_4(self):
        queue = [PS((0, 2, 3, 1), 'JK')]
        move = PS((2, 0, 9, 1), 'JKL')
        self.assertEqual(tiledriver.queue_processing(queue, move),
                         queue)

    def test_queue_processing_5(self):
        queue = [PS((0, 2, 3, 1), 'JK')]
        move = PS((2, 0, 5, 1), 'JKL')
        self.assertEqual(tiledriver.queue_processing(queue, move),
                         queue)

class TestInsertionSortPuzzles(unittest.TestCase):

    def test_insertion_sort_puzzles_1(self):
        queue = [PS((0, 2, 3, 1), 'JK'), PS((0, 2, 3, 1), 'J')]
        sortedd = [PS((0, 2, 3, 1), 'J'), PS((0, 2, 3, 1), 'JK')]
        self.assertEqual(tiledriver.insertion_sort_puzzles(queue),
                         sortedd)

    def test_insertion_sort_puzzles_2(self):
        queue = [PS((0, 2, 3, 1), 'JKL'), PS((0, 2, 3, 1), 'J')]
        sortedd = [PS((0, 2, 3, 1), 'J'), PS((0, 2, 3, 1), 'JKL')]
        self.assertEqual(tiledriver.insertion_sort_puzzles(queue),
                         sortedd)

    def test_insertion_sort_puzzles_3(self):
        queue = [PS((0, 2, 3, 1), 'JKKK'), PS((0, 2, 3, 1), 'J')]
        sortedd = [PS((0, 2, 3, 1), 'J'), PS((0, 2, 3, 1), 'JKKK')]
        self.assertEqual(tiledriver.insertion_sort_puzzles(queue),
                         sortedd)

    def test_insertion_sort_puzzles_4(self):
        queue = [PS((0, 2, 3, 1), 'JKK'), PS((0, 2, 3, 1), 'JK')]
        sortedd = [PS((0, 2, 3, 1), 'JK'), PS((0, 2, 3, 1), 'JKK')]
        self.assertEqual(tiledriver.insertion_sort_puzzles(queue),
                         sortedd)

    def test_insertion_sort_puzzles_5(self):
        queue = [PS((0, 2, 3, 1), 'JKLL'), PS((0, 2, 3, 1), 'JL')]
        sortedd = [PS((0, 2, 3, 1), 'JL'), PS((0, 2, 3, 1), 'JKLL')]
        self.assertEqual(tiledriver.insertion_sort_puzzles(queue),
                         sortedd)





if __name__ == "__main__":
    unittest.main()

