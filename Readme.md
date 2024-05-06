# Тема 9. Концепции и принципы ООП
Отчет по Теме #9 выполнил:
- Гребенщиков Евгений Олегович
- ИНО ОЗБ ПОАС-22-2

| Задание    | Сам_раб |
|------------|---------|
| Задание  | +       |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа
### Задание Садовник и помидоры.

```python
class Tomato:
    # Словарь стадий созревания помидоров
    states = {0: 'отсутствует', 1: 'цветение', 2: 'зеленый', 3: 'красный'}

    def __init__(self, index):
        # Каждый помидор имеет уникальный индекс и начальную стадию созревания
        self.index = index
        self.state = 0

    def grow(self):
        # Переводит помидор на следующую стадию созревания, если это возможно
        if self.state < len(self.states) - 1:
            self.state += 1

    def is_ripe(self):
        # Проверяет, достиг ли помидор стадии "красный"
        return self.state == 3


class TomatoBush:
    def __init__(self, num_tomatoes):
        # Создает список помидоров на кусте
        self.tomatoes = [Tomato(i) for i in range(num_tomatoes)]

    def grow_all(self):
        # Заставляет каждый помидор на кусте расти
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        # Проверяет, все ли помидоры на кусте созрели
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        # Очищает список помидоров после сбора урожая
        self.tomatoes = []


class Gardener:
    def __init__(self, name, tomato_bush):
        # Садовник имеет имя и куст, за которым он ухаживает
        self.name = name
        self.plant = tomato_bush

    def work(self):
        # Работа садовника заключается в уходе за кустом, т.е. в его росте
        self.plant.grow_all()

    def harvest(self):
        # Садовник собирает урожай, если все помидоры созрели
        if self.plant.all_are_ripe():
            self.plant.give_away_all()
            print("Урожай собран.")
        else:
            print("Не все помидоры созрели. Нужно еще немного подождать.")

    @staticmethod
    def knowledge_base():
        # Статический метод предоставляет общую информацию о садоводстве
        print("Садоводство - это отрасль сельского хозяйства, занимающаяся выращиванием овощей, фруктов, ягод, \n"
              "цветов и других растений на садовых участках. Основная цель садоводства заключается в получении \n"
              "качественных и вкусных продуктов для собственного потребления или сбыта. При садоводстве важную роль \n"
              "играют такие аспекты, как выбор и подготовка почвы, посадка растений, уход за ними (полив, подкормка, \n"
              "обрезка) и борьба с вредителями и болезнями.")


Gardener.knowledge_base()

bush = TomatoBush(5)
gardener = Gardener("Евгений", bush)

gardener.work()
gardener.harvest()

while not bush.all_are_ripe():
    gardener.work()

gardener.harvest()
```
### Результат
![Lab9](./img/img.png)