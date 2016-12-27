from bayes import *


def text_parse(context):
    import re
    list_of_tokens = re.split(r'\W*', context)
    list_of_tokens = filter(lambda x: len(x) > 3, list_of_tokens)
    list_of_tokens = map(str.lower, list_of_tokens)
    return list_of_tokens


def spam_test():
    ham_file = 'email/ham/%d.txt'
    spam_file = 'email/spam/%d.txt'
    doc_list = []
    full_text = []
    class_list = []
    # Initial training docs.
    for i in range(1, 26):
        word_list = text_parse(open(ham_file % i).read())
        doc_list.append(word_list)
        full_text.extend(word_list)
        class_list.append('ham')
        word_list = text_parse(open(spam_file % i).read())
        doc_list.append(word_list)
        full_text.extend(word_list)
        class_list.append('spam')
    # Construct test bunch.
    vocab_list = create_vocab_list(doc_list)
    test_set = []
    test_classes = []
    for i in range(10):
        rand_index = int(random.uniform(0, len(doc_list)))
        test_set.append(doc_list.pop(rand_index))
        test_classes.append(class_list.pop(rand_index))
    # Training emails.
    train_matrix = []
    train_classes = []
    for index, doc in enumerate(doc_list):
        train_matrix.append(set_of_words2vec(vocab_list, doc))
        train_classes.append(class_list[index])
    p_classes, p_cls_vocs, _ = trainNB0(train_matrix, train_classes)
    #####
    # Using to show
    #####
    # print p_classes, p_cls_vocs
    # for cls in p_cls_vocs:
    #     print cls
    #     print ''.join(map(str.ljust, vocab_list, [20] * len(vocab_list)))
    #     print ''.join(map(str.ljust, map(str, p_cls_vocs[cls]), [20] * len(vocab_list)))
    # Test training.
    error_count = 0
    for index, doc in enumerate(test_set):
        word_vec = set_of_words2vec(vocab_list, doc)
        test_class = classifyNB(word_vec, p_cls_vocs, p_classes)
        if test_class != test_classes[index]:
            error_count += 1
    err_percent = error_count / 10.0
    print 'err_percent is ', err_percent

if __name__ == '__main__':
    spam_test()
