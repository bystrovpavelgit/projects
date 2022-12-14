"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def check_age(age):
    """ function check_age """
    if age < 7:
        return "учится в детском саду"
    if 18 >= age >= 7:
        return "учится в школе"
    if 23 >= age > 18:
        return "учится в ВУЗе"
    if age > 23:
        return "работает"

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = int(input("Возраст? "))
    result = check_age(age)
    print(result)

if __name__ == "__main__":
    main()
