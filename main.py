
from bubble_sort import *

from simple_sort import *

Question = input("What sorting algorithm do you want to use ? [simple, bubble] ")

if Question == "simple":

    simple_sort = Simplesorting()

    simple_sort.__int__()

    simple_sort.sorting()

elif Question == "bubble":

    bubble_sorting = BubbleSorting()

    bubble_sorting.__init__()

    bubble_sorting.sorting()







