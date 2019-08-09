# Table of Contents

1.  [What it is](#orge5d1e8f)
2.  [Installation](#org6e8653b)
3.  [License](#orgf58afc7)
4.  [Contributors](#org8ff701e)


<a id="orge5d1e8f"></a>

# What it is

The purpose of this library is to support working with the OpenSource
CFD-toolbox [OpenFOAM](http://www.openfoam.org) and its forks

This [Python](http://www.python.org) library can be used to

-   analyze the logs produced by OpenFoam-solvers
-   execute OpenFoam-solvers and utilities and analyze their output
    simultaneously
-   manipulate the parameter files and the initial-conditions of a run
    in a non-destructive manner
-   plots the residuals of OpenFOAM solvers
-   lots of other stuff

Most of this functionality is made available to the user in the form
of command-line utilities.

PyFoam does all this strictly "from the outside": by writing parameter
files and reading the output of the solvers. Without compiled parts or
being linked to OpenFOAM.

More information is found on [the OpenFOAM Wiki](http://openfoamwiki.net/index.php/Contrib_PyFoam).
Introductory presentations on PyFoam can be found there


<a id="org6e8653b"></a>

# Installation

The easiest way to install PyFoam is the Python package-manager `pip`:

    pip install PyFoam

which will install PyFoam


<a id="orgf58afc7"></a>

# License

PyFoam is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version.  See the file COPYING in this directory,
for a description of the GNU General Public License terms under which
you can copy the files.


<a id="org8ff701e"></a>

# Contributors

If not otherwise noted in a source-files the primary author is Bernhard Gschaider

The people who contributed to PyFoam (If I forgot someone: tell me):

-   Bernhard Gschaider
-   Martin Beaudoin
-   Fabian Pollesböck
-   Etienne Lorriaux
-   Bruno Santos
-   Marc Immer
-   Oliver Borm
