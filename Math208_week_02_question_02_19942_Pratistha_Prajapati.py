import datetime
print(datetime.datetime.today())
import random

# Function to generate random numbers from a normal distribution
def create_normal_numbers(mean, std_dev, n):
    return [random.gauss(mean, std_dev) for _ in range(n)]

# Function to generate random numbers from a uniform distribution
def create_uniform_numbers(min_val, max_val, n):
    return [random.uniform(min_val, max_val) for _ in range(n)]

# Function to verify Chebyshev's inequality
def verify_Chebyshev_ineq(lst, k):
    mean = sum(lst) / len(lst)
    sd = (sum((x - mean) ** 2 for x in lst) / (len(lst) - 1)) ** 0.5
    lower_range = mean - k * sd
    upper_range = mean + k * sd
    count = sum(1 for x in lst if lower_range <= x <= upper_range)
    return count

# Test with random numbers from a normal distribution
n = 50
mean_normal = 10
std_dev_normal = 0.5
random_numbers_normal = create_normal_numbers(mean_normal, std_dev_normal, n)

k = 1
cnt = verify_Chebyshev_ineq(random_numbers_normal, k)
print(f"When k = {k}, P(|X-u|<k*sd) >= 1-1/k^2 is {cnt / n >= 1 - 1 / (k ** 2)}")

k = 2 ** 0.5
cnt = verify_Chebyshev_ineq(random_numbers_normal, k)
print(f"When k = {k}, P(|X-u|<k*sd) >= 1-1/k^2 is {cnt / n >= 1 - 1 / (k ** 2)}")

# Test with random numbers from a uniform distribution
min_uniform = -20
max_uniform = 20
random_numbers_uniform = create_uniform_numbers(min_uniform, max_uniform, n)

k = 1
cnt = verify_Chebyshev_ineq(random_numbers_uniform, k)
print(f"When k = {k}, P(|X-u|<k*sd) >= 1-1/k^2 is {cnt / n >= 1 - 1 / (k ** 2)}")

k = 2
cnt = verify_Chebyshev_ineq(random_numbers_uniform, k)
print(f"When k = {k}, P(|X-u|<k*sd) >= 1-1/k^2 is {cnt / n >= 1 - 1 / (k ** 2)}")
