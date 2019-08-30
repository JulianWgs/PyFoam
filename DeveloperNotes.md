# Table of Contents

1.  [This document](#org8540b8d)
2.  [Used language](#org529ffb3)
3.  [Setup for development](#orge6ad925)
    1.  [Additional software](#org03189f2)



<a id="org8540b8d"></a>

# This document


<a id="org529ffb3"></a>

# Used language


<a id="orge6ad925"></a>

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

    . ./setDevelopmentPath.sh

(this is sufficient if you want to use the current sources with the
system-Python)


<a id="org03189f2"></a>

## Additional software

To assist the development with

    pip install -r requirements_development.txt

you can install additional libraries for unit-testing and
documentation generation

Additional software that is used by some parts of PyFoam can be installed with

    pip install -r requirements_additional.txt
