import pytest
import unittest

from PyFoam.RunDictionary.ParameterFile import ParameterFile
from PyFoam.RunDictionary.SolutionDirectory import SolutionDirectory

from PyFoam.FoamInformation import foamTutorials

from os import path
from shutil import rmtree
from tempfile import mktemp

from .test_TimeDirectory import damBreakTutorial

class ParameterFileTest(unittest.TestCase):
    def setUp(self):
        self.dest=mktemp()
        SolutionDirectory(damBreakTutorial(),archive=None,paraviewLink=False).cloneCase(self.dest)

    def tearDown(self):
        rmtree(self.dest)

    @pytest.mark.skipif(foamTutorials()=='',reason="$FOAM_TUTORIALS is not defined")
    def testParameterFileRead(self):
        par=ParameterFile(path.join(self.dest,"system","controlDict"))
        self.assertEqual(par.readParameter("notHere"),"")
        self.assertEqual(par.readParameter("startTime"),"0")

    @pytest.mark.skipif(foamTutorials()=='',reason="$FOAM_TUTORIALS is not defined")
    def testParameterFileWrite(self):
        par=ParameterFile(path.join(self.dest,"system","controlDict"),backup=True)
        self.assertEqual(par.readParameter("startTime"),"0")
        par.replaceParameter("startTime","42")
        self.assertEqual(par.readParameter("startTime"),"42")
        par.restore()
        self.assertEqual(par.readParameter("startTime"),"0")

    @pytest.mark.skipif(foamTutorials()=='',reason="$FOAM_TUTORIALS is not defined")
    def testParameterReadWithTab(self):
        par=ParameterFile(path.join(self.dest,"system","controlDict"))
        par.replaceParameter("startTime"," 42")
        self.assertEqual(par.readParameter("startTime"),"42")
        par.replaceParameter("startTime","\t 42")
        self.assertEqual(par.readParameter("startTime"),"42")
