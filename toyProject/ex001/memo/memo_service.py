import memo_DB

def getTime(memo):
    return memo['작성시간']

def readLatest():
    memo_DB.userMemoList.sort(key=getTime, reverse=True)
    
    for memo in memo_DB.userMemoList:
        for key, value in memo.items():
            print(f'{key}: {value}')
        print('-' * 40)
        
def readOldest():
    memo_DB.userMemoList.sort(key=getTime)
    
    for memo in memo_DB.userMemoList:
        for key, value in memo.items():
            print(f'{key}: {value}')
        print('-' * 40)    

def readMonth():
    memoReadMonth = input('조회하고 싶은 월을 입력하세요. [숫자 두자리로 입력하세요. ex) 5월 -> 05] ')
    for memo in memo_DB.userMemoList:
        monthMemo = memo['작성시간'].split('-')[1]
        if memoReadMonth == monthMemo:
            print(memo)
        
def updateMemo():
    memoUpdate = input('수정할 메모의 날짜를 입력하세요. [ex)2026-05-28]')
    for memo in memo_DB.userMemoList:
        updateMemoDate = memo['작성시간'].split('-')[0]
        if memoUpdate == updateMemoDate:
            print(memo)
        