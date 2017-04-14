from lxml import etree


class XML:
    def get_text_by_id(self, tag_id, xml_file, tag_name):
        """
        input ID, XML file, tag_name
        outputs text of chosen tag_name
        Sort of weird code. Think this needs rework
        """
        complete_tree = etree.parse("xml/" + xml_file + ".xml")
        tag_id = str(tag_id)
        tag_id_tree = complete_tree.xpath(".//id[text()='" + tag_id + "']")
        parent = tag_id_tree[0].getparent()

        return parent.find(tag_name).text

    def get_list_by_id(self, tag_id, xml_file, tag_name):
        """
        input ID, XML file, tag_name
        outputs list with text of chosen tag_name
        VERY VERY Weird code change please quickly
        """
        complete_tree = etree.parse("xml/" + xml_file + ".xml")
        tag_id = str(tag_id)
        tag_id_tree = complete_tree.xpath(".//id[text()='" + tag_id + "']")
        list_types = tag_id_tree[0].getparent().findall("type")
        for e in list_types:
            find_all = e.getparent().findall(tag_name)
        list_types_l = []
        for i in find_all:
            list_types_l.append(i.text)
        return list_types_l
