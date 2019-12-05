from math import *
from pprint import pprint

def mirror_atlas(node, dimensions, distance):
    node_mirrored=[]
    for i in range(len(node)):
        points=[]
        for j in range(-(distance//dimensions[i])-1, (distance//dimensions[i]+2)):
            points.append(get_mirror(j, node[i], dimensions[i]))
        node_mirrored.append(points)
    print(pprint(node_mirrored),"end")
    return node_mirrored

def get_mirror(mirror, coordinates, dimensions):
    res=coordinates
    mirror_rotation=[2*coordinates, 2*(dimensions-coordinates)]
    if(mirror<0):
        for i in range(mirror, 0):
            res-=mirror_rotation[(i+1)%2]
    else:
        for i in range(mirror, 0, -1):
            res+=mirror_rotation[i%2]
    return res 

def answer(dimensions, your_position, guard_position, distance):
    mirrored = [mirror_atlas(your_position, dimensions,
        distance),mirror_atlas(guard_position, dimensions, distance)]
    pprint(mirrored)
    res=set()
    angles_dist={}
    for i in range(0, len(mirrored)):
        for j in mirrored[i][0]:
            for k in mirrored[i][1]:
                beam=atan2((your_position[1]-k), (your_position[0]-j))
                l=sqrt((your_position[0]-j)**2 + (your_position[1]-k)**2)
                if [j,k] != your_position and distance >= l:
                    if((beam in angles_dist and angles_dist[beam] > l) or beam not in angles_dist):
                        if i == 0:
                            angles_dist[beam] = l
                        else:
                            angles_dist[beam] = l
                            res.add(beam)
    return len(res)

dimensions = [3, 2]
captain_position = [1, 1]
badguy_position = [2, 1]
distance = 4

answer(dimensions,captain_position,badguy_position,distance)