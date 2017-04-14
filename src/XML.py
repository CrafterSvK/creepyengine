from lxml import etree


class XML:
    def get_text_by_id(self, id_input, xml_file, tag_name):
        """
        :param id_input: id of tag "id" in xml file you want to search in
        :param xml_file: name of xml file in which it will be found
        :param tag_name: name of a tag that will be output
        :return: text of tag in parent where is id_input located
        """
        xml_file_tree = etree.parse("xml/" + xml_file + ".xml")
        id_input = str(id_input)
        tag_id = xml_file_tree.xpath(".//id[text()='" + id_input + "']")
        tag_text = tag_id[0].getparent().find(tag_name).text

        return tag_text

    def get_list_by_id(self, id_input, xml_file, tag_name):
        """
        :param id_input: id of tag "id" in xml file you want to search in
        :param xml_file: name of xml file in which it will be found
        :param tag_name: name of a tag that will be output 
        :return: list of tags in parent where is id_input located
        """
        xml_file_tree = etree.parse("xml/" + xml_file + ".xml")
        id_input = str(id_input)
        tag_id = xml_file_tree.xpath(".//id[text()='" + id_input + "']")
        type_list_tag = tag_id[0].getparent().findall(tag_name)
        type_list_str = []

        for i in type_list_tag:
            type_list_str.append(i.text)

        return type_list_str
