# ThinkX

This package contains support code for [books by Allen B. Downey](http://greenteapress.com/wp/).  It provides the following modules:

* `thinkbayes`: Code for *Think Bayes*. 
* `thinkstats2`: Code for *Think Stats, 2nd edition*
* `thinkbayes2`: Code for *Think Bayes, 2nd edition*, not yet published.
* `thinkdsp`: Code for *Think DSP*
* `thinkplot`: Plotting code used in all of the books, mostly wrapper functions for `matplotlib.pyplot`

`thinkstats2` and `thinkbayes2` are actually the same file, so you can import it by either name.

[This package is on PyPi](https://pypi.python.org/pypi?name=thinkx&:action=display), so you should be able to install it by running the following on the command line:

    pip install thinkx

And then you can import whichever modules you need like this:

    import thinkplot
    import thinkdsp
    ...

These modules are also distributed individually in the repositories for the books, but if you download them that way, you would not normally install them.

Tests for these modules are in the `tests` directory.  If you discover a bug or want a new feature, an excellent way to report it is to add a test (which will presumably fail) and then send me a pull request.  Of course, you are also welcome to submit a solution!  Another good alternative is to create a new issue in this repository.
