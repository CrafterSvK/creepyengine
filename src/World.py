from random import randint
import XML


class World:
    xml = XML.XML()

    def generate_tile(self, x, y):
        rand_land_gen = randint(1, 3)
        land_name = self.xml.get_text_by_id(rand_land_gen, "world", "name")
        land_type_list = self.xml.get_list_by_id(rand_land_gen, "world", "type")
        land_type_str = " & ".join(land_type_list)
        land = "On " + str(x) + ", " + str(y) + ". There is " + land_name + ". It is " + land_type_str + " in here!"

        return land
