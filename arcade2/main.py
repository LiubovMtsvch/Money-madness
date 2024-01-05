import arcade
import random

import arcade.gui
import arcade.gui.widgets.buttons
import arcade.gui.widgets.layout



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
SCREEN_TITLE = "MoneyMadness"

SCENE_MENU = 'SCENE_MENU'
SCENE_GAME = 'SCENE_GAME'



COIN_COUNT = 100

ENEMY_COUNT = 100



class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

class Enemy(arcade.Sprite):

    def reset_pos(self):

        self.center_y = random.randrange(SCREEN_HEIGHT + 10,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        self.center_y -= 1

        if self.top < 0:
            self.reset_pos()



class Coin(arcade.Sprite):

    def reset_pos(self):

        self.center_y = random.randrange(SCREEN_HEIGHT + 10,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        self.center_y -= 1

        if self.top < 0:
            self.reset_pos()





class MyGame(arcade.Window):


    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        #self.music = arcade.load_sound(':resources:music/funkyrobot.mp3')
        #self.media_player = self.music.play()

        self.scene = SCENE_MENU
        self.scene = SCENE_MENU


        self.enemy_sprite_list = None



        self.coin_sprite_list = None
        self.pers = None

        self.score = 0

        self.sec_score = 10


        self.pers = arcade.Sprite('img/ghost.png', 0.1)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()


        arcade.set_background_color(arcade.color.BLIZZARD_BLUE)

        self.v_box = arcade.gui.UIBoxLayout()


        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(start_button)


        quit_button = QuitButton(text="Quit", width=200)
        self.v_box.add(quit_button)

        start_button.on_click = self.on_click_start


        ui_anchor_layout = arcade.gui.widgets.layout.UIAnchorLayout()
        ui_anchor_layout.add(child=self.v_box, anchor_x="center_x", anchor_y="center_y")

        self.manager.add(ui_anchor_layout)



    def setup(self):


        self.pers = arcade.SpriteList()
        self.enemy_sprite_list = arcade.SpriteList()
        self.coin_sprite_list = arcade.SpriteList()

        self.score = 0

        self.sec_score = 10



        for i in range(1, 25):
            enemy = Enemy("img/skull.png", 0.06)
            enemy.center_x = 1600
            enemy.center_y = random.randrange(SCREEN_WIDTH)
            self.enemy_sprite_list.append(enemy)



        for i in range(1, 45):

            coin = Coin("img/bitcoin.png", 0.07)


            coin.center_x = 1000
            coin.center_y = random.randrange(SCREEN_WIDTH)


            self.coin_sprite_list.append(coin)


        # sprite lists
        self.pers = arcade.Sprite('img/ghost.png', 0.1)  # 0.1% от размера всей картинки
        self.pers.center_x = 36
        self.pers.center_y = 28

        self.grass = arcade.Sprite(
            '../../pythonProject37/arcadegame/img/1619227503_19-phonoteka_org-p-trava-fon-multyashnii-25.png', 0.1)
        self.grass.center_x = 27
        self.grass.center_y = 34

        self.grass_2 = arcade.Sprite(
            '../../pythonProject37/arcadegame/img/1619227503_19-phonoteka_org-p-trava-fon-multyashnii-25.png', 0.1)
        self.grass_2.center_x = 333
        self.grass_2.center_y = 34

        self.grass_3 = arcade.Sprite(
            '../../pythonProject37/arcadegame/img/1619227503_19-phonoteka_org-p-trava-fon-multyashnii-25.png', 0.1)
        self.grass_3.center_x = 675
        self.grass_3.center_y = 34

        self.moon = arcade.Sprite('img/moon.png', 0.3)
        self.moon.center_x = 75
        self.moon.center_y = 442



        self.cloud = arcade.Sprite('img/cloudy.png', 0.3)
        self.cloud.center_x = 120
        self.cloud.center_y = 410


        self.gameover = arcade.Sprite('img/game-over.png', 0.30)

        self.gameover.center_x = 400

        self.gameover.center_y = 250


        self.house = arcade.Sprite('img/house.png', 0.3)

        self.house.center_x = 79

        self.house.center_y = 100


        self.landscape_sprite_list = arcade.SpriteList()
        self.landscape_sprite_list.append(self.house)
        self.landscape_sprite_list.append(self.grass)
        self.landscape_sprite_list.append(self.grass_2)
        self.landscape_sprite_list.append(self.grass_3)
        self.landscape_sprite_list.append(self.moon)
        self.landscape_sprite_list.append(self.cloud)





    def on_draw(self):



        self.clear()
        if self.scene == SCENE_MENU:
            self.manager.draw()


        elif self.scene == SCENE_GAME:
            self.landscape_sprite_list.draw()
            self.coin_sprite_list.draw()
            self.enemy_sprite_list.draw()


            if self.sec_score <= 0:
                self.gameover.draw()

          


            self.pers.draw()
            output = f"Score: {self.score}"
            arcade.draw_text(output, 98, 400, arcade.color.BLACK, 14)

            output_2 = f"Live: {self.sec_score}"
            arcade.draw_text(output_2, 98, 380, arcade.color.BLACK, 14)






    def on_update(self, delta_time):


        self.pers.update()
        self.coin_sprite_list.update()
        self.enemy_sprite_list.update()
        hit_list = arcade.check_for_collision_with_list(self.pers,
                                                        self.coin_sprite_list)

        hit_list_2 = arcade.check_for_collision_with_list(self.pers,
                                                          self.enemy_sprite_list)
        for enemy in hit_list_2:
            enemy.remove_from_sprite_lists()
            self.sec_score -=1




        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1



        if self.pers.center_x < 30:
            self.pers.change_x = 0
        elif self.pers.center_x > 777:
            self.pers.change_x = 0
        elif self.pers.center_y >= 460:
            self.pers.change_y = 0
        elif self.pers.center_y <= 20:
            self.pers.change_y = 0





    def on_click_start(self, event):

        self.setup()
        self.scene = SCENE_GAME
        self.manager.disable()
        print("Start:", event)


    def on_key_press(self, key, modifiers: int):  # функция для управления

        if key == arcade.key.UP:
            self.pers.change_y = 3
        if key == arcade.key.DOWN:
            self.pers.change_y = -3
        elif key == arcade.key.RIGHT:
            self.pers.change_x = 3
        elif key == arcade.key.LEFT:
            self.pers.change_x = -3

    def on_key_release(self, symbol: int, modifiers: int):  # срабатывает на отжатие клавиши
        if symbol == arcade.key.UP:
            self.pers.change_y = 0
        if symbol == arcade.key.DOWN:
            self.pers.change_y = 0
        elif symbol == arcade.key.RIGHT:
            self.pers.change_x = 0
        elif symbol == arcade.key.LEFT:
            self.pers.change_x = 0


def main():

    window = MyGame()
    window.setup()
    arcade.run()



if __name__ == "__main__":
    main()