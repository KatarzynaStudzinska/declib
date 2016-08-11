import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import random

file = open('A.txt')
data = []
for line in file:
    dane = line.split(" ")
    point = []
    for elem in dane:
        point.append(int(elem))
    data.append(point)


centroids = [[0,0,0,0,0,0,0,0,0],
            #[[1, 8, 3, 2, 1, 2, 4, 9, 8],
            #[1, 2, 2, 10, 3, 1, 1, 5, 1]
            # [7, 4, 1, 1, 2, 9, 7, 5, 2],
            # [2, 1, 1, 5, 1, 2, 5, 6, 1],
             [5, 5, 5, 5, 5, 5, 5, 5, 5]]
            # [1, 5, 3, 6, 10, 6, 3, 2, 2],
            # [2, 7, 8, 2, 1, 2, 4, 5, 4],
            # [2, 4, 3, 1, 10, 1, 1, 1, 1],
            # [4, 10, 4, 3, 2, 3, 5, 10, 9]]

def sum_of_squares (point, centroid, dimensions):
    """
    Function counts sum of squares. In 2D and 3D it can be understand as distance between point and centroid.
    :param point: point for which we count
    :param centroid: centroid for which we count
    :param dimensions: number of dimension/ params in vector
    :return: sum of squares: (point[0] + centroid[0])^2 + (point[1] + centroid[1])^2 + ...
    """
    summ = 0
    for i in range(dimensions):
        summ += (point[i] - centroid[i])**2
    return summ

def count_new_centroid(cluster):
    """
    For set of points we count new centroid, which will fit better than previous
    :param cluster: set of points
    :return: new centroid
    """
    new_centroid = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    if len(cluster) == 0:
        for i in range(9):
            new_centroid[i] = random.randint(1, 10)
    else:

        for point in cluster:
            for i in range(len(point)):
                new_centroid[i] += point[i]

        for i in range(len(new_centroid)):
            new_centroid[i] /= len(cluster)
    return new_centroid


if __name__ == "__main__":

    dimensions_number = 9
    clusters = []
    for counter in range(1000):
        clusters = [[], []]
        for point in data[:int(len(data)/3)]:

            distance_list = []
            for centroid in centroids:
                distance_list.append(sum_of_squares(point, centroid, dimensions_number))
            clust_index = distance_list.index(min(distance_list))
            clusters[clust_index].append(point)

        new_centroid_list = []
        for cluster in clusters:
            new_centroid_list.append(count_new_centroid(cluster))
        centroids = new_centroid_list

    colors = ['r', 'b']
    fig = plt.figure()
    rak_lub_nie = []
    for j in range(len(centroids)):
        color = colors[j] + 's'
        plt.plot(centroids[j][0], centroids[j][1], color)
        color_p = colors[j] + '.'
        for point in clusters[j]:
            plt.plot(point[0], point[1], color_p)
            if j == 0:
                rak_lub_nie.append([point, 0])
            else:
                rak_lub_nie.append([point, 1])

    testing_set = []
    rak = []
    nirak = []
    for point in data[int(len(data)/3):]:
        if sum_of_squares(point, centroids[0], dimensions_number) < sum_of_squares(point, centroids[1], dimensions_number):
            nirak.append(point)
            testing_set.append([point, 0])
        else:
            testing_set.append([point, 1])
            rak.append(point)

    for p in nirak:
        print(p)

    print("rak \n")

    for p in rak:
        print(p)


    plt.show()
    import json

    data = {"rak_lub_nierak": rak_lub_nie, "test": testing_set}
    with open('data.json', 'w') as fp:
        json.dump(data, fp)
