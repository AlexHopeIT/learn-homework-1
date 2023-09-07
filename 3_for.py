"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

product_list = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def count_sold(phone_sold):
    sold_sum = 0
    for sold in phone_sold:
        sold_sum += sold
    spld_avg = round(sold_sum / len(phone_sold), 2)
    return spld_avg

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    avg_sold_all = 0

    for one_phone in product_list:
      phone_sold_avg = count_sold(one_phone['items_sold'])
      print(f'Среднее количество продаж для {one_phone["product"]}: {phone_sold_avg}')
      print(f'Суммарное количество продаж для {one_phone["product"]}: {round(phone_sold_avg * len(one_phone["items_sold"]))}')
      avg_sold_all += phone_sold_avg

    print(f'Cуммарное количество продаж всех товаров: {round(avg_sold_all * len(one_phone["items_sold"]))}')
    print(f'Среднее количество продаж всех товаров: {avg_sold_all / len(product_list)}')

if __name__ == "__main__":
    main()
