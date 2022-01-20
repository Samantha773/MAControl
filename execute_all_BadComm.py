import os
import math
array = [1-math.log10(x) for x in range(1, 10)]
array_output = [1.0000, 0.6989, 0.5228, 0.3979, 0.3010, 0.2218, 0.1549, 0.0969, 0.0457]

# 算例生成方法 ————
# np.random.choice(3, 60)+1
# 算例检查方法 ————
# AA=list(A) # AA.count(2)

# n=10

os.system("python ./execute_Probability.py --numU=10 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.1 --pGG=0.1 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=10 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.1 --pGG=0.5 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=10 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.1 --pGG=0.9 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=10 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.5 --pGG=0.1 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=10 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.5 --pGG=0.5 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=10 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.5 --pGG=0.9 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=10 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.9 --pGG=0.1 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=10 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.9 --pGG=0.5 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=10 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.9 --pGG=0.9 "
          "--thr=0.4 ")

# n=50

os.system("python ./execute_Probability.py --numU=50 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.1 --pGG=0.1 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=50 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.1 --pGG=0.5 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=50 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.1 --pGG=0.9 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=50 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.5 --pGG=0.1 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=50 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.5 --pGG=0.5 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=50 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.5 --pGG=0.9 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=50 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.9 --pGG=0.1 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=50 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.9 --pGG=0.5 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=50 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.9 --pGG=0.9 "
          "--thr=0.4 ")

# n=100

os.system("python ./execute_Probability.py --numU=100 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.1 --pGG=0.1 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=100 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.1 --pGG=0.5 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=100 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.1 --pGG=0.9 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=100 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.5 --pGG=0.1 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=100 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.5 --pGG=0.5 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=100 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.5 --pGG=0.9 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=100 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.9 --pGG=0.1 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=100 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.9 --pGG=0.5 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=100 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.9 --pGG=0.9 "
          "--thr=0.4 ")

# n=300

os.system("python ./execute_Probability.py --numU=300 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.1 --pGG=0.1 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=300 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.1 --pGG=0.5 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=300 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.1 --pGG=0.9 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=300 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.5 --pGG=0.1 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=300 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.5 --pGG=0.5 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=300 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.5 --pGG=0.9 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=300 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.9 --pGG=0.1 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=300 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.9 --pGG=0.5 "
          "--thr=0.4 ")

os.system("python ./execute_Probability.py --numU=300 "
          "--typeT=2 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=3 --typeT=3 "
          "--typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=2 --typeT=3 --typeT=1 --typeT=2 --typeT=1 --typeT=3 "
          "--typeT=1 --typeT=1 --typeT=2 --typeT=3 --typeT=2 --typeT=1 --typeT=1 --typeT=3 --typeT=3 --typeT=2 "
          "--typeT=1 --typeT=2 --typeT=3 --typeT=3 --typeT=3 --typeT=1 --typeT=1 --typeT=2 --typeT=2 --typeT=2 "
          "--typeT=2 --typeT=3 --typeT=2 --typeT=2 --typeT=3 --typeT=3 --typeT=2 --typeT=2 --typeT=1 --typeT=1 "
          "--typeT=2 --typeT=1 --typeT=2 --typeT=2 --typeT=1 --typeT=3 --typeT=2 --typeT=3 --typeT=3 --typeT=2 "
          "--comm=GE --pBB=0.9 --pGG=0.9 "
          "--thr=0.4 ")
