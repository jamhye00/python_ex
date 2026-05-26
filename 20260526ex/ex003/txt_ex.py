# file = open('C:/khj/python/test.txt', 'w')  # 파일을 '쓰기' 모드로 open한다.
# result = file.write('Hello python!')        # 쓰기(write)
# print(f'result: {result}')                  # 문자(열)의 길이를 반환
# file.close()                                # 파일 닫기(close, 외부자원 해제)

# file = open('C:/khj/python/test.txt', 'r')           # 파일을 '읽기' 모드로 open한다.
# readResult = file.read()
# print(f'readResult: {readResult}')
# print(f'readResult type: {type(readResult)}')       # 텍스트 파일을 읽어올땐 무조건 str이다.

# readResult = int(readResult)
# readResult += 1
# print(f'readResult: {readResult}')

# file.close()

# file = open('C:/khj/python/test.txt', 'a')      # w는 전 데이터를 덮어씌우고 a는 이어붙인다.
# file.write('\nhello~')
# file.close()

# with open('C:/khj/python/test.txt', 'a') as file:       # close를 쓰지 않아도 됨
#     for n in range(10):                                 # hello를 10번 출력, for문 이용
#         file.write('\nhello~')

# file = open('C:/khj/python/test.txt', 'a')
# file.write('\nhi~')
# file.close()

# 예외 처리(보험)
# 세상에 모든 프로그램은 100% 완벽할 수 없다.

# print(10 + 20)      # 30
# try:
#     print(10 / 1)       # 에러 발생

# except Exception as e:  # Exception ---> 에러 내용 담음.
#     print(f'e: {e}')

# else:
#     print('에러가 발생하지 않으면 실행되는 코드')

# finally:
#     print('에러가 발생하든 안하든 무조건 실행되는 코드')

# print(10 - 20)      # X
# print(10 * 20)      # X

# 예외 처리의 기본 문법
'''
try ~ except
에러가 터질만한 곳만 찍어서 코드를 넣어야함 안 그러면 터지지 않는 곳도 실행이 안됨, 남발X
'''
