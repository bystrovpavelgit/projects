"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def check_str(str1, str2):
    """ function check_str """
    if not isinstance(str1, str) or not isinstance(str2, str):
        return 0
    if str1 == str2:
        return 1
    if len(str1) > len(str2):
        return 2
    if str2 == "learn":
        return 3


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(check_str(1, "learn"))
    print(check_str("l", "l"))
    print(check_str("------", 2))
    print(check_str("--", "learn"))
    print(check_str("pass pass", "learn"))
    
if __name__ == "__main__":
    main()
