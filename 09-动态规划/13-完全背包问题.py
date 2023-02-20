# 先遍历物品，再遍历背包
def test_complete_pack1(weight, value, bag_weight):
    dp = [0]*(bag_weight + 1)

    for i in range(len(weight)):
        for j in range(weight[i], bag_weight + 1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    
    print(dp)
    print(dp[bag_weight])


# 先遍历背包，再遍历物品
def test_complete_pack2(weight, value, bag_weight):
    dp = [0]*(bag_weight + 1)

    for j in range(bag_weight + 1):
        for i in range(len(weight)):
            if j >= weight[i]: dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    
    print(dp)
    print(dp[bag_weight])


if __name__ == '__main__':
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4
    test_complete_pack1(weight, value, bag_weight)
    test_complete_pack2(weight, value, bag_weight)