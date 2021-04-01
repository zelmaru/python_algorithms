arr = [3, 1, 5, 2, 8]

print(arr.pop(2))


def find_smallest(arr):
  smallest = arr[0]
  smallest_i = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_i = i
  return smallest_i

def selection_sort(arr):
  new_arr = []
  for i in range(len(arr)):
    smallest = find_smallest(arr)
    new_arr.append(arr.pop(smallest)) # print(arr.pop(1)) prints the element with the index and behind the scenes it removes the element from the array - print(arr) prints the new array
  return new_arr

print(selection_sort(arr))

    

