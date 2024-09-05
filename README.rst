Random Graph Generator
================================================================

Introduction
============
This program generates an unordered graph of ``n`` vertices and ``d`` density 
so that

- all possible edges over ``n`` vertices are listed, 
- they are then shuffled using ``random`` module, and 
- the first ``m`` edges are selected, where ``m`` is the number of edges
  determined by ``n`` and ``d``.

Usage
=====

.. code:: bash

    $ python random_graph_generator.py -h
    usage: random_graph_generator.py [-h] [-s SEED] -n VERTEX -d DENSITY

    Random graph generator

    optional arguments:
    -h, --help            show this help message and exit
    -s SEED, --seed SEED  Specify random number seed
    -n VERTEX, --vertex VERTEX
                        Specify number of vertices
    -d DENSITY, --density DENSITY
                        Specify graph density


    $ python random_graph_generator.py -s 384813823 -n 10 -d 0.3
    c seed 384813823
    c density 0.3
    p 10 13
    n 1
    n 2
    n 3
    n 4
    n 5
    n 6
    n 7
    n 8
    n 9
    n 10
    e 1 2
    e 1 9
    e 1 10
    e 2 9
    e 3 9
    e 4 5
    e 4 9
    e 4 10
    e 5 8
    e 5 10
    e 6 10
    e 7 8
    e 7 9

