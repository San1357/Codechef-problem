# Note:
# Problem Code:  UWCOI21D



# from collections import defaultdict
vertical_roads,horizontal_roads,k = list(map(int,input().split()))
# highways = defaultdict(int)
deliveries = list()
for _ in range(k):
    d = list(map(int,input().split()))
    cnt = 1
    x1,y1,x2,y2 = d
    # highways[y1] += cnt
    # highways[y2] += cnt
    deliveries.append((x1,y1,x2,y2))
# highway=(sorted(highways.items(), key=lambda x : x[1], reverse = True))[0][0]


ans = list()

cost = 0
for highway in range(1,horizontal_roads+1):
    cost = 0
    for x1,y1,x2,y2 in deliveries:
        # cost += abs(x2-x1)*1 + abs(y2-highway)*2 + abs(y1-highway)*2
        cost += min([2*(abs(x2-x1)+abs(y2-y1)), (abs(x2-x1)*1 + abs(y2-highway)*2 + abs(y1-highway)*2)])
        temp = cost
        # if y1 == y2:
        #     cost += min([2*(abs(x2-x1)+abs(y2-y1)), (abs(x2-x1)*1 + abs(y2-highway)*2 + abs(y1-highway)*2)])
        # else:
        #     cost += min([2*(abs(x2-x1)+abs(y2-y1)), (abs(x2-x1)*1 + abs(y2-highway)*2 + abs(y1-highway)*2)])
    if cost <= temp:
        ans.append(cost)
    # else:
    #     break
print(min(ans))
