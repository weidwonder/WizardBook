'''
Created on Oct 19, 2010

@author: Peter
'''
from collections import Counter
from numpy import *
import numpy


def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec


def create_vocab_list(data_set):
    """
    According to data_set to make a words set.
    :param data_set:
    :return:
    """
    vocab_set = set()
    for document in data_set:
        vocab_set.update(document)
    return list(vocab_set)


def set_of_words2vec(vocab_list, input_set):
    return_vec = [0] * len(vocab_list)
    for vocab in input_set:
        index = vocab_list.index(vocab)
        return_vec[index] += 1
    return return_vec


def cal_p_category(train_category):
    c = Counter(train_category)
    sum = float(len(train_category))
    category_p = {}
    for k, v in c.items():
        category_p[k] = v / sum
    return category_p


def convert_doc2matrix(docs):
    """
    This method convert word docs to digit matrix.
    :param docs:
    :return: a 2-dimension array.
    """
    word_set = create_vocab_list(docs)
    matrix = []
    for doc in docs:
        word_vec = set_of_words2vec(word_set, doc)
        matrix.append(word_vec)
    return matrix


def trainNB0(train_matrix, train_category):
    """
    This function is the method of train samples.
    :param train_matrix:
    :param train_category:
    :return:
    """
    category_ps = cal_p_category(train_category)
    c = Counter(train_category)
    num_of_vocabs = len(train_matrix[0])
    all_vocab_list = numpy.zeros(num_of_vocabs) + 1
    category_vocab_list = {k: numpy.zeros(num_of_vocabs) + 1 for k in category_ps.keys()}
    for index, doc in enumerate(train_matrix):
        doc = numpy.array(doc)
        all_vocab_list = all_vocab_list + doc
        category = train_category[index]
        category_vocab_list[category] += numpy.array(doc)
    p_all_vocab = map(math.log, all_vocab_list / sum(all_vocab_list))
    p_category_vocab = {}
    for category, v_list in category_vocab_list.items():
        p_category_vocab[category] = map(math.log, v_list / c[category])
    return category_ps, p_category_vocab, p_all_vocab


def classifyNB(vec2classify, p_category_vocab, category_ps):
    p4categories = {}
    for category, p_list in p_category_vocab.items():
        p4categories[category] = sum(vec2classify * numpy.array(p_list)) + category_ps[category]
    p_classes_sorted = sorted(p4categories, key=lambda x: p4categories[x], reverse=True)
    return p_classes_sorted[0]


if __name__ == '__main__':
    data_set, category = loadDataSet()
    word_vec = create_vocab_list(data_set)
    data_matrix = convert_doc2matrix(data_set)
    p_classes, p_category_dic, _ = trainNB0(data_matrix, category)
    test_words = loadDataSet()[0][1]
    print test_words
    test_vec = set_of_words2vec(word_vec, test_words)
    print classifyNB(test_vec, p_category_dic, p_classes)
