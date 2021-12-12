import xml.etree.ElementTree as ET

tree = ET.parse("data.xml")
root = tree.getroot()
# for child in root:
#     print(child.find("name").text)

useful = {"name","phone_code","capital","currency","latitude","longitude"}
new_root = ET.Element("regions")
for country in root:
    region = country.find("region").text
    subregion = country.find("subregion").text
    if not (region and subregion): continue
    region_node = new_root.find(f"region[@location='{region}']")
    if region_node is None:
        region_node = ET.SubElement(new_root, "region",attrib={"location":region})
    subregion_node = region_node.find(f"subregion[@location='{subregion}']")
    if subregion_node is None:
        subregion_node = ET.SubElement(region_node, "subregion",attrib={"location":subregion})
    country_node = ET.SubElement(subregion_node, "country")
    for node in country:
        if node.tag in useful and node.text:
            country_node.attrib[node.tag] = node.text
    
tree = ET.ElementTree(new_root)
tree.write("transform.xml",xml_declaration=True)