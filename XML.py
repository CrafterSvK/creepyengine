from lxml import etree


class XML:
    def get_tag_text_by_id(self, id, xml_file, tag_name):
        """
        input ID, XML file, tag_name
        outputs text of chosen tag_name
        Sort of weird code. Think this needs rework
        """
        complete_tree = etree.parse("xml/" + xml_file + ".xml")
        id = str(id)
        tag_id = complete_tree.xpath(".//id[text()='" + id + "']")
        parent = tag_id[0].getparent()

        return parent.find(tag_name).text
