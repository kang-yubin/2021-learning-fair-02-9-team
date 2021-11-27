def ison():
    print('출근체크를 시작하겠습니다.')
    day=input('오늘의 날짜를 입력하세요. (yyyy/mm/dd):')
    time=input('출근시간을 입력하세요. (00시 00분):')
    print ('신인수님 %s %s 출근 기록 되셨습니다.' %(day, time))
    islist.append ('신인수 %s %s 출근' %(day, time))
    print(islist)
    print()


def isoff():
    print('퇴근체크를 시작하겠습니다.')
    day=input('오늘의 날짜를 입력하세요. (yyyy/mm/dd):')
    time=input('퇴근시간을 입력하세요. (00시 00분):')
    print ('신인수님 %s %s 퇴근 기록 되셨습니다.' %(day, time))
    islist.append ('신인수 %s %s 퇴근' %(day, time))
    print(islist)
    print()


def ybon():
    print('출근체크를 시작하겠습니다.')
    day=input('오늘의 날짜를 입력하세요. (yyyy/mm/dd):')
    time=input('출근시간을 입력하세요. (00시 00분):')
    print ('강유빈님 %s %s 출근 기록 되셨습니다.' %(day, time))
    yblist.append ('강유빈 %s %s 출근' %(day, time))
    print(yblist)
    print()


def yboff():
    print('퇴근체크를 시작하겠습니다.')
    day=input('오늘의 날짜를 입력하세요. (yyyy/mm/dd):')
    time=input('퇴근시간을 입력하세요. (00시 00분):')
    print ('강유빈님 %s %s 퇴근 기록 되셨습니다.' %(day, time))
    yblist.append ('강유빈 %s %s 퇴근' %(day, time))
    print(yblist)
    print()


def ywon():
    print('출근체크를 시작하겠습니다.')
    day=input('오늘의 날짜를 입력하세요. (yyyy/mm/dd):')
    time=input('출근시간을 입력하세요. (00시 00분):')
    print ('임예원님 %s %s 출근 기록 되셨습니다.' %(day, time))
    ywlist.append ('임예원 %s %s 출근' %(day, time))
    print(ywlist)
    print()


def ywoff():
    print('퇴근체크를 시작하겠습니다.')
    day=input('오늘의 날짜를 입력하세요. (yyyy/mm/dd):')
    time=input('퇴근시간을 입력하세요. (00시 00분):')
    print ('임예원님 %s %s 퇴근 기록 되셨습니다.' %(day, time))
    ywlist.append ('임예원 %s %s 퇴근' %(day, time))
    print(ywlist)
    print()
        

def byon():
    print('출근체크를 시작하겠습니다.')
    day=input('오늘의 날짜를 입력하세요. (yyyy/mm/dd):')
    time=input('출근시간을 입력하세요. (00시 00분):')
    print ('장보연님 %s %s 출근 기록 되셨습니다.' %(day, time))
    bylist.append ('장보연 %s %s 출근' %(day, time))
    print(bylist)
    print()
    

def byoff():
    print('퇴근체크를 시작하겠습니다.')
    day=input('오늘의 날짜를 입력하세요. (yyyy/mm/dd):')
    time=input('퇴근시간을 입력하세요. (00시 00분):')
    print ('장보연님 %s %s 퇴근 기록 되셨습니다.' %(day, time))
    bylist.append ('장보연 %s %s 퇴근' %(day, time))
    print(bylist)
    print()



islist=[]
bylist=[]
yblist=[]
ywlist=[]


start = ''
while start != "끝" :
    print('출퇴근 프로그램을 시작합니다.')
    print('현재 알바생= 신인수, 임예원, 장보연, 강유빈')
    print()
    print('알바생의 이름+출/퇴근을 띄어쓰기 없이적으면 프로그램이 실행됩니다. / 예) 홍길동출근')
    print('프로그램을 종료하시려면 끝이라고 입력해주세요.')
    print('각 알바생별 출퇴근리스트를 보시려면 다음과 같이 입력 / 예) 홍길동출퇴근기록')
    print("==================================================")
    start = input('입력:')
    print("==================================================")

    if start == '신인수출근':
        ison()

    elif start == '신인수퇴근':
        isoff()

    elif start == '강유빈출근':
        ybon()

    elif start == '강유빈퇴근':
        yboff()

    elif start == '임예원출근':
        ywon()

    elif start == '임예원퇴근':
        ywoff()

    elif start == '장보연출근':
        byon()

    elif start == '장보연퇴근':
        byoff()

    elif start == '끝':
        print('프로그램을 종료합니다.')

    elif start == '신인수출퇴근기록':
        print(islist)
        print()

    elif start == '강유빈출퇴근기록':
        print(yblist)
        print()

    elif start == '장보연출퇴근기록':
        print(bylist)
        print()

    elif start == '임예원출퇴근기록':
        print(ywlist)
        print()

    else:
        print('올바르게 입력했는지 확인해주세요 !')
        print()
