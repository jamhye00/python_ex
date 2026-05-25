foodMenu = {
    '김치볶음밥': 7000,
    '돈까스': 8000,
    '라면': 4000,
    '제육볶음': 9000,
}

myFoodDB = []

SHOW_MENU = 1
ORDER_FOOD = 2
CANCEL_ORDER = 3
SHOW_ORDER_LIST = 4
SHOW_TOTAL_PRICE = 5
EXIT_PROGRAM = 6

flag = True

while flag:

    selectedMenuNum = int(input('1.메뉴 보기 2.음식 주문 3.주문 취소 4.주문 내역 5.총 금액 6.종료'))

    if selectedMenuNum == SHOW_MENU:
        for key, value in foodMenu.items():
            print(f'{key} : {value}원')
        # print(f'메뉴판입니다. {foodMenu}')

    elif selectedMenuNum == ORDER_FOOD:
        mySelectedFood = input('주문하실 음식을 입력해주세요. ')
        if mySelectedFood in foodMenu:
            print('주문 성공!')
            myFoodDB.append(mySelectedFood)
            print(myFoodDB)

        else:
            print(f'존재하지 않는 음식입니다. 메뉴판을 보고 다시 주문해주세요. {foodMenu}')

    elif selectedMenuNum == CANCEL_ORDER:
        myCancleFood = input('주문 취소할 음식을 입력해주세요. ')
        if myCancleFood in myFoodDB:
            myFoodDB.remove(myCancleFood)
            print(myFoodDB)
        else:
            print('주문하지 않은 음식입니다.')

    elif selectedMenuNum == SHOW_ORDER_LIST:
        if len(myFoodDB) > 0 :
            print(f' 주문한 음식은 {myFoodDB} 입니다.')
        else:
            print('주문한 내역이 없습니다.')

    elif selectedMenuNum == SHOW_TOTAL_PRICE:

        totalPrice = 0

        for food in myFoodDB:
            totalPrice += foodMenu[food]

        print(f'총 금액은 {totalPrice}원 입니다.')

    elif selectedMenuNum == EXIT_PROGRAM:
        print('종료합니다.')
        break