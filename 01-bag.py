def test_1_wei_bag_problem(bag_weight, weight, value):
    # 初始化: 全为0
    dp = [0] * (bag_weight + 1)

    # 先遍历物品, 再遍历背包容量
    for i in range(len(weight)):
        for j in range(bag_weight, weight[i] - 1, -1):
            # 递归公式
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    print(dp)


def test_2_wei_bag_problem1(bag_weight, weight, value) -> int: 
	rows, cols = len(weight), bag_weight + 1
	dp = [[0 for _ in range(cols)] for _ in range(rows)]
    
	# 初始化dp数组. 
	for i in range(rows): 
		dp[i][0] = 0
	first_item_weight, first_item_value = weight[0], value[0]
	for j in range(1, cols): 	
		if first_item_weight <= j: 
			dp[0][j] = first_item_value

	# 更新dp数组: 先遍历物品, 再遍历背包. 
	for i in range(1, len(weight)): 
		cur_weight, cur_val = weight[i], value[i]
		for j in range(1, cols): 
			if cur_weight > j: # 说明背包装不下当前物品. 
				dp[i][j] = dp[i - 1][j] # 所以不装当前物品. 
			else: 
				# 定义dp数组: dp[i][j] 前i个物品里，放进容量为j的背包，价值总和最大是多少。
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur_weight]+ cur_val)

	print(dp)


if __name__ == "__main__": 
    bag_weight = 4
    weight = [1, 3, 4]
    value = [15, 20, 30]
    test_1_wei_bag_problem(bag_weight, weight, value)