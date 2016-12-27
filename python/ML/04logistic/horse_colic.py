from numpy import mat, shape, array
from log_regies import sigmoid, stoc_grad_ascent1


def classify_vector(int_x, weights):
    prob = sigmoid(sum(int_x * weights))
    if prob > 0.5:
        return 1.0
    else:
        return 0.0


def colic_test():
    fr_train = open('test/horseColicTraining.txt')
    fr_test = open('test/horseColicTest.txt')
    train_set, train_labels = [], []
    for line in fr_train.readlines():
        current_line = line.split()
        current_vec = map(float, current_line)
        train_set.append(current_vec[: -1])
        train_labels.append(current_vec[-1])
    print shape(mat(train_set))
    print shape(mat(train_labels))
    weight = stoc_grad_ascent1(array(train_set), train_labels, 500)
    data_count, err_count = 0, 0
    for line in fr_test.readlines():
        data_count += 1
        current_line = line.split()
        current_vec = map(float, current_line)
        test_vec = current_vec[: -1]
        test_label = current_vec[-1]
        cal_label = classify_vector(test_vec, weight)
        if cal_label != test_label:
            err_count += 1
    print 'error percent is', float(err_count) / data_count

if __name__ == '__main__':
    colic_test()
