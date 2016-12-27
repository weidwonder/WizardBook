from numpy import mat, shape, ones, exp, array, arange
import random


def load_data_set():
    data_mat = []
    label_mat = []
    fr = open('test/testSet.txt')
    for line in fr.readlines():
        line_arr = line.strip().split()
        data_mat.append([1.0, float(line_arr[0]), float(line_arr[1])])
        label_mat.append(int(line_arr[2]))
    return data_mat, label_mat


def sigmoid(x):
    return 1.0 / (1 + exp(-x))
    # return 0.5 + (0 if x == 0 else (0.5 if x > 0 else -0.5))


def grad_ascent(data_mat_in, class_labels):
    data_matrix = mat(data_mat_in)
    label_matrix = mat(class_labels).transpose()
    m, n = shape(data_matrix)
    alpha = 0.001
    max_circles = 500
    weights = ones((n, 1))
    for k in xrange(max_circles):
        # print data_matrix * weights
        h = sigmoid(data_matrix * weights)
        error = (label_matrix - h)
        weights += alpha * data_matrix.transpose() * error
    return weights


def plot_best_fit(wei):
    import matplotlib.pyplot as plt
    weight = wei.getA()
    data_matrix, label_matrix = load_data_set()
    data_arr = array(data_matrix)
    n = shape(data_arr)[0]
    x_cord1, y_cord1 = [], []
    x_cord2, y_cord2 = [], []
    for i in range(n):
        if int(label_matrix[i]) == 1:
            x_cord1.append(data_arr[i, 1])
            y_cord1.append(data_arr[i, 2])
        else:
            x_cord2.append(data_arr[i, 1])
            y_cord2.append(data_arr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x_cord1, y_cord1, s=30, c='red', marker='s')
    ax.scatter(x_cord2, y_cord2, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weight[0] - weight[1] * x) / weight[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()


def stoc_grad_ascent(data_matrix, class_labels):
    """
    Core of logistic regression algorithm. Calculate weight from data_matrix.
    :param data_matrix:
    :param class_labels:
    :return:
    """
    m, n = shape(data_matrix)
    weights = ones(n)
    alpha = 0.01
    for index, arr in enumerate(data_matrix):
        error = class_labels[index] - sigmoid(sum(arr * weights))
        weights += alpha * error * arr
    return weights


def stoc_grad_ascent1(data_matrix, class_labels, num_iter=150):
    m, n = shape(data_matrix)
    weights = ones(n)
    for j in xrange(num_iter):
        data_index = range(m)
        for i in xrange(m):
            alpha = 1.0 / (1 + j + i) + 0.01
            rand_index = int(random.uniform(0, len(data_index)))
            h = sigmoid(sum(data_matrix[rand_index] * weights))
            error = class_labels[rand_index] - h
            weights += alpha * error * data_matrix[rand_index]
            del data_index[rand_index]
    return weights


if __name__ == '__main__':
    data_arr, label_mat = load_data_set()
    weight = stoc_grad_ascent1(array(data_arr), label_mat)
    print weight
    # weight = grad_ascent(array(data_arr), label_mat)
    # print weight
    plot_best_fit(weight)
