import os
import math

# np.random.choice(3, 10)+1

array = [1-math.log10(x) for x in range(1, 10)]
array_output = [1.0000, 0.6989, 0.5228, 0.3979, 0.3011, 0.2218, 0.1549, 0.0969, 0.0457]

# 0.3979 (B)

os.system("python ./execute_Probability.py --numU=25 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=B --p=0.3979 ")

os.system("python ./execute_Probability.py --numU=50 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=B --p=0.3979 ")

os.system("python ./execute_Probability.py --numU=100 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=B --p=0.3979 ")

os.system("python ./execute_Probability.py --numU=200 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=B --p=0.3979 ")

# 0.3011 (B)

os.system("python ./execute_Probability.py --numU=25 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=B --p=0.3011 ")

os.system("python ./execute_Probability.py --numU=50 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=B --p=0.3011 ")

os.system("python ./execute_Probability.py --numU=100 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=B --p=0.3011 ")

os.system("python ./execute_Probability.py --numU=200 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=B --p=0.3011 ")

# 0.2218 (B)

os.system("python ./execute_Probability.py --numU=25 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=B --p=0.2218 ")

os.system("python ./execute_Probability.py --numU=50 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=B --p=0.2218 ")

os.system("python ./execute_Probability.py --numU=100 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=B --p=0.2218 ")

os.system("python ./execute_Probability.py --numU=200 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=B --p=0.2218 ")

# 0.1549 (B)

os.system("python ./execute_Probability.py --numU=25 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=B --p=0.1549 ")

os.system("python ./execute_Probability.py --numU=50 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=B --p=0.1549 ")

os.system("python ./execute_Probability.py --numU=100 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=B --p=0.1549 ")

os.system("python ./execute_Probability.py --numU=200 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=B --p=0.1549 ")

# 0.0969 (B)

os.system("python ./execute_Probability.py --numU=25 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=B --p=0.0969 ")

os.system("python ./execute_Probability.py --numU=50 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=B --p=0.0969 ")

os.system("python ./execute_Probability.py --numU=100 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=B --p=0.0969 ")

os.system("python ./execute_Probability.py --numU=200 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=B --p=0.0969 ")

# end
