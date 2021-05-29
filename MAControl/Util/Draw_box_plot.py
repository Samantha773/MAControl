import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd


def get_box(data_num, tc):

    r1 = raw_data(data_num, 'TestN2-OK-A-Partial', 10)
    r2 = raw_data(data_num, 'TestN1-OK-A-Partial', 15)
    r3 = raw_data(data_num, 'Test1-OK-A-Partial',  20)
    r4 = raw_data(data_num, 'TestN3-OK-A-Partial', 25)

    g = 5

    rr1 = np.array([[r1[i][j][199] for j in range(32)] for i in range(g)]).T.reshape((4, 8*g), order='F') if tc == 1 \
        else np.zeros((4, 8*g))
    rr2 = np.array([[r2[i][j][199] for j in range(32)] for i in range(g)]).T.reshape((4, 8*g), order='F') if tc == 2 \
        else np.zeros((4, 8*g))
    rr3 = np.array([[r3[i][j][199] for j in range(32)] for i in range(g)]).T.reshape((4, 8*g), order='F') if tc == 3 \
        else np.zeros((4, 8*g))
    rr4 = np.array([[r4[i][j][199] for j in range(32)] for i in range(g)]).T.reshape((4, 8*g), order='F') if tc == 4 \
        else np.zeros((4, 8*g))

    r = np.concatenate((rr1, rr2, rr3, rr4), axis=1)
    box = pd.DataFrame(r)

    return box


def raw_data(data_num, name, uav_num):

    curdir = os.path.dirname(__file__)
    pardir = os.path.dirname(os.path.dirname(curdir))
    path = '/track/' + name

    coverage_set = list()

    for i in range(data_num):
        raw = np.loadtxt(pardir + path + '/cover_rate-' + str(uav_num) + '-1000-%d.txt' % i, comments='#')
        gen_list = list()
        for ind in range(8):
            for loop in range(4):
                k_index = (ind * 4 + loop) * 200 + 0
                array = raw[k_index:k_index + 200].T[1]
                gen_list.append(list(array))
        coverage_set.append(gen_list)

    return coverage_set


def set_group_color(f, k):

    for whisker in f['whiskers']:
        whisker.set(color=plt.get_cmap('tab10')(k), alpha=0.5, linewidth=0.3)
    for box in f['boxes']:
        box.set(color=plt.get_cmap('tab10')(k), alpha=0.5, linewidth=0.3)
        box.set(facecolor=plt.get_cmap('tab10')(k), alpha=0.5, linewidth=0.3)
    for median in f['medians']:
        median.set(color=plt.get_cmap('tab10')(k), alpha=0.9, linewidth=2)


if __name__ == '__main__':

    plt.rcParams['figure.dpi'] = 1600
    data_num = 8

    co = [[] for k in range(4)]
    for k in range(4):
        control_box = get_box(data_num, k+1)
        co[k] = control_box.boxplot(showfliers=False, patch_artist=True, showcaps=False, return_type='dict')
        set_group_color(co[k], k)

    k1_list = [i*20 for i in range(9)]   # actual
    # k2_list = ['', r'$\gamma = \frac{1}{3}\pi$', '', r'$\gamma = \frac{2}{3}\pi$',
    #           '', r'$\gamma = \pi$', '', r'$\gamma = \frac{4}{3}\pi$', '']  # show
    k2_list = ['', r'$N_A = 10$', '', r'$N_A = 15$', '', r'$N_A = 20$', '', r'$N_A = 25$', '']  # show
    plt.xticks(k1_list, k2_list)

    font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 13}
    plt.ylabel('Cover-Rate', font)

    plt.xlim((0, 160))
    plt.ylim((0.6, 1))
    curdir = os.path.dirname(__file__)
    pardir = os.path.dirname(os.path.dirname(curdir))
    plt.savefig(pardir+'/track/-plot-/draw-uav.png')
    plt.show()
