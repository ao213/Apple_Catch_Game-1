import random
from setting import *
import json


class Apple:
    def __init__(self, json):
        self.__down_speed = json['down_speed']
        self.__point = json['point']
        self.__spawn_rate = json['spawn_rate']
        self.image = 'img/{}'.format(json['image'])
        self.__dmg_point = json['dmg_point']

        self.__pos_x = random.randint(0, 800)
        self.__pos_y = 0

    def fall(self):
        self.__pos_y += self.__down_speed

    def get_pos_y(self):
        """y座標を返す

        Returns:
            int : y座標
        """
        return self.__pos_y

    def get_pos(self):
        """x座標とy座標を返す
        Returns:
            tuple : (x座標, y座標)
        """
        return self.__pos_x, self.__pos_y

    def get_hit_box(self):
        """りんごの当たり判定ゾーンを返す

        Returns:
            List : x座標のヒットボックス、y座標のヒットボックス
        """
        return self.__pos_x + 50, self.__pos_y

    def get_point(self):
        """ポイントを返す

        Returns:
            int : ポイント
        """
        return self.__point

    def get_damage_point(self):
        return self.__dmg_point

    def check_collision(self, player):
        """りんごがプレイヤーに当たったか判別する

        Args:
            apple(Apple): Appleのインスタンス

        Returns:
            bool: プレイヤーに当たったどうか
        """
        player_hit_box_left, player_hit_box_right = player.get_hit_box()
        apple_hit_box_x, apple_hit_box_y = self.get_hit_box()
        if (480 > apple_hit_box_y >= 450
                and player_hit_box_left <= apple_hit_box_x <= player_hit_box_right):
            return True
        return False

    def check_reach_bottom(self):
        """りんごが底部に到着したか判別する

        Returns:
            bool: リーチしたかどうか
        """
        pos_y = int(self.get_pos_y())
        if pos_y >= 500:
            return True
        return False

    @classmethod
    def create_apple(cls):
        json_list_for_apple = cls.create_list_by_json(APPLE_JSON)
        return Apple(random.choice(json_list_for_apple))

    @classmethod
    def create_apples(cls):
        """Appleのインスタンスを最大数生成してリストで返す

        Returns:
            List: Appleのインスタンスのリスト
        """
        json_list_for_apple = cls.create_list_by_json(APPLE_JSON)
        return cls.create_random_apples_to_limit(json_list_for_apple)

    @classmethod
    def create_list_by_json(cls, json_file):
        """ Jsonを読み込み、リスト化して返す

        Returns:
            List: Jsonデータをリスト化したもの
        """
        with open(json_file) as f:
            jsn = json.load(f)
            return [jsn_val for jsn_val in jsn.values()]

    @classmethod
    def create_random_apples_to_limit(cls, json_list):
        """ Jsonのリストの中からランダムの情報を使い、指定した数だけインスタンス化して返す

        Args:
            json_list (dict): Apple.jsonのデータをリスト化したもの

        Returns:
            List: Appleインスタンスのリスト
        """
        return [Apple(random.choice(json_list)) for _ in range(MAX_APPLE_NUM)]
