

def binary_search(list, item):
  low = 0
  high = len(list) - 1

  while low <= high:  # while we did not eliminate it to 1 element
    mid = (low + high) // 2 #get answer w/o the remainder
    guess = list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else: low = mid + 1
  return None #if no item found

my_list = [1, 2, 3, 4, 5, 6]
print(binary_search(my_list, 6))
print(binary_search(my_list, 0))
