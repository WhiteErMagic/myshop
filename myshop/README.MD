Первое задание first_task.py

    def print_function(arg):
        def do_generator():
            ind = 1
            for i in range(arg):
                for x in range(i+1):
                    if ind <= arg:
                        yield str(i+1)
                        ind += 1
                    else:
                        break
        print("".join(do_generator()))

    print_function(10)

Второе задание

    Рид ми короткое
    2 приложения goods - категории и товары и basket - корзина покупателя
    для разделения картинок товаров по размерам сделана таблица size,
    в ней хранятся варианту размеров, которые указываются в таблице самих картинок
    таблицы: Category - категории, Good - товары, Price - цены товаров,
    GoodImage - картинки товаров, size - размеры картинок, Basket - корзина,
    BasketGood - товары корзины.
