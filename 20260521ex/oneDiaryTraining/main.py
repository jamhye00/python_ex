from config_dir import config
from db import member_db
from member import member_dumy
from member import session

flag = True

while flag:
    selectedMenuNum = ''

    if session.signInedMemberId == '':
        selectedMenuNum = int(input('1.sign-up  2.sign-in  99.end'))
    else:
        selectedMenuNum = int(input('3.modify  4.delete  5.sign-out  99.end'))

    if selectedMenuNum == config.SIGN_UP:
        print('1. sign-up')
        uId = input('input new ID: ')
        uPw = input('input new PW: ')
        uMail = input('input new MAIL: ')
        uPhone = input('input new PHONE: ')
    
        member_db.memberDB[uId] = {
            'uId':uId,       
            'uPw':uPw,       
            'uMail':uMail,       
            'uPhone':uPhone       
        }

        print('New member sign-up success!!')

        if member_dumy.DEV_MOD:
            print(f'memberDb: {member_db.memberDB}')

    elif selectedMenuNum == config.SIGN_IN:
        print('2. sign-in')
        uId = input('input user ID: ')
        uPw = input('input user PW: ')

        if uId in member_db.memberDB:
            if member_db.memberDB[uId]['upw'] == uPw:
                print('sign-success!!')
            else:
                print('sign-in fail!! - PW error')
        else:
            print('sign-in fail!! - ID error')       

    elif selectedMenuNum == config.MODIFY:
        print('3. modify')
    elif selectedMenuNum == config.DELETE:
        print('4. delete')
    elif selectedMenuNum == config.SIGN_OUT:
        print('5. sign-out')       
    elif selectedMenuNum == config.SYSTEM_OUT:
        print('99. end')
        flag = False