from collections import OrderedDict
import xlwt, json

def json2excel(inputFile, outputFile):
    if inputFile.split('.')[1] != 'txt':
        print('please input .txt file!')
        return
    with open(inputFile, 'r') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)
        wb = xlwt.Workbook()
        ws = wb.add_sheet('city', cell_overwrite_ok=True)
        for index, (key, value) in enumerate(data.items()):
            ws.write(index, 0, key)
            ws.write(index, 1, value)
        wb.save(outputFile)

if __name__ == '__main__':
    json2excel('city.txt', 'city.xls')
