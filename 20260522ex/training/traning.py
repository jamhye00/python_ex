from datetime import datetime
print(datetime.today())

diaryList = {}
membersDB = {}
loginUser = ''
today = datetime.today().strftime('%Y-%m-%d')


while True:
    menu = int(input('1.일기쓰기    2.일기보기    3.종료    4.회원가입    5.로그인'))

    if menu == 1:
        diaryText = input('일기 입력: ')

        if loginUser != '':
            diaryList[loginUser].append(diaryText)
            print(f'{loginUser}님의 {today} 일기 내용은{diaryList[loginUser]}입니다.')
        else:
            print('로그인이 되어있지 않아 일기 내용이 저장되지 않습니다')

    elif menu == 2:
        for idx, i in enumerate(diaryList[loginUser]):
            print(f'{idx+1}: {i}')

    elif menu == 3:
        print('종료합니다')
        break

    elif menu == 4:
        uId = input('New user Id: ')
        uPw = input('New user Pw: ')
        uMail = input('New user Mail: ')
        uPhone = input('New user Phone: ')

        membersDB[uId] = {
            'uId': uId,
            'uPw': uPw,
            'uMail': uMail,
            'uPhone': uPhone
        }

        diaryList[uId] = []
    
    elif menu == 5:
        uId = input('user Id: ')
        uPw = input('user Pw: ')

        if uId in membersDB and membersDB[uId]['uPw'] == uPw:
            print('로그인 성공!')
            loginUser = uId
            print(f'로그인 되어있는 ID: {loginUser}')

        else:
            print('로그인 실패')
    
