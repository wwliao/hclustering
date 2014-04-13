# hclustering
**hclustering** is a Python script plotting the result of hierarchical
clustering with dendrogram and heat map.

## Dependencies
It needs Python 2.7 and the packages listed below:
- [NumPy](http://www.numpy.org/)
- [SciPy](http://www.scipy.org/)
- [Matplotlib](http://matplotlib.org/)
- [Pandas](http://pandas.pydata.org/)

## How to use it
Please see the command-line help:

    $ python hclustering.py -h
    usage: hclustering.py [-h] [--method STR] [--metric STR] [--threshold FLOAT]
                          data

    positional arguments:
      data               input data

    optional arguments:
      -h, --help         show this help message and exit
      --method STR       the linkage algorithm to use
      --metric STR       the distance metric to use
      --threshold FLOAT  color all the descendent links below a cluster node k the
                         same color if k is the first node below the threshold

## Demo time!

    $ python hclustering.py --method complete --metric correlation --threshold 0.49 data.txt

The output figure:
![](https://raw.githubusercontent.com/wwliao/hclustering/master/data_complete_correlation_hcluster.png)

## License
MIT License
