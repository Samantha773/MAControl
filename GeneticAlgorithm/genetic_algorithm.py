import numpy as np
import random
import os
import MAControl.Default.PolicyMaker_SelfOrganization as PM_S


class GA():
    def __init__(self, arglist):
        print('ga init')
        self.pop_size = arglist.pop_size
        self.generation_num = arglist.generation_num
        self.preserved_num = round(arglist.preserved_population*self.pop_size)
        self.collect_num = arglist.collect_num
        self.max_archetypes = arglist.max_behavior_archetypes
        self.crossover_rate = arglist.crossover_rate
        self.mutation_rate = arglist.mutation_rate
        self.mutation_neighborhood = arglist.mutation_neighborhood
        self.bit = 5

        self.ba_c = 2
        self.ba_w = 9
        self.ba_r = 3

        # 初始化随机种群
        self.population = [[] for i in range(self.pop_size)]
        for individual in self.population:
            for ba_arch in range(self.max_archetypes):
                individual.append([])
                for weight in range(self.ba_c+self.ba_w+self.ba_r):
                    individual[-1].append(np.random.random())

        self.score = np.zeros((self.pop_size, self.collect_num))
        self.new_population = list()
        self.binary_population = list()

    def evolve(self):

        self.select()

        self.encode()

        self.crossover()

        self.mutate()

        self.decode()

        if len(self.new_population) == self.pop_size:
            print('Evolution completed!')
        else:
            raise Exception('Evolution failed! Check the population.')

        self.population = self.new_population.copy()

    # 选出部分个体进入下一代
    def select(self):
        self.new_population.clear()
        self.binary_population.clear()

        score_sum = list()
        score_sum_individual = np.sum(self.score, axis=1)

        for i in range(self.pop_size):
            individual_score = [i, score_sum_individual[i]]
            score_sum.append(individual_score)
        score_sum = sorted(score_sum, key=lambda x: x[1], reverse=True)
        self.score = np.zeros((self.pop_size, self.collect_num))

        for i in range(self.preserved_num):
            self.new_population.append(self.population[score_sum[i][0]])

    # 交叉操作,交叉操作完成后，使得新种群数量与原种群保持一致
    def crossover(self):

        child = [[]] * len(self.binary_population)
        for i in range(0, (self.pop_size-self.preserved_num)):
            parent = random.sample(range(0, len(self.binary_population)), 2)

            # 行为原型交叉
            r1 = random.sample(range(0, (self.max_archetypes*self.ba_c)), 2)
            if r1[0] > r1[1]:
                a = r1[0]
                r1[0] = r1[1]
                r1[1] = a
            parent1_part1 = self.binary_population[parent[0]][0:(self.bit*self.max_archetypes*self.ba_c)]
            parent2_part1 = self.binary_population[parent[1]][0:(self.bit*self.max_archetypes*self.ba_c)]
            child1_part1 = parent2_part1[0:r1[0] * self.bit] + parent1_part1[r1[0] * self.bit:r1[1] * self.bit] + \
                           parent2_part1[r1[1] * self.bit:]
            child2_part1 = parent1_part1[0:r1[0] * self.bit] + parent2_part1[r1[0] * self.bit:r1[1] * self.bit] + \
                           parent1_part1[r1[1] * self.bit:]

            # 行为矩阵交叉
            r2 = random.sample(range(0, (self.max_archetypes*(self.ba_w+self.ba_r)), 2))
            if r2[0] > r2[1]:
                a = r2[0]
                r2[0] = r2[1]
                r2[1] = a
            parent1_part2 = self.binary_population[parent[0]][(self.bit*self.max_archetypes*self.ba_c):
                                                              (self.bit*self.max_archetypes*(self.ba_c+self.ba_w+self.ba_r))]
            parent2_part2 = self.binary_population[parent[1]][(self.bit*self.max_archetypes*self.ba_c):
                                                              (self.bit*self.max_archetypes*(self.ba_c+self.ba_w+self.ba_r))]
            child1_part2 = parent2_part2[0:r2[0] * self.bit] + parent1_part2[r2[0] * self.bit:r2[1] * self.bit] + \
                           parent2_part2[r2[1] * self.bit:]
            child2_part2 = parent1_part2[0:r2[0] * self.bit] + parent2_part2[r2[0] * self.bit:r2[1] * self.bit] + \
                           parent1_part2[r2[1] * self.bit:]
            child1 = child1_part1 + child1_part2
            child2 = child2_part1 + child2_part2
            a = random.random()
            if a < self.crossover_rate:
                child[i] = child1
            else:
                child[i] = child2
        self.binary_population = self.binary_population + child

    # 变异操作,不改变种群数量
    def mutate(self):
        # 采用随机位变异
        for i in range(0, len(self.binary_population)):
            if random.random() < self.mutation_rate:
                mun_bit = int((self.bit*self.max_archetypes*(self.ba_c+self.ba_w+self.ba_r)) * self.mutation_neighborhood)
                each_bit = random.sample(range(0, (self.bit*self.max_archetypes*(self.ba_c+self.ba_w+self.ba_r))), mun_bit)
                for j in range(0, len(each_bit)):
                    if self.binary_population[i][each_bit[j]] == 0:
                        self.binary_population[i][each_bit[j]] = 1
                    else:
                        self.binary_population[i][each_bit[j]] = 0

    # 将新种群编码为二进制形式
    def encode(self):

        def dec2bin(dec):
            binary = list()
            bin_dec = bin(dec)
            for i in range(2, len(bin_dec)):
                binary.append(int(bin_dec[i]))
            for i in range(2 + self.bit - len(bin_dec)):
                binary.insert(0, 0)
            return binary

        self.binary_population = [[] for i in range(self.preserved_num)]
        for ind, individual in enumerate(self.binary_population):
            for arch in range(self.max_archetypes):
                for c in range(self.ba_c):
                    current_weight = round(self.new_population[ind][arch][c]*(2**self.bit))
                    individual += dec2bin(current_weight)
            for arch in range(self.max_archetypes):
                for wr in range(self.ba_w + self.ba_r):
                    current_weight = round(self.new_population[ind][arch][self.ba_c + wr] * (2**self.bit - 1))
                    individual += dec2bin(current_weight)

    # 解码操作,将二进制编码解码为权重形式
    def decode(self):

        def bin2dec(binary_):
            binary_ = [str(i) for i in binary_]
            result = '0b' + ''.join(binary_)
            result = int(result, 2)
            return result

        # temp = self.new_population.copy()
        self.new_population.clear()
        for ind in range(len(self.binary_population)):
            individual = list()
            for bit in range(0, len(self.binary_population[ind]), self.bit):
                binary = self.binary_population[ind][bit:bit+self.bit]
                weight_value = bin2dec(binary) / (2**self.bit - 1)
                individual.append(weight_value)

            individual_arch = [[] for i in range(self.max_archetypes)]
            for arch in range(self.max_archetypes):
                individual_arch[arch] += individual[self.ba_c*arch:self.ba_c*(arch+1)]
                individual_arch[arch] += individual[self.ba_c*self.max_archetypes + (self.ba_w+self.ba_r)*arch:
                                                    self.ba_c*self.max_archetypes + (self.ba_w+self.ba_r)*(arch+1)]

            self.new_population.append(individual_arch)

    def save_pop(self):

        score_sum = list()
        score_sum_individual = np.sum(self.score, axis=1)

        for i in range(self.pop_size):
            individual_score = [i, score_sum_individual[i]]
            score_sum.append(individual_score)
        score_sum = sorted(score_sum, key=lambda x: x[1], reverse=True)

        open(os.path.dirname(__file__) + '/weight_model.txt', 'w')
        with open(os.path.dirname(__file__) + '/weight_model.txt', 'a') as f:
            for i in range(self.pop_size):
                rank = score_sum[i][0]
                f.write('Score: ' + str(score_sum[i][1]) + '\n')
                for arch in self.population[rank]:
                    f.write('Archetype: ')
                    for ele in arch:
                        f.write(str(round(ele, 3)) + ' ')
                    f.write('\n')
                f.write('\n' + '\n')
        pass
