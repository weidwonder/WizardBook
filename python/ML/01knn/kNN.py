from numpy import array, tile, zeros
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(in_x, data_set, labels, k):
    """This method is the core of KNN.
    :param in_x: vector of test.
    :param data_set: Data set you already you have.
    :param labels: Data set labels.
    :param k: K
    :return: The tag most probably is.
    """
    data_set_size = data_set.shape[0]
    diff_mat = tile(in_x, (data_set_size, 1)) - data_set
    sq_diff_mat = diff_mat ** 2
    sq_distance = sq_diff_mat.sum(axis=1)
    distances =sq_distance ** 0.5
    sorted_dist_indices = distances.argsort()
    class_count = {}
    for i in range(k):
        vote_i_label = labels[sorted_dist_indices[i]]
        class_count[vote_i_label] = class_count
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def file2matrix(filename):
    fr = open(filename)
    array_of_lines = fr.readlines()
    number_of_lines = len(array_of_lines)
    ret_matrix = zeros((number_of_lines, 3))
    class_label_vector = []
    index = 0
    for line in array_of_lines:
        line = line.strip()
        list_from_line = line.split('\t')
        ret_matrix[index, :] = list_from_line[:3]
        class_label_vector.append(int(list_from_line[-1]))
        index += 1
    return ret_matrix, class_label_vector

def auto_norm(data_set):
    min_vals = data_set.min(0)
    max_vals = data_set.max(0)
    ranges = max_vals - min_vals
    m = data_set.shape[0]
    norm_data_set = data_set - tile(min_vals, (m, 1))
    norm_data_set = norm_data_set/tile(ranges, (m, 1))
    return norm_data_set, ranges, min_vals

def dating_class_test():
    ho_ratio = 0.10
    dating_data_mat, dating_labels = file2matrix('datingTestSet2.txt')
    norm_mat, ranges, min_vals = auto_norm(dating_data_mat)
    m = norm_mat.shape[0]
    num_test_vecs = int(m * ho_ratio)
    err_count = 0.0
    for i in range(num_test_vecs):
        classifier_result = classify0(norm_mat[i, :], norm_mat[num_test_vecs: m, :],
                                      dating_labels[num_test_vecs: m], 3)
        print "the classifier came back with: %d, the real answer is: %d" % \
              (classifier_result, dating_labels[i])
        if (classifier_result != dating_labels[i]):
            err_count += 1
    print "the total error rate is: %f" % (err_count / num_test_vecs)

if __name__ == '__main__':
    # print classify0(array([0.5, 0]), createDataSet()[0], createDataSet()[1], 2)
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    print datingDataMat
    import matplotlib
    import matplotlib.pyplot as plt
    fig = plt.figure()
    datingDataMat = auto_norm(datingDataMat)[0]
    ax = fig.add_subplot(111)
    # ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
    # plt.show()
    # ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
    ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
    plt.show()

    dating_class_test()