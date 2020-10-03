a = [1,2]

def is_sorted_and_how(arr):
  if arr == sorted(arr):
      return "yes, ascending"
  elif arr == sorted(arr, reverse=True):
      return "yes, descending"
  return "no"

print(is_sorted_and_how(a))