import os
import math

# np.random.choice(3, 10)+1

array = [1-math.log10(x) for x in range(1, 10)]
array_output = [1.0000, 0.6989, 0.5228, 0.3979, 0.3011, 0.2218, 0.1549, 0.0969, 0.0457]

# 0.3 (GE)

os.system("python ./execute_Probability.py --numU=25 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=GE --pBB=0.3 ")

os.system("python ./execute_Probability.py --numU=50 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=GE --pBB=0.3 ")

os.system("python ./execute_Probability.py --numU=100 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=GE --pBB=0.3 ")

os.system("python ./execute_Probability.py --numU=200 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=GE --pBB=0.3 ")

# 0.5 (GE)

os.system("python ./execute_Probability.py --numU=25 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=GE --pBB=0.5 ")

os.system("python ./execute_Probability.py --numU=50 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=GE --pBB=0.5 ")

os.system("python ./execute_Probability.py --numU=100 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=GE --pBB=0.5 ")

os.system("python ./execute_Probability.py --numU=200 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=GE --pBB=0.5 ")

# 0.7 (GE)

os.system("python ./execute_Probability.py --numU=25 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=GE --pBB=0.7 ")

os.system("python ./execute_Probability.py --numU=50 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=GE --pBB=0.7 ")

os.system("python ./execute_Probability.py --numU=100 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=GE --pBB=0.7 ")

os.system("python ./execute_Probability.py --numU=200 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=GE --pBB=0.7 ")

# 0.9 (GE)

os.system("python ./execute_Probability.py --numU=25 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=GE --pBB=0.9 ")

os.system("python ./execute_Probability.py --numU=50 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=GE --pBB=0.9 ")

os.system("python ./execute_Probability.py --numU=100 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=GE --pBB=0.9 ")

os.system("python ./execute_Probability.py --numU=200 "
          "--typeT=1 --typeT=3 --typeT=1 --typeT=1 --typeT=3 --typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 "
          "--comm=GE --pBB=0.9 ")

# end
