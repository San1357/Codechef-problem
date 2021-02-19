'''
# Problem Code:LAYERS





#CODE:

tests = int(input())
for _ in range(tests):
    n, c = [int(j) for j in input().split()]
    rect_list = [[0] * 3 for _ in range(n)]
    for i in range(n):
        rect_list[i] = [int(j) for j in input().split()]
    colors = [0 for _ in range(c+1)]
    modified_rects = [[0,10**9,0]]
    for i in range(n-1,-1,-1):
        start = 0
        width = rect_list[i][0]
        height = rect_list[i][1]
        new_blocks = width * height
        for j, rect in enumerate(modified_rects):
            start_rect = rect[0]
            end_rect = rect[1]
            height_rect = rect[2]
            if end_rect >= width:
                if height_rect >= height:
                    new_blocks = 0
                else:
                    new_blocks -= height_rect * (width - start_rect)
                    modified_rects.insert(j,[start,width,height])
                    rect[0] = width
                break
            if height_rect >= height:
                new_blocks -= height * (end_rect - start_rect)
                start = end_rect
            else:
                new_blocks -= height_rect * (end_rect - start_rect)
                rect[2] = height_rect
                rect[0] = start
                rect[1] = start
        colors[rect_list[i][2]] += new_blocks
    for i in range(1,c+1):
        print(colors[i],end=" ")
    print("")
