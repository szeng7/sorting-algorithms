import random
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np
import argparse as ap
import math

"""
Sorting algorithm where you take a single element and keep moving it to the right
until the element to its right is larger than it (bubble it up).

Average O(n^2) time. It doesn't seem like it's O(n^2) below but you have to remember that this function gets
called n times (so n*n = n^2).
"""

def bubblesort(arr):
    for i in range(1, len(arr)):
        for x in range(0, len(arr) - i):
            if arr[x] > arr[x+1]:
                arr[x], arr[x+1] = arr[x+1], arr[x]
            yield arr

"""
Sorting algorithm where you take a single element as your "pointer" and then place it in
its final position from index 0 to that pointer. A good analogy is to think of sorting cards
in our hand. The elements to the left of the "pointer" are the cards in your hand and you're
trying to place the pointer in its right position.

Average O(n^2) runtime

"""

def insertionsort(arr):
    print("Inside")
    for i in range(1, len(arr)):
        for x in range(i, 0, -1):
            if arr[x] < arr[x-1]:
                arr[x], arr[x-1] = arr[x-1], arr[x]
            yield arr

"""
Sorting algorithm where you constantly find the minimum element and put it at the beginning. It
maintains two subarrays within the array: one that is sorted (with the min elements) and one that's
unsorted.

Average O(n^2) runtime
"""

def selectionsort(arr):
    for i in range(0, len(arr)):
        min_index = i
        for x in range(i, len(arr)):
            if arr[x] < arr[min_index]:
                min_index = x
            yield arr
        arr[min_index], arr[i] = arr[i], arr[min_index]
        yield arr

"""
Sorting algorithm where you pick a pivot and then move all of the elements to the
left and right sides of it based on their values (so you make sure they're on the
right side with respect to the pivot).

Average O(n log n) runtime
"""

def quicksort(arr, low, high):

    if low < high:
        i = low - 1
        pivot = arr[high]

        #O(n) time
        #Move elements to their appropriate spot around the pivot
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                yield arr

        arr[i+1], arr[high] = arr[high], arr[i+1]
        yield arr

        ption = i+1

        #O(log n) time
        yield from quicksort(arr, low, ption-1)
        yield from quicksort(arr, ption+1, high)
"""
Sorting algorithm that does "divide and conquer." It takes the array
and splits it in half until it gets to the smallest unit (a single element)
before then merging them back together and sorting them at the same time.

Average O(n log n) runtime
"""
def mergesort(arr):
    if len(arr) > 1:
        #find midpoint and split into two halves
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        #recursive call
        #O(log n)
        yield from mergesort(left)
        yield from mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            yield arr

        #checking if any are left
        #O(n)

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            yield arr

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            yield arr

"""
Sorting algorithm that's based on a max binary heap, where elements
are arranged in a special order such that the value of a parent node
is greater than its children's values. This means that we
can get the max value of the array in constant time before "heapifying"
to then put the max value of the array back at the top. We do this until
the heap is empty

Average O(n log n) runtime
"""

def heapsort(arr):
    def heapify(arr, n, i):
        max = i
        left = 2 * i + 1
        right = 2 * i + 2

        #see if root's left child exists and is greater than root
        if left < n and arr[max] < arr[left]:
            max = left

        #see if root's right child exists and is greater than root
        if right < n and arr[max] < arr[right]:
            max = right

        #change root
        if max != i:
            arr[i], arr[max] = arr[max], arr[i]
            yield arr
            yield from heapify(arr, n, max)

    n = len(arr)

    #build max heap
    for i in range(n, -1, -1):
        yield from heapify(arr, n, i)

    #extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        yield from heapify(arr, i, 0)

    yield arr



"""
Sorting algorithm where you have a set number of buckets and then
you split all your elements into their apporpriate buckets before
then sorting each bucket and then concatenating all of them

Average O(n+k) runtime where k is the number of buckets
"""
def bucketsort(arr):

    #insertion sort that's used as a helper function
    #to sort each bucket
    def helpersort(b):
        for i in range(1, len(b)):
            up = b[i]
            j = i - 1
            while j >=0 and b[j] > up:
                b[j + 1] = b[j]
                j -= 1
            b[j + 1] = up
        return b

    bucket_size = 1
    if len(arr) == 0:
        return arr

    #determine min and max values
    #O(n)

    min = arr[0]
    max = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
        elif arr[i] > max:
            max = arr[i]

    #initialize buckets
    #O(k)

    bucket_count = math.floor((max - min) / bucket_size) + 1
    buckets = []
    for i in range(0, bucket_count):
        buckets.append([])

    #distribute input array values into buckets
    #O(n)

    for i in range(0, len(arr)):
        buckets[math.floor((arr[i] - min) / bucket_size)].append(arr[i])

    #sort buckets and place back into input array
    #O(n)

    arr = []
    for i in range(0, len(buckets)):
        helpersort(buckets[i])
        for j in range(0, len(buckets[i])):
            arr.append(buckets[i][j])
            yield arr

"""
Sorting algorithm where the idea is to sort the elements by
the least significant digit before then moving on to the next
most significant digit

Average O(kn) runtime where k is the number of bits
required to represent the largest element
"""
def radixsort(arr):

    #function to do counting sort, where you count
    #the number of values with distinct key values
    #where exp1 is the sigfig place
    def countingsort(arr, place):

        n = len(arr)
        #sorted output array
        output = [0] * (n)
        count = [0] * (10)

        #store counts of appearances
        for i in range(0, n):
            index = arr[i] // place
            count[(index) % 10] += 1

        #change count[i] so that it contains the
        #position of the digit in output array

        for i in range(1, 10):
            count[i] += count[i-1]

        #build output array
        i = n - 1
        while i >= 0:
            index = (arr[i] // place)
            output[count[(index) % 10] - 1] = arr[i]
            count[(index) % 10] -= 1
            i -= 1

        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]
            yield arr

    max_val = max(arr)
    place = 1
    while max_val // place > 0:
        yield from countingsort(arr, place)
        place *= 10

def generateArray(length):
    arr = []
    for i in range(0, length):
        arr.append(2*i)
    random.shuffle(arr)
    return arr

def optionToFunction(argument, arr):
    switcher = {
        'bubble': bubblesort,
        'insertion': insertionsort,
        'selection': selectionsort,
        'quick': quicksort,
        'merge': mergesort,
        'heap': heapsort,
        'bucket': bucketsort,
        'radix': radixsort
    }
    function = switcher.get(argument, lambda: "Invalid month")
    if argument == 'quick':
        return function(arr, 0, len(arr)-1)
    else:
        return function(arr)

def main():

    p = ap.ArgumentParser()
    p.add_argument('sort', type=str, choices=['bubble', 'insertion', 'selection', 'quick', 'merge', 'heap', 'bucket', 'radix'], \
        help='type of sorting algorithm')
    ARGS = p.parse_args()

    N = 100
    fig, ax = plt.subplots()
    ax.set_title(ARGS.sort + " sort")
    arr = generateArray(N)
    generator = optionToFunction(ARGS.sort, arr)
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(2.1 * N))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]
    def update_fig(arr, rects, iteration):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=generator, interval=1,
        repeat=False)
    plt.show()

if __name__ == "__main__":
    main()