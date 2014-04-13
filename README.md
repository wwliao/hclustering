# hclustering
**hclustering** is a Python script plotting the result of hierarchical
clustering combined with dendrogram and head map.

## Dependencies
It needs Python 2.7 and the packages listed below:
- [NumPy](http://www.numpy.org/)
- [SciPy](http://www.scipy.org/)
- [Matplotlib](http://matplotlib.org/)
- [Pandas](http://pandas.pydata.org/)

## How to use it
Please see the command-line help:

    $ python hclustering.py -h
    usage: hclustering.py [-h] [--method METHOD] [--metric METRIC]
                          [--threshold THRESHOLD]
                          data

    positional arguments:
      data

    optional arguments:
      -h, --help            show this help message and exit
      --method METHOD
      --metric METRIC
      --threshold THRESHOLD

## Demo time!

    $ python hclustering.py --method complete --metric=correlation --threshold=0.49 data.txt

## License
MIT License
