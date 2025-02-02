from direct.showbase.ShowBase import ShowBase
from random import uniform
from panda3d.core import Vec3
from random import randint
import sys


class MyApp(ShowBase):
    def __init__(self):
        super().__init__()
        self.camera.setHpr(0, -45, 0)  # Нахиляємо камеру на 45 градусів вперед по осі X


        # Завантажуємо куб-гравець
        self.cube = self.loader.loadModel("models/box")  # Завантажуємо стандартну модель куба
        self.cube.setTexture(self.loader.loadTexture("crc.png"))  
        self.cube.reparentTo(self.render)  # Додаємо куб до сцени
        self.cube.setScale(0.5)  # Масштаб куба
        self.cube.setPos(0, 10, 0)  # Початкова позиція куба
        

        # Створюємо другий куб
        self.cube2 = self.loader.loadModel("models/box")  # Завантажуємо стандартну модель куба
        self.cube2.reparentTo(self.render)  # Додаємо куб до сцени
        self.cube2.setScale(0.5)  # Масштаб куба
        self.cube2.setPos(0,40,0)  # Початкова позиція куба
        self.cube2.setColor(1,0,1,1)

        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False



        # Обробка натискання клавіш
        self.accept("arrow_up", self.set_move_up, [True])
        self.accept("arrow_up-up", self.set_move_up, [False])
        self.accept("arrow_down", self.set_move_down, [True])
        self.accept("arrow_down-up", self.set_move_down, [False])
        self.accept("arrow_left", self.set_move_left, [True])
        self.accept("arrow_left-up", self.set_move_left, [False])
        self.accept("arrow_right", self.set_move_right, [True])
        self.accept("arrow_right-up", self.set_move_right, [False])


        # Додавання задачі для постійного оновлення гри
        self.taskMgr.add(self.update_game, "UpdateGame")
    

    def set_move_up(self, value):
        self.move_up = value

    def set_move_down(self, value):
        self.move_down = value

    def set_move_left(self, value):
        self.move_left = value

    def set_move_right(self, value):
        self.move_right = value

    def update_game(self, task):

        # # Завантажуємо звук
        # self.collision_sound = self.loader.loadSfx("sounds/collision.wav")
        # self.collision_sound.play()  # При зіткненні з об'єктом

        # Завантажуємо текстуру
        

        dt = globalClock.getDt()

        # Рух куба-гравця
        move_speed = 5
        if self.move_up:
            self.cube.setZ(self.cube.getZ() + move_speed * dt)
        if self.move_down:
            self.cube.setZ(self.cube.getZ() - move_speed * dt)
        if self.move_left:
            self.cube.setX(self.cube.getX() - move_speed * dt)
        if self.move_right:
            self.cube.setX(self.cube.getX() + move_speed * dt)

        self.cube2.setY(self.cube2.getY() - move_speed * dt)
        if self.cube2.getY() < -20:
            sys.exit()

        vector1 = Vec3(self.cube.getPos())
        vector2 = Vec3(self.cube2.getPos())

        distanse = (vector1-vector2).length()        
        if distanse < 0.5:
            self.cube2.setPos(randint(-5,5),40,randint(-5,5))


        return task.cont  # Продовжуємо задачу

# Створюємо і запускаємо додаток
app = MyApp()
app.run()
