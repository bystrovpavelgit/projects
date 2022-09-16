"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    import csv

    data = [{"name":"Ivan", "age":33, "job":"a"},
           {"name":"Petr", "age":43, "job":"b"},
           {"name":"Sidor", "age":30, "job":"c"},
           {"name":"Fedor", "age":40, "job":"d"}]

    with open("people.csv", "w", encoding="utf-8") as f:
        fields = ["name", "age", "job"]
        cc = csv.DictWriter(f, fieldnames=fields) #, delimiter=";"
        cc.writeheader()
        for row in data:
            cc.writerow(row)
    print("ok")

if __name__ == "__main__":
    main()
