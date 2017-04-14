from random import randint
import XML


class World:
    xml = XML.XML()

    def generate_tile(self, x, y):
        rand_land_gen = randint(1, 4)
        land_name = self.xml.get_text_by_id(rand_land_gen, "world", "region-type")
        land_type_list = self.xml.get_list_by_id(rand_land_gen, "world", "type")
        entities_list = self.xml.get_list_by_region(land_name, "entities", "name-plural")
        land_type_str = " & ".join(land_type_list) #not used right now
        land_list = [x, y, land_name, land_type_list, entities_list]

        return land_list
