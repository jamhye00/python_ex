foodMenu = {
    '햄버거': 5000,
    '감자튀김': 2500,
    '콜라': 2000,
    '치킨너겟': 4000
}

orderList = []

maxCount = 0
maxFood = ''

flag =  True

SHOW_MENU = 1
ORDER_FOOD = 2
CANCEL_ORDER = 3
SHOW_ORDER_LIST = 4
SHOW_TOTAL_PRICE = 5
SHOW_MAX_ORDER = 6
EXIT = 7

while flag:
    seletedMenuNum = int(input('1.메뉴보기 2.음식주문 3.주문취소 4.주문내역 5.총 금액 6.가장 많이 주문한 음식 7.종료'))
    
    if seletedMenuNum == SHOW_MENU:
        pass

    elif seletedMenuNum == ORDER_FOOD:
        myOrderFood = input('주문할 음식을 입력해주세요. ')

    elif seletedMenuNum == CANCEL_ORDER:
        pass

    elif seletedMenuNum == SHOW_ORDER_LIST:
        pass
    
    elif seletedMenuNum == SHOW_TOTAL_PRICE:
        pass

    elif seletedMenuNum == SHOW_MAX_ORDER:
        pass

    elif seletedMenuNum == EXIT:
        pass
