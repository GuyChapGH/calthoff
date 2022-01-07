import statistics as s

nums = [1, 4, 5, 78, 78, 100]

nums_mean = s.mean(nums)
print(nums_mean)

nums_mode = s.mode(nums)
print(nums_mode)

nums_var = s.variance(nums)
print(nums_var)

nums_std = s.stdev(nums)
print(nums_std)

