import heapq
'''
test case 1
'''
n = 3
customers = ["10/01 23:20:25 30",
"10/01 23:25:50 26",
"10/01 23:31:00 05",
"10/01 23:33:17 24",
"10/01 23:50:25 13",
"10/01 23:55:45 20",
"10/01 23:59:39 03",
"10/02 00:10:00 10"]
month_sec = {
    1:3600*24*31,
    2:3600*24*28,
    3:3600*24*31,
    4: 3600*24*30,
    5: 3600*24*31,
    6: 3600 * 24 * 30,
    7: 3600 * 24 * 31,
    8: 3600 * 24 * 31,
    9: 3600 * 24 * 30,
    10: 3600 * 24 * 31,
    11: 3600 * 24 * 30
}
'''
test case 2
'''
# n = 2
# customers = ["02/28 23:59:00 03",
#              "03/01 00:00:00 02",
#              "03/01 00:05:00 01"]
# month_sec = {
#     1:3600*24*31,
#     2:3600*24*28,
#     3:3600*24*31,
#     4: 3600*24*30,
#     5: 3600*24*31,
#     6: 3600 * 24 * 30,
#     7: 3600 * 24 * 31,
#     8: 3600 * 24 * 31,
#     9: 3600 * 24 * 30,
#     10: 3600 * 24 * 31,
#     11: 3600 * 24 * 30
# }
'''
test case 3
'''
# n = 2
# customers = ["02/28 23:59:00 03",
#              "03/01 00:00:00 02",
#              "03/02 00:05:00 01",
#              "03/04 00:05:00 01"]
# month_sec = {
#     1:3600*24*31,
#     2:3600*24*28,
#     3:3600*24*31,
#     4: 3600*24*30,
#     5: 3600*24*31,
#     6: 3600 * 24 * 30,
#     7: 3600 * 24 * 31,
#     8: 3600 * 24 * 31,
#     9: 3600 * 24 * 30,
#     10: 3600 * 24 * 31,
#     11: 3600 * 24 * 30
# }
# converting date/time to second
def time_conversion(time):
    time_arr = time.split(' ')
    h, m, s = map(int, time_arr[1].split(':'))
    mon, day = map(int, time_arr[0].split('/'))
    sec = 3600 * h + 60 * m + s
    day_sec = 3600 * 24 * (day - 1)
    mon_sec = 0
    for i in range(1,mon):
        mon_sec += month_sec[i]
    time = mon_sec + day_sec + sec
    return time
# time converted list
customers_sec = []
for time in customers:
    start_time = time_conversion(time)
    duration = 60 * int(time.split(' ')[2])
    customers_sec.append((start_time , duration))
customers_sec.sort()
# initialize kiosk information
kiosk_count = [0] * (n)
kiosk_status = []
for i in range(n):
    kiosk_status.append((0, i))
pq = []

while customers_sec:
    '''
    1.손님이 온다
    2.키오스크의 상황을 본다
    3.만약 비어있는 키오스크가 있다면 그런것들중 가장 작동안한지 오래된 키오스크로 배정한다
    4.다 작동중이라면 먼저 멈추는 것으로 배정한다
    '''
    new_customer, duration = customers_sec.pop(0)
    kiosk_accepted = False
    print(new_customer, new_customer+duration)
    print(kiosk_status)
    for i in range(len(kiosk_status)):
        # 키오스크 1번째껏부터 돌면서 배정 가능한곳이 있다면 배정한다
        if kiosk_status[i][0] <= new_customer:
            kiosk_status[i] = (new_customer+duration, kiosk_status[i][1])
            kiosk_count[kiosk_status[i][1]] += 1
            kiosk_accepted = True
            break
    # 손님 도착 시간 기준으로, 가능한 키오스크가 없는경우
    # 제일 먼저 끝나는 키오스크에 손님을 배정한다
    if kiosk_accepted == False:
        end_time, kiosk_num = heapq.heappop(kiosk_status)
        heapq.heappush(kiosk_status, (end_time+duration, kiosk_num))
        kiosk_count[kiosk_num] += 1
    print(kiosk_status)
    print(kiosk_count)

print(max(kiosk_count))
