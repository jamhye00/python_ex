'''
처음 프로그램이 실행되면 다음과 같은 메뉴를 출력한다.
메뉴: 1.회원가입   2.로그인   3.나의 정보 출력   4.모든 회원 정보 출력    99.종료
사용자가
'1.회원가입'을 선택하면 회원 ID, 회원 PW, 회원Email, 회원Phone 정보를 입력받아 회원가입 진행한다.
'2.로그인'을 선택하면 회원 ID, 회원 PW를 입력받아 로그인 '성공' 또는 '실패'를 출력한다.
'3.나의 정보 출력'을 선택하면 회원 ID와 회원 PW를 입력받아 일치하는 회원 정보를 모두 출력한다.
'4.모든 회원 정보 출력'을 선택하면 가입되어 있는 모든 회원 정보를 출력한다.
'99.종료'를 선택하면 프로그램을 종료시킨다.

심심하면> 특정 회원의 회원 ID와 회원 PW를 입력받아 인증되면 회원 정보를 수정하는 기능을 구현해보자!
'''

SIGN_UP = 1
SIGN_IN = 2
PRINT_MY_INFO = 3
PRINT_ALL_MEMBER_INFO = 4
SYSTEM_SHUTDOWN = 99

DEV_MOD = True

members = {}


if DEV_MOD:

    uIds = ['gildong', 'chanho', 'saeri']
    uPws = ['1234', '5678', '0000']
    uMails = ['gildong@gmail.com', 'chanho@naver.com', 'saeri@daum.net']
    uPhones = ['010-1234-5678', '010-0000-1345', '010-9876-5432']

    for n in range(len(uIds)):
        members[uIds[n]] = {
            'uId': [uIds[n]],
            'uPw': [uPws[n]],
            'uMail': [uMails[n]],
            'uPhone': [uPhones[n]]
        }

# functions START
def getSelectedMenuNum():
    selectedMenuNum = int(input('1.회원가입   2.로그인   3.나의 정보 출력   4.모든 회원 정보 출력   99.종료'))
    return selectedMenuNum

def setNewMember(uId, uPw, uMail, uPhone):
    members[uId] = {
                'uId': uId,
                'uPw': uPw,
                'uMail': uMail,
                'uPhone': uPhone
                }
    
def isMember(uId):
    if uId in members:
            print(f'{uId}는(은) 이미 사용중 입니다. 다시 확인하세요.')
            return True
    else:
        return False

def printAllMemberInfo(value):
    for key1, value1 in value.items():
                print(f'{key1}: {value1}')
    
# functions END


flag = True
while flag:
    
    userSelectedMenuNum = getSelectedMenuNum()

    if userSelectedMenuNum == SIGN_UP:
        uId = input('Input member ID: ')
        if not isMember(uId):
            uPw = input('Input member PW: ')
            uMail = input('Input member EMAIL: ')
            while True:
                if '@' not in uMail:
                    print('입력한 이메일 주소가 형식에 맞지 않습니다.')
                    uMail = input('Input member EMAIL: ')
                else:
                    break

            uPhone = input('Input member PHONE: ')

            setNewMember(uId, uPw, uMail, uPhone)
        
            print('SIGN-UP SUCCESS!!')

            if DEV_MOD: print(f'members: {members}')

    elif userSelectedMenuNum == SIGN_IN:
        signInCount = 1
        while True:
            uId = input('Input member ID: ')
            uPw = input('Input member PW: ')

            if uId in members:
                uInfo = members[uId]
                if uInfo['uPw'] == uPw:
                    print('SIGN-IN SUCCESS!!')
                else:
                    print('SIGN-IN FAIL!!')
                    signInCount += 1 
                    if signInCount > 3:
                        print('3회 이상 틀렸어요!')
                        break
            else:
                print('존재하지 않는 ID입니다. 다시 확인하세요.')

       

    elif userSelectedMenuNum == PRINT_MY_INFO:
        uId = input('Input member ID: ')
        uPw = input('Input member PW: ')

        if uId in members:
            uInfo = members[uId]
            if uInfo['uPw'] == uPw:
                print('SIGN-IN SUCCESS!!')

                print('-' * 30)
                for key, value in uInfo.items():
                    print(f'{key}: {value}')
                print('-' * 30)

            else:
                print('SIGN-IN FAIL!!')
        else:
            print('존재하지 않는 ID입니다. 다시 확인하세요.')


    elif userSelectedMenuNum == PRINT_ALL_MEMBER_INFO:
        for key, value in members.items():
            print(f'{key}님의 정보-----------------')
            printAllMemberInfo(value)
            print('-' * 30)

    elif userSelectedMenuNum == SYSTEM_SHUTDOWN:
        flag = False
        print('Good bye~')