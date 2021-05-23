import numpy as np
import os
import matplotlib.pyplot as plt


def draw_contrast_plot(data_num, name, up_, down_):

    curdir = os.path.dirname(__file__)
    pardir = os.path.dirname(os.path.dirname(curdir))
    path = '/track/' + name

    coverage_set = list()

    for i in range(data_num):
        coverage_set.append(np.loadtxt(pardir + path + '/cover_rate-5-100-%d.txt' % i, comments='#'))

    lt, _ = coverage_set[0].shape

    per_up = np.zeros(int(lt/20))
    per_median = np.zeros(int(lt/20))
    per_down = np.zeros(int(lt/20))

    for le in range(int(lt/20)):
        cur = np.array([coverage_set[k][le*20:(le+1)*20-1][1] for k in range(data_num)])
        per_up[le] = np.percentile(cur, up_)
        per_median[le] = np.percentile(cur, 50)
        per_down[le] = np.percentile(cur, down_)

    return per_up, per_median, per_down, int(lt/20)


if __name__ == '__main__':

    plt.rcParams['figure.dpi'] = 800
    plt.figure()
    line = plt.gca()

    data_num_ = 2
    up = 75
    down = 25

    # set controlled group parameters
    folder_con = '05-22-OK-A'
    con_color = 'red'
    con_up, con_median, con_down, size = draw_contrast_plot(data_num_, folder_con, up, down)

    # set experimental group parameters
    # folder_tr = 'experimental'
    # tr_color = 'green'
    # tr_up, tr_median, tr_down, size = draw_contrast_plot(data_num_, folder_tr, 20, 4000, up, down)

    # draw controlled group
    plt.fill_between(range(0, size), con_down, con_up, facecolor=con_color, alpha=0.1)
    line.plot(range(0, size), con_median, con_color, label='scene A')

    # draw experimental group
    # plt.fill_between(range(0, size), tr_down, tr_up, facecolor=tr_color, alpha=0.1)
    # line.plot(range(0, size), tr_median, tr_color, label='action by RL model')

    k1_list = [i*8 for i in range(17)]  # actual
    k2_list = [i for i in range(17)]  # show
    plt.xticks(k1_list, k2_list)
    plt.xlim(0, 150)
    plt.ylim(0, 1)

    # # set 1-10000 group parameters
    # folder_1 = '1'
    # color_1 = 'red'
    # up_1, median_1, down_1, size = draw_contrast_plot(data_num_, folder_1, 1, 10000, up, down)
    #
    # # set 3-10000 group parameters
    # folder_3 = '3'
    # color_3 = 'green'
    # up_3, median_3, down_3, size = draw_contrast_plot(data_num_, folder_3, 3, 10000, up, down)
    #
    # # set 5-10000 group parameters
    # folder_5 = '5'
    # color_5 = 'blue'
    # up_5, median_5, down_5, size = draw_contrast_plot(data_num_, folder_5, 5, 10000, up, down)
    #
    # # set 10-10000 group parameters
    # folder_10 = '10'
    # color_10 = 'purple'
    # up_10, median_10, down_10, size = draw_contrast_plot(data_num_, folder_10, 10, 10000, up, down)
    #
    # # set 20-10000 group parameters
    # folder_20 = '20'
    # color_20 = 'black'
    # up_20, median_20, down_20, size = draw_contrast_plot(data_num_, folder_20, 20, 10000, up, down)
    #
    # # draw 1-10000 group
    # plt.fill_between(range(0, size), down_1, up_1, facecolor=color_1, alpha=0.1)
    # line.plot(range(0, size), median_1, color_1, label='1 UAV')
    #
    # # draw 3-10000 group
    # plt.fill_between(range(0, size), down_3, up_3, facecolor=color_3, alpha=0.1)
    # line.plot(range(0, size), median_3, color_3, label='3 UAVs')
    #
    # # draw 5-10000 group
    # plt.fill_between(range(0, size), down_5, up_5, facecolor=color_5, alpha=0.1)
    # line.plot(range(0, size), median_5, color_5, label='5 UAVs')
    #
    # # draw 10-10000 group
    # plt.fill_between(range(0, size), down_10, up_10, facecolor=color_10, alpha=0.1)
    # line.plot(range(0, size), median_10, color_10, label='10 UAVs')
    #
    # # draw 20-10000 group
    # plt.fill_between(range(0, size), down_20, up_20, facecolor=color_20, alpha=0.1)
    # line.plot(range(0, size), median_20, color_20, label='20 UAVs')
    #
    # plt.xticks([0, 500, 1000, 1500, 2000], [0, 2500, 5000, 7500, 10000])
    # plt.xlim(0, 2000)
    # plt.ylim(0, 1.03)

    font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 13}
    plt.xlabel('Individual', font)
    plt.ylabel('Coverage Rate', font)
    plt.legend(loc=4)
    plt.grid()
    curdir = os.path.dirname(__file__)
    pardir = os.path.dirname(os.path.dirname(curdir))
    plt.savefig(pardir+'/track/-plot-/draw2.png')
    plt.show()
