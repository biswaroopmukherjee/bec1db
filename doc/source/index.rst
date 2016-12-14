.. bec1db documentation master file, created by
   sphinx-quickstart on Tue Dec 13 23:00:53 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

bec1db Documentation
*********************************************************

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   docnb.ipynb
   ***********



What is bec1db?
---------------
bec1db is a Python package that lets you quickly find the experimental
parameters for images taken in BEC1. It's still rather hacky, but it's slowly improving.


How do I use bec1db?
--------------------

A simple example::

    import bec1db as db

    tullia = db.Tullia()
    images = ['12-10-2016_23_52_56_TopA']
    params = ['RFspect']
    df = tullia.image_query(images, params)

The output dataframe looks like::

    RFspect                 imagename
    0   76.032  12-10-2016_23_52_56_TopA
    1   76.039  12-10-2016_23_52_05_TopB

To update the local database, run::

    tullia.refresh()