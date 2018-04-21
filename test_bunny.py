import unittest
from bunny import Bunny


class TestBunny(unittest.TestCase):

    def get_center_even_rows_odd_cols(self):
        garden = [[1, 3, 2], [1, 8, 0], [0, 3, 5], [9, 2, 3]]
        bunny = Bunny(garden)
        assert 1, 1 is bunny.get_center()

    def get_center_odd_rows_even_cols(self):
        garden = [[1, 3, 2, 7], [1, 8, 5, 8], [0, 3, 5, 8]]
        bunny = Bunny(garden)
        assert 1, 1 is bunny.get_center()

    def get_center_odd_rows_odd_cols(self):
        garden = [[1, 3, 2], [1, 4, 0], [0, 3, 5]]
        bunny = Bunny(garden)
        assert 1, 1 is bunny.get_center()

    def get_next_hop_has_no_hops(self):
        garden = [[0, 0],
                  [0, 8]]
        bunny = Bunny(garden)
        assert (None, None) == bunny.get_next_hop(0,0)

    def get_next_hop_simple(self):
        garden = [[6, 8],
                  [0, 0]]
        bunny = Bunny(garden)
        assert (1,1) == bunny.get_next_hop(0,0)

    def get_next_hop(self):
        garden = [[1, 3, 2, 7],
                  [1, 8, 3, 8],
                  [0, 3, 5, 8],
                  [9, 0, 9, 8]]

        bunny = Bunny(garden)
        assert (None, None) == bunny.get_next_hop(3, 0)
        # edges
        assert (0, 1) == bunny.get_next_hop(0, 0)
        assert (1, 3) == bunny.get_next_hop(0, 3)
        assert (3, 2) == bunny.get_next_hop(3, 3)
        assert (1, 2) == bunny.get_next_hop(1, 1)

        # choose in correct preference order - right, down, left, up
        assert (1, 1) == bunny.get_next_hop(2, 1)
        assert (3, 2) == bunny.get_next_hop(2, 2)
        assert (3, 3) == bunny.get_next_hop(3, 2)


    # tests for eat()
    def test_bunny_no_hop_small(self):
        garden = [[5, 0],
                  [0, 0]]

        bunny = Bunny(garden)
        num_carrots_eaten = bunny.eat()
        assert num_carrots_eaten == 5

    def test_bunny_no_hop_big(self):
        garden = [[1, 0, 2, 7],
                  [0, 8, 0, 8],
                  [0, 0, 5, 8],
                  [9, 0, 9, 8]]

        bunny = Bunny(garden)
        num_carrots_eaten = bunny.eat()
        assert num_carrots_eaten == 8

    def test_bunny_simple_multiple_hops_small(self):
        garden = [[6, 8],
                  [0, 0]]

        bunny = Bunny(garden)
        num_carrots_eaten = bunny.eat()
        assert num_carrots_eaten == (8 + 6)

    def test_bunny_simple_multiple_hops_big(self):
        garden = [[0, 0, 0, 0],
                  [0, 8, 0, 0],
                  [0, 6, 5, 0],
                  [0, 0, 0, 0]]

        bunny = Bunny(garden)
        num_carrots_eaten = bunny.eat()
        assert num_carrots_eaten == (8 + 6 + 5)

    def test_bunny_check_simple_loop(self):
        garden = [[5, 2],
                  [4, 3]]

        bunny = Bunny(garden)
        num_carrots_eaten = bunny.eat()
        assert num_carrots_eaten == (5 + 4 + 3 + 2)

    def test_bunny_check_complex_loop(self):
        garden = [[0, 1, 0, 0],
                  [0, 8, 2, 3],
                  [0, 6, 5, 4],
                  [0, 0, 0, 0]]

        bunny = Bunny(garden)
        num_carrots_eaten = bunny.eat()
        assert num_carrots_eaten == (8 + 6 + 5 + 4 + 3 + 2)


if __name__ == '__main__':
    unittest.main()
