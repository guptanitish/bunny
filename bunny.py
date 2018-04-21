class Bunny(object):
    def __init__(self, garden):
        self.garden = garden

    def get_center(self):
        num_rows = len(self.garden)
        num_cols = len(self.garden[0])

        begin_rows = (num_rows - 1) / 2
        end_rows = begin_rows + (1 - num_rows % 2)

        begin_cols = (num_cols - 1) / 2
        end_cols = begin_cols + (1 - num_cols % 2)

        num_carrots = 0
        x, y = None, None
        for i in range(begin_rows, end_rows):
            for j in range(begin_cols, end_cols):
                if self.garden[i][j] > num_carrots:
                    x, y = i, j

        assert x is not None
        assert y is not None

        return x, y

    '''
    find the next spot with most number of carrots
    if number of carrots are same, then preference is right, down, left, up
    '''
    def get_next_hop(self, i, j):
        next_i, next_j = None, None
        max_num_carrots = 0


        # right
        if j < len(self.garden) - 1 and self.garden[i][j + 1] > max_num_carrots:
            next_i, next_j = i, j + 1
            max_num_carrots = self.garden[i][j + 1]

        # down
        if i < len(self.garden) - 1 and self.garden[i + 1][j] > max_num_carrots:
            max_num_carrots = self.garden[i + 1][j]
            next_i, next_j = i + 1, j

        # left
        if j > 0 and self.garden[i][j - 1] > max_num_carrots:
            max_num_carrots = self.garden[i][j - 1]
            next_i, next_j = i, j - 1

        # up
        if i > 0 and self.garden[i - 1][j] > max_num_carrots:
            max_num_carrots = self.garden[i - 1][j]
            next_i, next_j = i - 1, j

        return next_i, next_j

    def eat(self):

        num_carrots_eaten = 0
        i, j = self.get_center()

        while True:
            num_carrots_eaten += self.garden[i][j]
            self.garden[i][j] = 0
            i, j = self.get_next_hop(i, j)
            if i is None or j is None:
                break

        return num_carrots_eaten
