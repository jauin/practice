# 원하는 날짜
wantedDay = '2021년 04월 27일'
# 원하는 시간
wantedTime = '19:'
# 부킹 팀


def openChrome():
    print("크롬을 시작한다.")

def goBookingPage():
    print("부킹페이지로 간다")



    
    
def checkDay(day):
    print(day, " 날에 예약 가능한 시간이 있는가?")
    return 1

def moveDayPage(day):
    print("예약일로 간다")
    print(day)
    return 99

def booking(bookingTime, teamNum):
    print("있으면, 예약한다.")
    print(bookingTime, " 시간대에",teamNum, "팀 부킹한다")


### 
openChrome()
z = checkDay(wantedDay)
if z == 1 : print("있다")
a = moveDayPage(wantedDay)
print(a)
booking(wantedTime, 3)



# def add(arg1, arg2):
#     c = arg1 + arg2
#     return c

# print(add(2, 3))
