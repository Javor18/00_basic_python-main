# Write a Python program to filter the height and width of students, which are stored in a dictionary.
# Original Dictionary:
# {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}

dic = eval(input())

# TODO: To make it more readable, you can split into multiple lines
sort_dic = {name: (height, weight) for name, (height, weight) in dic.items() if height >= 6 and weight >= 70}

sort_dic = {
  name: (height, weight)
  for name, (height, weight) in dic.items()
  if height >= 6 and weight >= 70
}

print(sort_dic)