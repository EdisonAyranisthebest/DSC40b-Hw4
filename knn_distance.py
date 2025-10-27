def knn_distance(arr, q, k):
    distances = []
    for point in arr:
        dist = abs(point - q)
        distances.append((dist, point))
    
    distances.sort()
    
    kth_distance, kth_point = distances[k-1]
    
    return (kth_distance, kth_point)