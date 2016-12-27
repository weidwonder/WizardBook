# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import matplotlib.pyplot as plt

decision_node = {
    'boxstyle': 'sawtooth',
    'fc': '0.8',
}
leaf_node = {
    'boxstyle': 'round4',
    'fc': '0.8'
}
arrow_args = {
    'arrowstyle': '<-'
}


def plot_node(node_txt, center_pt, parent_pt, node_type):
    create_plot.ax1.annotate(node_txt, xy=parent_pt, xycoords='axes fraction',
                             xytext=center_pt, textcoords='axes fraction', va='center',
                             ha='center', bbox=node_type, arrowprops=arrow_args)


def create_plot(in_tree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    create_plot.ax1 = plt.subplot(111, frameon=False, **axprops)
    plot_tree.total_w = float(get_num_leafs(in_tree))
    plot_tree.total_d = float(get_tree_depth(in_tree))
    plot_tree.xOff = -0.5 / plot_tree.total_w
    plot_tree.yOff = 1.0
    plot_tree(in_tree, (0.5, 1.0), '')
    plt.show()


def get_num_leafs(my_tree):
    num_leafs = 0
    label = my_tree.keys()[0]
    decision_dic = my_tree[label]
    for key in decision_node.keys():
        if isinstance(decision_node[key], dict):
            num_leafs += get_num_leafs(decision_dic)
        else:
            num_leafs += 1
    return num_leafs


def plot_mid_text(cntr_pt, parent_pt, txt_string):
    x_mid = (parent_pt[0] - cntr_pt[0]) / 2.0 + cntr_pt[0]
    y_mid = (parent_pt[1] - cntr_pt[1]) / 2.0 + cntr_pt[1]
    create_plot.ax1.text(x_mid, y_mid, txt_string)


def plot_tree(my_tree, parent_pt, node_txt):
    num_leafs = get_num_leafs(my_tree)
    depth = get_tree_depth(my_tree)
    label = my_tree.keys()[0]
    cntr_pt = (plot_tree.xOff + (1.0 + float(num_leafs)) / 2.0 / plot_tree.total_w, plot_tree.yOff)
    plot_mid_text(cntr_pt, parent_pt, node_txt)
    plot_node(label, cntr_pt, parent_pt, decision_node)
    second_dict = my_tree[label]
    plot_tree.yOff = plot_tree.yOff - 1.0 / plot_tree.total_d
    for key in second_dict.keys():
        if isinstance(second_dict[key], dict):
            plot_tree(second_dict[key], cntr_pt, str(key))
        else:
            plot_tree.xOff = plot_tree.xOff + 1.0 / plot_tree.total_w
            plot_node(second_dict[key], (plot_tree.xOff, plot_tree.yOff), cntr_pt, leaf_node)
            plot_mid_text((plot_tree.xOff, plot_tree.yOff), cntr_pt, str(key))
    plot_tree.yOff = plot_tree.yOff + 1.0 / plot_tree.total_d


def get_tree_depth(my_tree):
    max_depth = 0
    label = my_tree.keys()[0]
    decision_dic = my_tree[label]
    for key in decision_dic.keys():
        if isinstance(decision_dic[key], dict):
            this_depth = 1 + get_tree_depth(decision_dic[key])
        else:
            this_depth = 1
        max_depth = max(this_depth, max_depth)
    return max_depth


def retrieve_tree(i):
    list_of_trees = [
        {
            'no surfacing': {
                0: 'no',
                1: {
                    'flippers': {
                        0: 'no',
                        1: 'yes',
                    }
                }
            }
        },
        {
            'no surfacing': {
                0: 'no',
                1: {
                    'flippers':{
                        0: {
                            'head': {
                                0: 'no',
                                1: 'yes',
                            }
                        },
                        1: 'no',
                    }
                }
            }
        }
    ]
    return list_of_trees[i]


if __name__ == '__main__':
    # create_plot()
    tree = retrieve_tree(0)
    print tree
    print get_tree_depth(tree)
    print get_num_leafs(tree)
    create_plot(tree)
