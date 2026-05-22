def fun():
    print('module01의 함수가 실행됩니다.')

# print(f'module01의 __name__: {__name__}')
# __name__ 전역 변수는 파이썬 엔진에서 만들어주는 변수로, 
# 모듈에서 사용을 하면 모듈이름을 갖게 되고 __module01__
# 실행파일에서 사용을 하면 __main__이 된다

if __name__ == '__main__':
    fun()