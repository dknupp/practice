import pytest
import timeit
from string_compression import groupby_compress, iterative_compress


@pytest.fixture
def simple_string():
    return 'abbcccddddeeeee'


@pytest.fixture
def random_string():
    return (
        'zFZqPw0fMh5zYTRgg75kFkRH5XXzmN3uvOu2JTVuDmu3Pozg9T'
        '84SKCVKrcO9qaiKw4lEoDwfz0gb81KQWb3hbiVZa8cNOKeWNIv'
        'sDs79U1NvYn3hmwa3BzWD4n4nODm39YXq7pKkwSHVkfnGlPwK2'
        'RAkCol6JkElrCM3grr4XEehD2oA30H8ONUA7onqcjIlJI2eyX6'
        'fQ9Uamz6SOjtxMJR5ApbcYPKcCIEycy9uviUqVIZoozDe6HYbx'
        'MXogKLjG3jTNXcZ8vwI7DcsAU697ubD8MBE2N20eJMmpl5k5y0'
        'yGWkYbup2q04yLsKAYVSKglrfLLexmCIo1p7yZE8siVeOxPYR6'
        '3ypIiUxSW1Dqri1tzFWfbZnlvUrklcRiYwN0capHhO7kYmlsYF'
        'M83MTqMZpQoqqtwSAFKK5eYNWS7e79o4tO2ScJQ2DckxQw19ip'
        'qf4IHjzkHZmmnXtlZOPczOgryGi6YbzhX5hcenr1LUrr3vCa48'
        '5cmPawVBeXWqVfCwOkoxyBaR5MiuWHoAOkmnHwrhegNjqR3ONe'
        'tOl9ie3lNKz8MqoEMyFZ6Y3o63Ji7TmWw3QS0UprT7RD04R2wM'
        'GH4oVSPEyvfW8Sgn4O7JSOavWCX0yO3ozt412BeY6MIuOvW2EU'
        'JTB5DanplTGGyzbs21oe4n1syDUuHsFl2QVcVr45qSrN9tru2V'
        'MW5ilTnx0SWqQ0vmHiXqxDel4eMHtKnZ8nzkQJEc0EcHWpULAM'
        'HbieLFyyNTfL0C4QnmHm7tMt2NkA3EMJb5xRKq6MhFgufWBK45'
        'aEBfXJkZSwswTlSn9igJmvgLCMzUfkoLPXNZaLIA9DnZbRaXV2'
        'YSsbtta3PnhCS3HlFxeqtvMz41SEiERPtcyY8fafEykASq02M2'
        'QMiY1jrxSsbl06MfBs5EUU1H4GDqQg4brfKHHoB8I13Km2e0iQ'
        'bxNIj7otOxo4OQfIBZmu6iE0F91uxNgnRmy3ghAC595LMBG8Ip'
        'Ae6A8TnwKsbRAV2XO1xeT29HmbMYVlRvIbSitsYTuDYHwXhmPz'
        'gnnvSagDjvNW9PEiD8EfeUvlQluD1YsU0oQ6GRHGvmRGoi1fyu'
        'GvcIszYZe7o1scSkgsihIyr0IVSzCm2wPbf1Pl8UnqSbYtU99I'
        'EqZxvjFqq1TGcSpkVtKngz84DulOMqy85bMI6DAlvF0cJuAysb'
        'PUiXioFr0KE9TKJaRZKwVvRoQqNyF03GnNhhnRzvUYl4qhfAWi'
        '5kcVbCsasTsl1USUDLcKpIReI1CoHtc4xetD7ZDE4BR5yDFHST'
    )


@pytest.fixture
def compressible_string():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join([char * 50 for char in alphabet])


# Helper function
def function_timer(func, *args, **kwargs):
    def wrapped_func():
        return func(*args, **kwargs)
    return wrapped_func


def test_iterative_compress(simple_string):
    compressed = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
    assert iterative_compress(simple_string) == compressed


def test_groupby_compress(simple_string):
    compressed = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
    assert groupby_compress(simple_string) == compressed


@pytest.mark.parametrize('input_type',
                         [simple_string, compressible_string, random_string])
def test_compression_results_match(input_type):
    print '%s ' % input_type.__name__,
    groupby_results = groupby_compress(input_type())
    iterative_results = iterative_compress(input_type())
    assert groupby_results == iterative_results


@pytest.mark.parametrize('input_type',
                         [simple_string, compressible_string, random_string])
def test_compression_time_10k_iterations(input_type):
    print '%s --' % input_type.__name__,

    groupby_timer = function_timer(groupby_compress, input_type())
    groupby_results = timeit.timeit(groupby_timer, number=10000)

    iteration_timer = function_timer(iterative_compress, input_type())
    iteration_results = timeit.timeit(iteration_timer, number=10000)

    print 'groupby: {} iteration: {} '.format(groupby_results, iteration_results),


'''
TEST OUTPUT:
$ py.test -sv test_string_compression.py
==================================================================================== test session starts ====================================================================================
platform darwin -- Python 2.7.11, pytest-2.8.5, py-1.4.31, pluggy-0.3.1 -- /Users/dknupp/venvs/dev/bin/python2.7
cachedir: .cache
rootdir: /Users/dknupp/Documents/code/practice/string_compression, inifile:
plugins: cov-2.2.0
collected 8 items

test_string_compression.py::test_iterative_compress PASSED
test_string_compression.py::test_groupby_compress PASSED
test_string_compression.py::test_compression_results_match[input_type0] simple_string PASSED
test_string_compression.py::test_compression_results_match[input_type1] compressible_string PASSED
test_string_compression.py::test_compression_results_match[input_type2] random_string PASSED
test_string_compression.py::test_compression_time_10k_iterations[input_type0] simple_string -- groupby: 0.074786901474 iteration: 0.0289478302002 PASSED
test_string_compression.py::test_compression_time_10k_iterations[input_type1] compressible_string -- groupby: 0.737244129181 iteration: 1.03705096245 PASSED
test_string_compression.py::test_compression_time_10k_iterations[input_type2] random_string -- groupby: 15.5530238152 iteration: 2.28075313568 PASSED

================================================================================= 8 passed in 19.73 seconds =================================================================================
'''
