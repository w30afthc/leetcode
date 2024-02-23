"""
title : 常见排序算法
source : https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95
file:///D:/Program%20Files/Python311/Doc/html-zh-cn/howto/sorting.html
https://mp.weixin.qq.com/s/QvHqeVoeaexLyqIp7kdc1Q
"""

import random


def bubble_sort(arr):
    """冒泡排序

    比较两个相邻的元素，小在前，大在后
    一轮比较后较小的元素前进了一位，最大的元素在最后
    继续比较第二轮将第二大的元素放置在倒数第二位
    重复进行直到最后两个元素
    平均时间复杂度： O(n*n)
    最好情况： O(n)
    最坏情况： O(n*n)
    空间复杂度： O(1)
    排序方式： In-place
    稳定性： 稳定
    """
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def bubble_sort2(arr):
    """冒泡排序-优化2

    设置一个标记变量，记录当前循环是否发生了交换
    若未发生交换则表示已经全部有序，可以结束排序
    平均时间复杂度： O(n*n)
    最好情况： O(n)
    最坏情况： O(n*n)
    空间复杂度： O(1)
    排序方式： In-place
    稳定性： 稳定
    """
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def bubble_sort3(arr):
    """冒泡排序-优化3

    设置一个变量记录最后一次发生交换的位置
    此位置之后的元素因为没有发生交换，所以均已有序，下次循环中无需遍历
    平均时间复杂度： O(n*n)
    最好情况： O(n)
    最坏情况： O(n*n)
    空间复杂度： O(1)
    排序方式： In-place
    稳定性： 稳定
    """
    last_swap_index = len(arr) - 1
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(last_swap_index):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                last_swap_index = j + 1
        if not swapped:
            break


def selection_sort(arr):
    """选择排序

    选出最小（大）的元素，放在最前面
    再从剩下的元素中选择次最小（大）的元素，放在第二个位置
    重复上述过程直至最后两个元素
    平均时间复杂度： O(n*n)
    最好情况： O(n*n)
    最坏情况： O(n*n)
    空间复杂度： O(1)
    排序方式： In-place
    稳定性： 不稳定
    """
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def selection_sort2(arr):
    """选择排序-二元选择排序

    每次遍历从未排序的中间找出最小和最大两个值，分别交换到首尾
    这样只需要遍历一半的数组长度即可完成排序
    平均时间复杂度： O(n*n)
    最好情况： O(n*n)
    最坏情况： O(n*n)
    空间复杂度： O(1)
    排序方式： In-place
    稳定性： 不稳定
    """
    for i in range(len(arr)//2):
        min_index = i
        max_index = i
        for j in range(i + 1, len(arr)-i):
            if arr[min_index] > arr[j]:
                min_index = j
            if arr[max_index] < arr[j]:
                max_index = j
        if min_index == max_index:
            break
        arr[i], arr[min_index] = arr[min_index], arr[i]
        if max_index == i:
            max_index = min_index
        arr[len(arr)-1-i], arr[max_index] = arr[max_index], arr[len(arr)-1-i]


def insert_sort1(arr):
    """插入排序-交换法

    将前面的元素视为已经排好序的序列（初始 1 个）
    每次从后面尚未排序的序列中拿出首个元素 current，依次与前面已经排序好的元素倒叙比较
    若 current 小于比较的元素，则交换彼此位置
    若 current 不小于比较元素，则当前位置就是 current 应在的位置
    平均时间复杂度： O(n*n)
    最好情况： O(n)
    最坏情况： O(n*n)
    空间复杂度： O(1)
    排序方式： In-place
    稳定性： 稳定
    """
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insert_sort2(arr):
    """插入排序-移动法

    将前面的元素视为已经排好序的序列（初始 1 个）
    每次从后面尚未排序的序列中拿出首个元素 current，依次与前面已经排序好的元素倒叙的比较
    若 current 小于前面的元素，则比较的元素后退一位
    若 current 不小于比较元素，则比较元素的下一位就应当是 current
    平均时间复杂度： O(n*n)
    最好情况： O(n)
    最坏情况： O(n*n)
    空间复杂度： O(1)
    排序方式： In-place
    稳定性： 稳定
    """
    for i in range(1, len(arr)):
        current = arr[i]
        pre_index = i - 1
        while pre_index >= 0 and arr[pre_index] > current:
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index + 1] = current


def shell_sort(arr):
    """希尔排序

    """
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap):
            j = i + gap
            while j < len(arr):
                current = arr[j]
                pre_index = j - gap
                while pre_index >= i and current < arr[pre_index]:
                    arr[pre_index + gap] = arr[pre_index]
                    pre_index -= gap
                arr[pre_index + gap] = current
                j += gap
        gap //= 2


def shell_sort2(arr):
    """希尔排序- Shell 增量序列

    在插入排序的基础上，每次与前 gap 个元素比较后换位
    gap 取 2 * gap
    尽可能快地将较小的数搬运到前方，将较大的数搬运至后方
    平均时间复杂度： O(n*log n) TODO
    最好情况： O(n*log n*log n)
    最坏情况： O(n*log n*log n)
    空间复杂度： O(1)
    排序方式： In-place
    稳定性： 不稳定
    """
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            current = arr[i]
            pre_index = i - gap
            while pre_index >= 0 and arr[pre_index] > current:
                arr[pre_index + gap] = arr[pre_index]
                pre_index -= gap
            arr[pre_index + gap] = current
        gap = gap // 2


def shell_sort3(arr):
    """希尔排序- Knuth 增量序列

    在插入排序的基础上，每次与前 gap 个元素比较后换位
    gap 取 3 * gap + 1
    尽可能快地将较小的数搬运到前方，将较大的数搬运至后方
    平均时间复杂度： O(n*log n) TODO
    最好情况： O(n*log n*log n)
    最坏情况： O(n*log n*log n)
    空间复杂度： O(1)
    排序方式： In-place
    稳定性： 不稳定
    """
    gap = 1
    while gap < len(arr) / 3:
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap = gap // 3


def merge_sort(arr):
    """归并排序

    假设数组左右两边均已排序好，使用双指针分别从左右两个数组中挑选最小的元素放入新的数组中
    递归解决左右两个数组使其排序
    平均时间复杂度： O(n*log n) TODO
    最好情况： O(n*log)
    最坏情况： O(n*log)
    空间复杂度： O(n)
    排序方式： Out-place
    稳定性： 稳定
    """
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left, right = arr[0:middle], arr[middle:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result


def quick_sort(arr, left=None, right=None):
    """快速排序

    从数列中挑选一个基准 pivot，遍历数组，比基准小的放在基准前，比基准大的放在基准后
    递归的把基准前后的的子数组执行上述操作
    平均时间复杂度： O(n*log n) TODO
    最好情况： O(n*log)
    最坏情况： O(n*n)
    空间复杂度： O(log n)
    排序方式： In-place
    稳定性： 不稳定 TODO
    """
    left = 0 if left is None else left
    right = len(arr) - 1 if right is None else right
    if left < right:
        partition_index = partition(arr, left, right)
        quick_sort(arr, left, partition_index - 1)
        quick_sort(arr, partition_index + 1, right)


def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[pivot] > arr[i]:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1
        i += 1
    arr[pivot], arr[index-1] = arr[index-1], arr[pivot]
    return index - 1


def heap_sort(arr):
    """堆排序


    """
    build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i)


def build_max_heap(arr):
    for i in range(len(arr) // 2 - 1, 0, -1):
        max_heapify(arr, i, len(arr))


def max_heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size)


if __name__ == "__main__":
    list1 = random.choices(list(range(10)), k=random.randint(1, 20))
    # random.shuffle(list1)
    # list1 =  [6, 2, 1, 3, 5, 4]

    print("Before sort: ", list1)
    heap_sort(list1)
    print("After sort: ", list1)
