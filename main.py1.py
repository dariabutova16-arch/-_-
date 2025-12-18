# Максимальний за модулем елемент масиву
def max_abs_element(arr):
    max_elem = arr[0]
    for i in range(1, len(arr)):
        if abs(arr[i]) > abs(max_elem):
            max_elem = arr[i]
    return max_elem


# Сума елементів між першим і другим додатними
def sum_between_positives(arr):
    first = None
    second = None

    for i in range(len(arr)):
        if arr[i] > 0:
            if first is None:
                first = i
            else:
                second = i
                break

    if first is None or second is None or second == first + 1:
        return 0

    s = 0
    for i in range(first + 1, second):
        s += arr[i]

    return s


# Переміщення нульових елементів у кінець
def move_zeros_to_end(arr):
    result = []
    zeros = 0

    for x in arr:
        if x == 0:
            zeros += 1
        else:
            result.append(x)

    for i in range(zeros):
        result.append(0)

    return result


# Головна програма
def main():
    n = int(input("Введіть кількість елементів масиву: "))
    arr = []

    for i in range(n):
        arr.append(float(input(f"Введіть елемент {i + 1}: ")))

    print("Початковий масив:", arr)
    print("Максимальний за модулем елемент:", max_abs_element(arr))
    print("Сума між першим і другим додатними:",
          sum_between_positives(arr))
    print("Масив після перенесення нулів:",
          move_zeros_to_end(arr))


main()
