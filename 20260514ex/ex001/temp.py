# split() - 쪼갠다. / 괄호 안은 쪼개는 기준 ex) 공백, + 등
names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')
print(f'names: {names}')
print(f'names type: {type(names)}')

str = '박찬호 이승엽 박세리 박지성 이순철 선동열 손흥민 김연아'
splitedStr = str.split(' ')
print(f'splitedStr: {splitedStr}')
# split으로 데이터를 쪼개면 데이터 타입은 list이다.
print(f'splitedStr type: {type(splitedStr)}')

# list -> tuple
splitedStr = tuple(splitedStr)
print(f'splitedStr: {splitedStr}')
print(f'splitedStr type: {type(splitedStr)}')