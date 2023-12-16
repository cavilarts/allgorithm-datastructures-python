weigth = [30, 50, 10, 70, 40]
value = [150, 100, 90, 140, 120]
capacity = 150

def fractional_knapsack(value, weigth, capacity):
  n = len(value)
  items = list(range(len(value)))
  ratio = [v//w for v, w in zip(value, weigth)]
  
  # items = list(range(len(value)))
  # print(items)
  # ratio = [v//w for v, w in zip(value, weigth)]
  # print(ratio)
  # str_ratios = sorted(ratio, reverse=True)
  # print(str_ratios)
  # items.sort(key=lambda i: ratio[i], reverse=True)
  # print(items)
  
  # max_value = 0
  # fractions = [0] * len(value)
  # print(fractions)
  # for i in items:
  #   if weigth[i] <= capacity:
  #     fractions[i] = 1
  #     max_value += value[i]
  #     capacity -= weigth[i]
  #   else:
  #     fractions[i] = capacity // weigth[i]
  #     max_value += value[i] * capacity // weigth[i]
      
  # return max_value

print(fractional_knapsack(value, weigth, capacity))
  