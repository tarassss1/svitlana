from direct.showbase.ShowBase import ShowBase
from random import uniform
from panda3d.core import Vec3

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()

        # Завантажуємо куб-гравець
        self.cube = self.loader.loadModel("models/box")  # Завантажуємо стандартну модель куба
        self.cube.reparentTo(self.render)  # Додаємо куб до сцени
        self.cube.setScale(0.5)  # Масштаб куба
        self.cube.setPos(0, 10, 0)  # Початкова позиція куба

        # Завантажуємо квадрат, який летить по осі X
        self.square = self.loader.loadModel("models/box")  # Використовуємо такий же куб для квадрату
        self.square.reparentTo(self.render)
        self.square.setScale(0.3)  # Зменшуємо розмір квадрата
        self.square.setColor(1, 0, 0, 1)  # Червоний колір
        self.square.setPos(10, 10, 0)  # Початкова позиція квадрата

        # Створюємо змінні для руху
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

        # Обробка натискання клавіш
        self.accept("arrow_up", self.set_move_up, [True])
        self.accept("arrow_up-up", self.set_move_up, [False])

        # Додавання задачі для постійного оновлення гри
        self.taskMgr.add(self.update_game, "UpdateGame")

    def set_move_up(self, value):
        self.move_up = value

    def update_game(self, task):
        """Оновлення стану гри кожен кадр."""
        dt = globalClock.getDt()

        # Рух куба-гравця
        move_speed = 5
        if self.move_up:
            self.cube.setY(self.cube.getY() + move_speed * dt)



        return task.cont  # Продовжуємо задачу

# Створюємо і запускаємо додаток
app = MyApp()
app.run()
