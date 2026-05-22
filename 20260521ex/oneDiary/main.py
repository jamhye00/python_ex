from config_dir.dir import config
from member import session
from db import member_db
from member import member_dumy
from db import diary_db
import copy
from datetime import datetime

if config.DEV_MOD:
    member_dumy.dumyInit()
    print(f'memberDB: {member_db.memberDB}')
    print(f'diaryDB: {diary_db.diaryDB}')

flag = True

while flag:

    menuNum = ''
    if session.signInedMemberId == '':
        # sign out 상태
        menuNum = int(input('1.sign-up   2.sign-in   6.write   7.read   99.end '))
        
    else:
        # sign in 상태
        menuNum = int(input('3.modify   4.delete   5.sign-out   6.write   7.read   99.end '))

    if menuNum == config.SIGN_UP:
        print('1.sign-up')
        uId = input('Please input new member ID: ')
        uPw = input('Please input new member PW: ')
        uMail = input('Please input new member MAIL: ')
        uPhone = input('Please input new member PHONE: ')
        uRegDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        member_db.memberDB[uId] = {
            'uId': uId,
            'uPw': uPw,
            'uMail': uMail,
            'uPhone': uPhone,
            'uRegDate': uRegDate
        }

        print('New member sign-up success!!')

        if config.DEV_MOD:
            print(f'memberDB: {member_db.memberDB}')

        diary_db.diaryDB[uId] = []
        if config.DEV_MOD:
            print(f'diaryDB: {diary_db.diaryDB}')

    elif menuNum == config.SIGN_IN:
        print('2.sign-in')
        uId = input('Please input member ID: ')
        uPw = input('Please input member PW: ')

        if uId in member_db.memberDB:
            if member_db.memberDB[uId]['uPw'] == uPw:
                print('sign-in success!!')
                session.signInedMemberId = uId
            else:
                print('sign-in fail!! -- PW error')
        else:
            print('sign-in fail!! -- ID error')

        # if uId in member_db.memberDB and member_db.memberDB[uId]['uPw']

    elif menuNum == config.MEMBER_MODIFY:
        print('3.modify')
        '''
        ID, PW, MAIL, PHONE 이 중에서 어떤 정보들만 수정 가능하게 할 것인지 정하기.
        ID : 수정 X, 이미 탈퇴한 회원의 ID라도 절대 변경 사용할 수 없다.
        PW : 수정이 가능하지만, 쉽게 변경할 수는 없다.
        MAIL: 비교적 단순하게 수정 가능
        PHONE : 비교적 단순하게 수정 가능
        '''

        uPw = input('Please input member PW: ')
        uMail = input('Please input member MAIL: ')
        uPhone = input('Please input member PHONE: ')

        '''
        - member_db 모듈에 있는 memberDB 딕셔너리에서 회원정보를 변경한다.
        - 지금 현재 memberDB에는 'gildong', 'chanho' 회원이 있는데,
          현재 로그인 되어 있는 회원 정보를 불러와 그 정보를 수정
        - session.signInedMemberId = '' 에서 # SIGN-OUT 생각하면 된다.
          현재 로그인 되어 있는 회원 ID를 가져와 사용하면 된다.
        '''
        currentSignInedMemberID = session.signInedMemberId
        # print(currentSignInedMemberID)
        # print(type(currentSignInedMemberID))
        memberInfo = member_db.memberDB[currentSignInedMemberID]
        if config.DEV_MOD: print(f'memberInfo: {memberInfo}')

        memberInfo['uPw'] = uPw
        memberInfo['uMail'] = uMail
        memberInfo['uPhone'] = uPhone

        if config.DEV_MOD: print(f'after modify: {memberInfo}')

    elif menuNum == config.MEMBER_DELETE:
        print('4.delete')
        '''
        - 현재 로그인 되어 있는 회원 ID를 session.signInedMemberId에서 가져와서
        - 해당하는 회원 정보를 member_db.memberDB에 삭제
        '''
        currentSignInedMemberID = session.signInedMemberId
        del member_db.memberDB[currentSignInedMemberID]

        print('Member info deleted!!')
        session.signInedMemberId = ''
        if config.DEV_MOD: print(f'member_db.memberDB: {member_db.memberDB}')

    elif menuNum == config.SYSTEM_OUT:
        print('99.end')
        flag = False
    elif menuNum == config.SIGN_OUT:
        print('5.sign-out')
        session.signInedMemberId = ''
        print('sign-out success!!')
        '''
        - 메뉴 변경
        - 로그인 값 없애기.
        - session 모듈에 signInedMemberId 변수에 있는 것.
        '''

    elif menuNum == config.DIARY_WRITE:
        print('6.write')

        if session.signInedMemberId == '':
            print('Sorry! Please sign-in!')
            
        else:
            while True:
                diaryTxt = input('Write a short diary entry in 10 words or fewer.')
                if len(diaryTxt) > 10:
                    print(f'It exceeded 10 characters.({len(diaryTxt)}) Please write it again.')
                else:
                    diary_db.diaryDB[session.signInedMemberId].append(diaryTxt)
                    if config.DEV_MOD: print(f'diary_db.diaryDB: {diary_db.diaryDB}')
                    break
       
    elif menuNum == config.DIARY_READ:
        print('7.read')

        if session.signInedMemberId == '':
            print('Sorry! Please sign-in!')

        else:
            currentSignInedMemberID = session.signInedMemberId
            myDiaries = diary_db.diaryDB[currentSignInedMemberID]

            deepCopyedDiaries = copy.deepcopy(myDiaries)
            deepCopyedDiaries.reverse()             # 순서 바뀐다.

            for idx, diaryTxt in enumerate(deepCopyedDiaries):
                print(f'({idx+1}): {diaryTxt}')