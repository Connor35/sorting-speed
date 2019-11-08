################################
################################
################################
################################
# Timing Common Sorting Algorithms
# Connor Whitbey

import random
import time

################################
################################
# MERGESORT
def mergesort(a):
	if(len(a) == 1):
		return a
	else:
		left = a[:len(a)//2]
		right = a[len(a)//2:]

		left = mergesort(left)
		right = mergesort(right)

		sorted_a = _merge(left, right)
		return sorted_a


def _merge(left, right):
	a = []
	left_idx = 0
	right_idx = 0
	while (left_idx < len(left) or right_idx < len(right)):
		if (left_idx == len(left)):
			a.append(right[right_idx])
			right_idx += 1
		elif (right_idx == len(right)):
			a.append(left[left_idx])
			left_idx += 1
		elif left[left_idx] <= right[right_idx]:
			a.append(left[left_idx])
			left_idx += 1
		else:
			a.append(right[right_idx])
			right_idx += 1

	return a
################################
################################


################################
################################
# QUICKSORT
def quicksort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)
################################
################################


################################
################################
# INSERTION SORT
def insertionsort(a):
    len_a = len(a)
    if len_a == 0 or len_a == 1:
        return a
    arr = []
    for i in range(0, len_a):
        element = a[i]
        arr = _insert(arr, element)
    return arr

def _insert(arr, element):
    len_arr = len(arr)
    if len_arr == 0:
        arr.append(element)
        return arr
    for i in range(0, len_arr):
        if element < arr[i]:
            arr.insert(i, element)
            return arr
    arr.append(element)
    return arr

################################
################################


################################
################################
# DRIVER

if __name__ == "__main__":

    #### create random arrays ####
    a1, b1, c1, d1 = [], [], [], []
    a2, b2, c2, d2 = [], [], [], []
    a3, b3, c3, d3 = [], [], [], []

    print("\nCreating randomized arrays...")

    for i in range(1, 100):
        element = random.randrange(1000)
        a1.append(element)
        a2.append(element)
        a3.append(element)
    print("\t'a' created (length 100)")

    for i in range(1, 1000):
        element = random.randrange(1000)
        b1.append(element)
        b2.append(element)
        b3.append(element)
    print("\t'b' created (length 1000)")

    for i in range(1, 10000):
        element = random.randrange(1000)
        c1.append(element)
        c2.append(element)
        c3.append(element)
    print("\t'c' created (length 10000)")

    for i in range(1, 100000):
        element = random.randrange(1000)
        d1.append(element)
        d2.append(element)
        d3.append(element)
    print("\t'd' created (length 100000)")

    print("...all arrays created")
    print("\n\tTIMING RESULTS\n")

    #### create timing variables ####
    time_1, time_2 = 0, 0

    qsort_time_a = 0
    qsort_time_b = 0
    qsort_time_c = 0
    qsort_time_d = 0

    msort_time_a = 0
    msort_time_b = 0
    msort_time_c = 0
    msort_time_d = 0

    isort_time_a = 0
    isort_time_b = 0
    isort_time_c = 0
    isort_time_d = 0

    #### time quicksort ####
    time_1 = time.time()
    a1 = quicksort(a1)
    time_2 = time.time()
    qsort_time_a = time_2 - time_1

    time_1 = time.time()
    b1 = quicksort(b1)
    time_2 = time.time()
    qsort_time_b = time_2 - time_1

    time_1 = time.time()
    c1 = quicksort(c1)
    time_2 = time.time()
    qsort_time_c = time_2 - time_1

    time_1 = time.time()
    d1 = quicksort(d1)
    time_2 = time.time()
    qsort_time_d = time_2 - time_1

    #### time mergesort ####
    time_1 = time.time()
    a2 = mergesort(a2)
    time_2 = time.time()
    msort_time_a = time_2 - time_1

    time_1 = time.time()
    b2 = mergesort(b2)
    time_2 = time.time()
    msort_time_b = time_2 - time_1

    time_1 = time.time()
    c2 = mergesort(c2)
    time_2 = time.time()
    msort_time_c = time_2 - time_1

    time_1 = time.time()
    d2 = mergesort(d2)
    time_2 = time.time()
    msort_time_d = time_2 - time_1

    #### time insertionsort ####
    time_1 = time.time()
    a3 = insertionsort(a3)
    time_2 = time.time()
    isort_time_a = time_2 - time_1

    time_1 = time.time()
    b3 = insertionsort(b3)
    time_2 = time.time()
    isort_time_b = time_2 - time_1

    time_1 = time.time()
    c3 = insertionsort(c3)
    time_2 = time.time()
    isort_time_c = time_2 - time_1

    # 100,000 elements takes approximately 5 minutes
    # time_1 = time.time()
    # d3 = insertionsort(d3)
    # time_2 = time.time()
    # isort_time_d = time_2 - time_1

    #### print results####
    print("Quicksort:")
    print("'a1' time: " + str(round(qsort_time_a, 4)))
    print("'b1' time: " + str(round(qsort_time_b, 4)))
    print("'c1' time: " + str(round(qsort_time_c, 4)))
    print("'d1' time: " + str(round(qsort_time_d, 4)))
    print("")

    print("Mergesort:")
    print("'a2' time: " + str(round(msort_time_a, 4)))
    print("'b2' time: " + str(round(msort_time_b, 4)))
    print("'c2' time: " + str(round(msort_time_c, 4)))
    print("'d2' time: " + str(round(msort_time_d, 4)))
    print("")

    print("Insertionsort:")
    print("'a3' time: " + str(round(isort_time_a, 4)))
    print("'b3' time: " + str(round(isort_time_b, 4)))
    print("'c3' time: " + str(round(isort_time_c, 4)))
    print("'d3' time: -too slow-")
    print("")

################################
################################

################################
################################
################################
################################
# EOF