# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

def func(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key  # Если значение хешируемо, используем его как ключ
        except TypeError:
            result[str(value)] = key  # Если нет, используем строковое представление
    return result

print(func(a=10, b="hello", c=(1, 2, 3)))  
# {10: 'a', 'hello': 'b', (1, 2, 3): 'c'}

print(func(x=[1, 2, 3], y={"key": "value"}, z={1, 2, 3}))  
# {'[1, 2, 3]': 'x', "{'key': 'value'}": 'y', '{1, 2, 3}': 'z'}
