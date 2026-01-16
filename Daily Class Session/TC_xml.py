import xml.etree.ElementTree as ET
tree = ET.parse("student.xml")
root=tree.getroot()

for student in root.findall("student"):
    id = student.find("id").text
    name = student.find("name").text
    marks = student.find("marks").text
    print(id,name,marks)


root = ET.Element("employee")
emp1 = ET.SubElement(root,"emp")
ET.SubElement(emp1, "id").text ="101"
ET.SubElement(emp1,"name").text ="ravi"
ET.SubElement(emp1,"salary").text = "20000"

tree = ET.ElementTree(root)
tree.write("employee.xml")
print("xml file written Successfully")