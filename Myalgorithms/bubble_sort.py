def bubble_sort(list):
    for number in list:
        print(list[number])
        for number2 in list:
            print(list[number2])
            if list[number] > list[number2+1]:
                list[number], list[number2] = list[number2+1], list[number]
                print(list[number], list[number2])
            else:
                number += 1
                break
    return list


print(bubble_sort(list = [1, 3, 2, 5, 7, 6, 8]))