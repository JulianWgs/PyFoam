# Table of Contents

1.  [This document](#org398b18e)
    1.  [Code structure and code style](#orgeb1a9bb)
2.  [Used language and libraries](#org89b41d8)
3.  [Repository](#orga3b8d84)
    1.  [Repository organization](#org07516c3)
4.  [Setup for development](#org2f91a53)
    1.  [Additional software](#org57e9903)
    2.  [API-documentation](#orgeb5e516)
5.  [Testing](#org2f4f2a0)



<a id="org398b18e"></a>

# This document

The purpose of this document is to give those who want to contribute
to PyFoam some pointers on *Dos* (there are not many *Don'ts*) and
information on technical decisions that might be annoying at first


<a id="orgeb1a9bb"></a>

## Code structure and code style

This code was developed over more than 15 years. As it tries to be
backward-compatible some of the variable/method/class-names are not
how I would name them nowadays. I'm therefor in no position to ask
other people to conform to some *coding style* but it is
recommended for contributions to conform to the *PEP 8* style and
diverge from that style where it makes the code consistent with the
module code is added to

New modules should be added to one of the major sub-modules
(directories) that are already there.

Documentation strings are appreciated

New applications should have a small script in the `bin`-directory
(see the code there). The main code should by in the
`Applications`-submodule (as this allows including the code in
other scripts without calling the utility) and be a sub-class of
the `PyFoamApplication`-class as this adds some functionality
out-of-the-box and gives the users a consistent experiance across
utilities


<a id="org89b41d8"></a>

# Used language and libraries

This library is aimed at Python 3 but for the time being it is
compatible with Python 2 through the use of the `six`-library. The
reason for this is that for the majority of the distributions used
in work environment Python 2.7 (or even 2.6) is still the default
Python and making the library purely Python 3 would be problematic
on these machines. Therefor constructs that are not supported in
Python 2 should be avoided

To ease installation `PyFoam` also tries to require as little other
libraries as possible. The notable exception is `numpy` as

1.  this is essential for plotting
2.  it is essential for Python in a scientific/technical environment
    and therefor available on most platforms that support Python

Some other essential libraries are included in the `ThirdParty`
module to avoid installation/compatibility problems. These are

-   **six:** allows making the code compatible with Python 3 **and**
    Python 2
-   **ply:** parser library. This is essential for the flexible parsing
    of OpenFOAM-files
-   **Gnuplot:** use `gnuplot` for plotting
-   **tqdm:** Progress bars
-   **pyratemp:** templating library

These libraries were included

-   because their functionality wasn't available out of the box in
    Python
-   they were small
-   their license is compatible with the GPL

Wherever possible the *batteries-included* libraries of Python
should be used


<a id="orga3b8d84"></a>

# Repository

The official source repository is found at
<https://sourceforge.net/p/openfoam-extend/PyFoam/ci/default/tree/>
and<sup><a id="fnr.1" class="footref" href="#fn.1">1</a></sup> can be cloned with

    hg clone http://hg.code.sf.net/p/openfoam-extend/PyFoam

Pull requests from other public repositories that support Mercurial
are accepted as well (avoid BitBucket as they are closing down their
Mercurial offering)

People who insist on using `git` should consider a hard fork as only
Mercurial repositories will be merged (but I assume that everyone is
flexible enough to broaden his perspective by learning a new source
control system. A quick listing of the differences can be found at
<https://www.mercurial-scm.org/wiki/GitConcepts>)


<a id="org07516c3"></a>

## Repository organization

The organization of the repository is according to the Driessen
branching model described here
<https://nvie.com/posts/a-successful-git-branching-model/> . To
enforce it this mercurial extension is recommended
<https://bitbucket.org/yujiewu/hgflow/wiki/Home>
For instance if a new feature `foo` should be added then a command

    hg flow feature start foo

creates a new branch `feature/foo` from the develop branch which
later can be merged back with

    hg flow feature finish

but it is preferred that this merge is left to the one merging the
pull-request


<a id="org2f91a53"></a>

# Setup for development

It is recommended to set up a "clean" environment for
development. This makes sure that by accident no libraries are used
that are "by accident" on the developer system but not present
otherwise

The following example assumes that you want to set up an environment
for Python 3.6. First set up the virtual environment

    python3.6 -m venv venv36

then activate it (this has to be done every time to work in this
environment) with

    . ./venv36/bin/activate

and install the requirements that `PyFoam` absolutely needs with

    pip install -r requirements.txt

Lastly make sure that the current sources are used instead of a
pre-installed `PyFoam` with

    source ./setDevelopmentPath.sh

(this is sufficient if you want to use the current sources with the
system-Python)


<a id="org57e9903"></a>

## Additional software

To assist the development with

    pip install -r requirements_development.txt

you can install additional libraries for unit-testing and
documentation generation

Additional software that is used by some parts of PyFoam can be installed with

    pip install -r requirements_additional.txt


<a id="orgeb5e516"></a>

## API-documentation

The API-documentation can be generated by calling

    make docu

if `Sphinx` is installed


<a id="org2f4f2a0"></a>

# Testing

It is recommended to run the tests that come with the sources before
committing changes. If possible it is also recommended to add new
unit-tests.

The tests are in the directory `unittests`. The structure of this
directory is similar to that of the library directory `PyFoam`. Each
directory (except `ThirdParty`) has its correspondent. Each source
file has a corresponding test file with a name prefix `test_`. Some
of these test files only have an import of the original file but no
real tests. The purpose of these files is to make sure that the
library file is at least syntactically correct.

The unit tests can be run either with

    make tests

or

    py.test

For running the tests the [pytest](https://pypi.org/project/pytest/) library has to be installed. This
library extends the `unittest` library and makes them easoer to
write. Most unittests were developed with another library but still
work with `pytest` (the were not "ported" to the new style of
`pytest` because they still work). It is recommended to develop new
tests using the `pytest` style

A lot of tests don't work if no OpenFOAM is activated because they
rely on tutorial files. These tests are automatically skipped if no
OpenFOAM is installed

To make sure that `PyFoam` works with different Python-versions the
utility `tox` can be used. By calling

    tox

the tests are run with Python 2.7, 3.6 and 3.7 (this includes
generating packages as simulating their installation)


# Footnotes

<sup><a id="fn.1" href="#fnr.1">1</a></sup> Yeah. Sourceforge is not the hippest kid on the block but it
has consistently provided its services for well over 10 years
