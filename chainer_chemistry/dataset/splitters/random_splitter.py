import numpy
from chainer_chemistry.dataset.splitters.base_splitter import BaseSplitter


class RandomSplitter(BaseSplitter):
    """Class for doing random data splits.

    Parameters
    ----------
    dataset: NumpyTupleDataset, numpy.ndarray
        Dataset.
    seed: int (Optional, Default None)
        Random seed.
    frac_train: float (Optional, Default .8)
        Fraction of dataset put into training data.
    frac_valid: float (Optional, Default .1)
        Fraction of dataset put into validation data.
    frac_test: float (Optional, Default .1)
        Fraction of dataset put into test data.
    converter: callable
    return_index: Boolean (Optional, Default True)
        If `True`, this function returns only indexes. If `False`, this
        function returns splitted dataset.

    Returns
    -------
    SplittedDataset : tuple (train, valid, test)
        splitted dataset or indexes

    Examples
    --------
    >>> from chainer_chemistry.datasets import NumpyTupleDataset
    >>> from chainer_chemistry.dataset.splitters import RandomSplitter
    >>> a = numpy.random.random((10, 10))
    >>> b = numpy.random.random((10, 8))
    >>> c = numpy.random.random((10, 1))
    >>> d = NumpyTupleDataset(a, b, c)
    >>> splitter = RandomSplitter()
    >>> splitter.train_valid_test_split()
    >>> train, valid, test =
                splitter.train_valid_test_split(dataset, return_index=False)
    >>> print(len(train), len(valid), len(test))
    8, 1, 1
    """
    def _split(self, dataset, frac_train=0.8, frac_valid=0.1, frac_test=0.1,
               **kwargs):
        seed = kwargs.get('seed', None)
        numpy.testing.assert_almost_equal(frac_train + frac_valid + frac_test,
                                          1.)

        if seed is not None:
            perm = numpy.random.RandomState(seed).permutation(len(dataset))
        else:
            perm = numpy.random.permutation(len(dataset))
        train_data_size = int(len(dataset) * frac_train)
        valid_data_size = int(len(dataset) * frac_valid)
        return (perm[:train_data_size],
                perm[train_data_size:train_data_size + valid_data_size],
                perm[train_data_size + valid_data_size:])
