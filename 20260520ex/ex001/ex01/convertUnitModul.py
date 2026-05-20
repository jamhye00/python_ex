def convertUnit(lenMm):

    unitDic = {}

    unitDic['cm'] = lenMm * .1
    unitDic['m'] = lenMm * .001
    unitDic['inch'] = lenMm * .03937
    unitDic['ft'] = lenMm * .003281

    return unitDic

def printLength(lengths):
    for len in lengths.keys():
        print(f'{len}: {lengths[len]}{len}')

inputMmData = int(input('길이(mm)를 입력하세요. '))
resultData = convertUnit(inputMmData)
printLength(resultData)
