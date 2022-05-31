from superhero_api import Superhero

hulk = Superhero('Hulk')
captain_america = Superhero('Captain America')
thanos = Superhero('Thanos')
spider_man = Superhero('Spider-Man')
error = Superhero('error')

hulk.get_intelligence()
captain_america.get_intelligence()
thanos.get_intelligence()
spider_man.get_intelligence()
error.get_intelligence()


def the_most_intel(*args):
    list_of_heroes = [*args]
    # удаляем несуществующих супергероев из списка
    for i in reversed(list_of_heroes):
        if i.intelligence == 0:
            list_of_heroes.remove(i)
    list_of_heroes.sort(key=lambda x: x.intelligence, reverse=True)
    if not list_of_heroes:
        print('К сожалению, ни у одного из супергероев невозможно узнать параметры')
        return
    print(f"Среди {' ,'.join([x.name for x in list_of_heroes])} "
          f"самый умный: {list_of_heroes[0].name} с интеллектом {list_of_heroes[0].intelligence}")
    return list_of_heroes[0]


if __name__ == "__main__":
    the_most_intel(hulk, captain_america, spider_man, thanos, error)
