from random import randint
from xml.etree import ElementTree


class World:
    def generate_tile(self, x, y):

        type_land = randint(1, 3)
        number_entities = randint(1, 20)
        active_entities = randint(1, number_entities)
        passive_entities = number_entities - active_entities
        land = [x, y, type_land, number_entities, passive_entities, active_entities]

        if type_land == 1:
            type_land_s = "desert"
            active_entities_s = "cojots"
            passive_entities_s = "cactuses"
        elif type_land == 2:
            type_land_s = "moutains"
            active_entities_s = "birds"
            passive_entities_s = "rocks"
        elif type_land == 3:
            type_land_s = "plain"
            active_entities_s = "wolfs"
            passive_entities_s = "trees"
        else:
            type_land_s = "void xD"

        print("On", x, "x", y, "there's", type_land_s, "and", active_entities, active_entities_s, passive_entities, passive_entities_s, "!")
        return land

    def get_file(self):
        tree = ElementTree.parse('xml/entities.xml')
        root = tree.getroot()
        for child in root:
            print(child.tag, child.attrib)
        return 0