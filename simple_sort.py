"""
Simple Sorting

This sorting algo compare the first number of the {min_number} with the number that follow and if

the number that follow is smaller than th min_number

the two number exchange their position

"""


class Simplesorting:

    def __int__(self):

        self.list = [12, 12, 14, 6, 5, 7]

        self.new_list = []

    def sorting(self):

        print("Unsorted list :", self.list)

        for self.unsorted_index in range(0, len(self.list)-1):

            self.min_index = self.unsorted_index

            self.min_num = self.list[self.unsorted_index]

            for i in range(self.unsorted_index + 1, len(self.list)):

                if self.list[i] < self.min_num:

                    self.min_num = self.list[i]

                    self.min_index = i

            self.list[self.min_index] = self.list[self.unsorted_index]

            self.list[self.unsorted_index] = self.min_num

        print("Sorted list :", self.list)
