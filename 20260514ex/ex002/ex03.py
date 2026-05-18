# CRUD
'''
C : Create 생성, 추가
R : Read   조회
U : Update 수정
D : Delete 삭제
'''

'''
딕셔너리 (Dictionary): {key: value}
'''
# C: Create
student = {
    '학번': 123456789,      # key: value
    '이름': '홍길동',
    '나이': 20,
    '성별': 'M',
    '연락처': '010-1234-5678'
}

print(f'student: {student}')
print(f'student type: {type(student)}')

# R: Read
sNo = student['학번']
print(f'sNo: {sNo}')
print(f'sNo type: {type(sNo)}')

# U: Update
sName = student['이름']
print(f'sName: {sName}')        # 홍길동 > 홍길자

student['이름'] = '홍길자'
sName = student['이름']
print(f'sName: {sName}')        # 홍길자

# D: Delete
del student['연락처']
print(f'student: {student}')

# keys(), values(), items()     # 딕셔너리에서 이용되는 함수

# 1) keys(): 딕셔너리 자료형에서 키값들만 몽땅 뽑는다.
# 뽑은 키들은 리스트와 비슷한 데이터 타입이다.
keys = student.keys()
print(f'keys: {keys}')
print(f'keys type: {type(keys)}')

for key in keys:    # dict_keys(['학번', '이름', '나이', '성별'])
    print(f'key: value = {key}: {student[key]}')

# 2) values() : 딕셔너리에서 벨류값들만 몽땅 뽑는다. 
# 뽑은 벨류들은 리스트와 비슷한 데이터 타입이다.
values = student.values()
print(f'values: {values}')
print(f'values type: {type(values)}')

for value in values:
    print(f'value: {value}')

# 3) items()
items = student.items()     # key & value 값을 둘다 뽑아낼때
print(f'items: {items}')    # items: dict_items([('학번', 123456789), ('이름', '홍길자'), ('나이', 20), ('성별', 'M')])
# 리스트 안에 하나 하나 아이템은 튜플로 되어있다.
# for문을 이용한 전체데이터 조회
for item in items:
    print(f'item: {item}')      # 튜플로 출력됨, item: ('학번', 123456789), item: ('이름', '홍길자') ...
    print(f'item[0], item[1]: {item[0]}, {item[1]}')
'''
위의 구조는 item 튜플 -> ('학번', 123456789) -> item[0], item[1]
'''

for key, value in items:
    print(f'key: value = {key}: {value}')       # 인덱스에 접근하지 않고 조회, '구조분해할당' 문법

'''
key, value = ('학번', 123456789)
'''

# 구조분해할당
# a, b = (10, 20)
# print(f'a: {a}, b: {b}')

# 구조분해 할당을 안 쓸 경우
# c = (10, 20)
# a = c[0]
# b = c[1]
# print(f'a: {a}, b: {b}')

a = 10
b = 20

# swapping -> a: 20, b: 10
'''
temp = a
a = b       # a: 20
b = temp    # b: 10
'''
# 위의 것과 같은 거
# a, b = b, a

scores = [10, 20, 30, 40, 50, 60]
'''
a = 10
b = 20
c = [30, 40, 50, 60]
'''
a, b, *c =scores
print(f'a: {a}')
print(f'b: {b}')
print(f'c: {c}')

'''
a: 10
b: 20
c: [30, 40, 50, 60]
'''

# quiz) 다음은 스포츠 센터 회원 정보를 나타낸 표이다.
# 표를 보고 파이썬을 이용해서 컨테이너 자료형으로 만드시오.
members = {
    '2019-052001':{
        '이름': '박찬호',
        '나이': 25,
        '성별': 'M',
        '연락처': '010-1234-5678',
        '이용서비스': ['헬스, 수영'],
        '할인율': 0
    }
}
# info = members['2019-052001']
# print(f'info: {info}')      # 박찬호+25+M+010-1234-5678+헬스,수영+0
# infos = info.split('+')
# print(f'infos: {infos}')    # ['박찬호', '25', 'M', '010-1234-5678', '헬스,수영', '0']

print(members['2019-052001'])
print(members['2019-052001']['이름'])
print(members['2019-052001']['나이'])
print(members['2019-052001']['할인율'])
print(members['2019-052001']['이용서비스'])