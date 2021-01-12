# BA_b = [b.C1  b.C2  b.C3  b.C4  b.W1  b.W2  b.W3  b.W4  b.W5  b.W6  b.W7  b.W8, b.W9, b.W10]
# seen_uav     # rule1 rule2 rule3 rule4   # align 聚拢 分散 / evade
# seen_target  # rule5 rule6 rule7 rule8   # 最近目标吸引+排斥 所有目标吸引+排斥
# other        # rule9 rule10              # 随机游走 / balance

SYS = list()
#                                    w1    w2    w3    w4    w5    w6    w7    w8    w9    w10
SYS.append([0.70, 0.10, 0.00, 0.00, 1.00, 0.90, 0.10, 1.00, 0.55, 0.45, 0.55, 0.45, 0.70, 0.30])  # 聚拢
SYS.append([0.00, 0.00, 0.07, 0.01, 1.00, 0.10, 0.90, 1.00, 0.55, 0.45, 0.55, 0.45, 0.70, 0.30])  # 分散
SYS.append([0.10, 0.70, 0.00, 0.00, 1.00, 0.55, 0.45, 1.00, 0.55, 0.45, 0.80, 0.20, 0.70, 0.30])  # 吸引
SYS.append([0.00, 0.00, 0.01, 0.07, 1.00, 0.55, 0.45, 1.00, 0.55, 0.45, 0.20, 0.80, 0.70, 0.30])  # 排斥
