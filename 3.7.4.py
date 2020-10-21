from xml.etree import ElementTree as ET
from lxml import etree as letree


inputinfo = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube><cube1/></cube>'
#inputinfo = input().rstrip()
xmlinfo = ET.fromstring(inputinfo)
xmlinforoot = xmlinfo.getroot()

xmlinfo1 = ET.parse(r"D:\Programming\filein.txt")
xmlinfo1root = xmlinfo1.getroot()
print(type(xmlinfo))
#print(type(xmlinforoot), xmlinforoot.attrib)
#print(xmlinfo.tag, xmlinfo.attrib, xmlinfo.tail, xmlinfo.text, len(xmlinfo))
print(type(xmlinfo1))
print(type(xmlinfo1root), xmlinfo1root.attrib)

print(xmlinfo1root.g)
print('------')
print(xmlinfo.findall('cube/[@color]'))
#for event, elem in ET.iterparse(r"D:\Programming\filein.txt"):
#    print(event, elem.tag, elem.attrib)
#for _ in xmlinfo.iter('cube'):
#    print(_.tag, _.attrib['color'])
#print('------')

def getobject(obj, deep=1, value=1):
    if 'color' not in obj.attrib:
        return
#    print('\t'*deep, obj.tag, obj.attrib, deep, value, cubiclist)
    cubiclist.setdefault(obj.attrib['color'], 0)
    cubiclist[obj.attrib['color']] += value
    for _ in list(obj):
        getobject(_, deep + 1, value + 1)

cubiclist = {}
getobject(xmlinfo)
print(f"{cubiclist['red']} {cubiclist['green']} {cubiclist['blue']}")
#print('------')
#print(type(xmlinfo1))
#print()

#for _ in xmlinfo1.getroot():
#    print(_, end='')
#    pass
#print(ET.tostringlist(xmlinfo))
#print('\n','-------')
xmlinfo2 = ET.parse(r"D:\Programming\filein.txt")
for _ in xmlinfo2.iter():
    #print(_.tag, _.attrib)
    pass
#print(letree.tostring(xmlinfo))
