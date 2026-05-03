test = ["1", "2", "3", 5, "5", "6", "7", "8", "9"]

# if isinstance(test, list):
#     for i in test:
#         if not isinstance(i, str):
#             raise TypeError("Должен быть список строк!!! 🤬🤬🤬")
#     answer = test


"""
    Функция all() - возращает True, если все элементы вернули True.
    Если all() находит хотя бы один False он сразу останавливается.
"""
if all(isinstance(i, str) for i in test):
    print("Выполнилось")
else:
    print("Не выполнилось")


"""
    Функция any() - возращает True, если хотя бы один элемент вернул True.
    Если any() находит хотя бы один True он сразу останавливается.
"""
if any(isinstance(i, int) for i in test):
    print("Выполнилось")
else:
    print("Не выполнилось")
