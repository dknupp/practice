import pytest
from binary_search_tree import Tree


@pytest.fixture
def tree():
    '''
          10
        0    15
     -2    4    18
    '''
    t = Tree()
    for n in (10, 15, 0, 4, 18, -2):
        t.insert(n)
    return t


def test_tree_insert(tree):
    assert tree.root.val == 10
    assert tree.find(10)


def test_tree_find_smaller_than_root(tree):
    assert tree.find(4)


def test_tree_find_larger_than_root(tree):
    assert tree.find(15)


def test_empty_tree_find_fails():
    t = Tree()
    assert t.find(10) is False


def test_tree_find_fails(tree):
    assert tree.find(999) is False


def test_tree_inorder_traversal(tree, capsys):
    # left, root, right
    tree.inorder()
    out, err = capsys.readouterr()
    assert out.split() == ['-2', '0', '4', '10', '15', '18']


def test_tree_preorder_traversal(tree, capsys):
    # root, left, right
    tree.preorder()
    out, err = capsys.readouterr()
    assert out.split() == ['10', '0', '-2', '4', '15', '18']


def test_tree_postorder_traversal(tree, capsys):
    # left, right, root
    tree.postorder()
    out, err = capsys.readouterr()
    assert out.split() == ['-2', '4', '0', '18', '15', '10']


'''
TEST OUTPUT
$ py.test -sv --cov binary_search_tree.py test_binary_search_tree.py
=================================================================================== test session starts ===================================================================================
platform darwin -- Python 2.7.11, pytest-2.8.5, py-1.4.31, pluggy-0.3.1 -- /Users/dknupp/venvs/dev/bin/python2.7
cachedir: .cache
rootdir: /Users/dknupp/Documents/code/practice/binary_search_tree, inifile:
plugins: cov-2.2.0
collected 8 items

test_binary_search_tree.py::test_tree_insert PASSED
test_binary_search_tree.py::test_tree_find_smaller_than_root PASSED
test_binary_search_tree.py::test_tree_find_larger_than_root PASSED
test_binary_search_tree.py::test_empty_tree_find_fails PASSED
test_binary_search_tree.py::test_tree_find_fails PASSED
test_binary_search_tree.py::test_tree_inorder_traversal PASSED
test_binary_search_tree.py::test_tree_preorder_traversal PASSED
test_binary_search_tree.py::test_tree_postorder_traversal PASSED
-------------------------------------------------------------------- coverage: platform darwin, python 2.7.11-final-0 ---------------------------------------------------------------------
Name                    Stmts   Miss  Cover
-------------------------------------------
binary_search_tree.py      66      2    97%

================================================================================ 8 passed in 0.02 seconds =================================================================================
'''
