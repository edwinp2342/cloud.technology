import random
import math
def cal_int_sq_rt():
    number = random.randint(1, 101)
    sq_rt = math.isqrt(number)
    print(f"Square root of {number} = {sq_rt}")
cal_int_sq_rt()
