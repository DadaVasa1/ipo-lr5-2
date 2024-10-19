
str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")

str1 = sorted(str1.lower()) # сортирует по алфавиту
str2 = sorted(str2.lower())

if str1 == str2:
  print("Строки являются анаграммами")
else:
  print("Строки не являются анаграммами")
