movieMenu = {
    '범죄도시': 12000,
    '파묘': 13000,
    '인사이드아웃2': 11000,
    '듄': 14000
}

reservationList = []
remainingSeats = 20

flag = True

MOVIE_LIST = 1
RESERVE_MOVIE = 2
CANCLE = 3
RESERVATION_LIST = 4
TOTAL_PRICE = 5
EXIT = 6


while True:
    selectedMenuNum = int(input('1.영화목록 2.영화예매 3.예매취소 4.예매내역 5.총금액 6.종료'))

    if selectedMenuNum == MOVIE_LIST:
        for key, value in movieMenu.items():
            print(f'{key} : {value}')

    elif selectedMenuNum == RESERVE_MOVIE:
        reserveMovie = input('예매할 영화를 입력하세요. ')

        if reserveMovie in movieMenu:    
            reservationList.append(reserveMovie)
            print(reservationList)
            remainingSeats -= 1
            print(f'남은 좌석 수: {remainingSeats}')
            
        else:
            print('존재하지 않는 영화입니다.')

    elif selectedMenuNum == CANCLE:
        cancleMovie = input('취소할 영화를 입력하세요. ')

        if cancleMovie in reservationList:
            reservationList.remove(cancleMovie)
            remainingSeats += 1
            print('예매가 취소되었습니다.')
        else:
            print('해당 영화 예매 내역이 없습니다.')
            
        print(reservationList)
        print(f'남은 좌석 수: {remainingSeats}')

    elif selectedMenuNum == RESERVATION_LIST:

        maxCount = 0
        maxMovie = ''

        print(f'예매한 영화는 {reservationList}이고, 총 예매 수는 {len(reservationList)}개입니다.')
        for movie in movieMenu:
            count = reservationList.count(movie)
            if count > maxCount:
                maxCount = count
                maxMovie = movie
        print(f'가장 많이 예매한 영화는 {maxMovie} 입니다.')

    elif selectedMenuNum == TOTAL_PRICE:
        totalPrice = 0
        for movie in reservationList:
            totalPrice += movieMenu[movie]
        print(f'총 {totalPrice}원 입니다.')
        
    elif selectedMenuNum == EXIT:
        print('종료합니다.')
        break
