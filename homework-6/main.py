from src.item import Item
from src.pathich import Csv_path

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv(Csv_path)
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(Csv_path)
    # InstantiateCSVError: Файл item.csv поврежден
