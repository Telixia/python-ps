"""
Refer: https://www.codesdope.com/course/data-structures-heap/
"""
heap_size = 10


# function to get a right child of a node
def get_right_child(A, index):
    if 2 * index + 1 < len(A) and index >= 1:
        return 2 * index + 1
    return -1


# function to get the left child of a node
def get_left_child(A, index):
    if 2 * index < len(A) and index >= 1:
        return 2 * index
    return -1


# function to get the parent of a node
def get_parent(A, index):
    if index > 1 and index < len(A):
        return index // 2
    return -1


def max_heapify(A, index):
    left_child_index = get_left_child(A, index)
    right_child_index = get_right_child(A, index)

    # finding the largest among left child, right child and current index
    largest = index

    if left_child_index <= heap_size and left_child_index > 0:
        if A[left_child_index] > A[largest]:
            largest = left_child_index

    if right_child_index <= heap_size and right_child_index > 0:
        if A[right_child_index] > A[largest]:
            largest = right_child_index

    # largest is not the node, node is not a heap
    if largest != index:
        A[index], A[largest] = A[largest], A[index]
        max_heapify(A, largest)


def build_max_heap(A):
    for i in range(heap_size // 2, 0, -1):
        max_heapify(A, i)


if __name__ == '__main__':
    A = [0, 15, 20, 7, 9, 5, 8, 6, 10, 2, 1]
    build_max_heap(A)
    print(A[1:heap_size + 1])
