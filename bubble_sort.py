
""""
Bubble Sorting

    ( 5 1 4 2 8 ) → ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
    ( 1 5 4 2 8 ) → ( 1 4 5 2 8 ), Swap since 5 > 4
    ( 1 4 5 2 8 ) → ( 1 4 2 5 8 ), Swap since 5 > 2
    ( 1 4 2 5 8 ) → ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

     Then the algorithm repeat the process untill it cannot swap again
"""


class BubbleSorting:

    def __init__(self):

        self.list = [5, 1, 4, 2, 8, 8, 1]

    def sorting(self):

        print("Unsorted list : ", self.list)

        # first number selected i

        for i in range(0, len(self.list)):

            # second number selected j
            for j in range(len(self.list)-1):

                # comparing the two number i , j
                if self.list[j] > self.list[i]:

                    # if j > i , change the position of the two
                    self.list[j], self.list[i] = self.list[i], self.list[j]

        print("Sorted list : ", self.list)





















