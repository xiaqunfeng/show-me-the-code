#-*- coding: utf-8-*-

import xlrd, codecs, json
from lxml import etree
from collections import OrderedDict

def xls2xml(filename, outfile):
    with xlrd.open_workbook(filename) as excel:
        #table = excel.sheet_by_name('student')
        table = excel.sheet_by_index(0)

    data = OrderedDict()
    for i in range(table.nrows):
        key = str(int(table.row_values(i)[0]))
        value = str(table.row_values(i)[1:])
        data[key] = value

    output = codecs.open(outfile, 'w', 'utf-8')
    root = etree.Element('root')
    students_xml = etree.ElementTree(root)
    students = etree.SubElement(root, 'students')
    students.append(etree.Comment('\n\t学生信息表\n\t"d" :[名字, 数学, 语文, 英语]\n'))
    students.text = '\n\t学生信息表\n\t"d" :[名字, 数学, 语文, 英语]\n'
    students.text = '\n'+str(json.dumps(data, indent=4, ensure_ascii=False))+'\n'
    output.write('<?xml version="1.0" encoding="UTF-8"?>\n' + etree.tounicode(students_xml.getroot()))
    output.close()

if __name__ == '__main__':
    xls2xml('student.xls', 'student.xml')
