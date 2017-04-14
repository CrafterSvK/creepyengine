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
        search_list_tag = tag_id[0].getparent().findall(tag_name)
        search_list_str = []

        for i in search_list_tag:
            search_list_str.append(i.text)

        return search_list_str

    def get_list_by_region(self, region_type, xml_file, tag_name):
        """
        :param region_type: type of region that you want to search in
        :param xml_file: name of xml file in which it will be found
        :param tag_name: name of tag you want list of
        :return: 
        This seems messy. Check please.
        """
        xml_file_tree = etree.parse("xml/" + xml_file + ".xml")
        region_type_tag = xml_file_tree.xpath(".//region[text()='" + region_type + "']")
        search_list_str = []

        for i in region_type_tag:
            search_list_tag = i.getparent().findall(tag_name)
            for e in search_list_tag:
                search_list_str.append(e.text)

        return search_list_str
