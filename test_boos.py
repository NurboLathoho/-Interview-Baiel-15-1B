# 8 задание 
def even_numbers(numbers):

  even_list = []
  for number in numbers:
    if number % 2 == 0:
      even_list.append(number)
  return even_list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_list = even_numbers(numbers)
print(f"Исходный список: {numbers}")
print(f"Список четных чисел: {even_numbers_list}")

# 9 Задание 

def is_subset(set1, set2):
  return set1.issubset(set2)

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(is_subset(set1, set2))

# 10 Задание 

def delete(num):
  return set(num)

numbers = [1, 2, 2, 3, 4, 4, 5]
numbers_2 = delete(numbers)
print(numbers_2) 
