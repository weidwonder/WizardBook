import operator

try:
    from cmath import log
except:
    from math import log
from collections import Counter


def calc_shannon_ent(data_set):
    """ Entropy calculating method.
    :param data_set:
    :return:
    """
    num_entries = len(data_set)
    label_counts = Counter([vec[-1] for vec in data_set])
    shanno_ent = 0.0
    for key in label_counts:
        prob = float(label_counts[key]) / num_entries
        shanno_ent -= prob * log(prob, 2).real
    return shanno_ent


def create_data_set():
    data_set = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no'],
    ]
    labels = ['no surfacing', 'flippers']
    return data_set, labels


def split_data_set(data_set, axis, value):
    """ Pick up all vectors that element at index of axis equal to value.
    :param data_set:
    :param axis:
    :param value:
    :return:
    """
    ret_data_set = []
    for feat_vec in data_set:
        if feat_vec[axis] == value:
            reduce_feat_vec = feat_vec[:axis]
            reduce_feat_vec.extend(feat_vec[axis + 1:])
            ret_data_set.append(reduce_feat_vec)
    return ret_data_set


def choose_best_feature_to_split(data_set):
    num_features = len(data_set[0]) - 1
    base_entropy = calc_shannon_ent(data_set)
    best_info_gain = 0.0
    best_feature = -1
    for i in range(num_features):
        feat_list = [example[i] for example in data_set]
        unique_vals = set(feat_list)
        new_entropy = 0.0
        for value in unique_vals:
            sub_data_set = split_data_set(data_set, i, value)
            prob = len(sub_data_set) / len(data_set)
            new_entropy += prob * calc_shannon_ent(sub_data_set)
        info_gain = base_entropy - new_entropy
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature = i
    return best_feature


def majority_cnt(class_list):
    class_count = Counter(class_list)
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def create_tree(data_set, labels):
    class_list = [example[-1] for example in data_set]
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    if len(data_set[0]) == 1:
        return majority_cnt(class_list)
    best_feat = choose_best_feature_to_split(data_set)
    best_feat_label = labels[best_feat]
    my_tree = {best_feat_label: {}}
    del labels[best_feat]
    feat_values = [example[best_feat] for example in data_set]
    unique_vals = set(feat_values)
    for value in unique_vals:
        sub_labels = labels[:]
        my_tree[best_feat_label][value] = create_tree(split_data_set(data_set, best_feat, value), sub_labels)
    return my_tree


def classify(input_tree, feat_labels, test_vec):
    label = input_tree.keys()[0]
    second_dict = input_tree[label]
    feat_index = feat_labels
    key = test_vec[feat_index]
    if isinstance(second_dict[key], dict):
        class_label = classify(second_dict[key], feat_labels, test_vec)
    else:
        class_label = second_dict[key]
    return class_label


if __name__ == '__main__':
    my_dat, labels = create_data_set()
    print calc_shannon_ent(my_dat)
    print split_data_set(my_dat, 0, 1)
    print split_data_set(my_dat, 0, 0)
    print choose_best_feature_to_split(my_dat)
    print '+' * 30
    print create_tree(my_dat, labels)