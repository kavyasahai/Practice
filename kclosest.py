import math

def kClosest(points,K):
    final_arr=[]
    dist_dict={}
    for point in points:
        dist_dict[points.index(point)]=math.sqrt(point[0]**2+point[1]**2)
    print(dist_dict)
    sorted_dist = [K for K in sorted(dist_dict, key=dist_dict.get, reverse=False)]

    for i in range(K):
        final_arr.append(points[sorted_dist[i]])

    return final_arr


print(kClosest([[3,3],[5,-1],[-2,4]],2))

