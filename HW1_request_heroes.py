from superhero_api import Superhero

"""
Программа выводит супергероя с максимальным интеллектом.
Решено выполнить через классы, где каждый супергерой - это экземпляр класс.
Основные функции в модуле superhero_api
"""
hulk = Superhero('Hulk')
captain_america = Superhero('Captain America')
thanos = Superhero('Thanos')
spider_man = Superhero('Spider-Man')
ded_moroz = Superhero('Дед-Мороз')

hulk.get_intelligence()
captain_america.get_intelligence()
thanos.get_intelligence()
spider_man.get_intelligence()
ded_moroz.get_intelligence()


def the_most_intel(*args):
    # сравниваем интеллекты героев (любое число)
    list_of_heroes = [*args]
    # удаляем несуществующих супергероев из списка (по умолчанию у несуществующего героя интеллект 0)
    for i in reversed(list_of_heroes):
        if i.intelligence == 0:
            list_of_heroes.remove(i)
    list_of_heroes.sort(key=lambda x: x.intelligence, reverse=True)
    if not list_of_heroes:
        # проверка на отсутствие данных интеллекта у всех супергероев
        print('К сожалению, ни у одного из супергероев невозможно узнать параметры')
        return
    print(f"Среди {' ,'.join([x.name for x in list_of_heroes])} "
          f"самый умный: {list_of_heroes[0].name} с интеллектом {list_of_heroes[0].intelligence}")
    return list_of_heroes[0]


if __name__ == "__main__":
    the_most_intel(hulk, captain_america, spider_man, thanos, ded_moroz)  # протестируем с несуществующим супергероем
