# 지역변수(로컬) vs 전역변수(글로벌)
# 지역변수는 함수 내부에서 선언된 변수로 함수 내부에서만 사용 가능합니다.
# 전역변수는 함수 외부에서 선언된 변수로 함수 내/외부에서 사용 가능합니다.

# num = 10

# def fun():
#     print(f'num: {num}')    # 10, 전역변수 num -> 함수 내부에 num이 없으면 전역변수의 num을 찾음

# print(f'num: {num}')        # 10, 전역변수 num

# fun()


# num = 10

# def fun():
#     num = 20                # 지역변수
#     print(f'num: {num}')    # 20, 지역변수 num

# print(f'num: {num}')        # 10, 전역변수 num

# fun()

# num = 10

# def fun():
#     global num
#     num = num + 1           # 데이터 수정 num(전역변수) = 10 + 1
#     print(f'num: {num}')    # UnboundLocalError -> global 키워드를 사용하지 않으면 뜨는 error

# print(f'num: {num}')        # 10, 전역변수 num

# fun()
'''
global 키워드는 함수 내에서 전역변수의 값을 '수정'하고자 할때 반드시 명시하자.
'''

# quiz) 웹사이트의 누적방문 횟수 프로그램
# 웹사이트 방문 여부를 입력받아 웹사이트의 누적 방문 횟수를 출력해봅시다

# flag = True
# totalVisitor = 0

# def countVisitor():
#     global totalVisitor
#     totalVisitor += 1

# while flag:
#     selectedMenuNum = int(input('1.웹사이트 방문      2.종료'))

#     if selectedMenuNum == 1:
#         countVisitor()
#         print(f'누적 방문 횟수: {totalVisitor}')

#     else:
#         flag = False
#         print('Good bye~')

# 매개변수(******************중요*******************)
# 매개: 둘 사이에서 양편의 '관계를 맺어' 줌
# 함수를 사용하기 위해 먼저 함수를 정의하고 필요할 때 호출합니다.
# 이때, 함수를 정의하는 족을 함수 정의부(선언부), 함수를 호출하는 쪽을 호출부라고 합니다.

# 함수를 호출할 때 데이터를 넘겨줄 수 있는데, 이 데이터를 '인수'라고 합니다.
# 함수 정의부는 인수를 받으면 '매개변수' 라는 변수에 저장합니다.
# 그리고 매개변수는 지역변수의 일종입니다.

# def greet():
#     print(f'홍길동님 안녕하세요.')          

# greet()                                 # 홍길동님 안녕하세요. 만 출력이됨

# def greet(name, age):
#     # name = '홍길동' or '박찬호' or '박세리'
#     print(f'{name}님 안녕하세요. 나이는 {age}입니다.')

# greet('홍길동', 25)
# greet('박찬호', 20)
# greet('박세리', 30)                 # 두 개의 데이터를 받을 때는 변수도 2개 지정

# 두 개 이상의 매개변수
# 인수의 개수와 순서에 쌍을 맞춰서 선언합니다. ex) greet(name, age), greet('홍길동', 25)
# 쌍을 안 맞췄을때 TypeError: greet() missing 1 required positional argument: 'age' 뜸
# 한 개를 선언하고 두 개의 데이터를 받을 때 TypeError: greet() takes 1 positional argument but 2 were given 뜸

# def forecastWeather(temp, humi, rain):
#     print('날씨 예보입니다.')
#     print(f'최고 온도: {temp}도')
#     print(f'평균 습도: {humi}%')
#     print(f'비올 확률: {rain}%')

# forecastWeather(35, 70, 80)

# 인수의 개수를 모르는 경우
# 우리 학급 학생들의 시험점수 총합과 평균을 구하는 함수를 만들자.
# 우리 학습 학생 수는 총 3명이다.

# def printScoresForStudent(score1, score2, score3):
#     totalScore = score1 + score2 + score3
#     averageScore = totalScore / 3

#     print(f'총합: {totalScore}')
#     print(f'평균: {averageScore}')

# printScoresForStudent(90, 80, 100)


# def printScoresForStudent(subject, *scores):                 
# # *를 입력하면 호출부에서 몇 개든 받음  # ex)*scores -> 가변인자
# # 들어오는 데이터만큼 프로그램이 리스트이긴한데 데이터가 왜곡이 되면 안되기때문에 튜플을 만듬 list -> tuple
# # 지역변수이면서 매개변수이면서 레퍼런스
# # 가변인자는 다른 매개변수와 쓸땐 매개변수 위치가 가장 뒷 쪽에 있어야한다.
# # 매개 변수는 순서대로.
#     print(f'scores type: {type(scores)}')           # scores type: <class 'tuple'>
#     print(f'scores length: {len(scores)}')          # 호출부에서 던지는 갯수

#     totalScore = 0
#     for score in scores:
#         totalScore += score

#     print(f'{subject} 과목 총합: {totalScore}')
#     averageScore = totalScore / len(scores)
#     print(f'{subject} 과목 평균: {averageScore}')

# # 90, 80, 100
# printScoresForStudent('국어',90, 80, 100)

'''
선생님이 몇 명일지 모르는 학생의 점수를 입력한다.
이때 학생 점수의 총합과 평균을 구하는 함수를 만들고
이를 이용하는 프로그램을 만들어보자.
'''
# flag = True
# studentScores = []

# def printScoresForStudent(scores):              # scores = [,,,,,,,,]
#     if len(scores) == 0:
#         print('학생 수가 0명이라 총점과 평균을 구할 수 없습니다.')
#     else:
#         totalScore = 0
#         for score in scores:
#             totalScore += score

#         average = totalScore / len(scores)
#         print(f'총점: {totalScore}')
#         print(f'평균: {average}')


# while flag:
#     selectedMenuNum = int(input('1.학생 점수 입력            2.종료 '))
#     if selectedMenuNum == 1:
#         score = int(input('학생 점수 입력: '))
#         studentScores.append(score)
#     else:
#         flag = False

# printScoresForStudent(studentScores)


# quiz) SMS와 MMS 구별하기
'''
문자를 보낼 때 100자 이하인 경우에는 단문 메시지(SMS)로 50원을 부과합니다.
그런데 100자를 넘어가면 장문 메시지(MMS)로 변경되면서 100원이 부과됩니다.
단문과 장문을 구별해서 돈을 부과하는 프로그램을 만들어봅시다. 
'''

# def sendUserMessage(str):
#     strLength = len(str)
#     print(f'사용자가 입력한 문자 길이: {strLength}')

#     if strLength <= 100:
#         print(f'SMS 발송 완료')
#         print('50원 부과!')
#     else:
#         print(f'MMS 발송 완료')
#         print('100원 부과!')

# inputData = input('문자 입력: ')
# sendUserMessage(inputData)

# 인수와 매개변수의 순서가 일치하지 않을 경우
# def printMemberInfo(name, email, major, grade):
#     print(f'Name\t: {name}')
#     print(f'Email\t: {email}')
#     print(f'Major\t: {major}')
#     print(f'Grade\t: {grade}')
#     print('-----------------------------------------')

# printMemberInfo('Hong Gildong', 'gildong@gmail.com', 'art', 1)
# printMemberInfo(email = 'gildong@gmail.com',        # (좋지 않은 방법)
#                 name = 'Hong Gildong',
#                 major = 'art',
#                 grade = 1)

# def printMemberInfo(info):
#     print(f'name: {info['name']}')
#     print(f'email: {info['email']}')
#     print(f'major: {info['major']}')
#     print(f'grade: {info['grade']}')

# # 한 번만 쓸때
# printMemberInfo({
#     'name': 'Hong Gildong',
#     'email': 'gildong@gmail.com',
#     'major': 'art',
#     'grade': 1
# })

# # 재사용 할 때
# memberInfo = {
#         'name': 'Hong Gildong',
#         'email': 'gildong@gmail.com',
#         'major': 'art',
#         'grade': 1
#     }

# printMemberInfo(memberInfo)

# 매개변수의 기본값 설정
# 직원 급여 지급 프로그램을 만들어보자!
# def setSalary(name, pay = 200):
#     print(f'{name}의 급여는 {pay}만 원 지급!')

# setSalary('박찬호', 400)
# setSalary('박세리', 600)
# setSalary('박용택')                     # 이럴 경우 매개변수의 기본값을 설정한다.

# 데이터 반환(return)
# 데이터 반환이란, 함수는 실행이 끝난 후에 결과물(값)을 호출부로 반환할 수 있습니다.
# 이때 사용하는 키워드가 'return' 입니다.
# 덧셈 연산 함수를 만들어 결과를 출력하는 프로그램을 만들어보자!


# def printResult(value):
#     print(f'result: {value}')

# def addFuntion(n1, n2):                 # 기능을 2개를 가지고 있음 더하는 것과 출력하는 것
#     sum = n1 + n2
#     # print(f'결과 값: {sum}')
#     printResult(sum)
#     return sum

# addFuntion(10, 20)
# # print(f'result: {result}')

# DEV_MOD = False

# def fun1():
#     print('111111111111111')    # -> 이것만 출력하고 싶을때 return을 쓴다 호출부로 넘겨버리는 역할
#     if DEV_MOD == True:
#         print('222222222222222')    # return 이하의 내용은 실행이 안됨 (개발단계에서 디버깅 용도로만 사용할때도 씀)
#         return
#     print('333333333333333')

# fun1()

# 별탑 만들기
# def increaseStart(limitStarCount):
#     # print('*')
#     # print('**')
#     # print('***')
#     # print('****')
#     # print('*****')
#     # print('******')
#     # print('*******')

#     for n in range(7):
#         print('*' * n)
#         if n == limitStarCount:
#             break

# increaseStart(5)

# 7 ~ 8교시
# Toy 프로젝트 진행
'''
처음 프로그램이 실행되면 다음과 같은 메뉴를 출력한다.
메뉴: 1.회원가입   2.로그인   3.특정 회원 정보 출력   4.모든 회원 정보 출력    99.종료
사용자가
'1.회원가입'을 선택하면 회원 ID, 회원 PW, 회원Email, 회원Phone 정보를 입력받아 회원가입 진행한다.
'2.로그인'을 선택하면 회원 ID, 회원 PW를 입력받아 로그인 '성공' 또는 '실패'를 출력한다.
'3.특정 회원 정보 출력'을 선택하면 회원 ID와 회원 PW를 입력받아 일치하는 회원 정보를 모두 출력한다.
'4.모든 회원 정보 출력'을 선택하면 가입되어 있는 모든 회원 정보를 출력한다.
'99.종료'를 선택하면 프로그램을 종료시킨다.

심심하면> 특정 회원의 회원 ID와 회원 PW를 입력받아 인증되면 회원 정보를 수정하는 기능을 구현해보자!
'''
flag = True
userInfos = {}

def inputUserInfo():
    inputUserId = input('ID: ')
    inputUserPw = input('Pw: ')

    

    if inputUserId == userInfos[inputUserId]['uId'] and inputUserPw == userInfos[inputUserId]['uPw']:
        print('성공!')
        return inputUserId

    else:
        print('실패...')

while flag:

    SelectedMenuNum = int(input('1.회원가입  2.로그인   3.특정 회원 정보 출력  4.모든 회원 정보 출력   99.종료'))

    if SelectedMenuNum == 1:

        userId = input('ID: ')
        userPw = input('Pw: ')
        userEmail = input('Email: ')
        userPhone = input('Phone: ')

        userInfos[userId] = {
            'uId': userId,
            'uPw': userPw,
            'uEmail': userEmail,
            'uPhone': userPhone
        }

        print('회원가입 되었습니다!')
        
    elif SelectedMenuNum == 2:
        inputUserInfo()

    elif SelectedMenuNum == 3:
        loginUserId = inputUserInfo()

        for key, value in userInfos[loginUserId].items():
                print(f'{key}: {value}')
                

    elif SelectedMenuNum == 4:

        for user in userInfos.values():
                
            print('-------------------')

            for key, value in user.items():
                print(f'{key}: {value}')

            
    elif SelectedMenuNum == 99:

        print('종료합니다.')
        break


