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
