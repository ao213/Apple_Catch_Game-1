from setting import MAX_HP


class Player:
    def __init__(self):
        self.__hp = MAX_HP
        self.__point = 0
        self.__score = 0
        self.__pos_x = 0
        self.__pos_y = 500
        self.image = "img/box.png"
        self.__hit_box_height = 30
        self.__hit_box_width = 90

    def get_hit_box(self):
        """ヒットボックスを返す

        Returns:
            List: [ヒットボックスの左座標, ヒットボックスの右座標]
        """
        return self.__pos_x, self.__pos_x + self.__hit_box_width

    def set_player_position(self, x):
        if x >= 800:
            self.__pos_x = 800
        else:
            self.__pos_x = x

    def get_pos(self):
        return self.__pos_x, self.__pos_y

    def get_hp(self):
        return self.__hp

    def get_point(self):
        return self.__point

    def add_point(self, point):
        self.__point += point

    def receive_damage(self, apple):
        self.__hp = self.__hp - apple.get_damage_point()
        # TODO: HUDに移動する
        #
