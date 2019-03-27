# Filename: defaultdict_count_word.py
# Author: meizhaohui

def count_words(article):
    from collections import defaultdict as dt
    # replace \n to space,then split to list
    article_list = article.replace('\n',' ').split()
    # counts = {}
    counts = dt(int)
    for word in article_list:
        # if word not in counts:
        #     counts[word] = 1
        # else:
        #     counts[word] += 1
        counts[word] += 1
    print(counts)
    
    
if __name__ == '__main__':
    article='''This module implements specialized container datatypes providing
alternatives to Python's general purpose built-in containers, dict,
list, set, and tuple.

* namedtuple   factory function for creating tuple subclasses with named fields
* deque        list-like container with fast appends and pops on either end
* ChainMap     dict-like class for creating a single view of multiple mappings
* Counter      dict subclass for counting hashable objects
* OrderedDict  dict subclass that remembers the order entries were added
* defaultdict  dict subclass that calls a factory function to supply missing values
* UserDict     wrapper around dictionary objects for easier dict subclassing
* UserList     wrapper around list objects for easier list subclassing
* UserString   wrapper around string objects for easier string subclassing

'''
    count_words(article)