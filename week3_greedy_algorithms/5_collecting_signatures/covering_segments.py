# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    # points = []
    # #write your code here
    # index=0
    # print(segments)
    # segments.sort(key=lambda x:x[1])
    # print(segments)

    # covered= [0]*len(segments)
    # for s in segments:
    #     points.append(s.start)
    #     points.append(s.end)
    # return points
    segments.sort(key = lambda x: x[1])
    index = 0
    coordinates = []
    print(segments)
    while index < n:
        curr = segments[index]
        while index < n-1 and curr[1]>=segments[index+1][0]:
            print(curr[1], '  ',segments[index+1][0])
            index += 1
        coordinates.append(curr[1])
        index += 1
    print(len(coordinates))
    print(' '.join([str(i) for i in coordinates]))


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *data = map(int, input.split())
    # print(data)
    n = 4
    data = [4, 7, 1, 3, 2, 5, 5, 6]
    # print(data[1::2])
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    # print(segments)
    points = optimal_points(segments)
    # print(len(points))
    # print(*points)
