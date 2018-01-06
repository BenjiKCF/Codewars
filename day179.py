def name_shuffler(str_):
    str_ = str_.split(' ')
    return ' '.join([str_[1], str_[0]])

print name_shuffler('john McClane')
