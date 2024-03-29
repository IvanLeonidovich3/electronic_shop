import csv

import src


class InstantiateCSVError:
    def __init__(self):
        self.message = "Файл item.csv поврежден"


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if issubclass(other.__class__, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError('можно слкадывать только с подклассами Item')

    @property
    def name(self):

        return self.__name

    @name.setter
    def name(self, name):

        if 0 < len(name) < 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        """метод создания экземпляров класса из файла items.csv"""

        cls.all = []
        with open(src.items.csv, newline='', encoding='windows-1251', errors='replace') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row["name"], row["price"], row["quantity"])
        try:
            with open(src.items.csv, 'r', encoding="windows-1251") as csv_file:
                csv_data: csv.DictReader = csv.DictReader(csv_file)
                csv_data_list = list(csv_data)
                for line in csv_data_list:
                    if (line.get('name') and line.get('price') and line.get('quantity')) in ['', None]:
                        raise InstantiateCSVError
        except FileNotFoundError:
            print('Отсутствует файл items.csv')
            return 'Отсутствует файл items.csv'
        except InstantiateCSVError as exp:
            print(exp.message)
            return exp.message
        else:
            return True

    @staticmethod
    def string_to_number(string_num):
        """возвращает целое число из строки"""

        if isinstance(string_num, str):
            return round(float(string_num.split('.')[0]))
        else:
            print('Данная запись не является числом-строкой')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        """

        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """

        self.price = self.price * self.pay_rate
