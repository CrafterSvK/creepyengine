from random import randint
import XML


class World:
    xml = XML.XML()

    def generate_tile(self, x, y):
        type_land = randint(1, 3)
        type_land_s = self.xml.get_text_by_id(type_land, "world", "name")
        list_type_xml = self.xml.get_list_by_id(type_land, "world", "type")
        land = "You are in " + type_land_s + ". It is ", list_type_xml, " in here!"

        return land
