from numpy import zeros
from os import listdir
from kNN import classify0


def img2vector(filename):
    return_vect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        line_str = fr.readline()
        for j in range(32):
            return_vect[0, 32* i + j] = int(line_str[j])
    return return_vect

def hand_writing_class_test():
    hw_labels = []
    training_file_list = listdir('trainingDigits')
    m = len(training_file_list)
    training_mat = zeros((m, 1024))
    for i in range(m):
        file_name_str = training_file_list[i]
        file_str = file_name_str.split('.')[0]
        class_num_str = int(file_str.split('_')[0])
        hw_labels.append(class_num_str)
        training_mat[i, :] = img2vector('trainingDigits/' + file_name_str)
    test_file_list = listdir('testDigits')
    error_count = 0.0
    m_test = len(test_file_list)
    for i in range(m_test):
        file_name_str = test_file_list[i]
        file_str = file_name_str.split('.')[0]
        class_num_str = int(file_str.split('_')[0])
        vector_under_test = img2vector('testDigits/' + file_name_str)
        classifier_result = classify0(vector_under_test, training_mat, hw_labels, 3)
        print 'the classifier came back with: %d, the real answer is: %d,' % (classifier_result, class_num_str)
        if classifier_result != class_num_str:
            error_count += 1
    print "the total number of errors is: %d" % error_count
    print "the total error rate is: %f" % (error_count/float(m_test))

if __name__ == '__main__':
    hand_writing_class_test()
