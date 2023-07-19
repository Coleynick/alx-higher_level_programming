def weight_average(my_list=[]):
    if not my_list:
        return 0

    totalSum_weight = 0
    total_weights = 0

    for result, weight in my_list:
        totalSum_weight += result * weight
        total_weights += weight

    return totalSum_weight / total_weights
