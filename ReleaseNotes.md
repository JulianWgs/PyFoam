# Table of Contents

1.  [Version 0.6.11 - Not yet released](#org7d0a904)
    1.  [Major changes](#orgcc99e18)
    2.  [Incompatibilities](#org95740df)
        1.  [Behaviour reading `customRegexp`](#orgb70244a)
        2.  [Gnuplot does not use `FIFO` as the default anymore](#org0b6f6e5)
    3.  [New feature/utilities](#org6278bb6)
    4.  [Enhancements to Utilities](#orgcecbf3f)
        1.  [Replay data-files in `customRegexp`](#orgba52fd9)
        2.  [Macro expansion in `customRegexp`](#orgad0a313)
        3.  [`progress` entry in `customRegexp` now allows `format` strings](#orgb7b3dd3)
        4.  [`pyFoamRedoPlot.py` allows passing terminal options](#orge4c3a45)
        5.  [`pyFoamPlotWatcher.py` stops scanning the file is `--end` was specified](#org940c08c)
        6.  [Hardcopies of custom plots have more descriptive names](#orgf2fbe54)
        7.  [Plotting in Gnuplot can switch between using FIFO or regular files](#org65f6a8e)
        8.  [`pyFoamPrepareCase.py` calls script after copying initial conditions](#orgd1460d6)
        9.  [`--stop-after-template` and `--keep-zero` improve control in `pyFoamPrepareCaseParameters.py`](#org9e7c677)
        10. [`pyFoamPVSnapshot.py` allows specification of the image quality](#orgd5dd8a6)
        11. [Image size specification for `pyFoamPVSnapshot.py`](#org6eef3ba)
        12. [Setting separation of views and background transparency in `pyFoamPVSnapshot.py`](#org2be4504)
        13. [`pyFoamPVLoadState.py` automatically uses decomposed or reconstructed data](#org430a1aa)
        14. [Change directory for `pyFoamPrepareCase.py` to target](#org8a2f1f9)
        15. [`pyFoamPrepareCase.py` can create an example case](#org7cc16b5)
        16. [`pyFoamPrepareCase` prints derived values](#org6fcc9dc)
        17. [`pyFoamPVSnapshot` allows specifying different colors for different views](#org4c9de57)
        18. [`alternateLogscale` for custom plots](#org60b9dfb)
        19. [`pyFoamBinarySize.py` now calculates documentation size as well](#org1c20b9e)
        20. [`pyFoamCompareDictionary.py` allows specification of significant digits](#orgd749f00)
    5.  [Enhancements to the Library](#org7c6085e)
        1.  [`progress`-data is automatically converted to `float`](#org5cea91d)
        2.  [Additional directories in `FoamInformation`](#org9882302)
        3.  [`BoolProxy` now works correctly with `!=`](#org6d4ad46)
    6.  [Bug fixes](#orga1cac94)
        1.  [With dynamic plots names with `_slave` are problematic](#org97cc4d8)
        2.  [New-style dimensioned scalars fail](#orgee69615)
        3.  [`pyFoamPVSnapshot.py` not working with Paraview 5.6](#orgd62d349)
        4.  [`customRegexp` farthes away was used](#orgcb690ac)
        5.  [`ParameterFile`-class got confused by commented lines](#orgcfd9719)
        6.  [`pyFoamBinarySize.py` did not count files in `build`](#org2cfa48d)
        7.  [Binary files with `ParsedParameterFile` not working in PYthon 3](#orgf4bf8ba)
    7.  [Infrastructure](#org57f3dbc)
    8.  [ThirdParty](#org1046e67)
2.  [Version 0.6.10 - 2018-08-12](#org36b92c7)
    1.  [Incompatibilities](#orge225361)
        1.  [`pyFoamPrepareCase.py` does not execute decomposition scripts for single processor cases](#org645bbc1)
    2.  [New feature/utilities](#org790d1fa)
        1.  [Utility `pyFoamFunkyDoCalc.py` to compare data from `funkyDoCalc`](#orgce8148a)
    3.  [Enhancements to Utilities](#org94bc4a8)
        1.  [Recursive searching for `pyFoamListCases.py`](#orgb40d3d5)
        2.  [Look for `customRegexp` in parent directories](#org64a7f8c)
        3.  [`pyFoamPrepareCase.py` does not execute decomposition scripts for single processor cases](#org6482de5)
        4.  [`pyFoamPrepareCase.py` checks for proper decomposition](#org9b738a6)
        5.  [`pyFoamPlotWatcher.py` automatically uses newest logfile](#org12dda64)
    4.  [Enhancements to the Library](#org83c9a38)
        1.  [`FoamFileGenerator` handles `OrderedDict`](#orgc3269fd)
        2.  [`#sinclude` handled as an alias to `#includeIfPresent`](#org9e4bac4)
        3.  [OpenFOAM 6 correctly recognized](#orgec04024)
    5.  [Bug fixes](#org077cb49)
        1.  [`pyFoamPrepareCase.py` did not remove `processor`-directories](#org26e29a4)
    6.  [Infrastructure](#orgaf17c68)
        1.  [Single digit version numbers supported](#org2f61d6f)
3.  [Version 0.6.9 - 2018-02-25](#org9b4299d)
    1.  [Major changes](#orgc16f8ae)
        1.  [Add `curses`-output to Utilities](#org8c83c28)
    2.  [Incompatibilities](#org0fdb5ba)
        1.  [`pyFoamPrepareCase.py` creates `.foam`-file](#org24cd8d5)
        2.  [Hardcoded Foam-Version upgraded to `4.0`](#org92516b9)
        3.  [`none` no longer parsed as an equivalent for `false`](#orgd78b3c9)
    3.  [New features/utilities](#org69be120)
        1.  [`pyFoamJoinTimelines.py` to join Timelines from restarts](#orgbe9eace)
        2.  [`pyFoamRestartRunner.py` to automatically restart runs](#orgcb06231)
    4.  [Enhancements to Utilities](#org293562d)
        1.  [Special snapshot utilities to use MESA](#orga3c1ed2)
        2.  [Automated plotting of film properties](#orgf54541a)
        3.  [`pyFoamClearCase.py` automatically executes an existing `Allclean`](#org4ff56ff)
        4.  [`pyFoamPrepareCase.py` executes tutorial scripts if available](#org465f949)
        5.  [Script for clearing in `pyFoamPrepareCase.py`](#org9581ee4)
        6.  [`pyFoamPlotWatcher.py` now can handle multiple files](#orgfdb6512)
        7.  [`pyFoamPrepareCase.py` now allows separate decomposition scripts](#org77e1322)
        8.  [Runner-utilities now create seperate logfiles on restart](#org1e4d8ab)
        9.  [`pyFoamPVSnapshot.py` improves rewriting of state-files](#org135884d)
        10. [`pyFoamPackCase.py` adds parallel data](#org9fd5484)
        11. [`--replacement`-option in `pyFoamPVSnapshot.py` supports Foam-format](#orgc9a51a4)
        12. [`pyFoamPVSnapshot.py` improved error messages with problems in replacement](#org67823a4)
        13. [`customRegexp` now searched in parent directories](#org6552dea)
    5.  [Enhancements to the Library](#org793ee52)
        1.  [`Paraview.StateFile` extended](#org6bf356e)
        2.  [`BasicRunner` now checks for regular End](#org733a062)
    6.  [Bug fixes](#orgab00fa8)
        1.  [`pyFoamPrepareCaser.py` ran out of memory for large script outputs](#org1d50962)
        2.  [No Courant number plottet if `WM_PROJECT_VERSION` is unset](#orgb6bbeb1)
        3.  [Rescale does not work for streamlines in `pyFoamPVSnapshot.py`](#orgb0602de)
        4.  [Server not correctly running on Python 2.7 with `socketserver`](#org7c2278d)
4.  [Version 0.6.8.1 - 2017-08-03](#orgc6e6588)
    1.  [Bug fixes](#org8c6638c)
        1.  [Fork not correctly detected for `v1706`](#org8a792d7)
5.  [Version 0.6.8 - 2017-07-06](#org0555746)
    1.  [Major changes](#org17d70de)
        1.  [`pyFoamNet`-utilities now work without a Meta-Server](#org58fd6f1)
    2.  [New features/utilities](#org7a9e456)
        1.  [Added module `PyFoam.Infrastructure.Authentication`](#org106028f)
    3.  [Enhancements to Utilities](#orgbb901de)
        1.  [`pyFoamClearCase.py` now has `-dry-run` option](#orgac7bb71)
        2.  [New option `--keep-time` for `pyFoamClearCase.py`](#org0c03634)
        3.  [`pyFoamNetList.py` no longer needs a meta-server to work](#org1be3164)
    4.  [Enhancements to the Library](#org093457b)
        1.  [Better calculation of used memory in runs](#org4cf2f23)
        2.  [Pre and post-hooks are now also searched in `PyFoam.Site`](#org97deaf9)
        3.  [Adapted to correctly detect `OpenFOAM+ v1706`](#org22c626c)
    5.  [Infrastructure](#orgbe7391a)
        1.  [The `Runner`-utilities now register as `ZeroConf`-services](#orgde222f0)
    6.  [Bug fixes](#org02969bc)
        1.  [`--keep-interval` in `pyFoamClearCase.py` not working for parallel-cases](#orgb32b504)
6.  [Version 0.6.7 - 2017-06-04](#org90f5e54)
    1.  [Requirements](#org5722e2d)
        1.  [Now at least Python 2.6 required](#orgcecc454)
    2.  [Incompatibilities](#org4f0ed16)
        1.  [Names of files generated by `pyFoamPVSnapshot.py` differ](#orgfa6c766)
    3.  [New features/utilities](#orgcca0dd5)
        1.  [Utility `pyFoamListProfilingInfo.py` to print profiling data](#org2095586)
        2.  [Utility `pyFoamBlockMeshConverter.py` to convert a 2D-mesh to 3D](#orgc939fa6)
    4.  [Enhancements to Utilities](#org26e0cda)
        1.  [`customRegexp` now can scan for texts](#org7c15240)
        2.  [Lines in `PyFoamHistory` escaped](#org537e5ac)
        3.  [`--values-string` of `pyFoamPrepareCase.py` now accepts OpenFOAM-format](#org4b4b3d4)
        4.  [`pyFoamRunner.py` and `pyFoamPlotRunner.py` allow automatic selection of solver](#orgd6335a7)
        5.  [Calculations (data transformations) in `customRegexp`](#orgab479ce)
        6.  [Multi-part `idNr` for `dynamic` in `customRegexp`](#org626d9f0)
        7.  [`pyFoamListCases.py` detects dead runs](#orgd330c7f)
        8.  [Improved time-handling of `pyFoamPVSnapshot.py`](#org7deb9d1)
        9.  [Default plots can be set in configuration](#org9c378ae)
        10. [`derivedParameters.py`-script called from `pyFoamPrepareCase.py` allows error reporting](#orgcb6efe0)
    5.  [Enhancements to the Library](#org366ed9f)
        1.  [Detection of new versions of OpenFOAM-foundation and OpenFOAM+](#orgfeaa12a)
        2.  [`SpreadsheetData` now handles string data](#orgb6a17e9)
        3.  [`TimelineData` tolerates string values](#orga849b29)
        4.  [`()` operator of `SpreadsheetData` works without name](#org996cd21)
        5.  [New function `setCurrentTimeline` in `PyFoam.Paraview.Data` to get data at time](#org68ed43a)
        6.  [User-specific temporary directory](#orgb366b79)
        7.  [`Gnuplot`-plots now get better titles](#org83801cd)
        8.  [`ParsedParameterFile` now supports `#includeFunc`](#org8c2c21b)
        9.  [New utility function `findFileInDir`](#org8e0f5b0)
        10. [`humandReadableDuration` added to `PyFoam.Basics.Utilities`](#org4f3569a)
    6.  [Infrastructure](#orgedfedbb)
        1.  [`pyFoamVersion.py` now reports the versions of the `ThirdParty`-packages](#org4953bec)
    7.  [Bug Fixes](#orga723922)
        1.  [Application classes fail in Paraview](#org50bab27)
        2.  [Scripts in `pyFoamPrepareCaseParameters.sh` not working on Mac OS X](#orgd09113b)
        3.  [Processor-directories unsorted in `SolutionDirectory`](#org0b4d996)
        4.  [Deleting failed if a file did't exist](#orgb8757a5)
        5.  [Missing files in `RegionCases`](#org9bd0471)
        6.  [Wrong `solver` in `pyFoamListCase.py`](#org9daea85)
    8.  [ThirdParty](#orgf589280)
        1.  [Updated `tqdm` to version 4.8.4](#org84edc71)
        2.  [Updated `PLY` to version 3.9](#org1ff561c)
        3.  [Updated `six` to 1.10.0](#org5d78905)
7.  [Version 0.6.6 - 2016-07-15](#orgc9a6c22)
    1.  [Incompatibilities](#orge5b3247)
        1.  [Changes in `IPython`-notebooks 3.0](#orgdf09416)
    2.  [Enhancements to Utilities](#org99e069c)
        1.  [`pyFoamPrepareCase.py` executes `setFields` if appropriate](#orgf993d12)
        2.  [Plotting utilities now automatically add custom plots depending on the solver name](#org6b9970c)
        3.  [`alternateAxis`-entries now can be regular expressions](#org9157e1c)
        4.  [Plotting utilities now allow choice of Gnuplot terminal](#org2281397)
        5.  [Plotting utilities now sort legend by name](#org9dd160a)
        6.  [`pyFoamExecute.py` allows calling with debugger](#orgcbe8d5e)
        7.  [`pyFoamPrepareCase.py` fails if execution of a script fails](#orgf9e5052)
        8.  [`--hardcopy` in plotting library now allows modification of `gnuplot`-terminals](#org3373ec8)
        9.  [`pyFoamPrepareCase.py` writes state information about what it is currently doing](#org7918a49)
        10. [`pyFoamBinarySize.py` can handle new location of binaries in OpenFOAM 3.0](#org74cb96f)
        11. [`Runner`-utilites now can signal on `blink(1)`-devices](#orgf86b1d5)
        12. [`pyFoamExecute.py` can flash a `blink(1)`](#org77ab9c9)
        13. [`pyFoamDecompose.py` allows using a template file](#orgb51b8e8)
        14. [`pyFoamTimelinePlot.py` now handles new format of probe files](#org1ee5c2e)
        15. [`ReST`-report of `pyFoamPrepareCase.py` now reports derived parameters](#org6249067)
        16. [`pyFoamPrepareCase` can now ignore directories](#org720ce29)
        17. [`pyFoamConvertToCSV.py` allows adding formulas to XLSX-files](#org90acc18)
        18. [`pyFoamListCases.py` now displays mercurial info](#orge30c165)
        19. [Progress bar added to utilities with long run-time](#org35d2f48)
        20. [Utilities that clear data can now report what is cleared](#org7bf29ae)
        21. [`pyFoamConvertToCSV.py` now allows manipulating the input](#org0c1b4e8)
    3.  [Enhancements to the Library](#org9f61ff6)
        1.  [Detection of `OpenFOAM-dev`](#org399af66)
        2.  [Add `OpenFOAM+` as a fork](#org5f72765)
        3.  [Accept new convention for location of `blockMeshDict`](#org7ffbe95)
        4.  [Handling of complex data by `Configuration`](#org8eb5c56)
        5.  [`Configuration` has method `getArch` for architecture dependent settings](#org52590ec)
        6.  [`execute`-method from `PyFoam.Basics.Utilities` returns status-code](#org64aecbf)
        7.  [`BasicRunner` now supports more ways of stopping runs](#orgcd17a34)
        8.  [Added `Blink1` class to support `blink(1)` devices](#org5d67cff)
        9.  [`ParsedParameterFiles` now supports `includeEtc`](#orgb20db51)
        10. [Parses uniform fields correctly](#orgb335211)
        11. [`toNumpy`-method added to `Unparsed` and `Field`](#org28e490a)
        12. [Added module `PyFoam.RunDictionary.LagrangianPatchData` to read data from patch function object](#orgee03d64)
        13. [Added module `PyFoam.RunDictionary.LagrangianCloudData` to read cloud data](#orgf4aa34a)
        14. [Method `code` added to =RestructuredTextHelper](#org9e92b8d)
        15. [`ParsedParameterFile` now parses new dimension format correctly](#org31c9b7c)
        16. [`ParsedParameterFiel` now parses uniform fields correctly](#org96e2f2c)
    4.  [Infrastructure](#org5993005)
        1.  [Change of documentation from `epydoc` to `sphinx`](#org3a5ee18)
        2.  [Adaptions to the unittests](#orgacd4454)
    5.  [Bug fixes](#org4ade042)
        1.  [Wrong format of `ExecutionTime` breaks plotting utilities](#org114861f)
        2.  [`phases` not working with dynamic plots](#org6ed440b)
        3.  [Phase name added to function object output](#orgf79d535)
        4.  [One region mesh too many in utilities that change the boundary](#org2ff6ee3)
        5.  [`pyFoamClearCase.py` fails on write-protected case](#org37a73db)
        6.  [Copying of directories in `pyFoamPrepareCase.py` confused by zipped files](#orgb8e828b)
        7.  [Wrong times for multi-view layouts in `pyFoamPVSnapshots.py`](#orga0b8a60)
        8.  [First timestep not plotted (and not stored)](#org1248f36)
        9.  [`DYLD_LIBRARY_PATH` not passed on *Mac OS X 10.11*](#org5afd363)
        10. [Newer versions of `pandas` broke the writing of excel files with `pyFoamConvertToCSV.py`](#org34a14ec)
        11. [Capital `E` in exponential notation for floats breaks parser](#org4b8dd89)
        12. [`Runner`-utilities clear processor directories if first time in parallel data differs](#orgceb54d5)
        13. [Utilities `pvpython` not working when installed through `distutils`](#org08add87)
    6.  [ThirdParty](#org706f5c2)
        1.  [Added `tqdm` for progress bars](#orgb4bedb7)
8.  [Version 0.6.5 - 2015-06-01](#org90befcc)
    1.  [Major changes](#org837f805)
        1.  [PyFoam now on *Python Package Index*](#org06c5fa8)
    2.  [Incompatibilities](#org9e30c7f)
        1.  [`ArchiveDir` in `SolutionDirectory` discouraged](#orgcc85f9c)
        2.  [Pickled data files now written as binary](#orgeb7e24d)
        3.  [The `PlotRunner` and `PlotWatcher` now don't strip spaces](#orgc1d5ca5)
        4.  [Different column names in `pyFoamConvertToCSV.py`](#orgbf372b4)
        5.  [`pyFoamChangeBoundaryName.py` and `pyFoamChangeBoundaryType.py` automatically modify `processorX`](#org8b1cdcd)
    3.  [Bugfixes](#orgb5857ee)
        1.  [Arbitrary commands in `TemplateFile` passed to file](#org0cce517)
        2.  [Pickled files not opened in binary mode](#orgfbe2cc9)
        3.  [Additional fixes for Python 3](#org964af14)
        4.  [`ParsedParameterFile` fails if "complete" dictionary is `#include` ed](#org97dd460)
        5.  [`ParsedParameterFile` fails if there is more info after `#include`](#org256d391)
        6.  [`pyFoamDisplayBlockMesh.py` not working with VTK 6](#org4da5f8c)
        7.  [`pyFoamCreateModuleFile.py` failed with environment variables containing `=`](#org3cd7c90)
        8.  [Fix import in `GeneralVCSInterface`](#org69da715)
        9.  [Support of old format in `ParsedBlockMeshDict` broken](#org52157fe)
        10. [`TemplateFile` not correctly working in Python 3](#org5b04cc2)
        11. [Certain things not done by `pyFoamPrepareCase` in `--quiet` was set](#orgb4d8ec4)
        12. [Annoying warning at the start of the run](#org65639cc)
        13. [Redirected values](#org2743fd9)
        14. [Behavior of Template-engine not consistent in Python3 and Python2](#org67bb9e5)
        15. [Braces, brackets, parentheses in column name broke `RunDatabase`](#orga8fdd14)
        16. [Finding of installations in alternate locations broken](#org286fab7)
        17. [Failing on 3.x if socket for server thread already occupied](#orgb8a7b40)
    4.  [Enhancements to Utilities](#org37810e6)
        1.  [`pyFoamPrepareCase` recognizes multi-region cases](#org17d86a3)
        2.  [`pyFoamPrepareCase` adds specialized templates](#org3a4f32d)
        3.  [`pyFoamPrepareCase` keeps data generated by meshing script](#orgc2a9315)
        4.  [`pyFoamPrepareCase` adds possibility for a file with default values](#org5bbb50e)
        5.  [`pyFoamPrepareCase` writes report about the variables](#org08a0dcf)
        6.  [Gnuplot can be styled with default commands](#org0e9f5f5)
        7.  [`pyFoamPVSnapshot.py` now supports Paraview 4.2 and later](#orgfbf177f)
        8.  [`pyFoamPVSnapshot.py` allows switching between decomposed and reconstructed data](#orgd3f9c72)
        9.  [`pyFoamPVSnapshot.py` allows changing the field for sources](#org76523c4)
        10. [`pyFoamPVSnapshot.py` allows rescaling the color-legend](#org0396936)
        11. [`pyFoamPVsnapshot` reads parameters written by `pyFoamPrepareCase.py`](#org4e2173a)
        12. [`pyFoamListCases.py` allows filtering](#org52ddd13)
        13. [`pyFoamRunParametervariation.py` now allows dictionaries](#org50525aa)
        14. [`pyFoamConvertToCSV.py` now has all functionality of `pyFoamJoinCSV.py`](#orgf0b422d)
        15. [`dynamic` in `customRegexp` now allows composition from multiple match-groups](#orgf85b209)
        16. [New type `dynamicslave` in `customRegexp`](#orgad21b17)
        17. [Additional profiling option `--profile-line-profiler`](#org62e1e49)
        18. [Utilities that use templates can be customized with the configuration](#org91e5241)
        19. [`LocalConfigPyFoam` now can be read **before** argument parsing](#orgd547be9)
        20. [`pyFoamConvertToCSV.py` automatically selects the output format with `--automatic-format`](#orgc4e2b31)
        21. [`pyFoamConvertToCSV.py` allows adding original data as separate sheets](#orgcb7e94f)
        22. [`pyFoamConvertToCSV.py` has improved naming of columns](#org8e37034)
        23. [`pyFoamConvertToCSV.py` now supports sets-files](#org8398d5c)
        24. [`pyFoamPrepareCase.py` can calculate derived values with a script](#orgfa94678)
        25. [`pyFoamPrepareCase.py` adds a variable `numberOfProcessors`](#org1da6355)
        26. [`pyFoamChangeBoundaryName.py` and `pyFoamChangeBoundaryType.py` now support decomposed cases](#orgfcde9a5)
        27. [`pyFoamPrepareCase.py` has possibility for templates after the final stage](#orgda2ac0f)
        28. [`pyFoamRunParameterVariation` allows adding postfix to cloned cases](#orge24a012)
        29. [`pyFoamConvertToCSV` now allows setting of default input file format](#org6fa9fd7)
        30. [`pyFoamListCases.py` adds the hostname to the printed information](#org822780f)
        31. [`pyFoamPrepareCase.py` allows cloning](#orgb727e4b)
    5.  [Enhancements to the Library](#org3d1facc)
        1.  [`SolutionDirectory` detects multiple regions](#orgeeebf0b)
        2.  [`BoolProxy` now compares like builtin `bool`](#orgbb3a827)
        3.  [`PyFoamApplication`-class now supports `pvpython` for debugging](#org36667ea)
        4.  [`TemplateFile` now allows more flexible assignments](#org57b05b6)
        5.  [`ThirdParty`-library `six` upgraded to 1.9.0](#org207f5b1)
        6.  [Additional markup in `RestructuredTextHelper`](#org5b6cb06)
        7.  [`SpreadsheetData` can now read files produced by the `sets`-functionObject](#org91bb0d7)
    6.  [Infrastructure](#orge4868bf)
        1.  [Adaption of Debian packaging to new conventions](#org5af9bae)
    7.  [Development changes](#org7ee55d6)
        1.  [Now uses `pytest` for unittesting](#org61fc291)
9.  [Version 0.6.4 - 2014-11-24](#orgadf4fc4)
    1.  [Requirements](#orgc444f6f)
    2.  [Future changes](#org3d4e387)
        1.  [Redundant utilities `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py` unified](#org2a473dc)
    3.  [Major changes](#org6d9eac0)
        1.  [Multi-line regular expressions in `customRegexp`](#orga62f6f8)
        2.  [Enhancement of `pyFoamPrepare.py`](#org4b34ec9)
        3.  [Enhancements of the CSV-utilities](#org54e8f52)
        4.  [Environment variable `PYFOAM_SITE_DIR` and `PYFOAM_DIR`](#org154001d)
    4.  [Incompatibilities](#org83ddbb6)
        1.  [Option `--silent` removed from `pyFoamPrepareCase.py`](#org156e8e9)
        2.  [Keys in `RunDatabase` with column-names that contain upper-case letters change](#orgc40d03b)
        3.  [Change in unique variable names in `pyFoamConvertToCSV.py`](#org064d808)
        4.  [`PyFoam.IPython`-module renamed to `PyFoam.IPythonHelpers`](#orgcf4f4c2)
    5.  [Bugfixes](#orgbf99e07)
        1.  [Templates in `pyFoamPrepareCase.py` did not keep permissions](#org3b869aa)
        2.  [`pyFoamComparator.py` failed due to circular dependency](#org3b1f15e)
        3.  [`pyFoamDumpRunDatabaseToCSV.py` fails if Pandas-data is requested](#orga360801)
        4.  [`sort` for list broke code on Python 3](#orgcc9ef74)
        5.  [Changing the OF-version does not work in Python 3](#orgff0ead5)
        6.  [`addData` in `PyFoamDataFrame` extrapolates for invalid values](#org407a0b2)
        7.  [`--keep-last` did not work for `pyFoamClearCase.py` and parallel cases](#org6b31e0c)
        8.  [`pyFoamDumpRunDatabaseToCSV.py` does not add basic run information](#org251553a)
        9.  [Restore of `FileBasisBackup` did not work](#org01c5894)
        10. [Remove circular dependency in `DataStructures`](#org5e94bd0)
    6.  [New features/Utilities](#org237943c)
        1.  [`pyFoamRunParameterVariation.py`](#orgcb1ac46)
        2.  [`pyFoamBinarySize.py`](#org615335e)
        3.  [`pyFoamBlockMeshRewrite.py`](#orgcd3d92d)
    7.  [Enhancements to Utilities](#org2d467dd)
        1.  [`pyFoamChangeBoundaryType.py` allows setting additional values](#orgcb34fd4)
        2.  [`pyFoamPrepareCase.py` now has OF-version and fork as defined variables](#org347f336)
        3.  [`pyFoamPrepareCase.py` now allows "overloading" another directory](#org63afcbd)
        4.  [`pyFoamIPythonNotebook.py` adds improvements to the notebook](#orgcf2e1f9)
        5.  [`pyFoamListCases.py` more tolerant to faulty `controlDict`](#org4cd1198)
        6.  [`pyFoamDumpConfiguration.py` prints sections and keys alphabetically](#orgf09c121)
        7.  [`pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py` read and write Excel-files](#org8750c1e)
        8.  [Flexible variable filtering in `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py`](#org1f79484)
        9.  [Columns in `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py` can be recalculated](#org722b4d6)
        10. [Testing for `Numeric` removed from `pyFoamVersion.py`](#orge839bc4)
    8.  [Enhancements to the Library](#org56f1593)
        1.  [Subclass of `ClusterJob` that support `PrepareCase`](#org006c877)
        2.  [Subclass of `ClusterJob` that support `RunParameterVariation`](#org0520fe4)
        3.  [`execute` in `PyFoam/Utilities` fails if script is not executable](#org917d6f1)
        4.  [`foamVersion` uses a separate wrapper class for `tuple`](#org84c078a)
        5.  [Move calculation of disk usage to `Utilities`](#org1371fd8)
        6.  [Enhancement of `--help`](#org8af6285)
        7.  [`which`-routine in `Utitlities` uses native Python-routine](#org26b14d6)
        8.  [`FileBasis` now allows file handles instead of the filename](#org5e1a0f2)
        9.  [`BlockMesh` doesn't force writing to file anymore](#orgbc8489f)
        10. [Additional methods for `BlockMesh`-class](#org8a697e9)
        11. [`LineReader` allows keeping spaces on left](#org87f6e7e)
        12. [`TemplateFile` now allows writing of assignment-results in file](#org9cf54da)
        13. [`SolverJob` now allows passing of parameters to the solver](#orgb91d014)
        14. [`SpreadsheetData` now allows reading from an Excel file](#orgb48f232)
        15. [`SpreadsheetData` allows recalculating columns](#org3fb4a0d)
    9.  [Known bugs](#orgf43d83b)
        1.  [Timelines not forgotten for multiple runner calls](#orga403ece)
10. [Version 0.6.3 - 2014-06-23](#org017701f)
    1.  [Requirements](#orged77a1d)
    2.  [Major changes](#orgcc80bb8)
        1.  [Version changing supports forks of OpenFOAM](#orge28a831)
    3.  [Incompatibilities](#orga5eefde)
        1.  [Change of command interface of `pyFoamSTLUtility.py`](#org1794e8e)
        2.  [If `0.org` is present `pyFoamCloneCase.py` and `pyFoamPackCase.py` ignore `0`](#org6c8e094)
    4.  [Bugfixes](#orga0c764a)
        1.  [PlotWatcher has long times between updates if pickling takes long](#org1b0149d)
        2.  [`pyFoamPVSnapshot.py` fails for newer paraview-versions](#orgdd092e9)
        3.  [SamplePlot failed when valueNames are unspecified](#org9406646)
        4.  [`pyFoamTimelinePlot.py` failed Numpy/Pandas output of vector fields](#orgd7c097c)
        5.  [`alternateAxis` ignored for slave](#org87ee89f)
        6.  [`pyFoamCaseReport.py` more stable for binary `boundary`-files](#org805e442)
        7.  [`SpreadsheetData` returns data which breaks certain Pandas-operations](#orgfd5ec9f)
        8.  [`pyFoamCloneCase.py` added duplicates to the archive](#org1ff4c14)
        9.  [`nonuniform` of length 3 not correctly printed](#orgc8eaa3b)
    5.  [New features/Utilities](#orgd29b618)
        1.  [`pyFoamPrepareCase.py` for case preparation](#orgd75aa43)
        2.  [`pyFoamIPythonNotebook.py` for generating and manipulating IPython-notebooks](#org18f28ab)
        3.  [Additional sub-module `PyFoam.IPython`](#org9ae8ff2)
        4.  [Additional sub-module `PyFoam.Wrappers`](#org64737a4)
    6.  [Enhancements to Utilities](#org9add3db)
        1.  [`pyFoamSampleplot` has option to use index instead of time in filenames](#org6f440d2)
        2.  [`pyFoamListCases.py` Allows addition of custom data](#org685a706)
        3.  [Switch compiler versions](#orge4ebf39)
        4.  [`pyFoamVersion.py` reports the installed versions better](#org06414b0)
        5.  [Offscreen rendering can be switched off in `pyFoamPVSnapshot.py`](#orge5d9aaf)
        6.  [Write 3D-data in `pyFoamPVSnapshot.py`](#orgd404e8f)
        7.  [Added capabilities to `pyFoamSTLUtility`](#org4d3d3d3)
        8.  [`pyFoamDecomposer.py` switches off function objects](#org5955867)
        9.  [`pyFoamCloneCase.py` clones more stuff](#org17a3786)
    7.  [Enhancements to the Library](#orge109e86)
        1.  [`BasicRunner` now can print the command line that is actually used](#org25f72e0)
        2.  [`ClusterJob` now can live without a machinefile](#orgb4a7043)
        3.  [Enhanced treatment of symlinks during cloning](#org5068755)
        4.  [`AnalyzedCommon` clears the `analyzed`-directory](#org040a19a)
        5.  [`TimelineDirectory` is more tolerant](#org8daa4d8)
        6.  [Possibility of a subcommand-interface for utilities](#org7c707fc)
        7.  [`STLUtility` accepts file-handles](#orgdaf026a)
        8.  [`addClone` in `SolutionDirectory` accepts glob patterns](#org2fed06f)
        9.  [`execute` in `Utilities` allows specification of working directory and echoing of output](#org704211e)
        10. [`rmtree` and `copytree` more tolerant](#org754309f)
        11. [Enhanced support for booleans in the parser](#org948e00f)
        12. [Application classes now allow specifying options as keyword parameters](#org3bbd08c)
        13. [`SolutionDirector` now can classify directories in the `postProcessing`-directory](#orgb982259)
        14. [`pyFoamSamplePlot.py` now more flexible for distributions](#org2e3d373)
        15. [`DictProxy` now has a `dict`-like `update`-method](#orge7f8a5c)
        16. [`FoamFileGenerator` automatically quotes strings](#org550293a)
        17. [Children of `FileBasis` now can be used with the `with`-statement](#orgd2e184c)
11. [Version 0.6.2 - 2013-11-03](#org47681e4)
    1.  [Major changes](#org0da9ff9)
        1.  [Use of `pandas`-library](#orgb7c0f5d)
    2.  [Incompatibilities](#org3d63a95)
        1.  [Different separator for databases in CSV-files](#orgad13a0b)
        2.  [Change of independent variable name in sample data](#orgd27a16f)
    3.  [Bugfixes](#orgf8a3cd1)
        1.  [`pyFoamPackCase.py` does not handle symbolic links correctly](#org5be4202)
        2.  [`pyFoamPotentialRunner.py` not working with OpenFOAM 2.0 or newer](#org1689779)
        3.  [`pyFoamListCase.py` fails with `controlDict` that use preprocessing](#orga9a7d27)
        4.  [Cloning fails in symlink-mode if files are specified twice](#orga5051a7)
    4.  [Utilities](#org86a0a2f)
        1.  [`pyFoamPotentialRunner.py` now allows removing of `functions` and `libs`](#orgf506478)
        2.  [The Runner-utilities now have more options for clearing](#orgc09249d)
    5.  [Library](#orga3a01ed)
        1.  [`SolutionDirectory` and `TimeDirectory` are more tolerant](#org67ba29c)
        2.  [`ClusterJob` now handles template files](#orgb4b3041)
        3.  [Additional parameters in `ClusterJob`](#org40b6596)
        4.  [Custom data in directory easier accessible](#org2426708)
        5.  [`SolverJob` now allows compression of output](#org854459d)
        6.  [`PyFoamApplication`-class now allows quick access to data](#org6c4878e)
    6.  [New features/Utilities](#org662f88e)
        1.  [Post-run hook that sends mail at the end of run](#org1aaae5d)
        2.  [New utility `pyFoamCompressCases.py`](#org72cb81e)
        3.  [Paraview-module to read additional data](#org815bdf3)
    7.  [Enhancements](#org2abe3ac)
        1.  [`pyFoamRedoPlot.py` can plot in XKCD-mode](#orgd99f4a9)
        2.  [`pyFoamListCases.py` now displays disk usage in human readable form](#orgf15c6e1)
        3.  [`pyFoamClearCase.py` more flexible in selection of data to be removed](#org771360c)
        4.  [`pyFoamFromTemplate.py` automatically chooses template and default values](#orgd0a0e62)
        5.  [`pyFoamDumpRunDatabaseToCSV.py` can disable standard-fields](#orga239dc6)
        6.  [`pyFoamDumpRunDatabaseToCSV.py` prints `pandas`-object](#org9dca4e4)
        7.  [Better debugging with `ipdb`](#org0a276bf)
        8.  [Interactive shell after execution for utilities](#org896ecb8)
        9.  [Utilities that read quantitative data convert to `pandas`-data and/or `numpy`](#org0a0d8c1)
        10. [Utilities that read quantitative data write Excel files](#orgc9afb9e)
        11. [Specify additional settings for `GnuPlot` in `customRegexp`](#org217700b)
        12. [More flexible data specification for `pyFoamSamplePlot.py`](#org4badce1)
        13. [`pyFoamSamplePlot.py` now allows specification of x-range](#orgdd48a3e)
12. [Version 0.6.1 - 2013-05-24](#orga41e16c)
    1.  [Major changes](#org3fa3bfd)
    2.  [Bugfixes](#org490fe11)
        1.  [Restoring of `controlDict` after `write`](#orgab82433)
        2.  [Custom-plot type `slave` not working if no `master` defined](#org0784c9d)
        3.  [`-list-only` did not correctly parse lists with a numeric prefix](#org5d9d14b)
    3.  [Utilities](#orgd03557b)
        1.  [`pyFoamBuildHelper.py` now allow more than one action](#org06f52fc)
        2.  [Utilities warn if OpenFOAM-version is unset](#orgc45da84)
        3.  [`pyFoamUpgradeDictionariesTo20.py` allows single files](#org85625e1)
        4.  [`pyFoamUpgradeDictionariesTo20.py` transforms reaction-schemes](#org2d30227)
        5.  [`pyFoamUpgradeDictionariesTo20.py` transforms thermophysical data](#orgd3c4558)
        6.  [`pyFoamCloneCase` now allows creating directory that symlinks to the original](#org4cddfe8)
        7.  [`pyFoamClearCase.py` now removes `postProcessing` and allows removal of additional files](#org1d7b676)
        8.  [Improvements to `pyFoamVersion.py`](#orge35c691)
        9.  [Additional files automatically cloned](#org17ad99d)
        10. [`pyFoamDisplayBlockMesh.py` uses the same options for template format as `pyFoamFromTemplate.py`](#org53f1f07)
    4.  [Library](#orga97ea30)
        1.  [Improvements in syntax of `ParsedParameterFile`](#org7ce956b)
        2.  [`Utilities`-class now function to find files matching a pattern](#org2acdff1)
        3.  [VCS ignores more files](#orgfe7c1e1)
    5.  [New features/Utilities](#orgeeecaa3)
        1.  [New Utility `pyFoamSymlinkToFile.py`](#org33cc91a)
13. [Version 0.6.0 - 2013-03-14](#orge4489b2)
    1.  [Major changes](#org4dee8d3)
        1.  [Adaption to work with Python3](#org337c89e)
        2.  [New ThirdParty-Libraries](#org63f6fe5)
        3.  [Porting to `Windows`](#org95468f8)
        4.  [Experimental port to `pypy`](#org6876252)
    2.  [Third-Party](#org194d82f)
        1.  [Upgraded `ply` to 3.4](#org77d31ae)
    3.  [Infrastructure](#org90f2281)
        1.  [Parameters can't be modified in `CTestRun` after initialization](#orgf445a68)
        2.  [Treat timeouts in the `MetaServer` right](#orgcf15253)
        3.  [Add `execute`-method to `ClusterJob`](#org5525e90)
        4.  [Add possibility to run specific modules before or after the solver](#orga7ad368)
        5.  [Parameters added to the info about the run](#org2716d1a)
        6.  [Parameter handling in `ClusterJob` extended](#orgde696ef)
        7.  [Run data written alongside `PickledPlots`](#orgf3a3305)
        8.  [`BasicRunner` collects error and warning texts](#org399a0c6)
    4.  [Library](#org53931dd)
        1.  [`TemplateFile` now uses `pyratemp`](#org60df394)
        2.  [Clearer error message in Application-classes](#orge71d3e2)
        3.  [Output is only colored if it goes to the terminal](#org19d12a5)
        4.  [`error`-method of application classes now raises an exception](#org0669553)
        5.  [`ParsedParameterFile` now knows how to handle binary files](#org366d5be)
        6.  [`LabledReSTTable` for more flexible table generation](#orga9bd89f)
        7.  [Plotting classes now allow setting of `xlabel`](#org0411108)
    5.  [Utilities](#orgf3b7711)
        1.  [`pyFoamFromTemplate.py` with new templating engine](#orgeb9b864)
        2.  [`pyFoamSamplePlot.py` allows using the reference data as basis for comparison](#orga7c06f8)
        3.  [Scaling and offsets are now used in plots of `pyFoamSamplePlot.py`](#orgf12beb5)
        4.  [`pyFoamPrintData2DStatistics.py` prints relative average error](#org0600484)
        5.  [Enhancements to `pyFoamVersion.py`](#org71e938a)
        6.  [`pyFoamRunner.py` allows hooks](#org331179e)
        7.  [`pyFoamRedoPlots.py` supports range for plots](#orgc7c1720)
        8.  [`pyFoamDisplayBlockMesh.py` no supports templates](#org9b32884)
        9.  [`pyFoamCaseReport.py` is tolerant towards binary files](#org711a356)
        10. [`pyFoamSamplePlot.py` and `pyFoamTimelinePlot.py` raise error if no plots are generated](#org0b8d8f0)
        11. [`pyFoamSurfacePlot.py` can wait for a key](#orgd3c6d1e)
        12. [`pyFoamEchoDictionary.py` is more flexible with binary files](#org5e71adf)
        13. [All utilities now have a switch that starts the debugger even with syntax-errors](#org1331150)
        14. [Utilities now can be killed with `USR1` and will give a traceback](#org8dcba13)
        15. [Switch to switch on **all** debug options](#org00a972e)
        16. [Plotting utilities now allow specification of x-Axis label](#org5400710)
        17. [Metrics and compare for `pyFoamTimelinePlot.py` and `pyFoamSamplePlot.py` support time ranges](#org1a391ca)
        18. [`pyFoamDisplayBlockMesh.py` allows graphical selection of blocks and patches](#orgda13303)
        19. [`pyFoamCloneCase.py` and `pyFoamPackCase.py` accept additional parameters](#org24b279b)
        20. [`pyFoamListCases.py` now calculates estimated end-times](#org267feda)
    6.  [New features](#org1878022)
        1.  [Different "phases" for multi-region solvers](#org95ca548)
        2.  [`pyFoamChangeBoundaryType.py` allows selection of region and time](#org2c35065)
        3.  [New class for storing case data in a sqlite-database and associated utilities](#org9f2b8a5)
    7.  [Bugfixes](#org5bdf7ea)
        1.  [Only binary packages of 1.x were found](#orgffd236d)
        2.  [Option group *Regular expressions* was listed twice](#org9c38a73)
        3.  [`--clear`-option for `pyFoamDecompose.py` not working](#orga4a2fcc)
        4.  [`pyFoamDisplayBlockmesh.py` not working with variable substitution](#org6a2fdf4)
        5.  [Option `--function-object-data` of `pyFoamClearCase.py` not working with directories](#orgba3b908)
        6.  [`nonuniform` of length 0 not correctly printed](#orgaca12e4)
        7.  [Building of pseudocases with `pyFoamRunner.py` broken](#org81c06f7)
        8.  [`pyFoamRedoPlot.py` did not correctly honor `--end` and `--start`](#orgc35a6d1)
        9.  [`WriteParameterFile` does not preserve the order of additions](#org099790c)
        10. [Wrong number of arguments when using `TimelinePlot` in `positions`-mode](#orgf267061)
        11. [`ClusterJob` uses only `metis` for decomposition](#orgd40a214)
        12. [`pyFoamSamplePlot.py` and `pyFoamTimelinePlot.py` produced no pictures for regions](#orga9f9b04)
        13. [Barplots in `pyFoamTimelinePlot.py` not working if value is a vector](#org2d32b20)
        14. [Mysterious deadlocks while plotting long logfiles](#orga2d7c00)
        15. [Scanning linear expressions form the block coupled solver failed](#org716c979)
        16. [`#include` not correctly working with macros in the included file](#org005209b)
        17. [Macros not correctly expanded to strings](#orgc1f90d6)
        18. [`pyFoamPackCase.py` in the working directory produces 'invisible' tar](#org2c537b8)
        19. [String at the end of a linear solver output makes parsing fail](#org1956e3f)
        20. [Paraview utilities not working with higher Paraview versions](#org959755c)
        21. [Camera settings not honored with `pyFoamPVSnapshot.py`](#orga899b7f)
14. [Version 0.5.7 - 2012-04-13](#orgfa30d27)
    1.  [Parser improvements](#orgc539561)
    2.  [Utility improvements](#orga9d4c12)
    3.  [New Utilities](#org35fbea6)
    4.  [Library improvements](#org10b8650)
    5.  [Removed utilities](#org6772fc3)
    6.  [Thirdparty](#orgba388d5)
    7.  [Other](#org9f63d55)
15. [Older Versions](#orgdcf54b9)


<a id="org7d0a904"></a>

# Version 0.6.11 - Not yet released


<a id="orgcc99e18"></a>

## Major changes


<a id="org95740df"></a>

## Incompatibilities


<a id="orgb70244a"></a>

### Behaviour reading `customRegexp`

Macro expansion in the `customRegexp` might break it for some
cases


<a id="org0b6f6e5"></a>

### Gnuplot does not use `FIFO` as the default anymore

See the relevant entry in *Enhancements to Utilities*

A potential problem is that the new implementation leaves files in
the `/tmp` filesystem


<a id="org6278bb6"></a>

## New feature/utilities


<a id="orgcecbf3f"></a>

## Enhancements to Utilities


<a id="orgba52fd9"></a>

### Replay data-files in `customRegexp`

There are two new `type` s available in `customRegexp`: `data` and
`dataslave`. These have to have one of the enxtries `csvName`,
`excelName` or `txtName` with the name of a "spreadsheet type"
file. The data from this file will be plotted according to the
current simulation time. With `dataslave` it will be plotted to
another plot.

The entry `timeName` interprets the name of the column that is to
be interpreted as the time and either `validData` or
`validMatchRegexp` select the other columns to plot.

`skip_header`, `stripCharacters` and `replaceFirstLine` are other
parameters of the `SpreadsheetData`-class that preprocess the file
to conform to an expected format


<a id="orgad0a313"></a>

### Macro expansion in `customRegexp`

In the `customRegexp` it is now possible to use the usual
OpenFOAM-macro-expansions with `$` etc. This makes


<a id="orgb7b3dd3"></a>

### `progress` entry in `customRegexp` now allows `format` strings

The `progress` entry in `customRegexp`-entries now allows strings
in the format of the `str.format` method in Python. So instead off

    progress "$0: $1";

one can write

    progress "{0}: ${1}";

The advantage of this format is additional flexibility. For
instance the length of the strings can be fixed

    progress "{0:5}: ${1:10}";

Note: the entries are strings. Not numbers as expected


<a id="orge4c3a45"></a>

### `pyFoamRedoPlot.py` allows passing terminal options

The utility now allows passing options to the plotting
implementation with the `--terminal-options`-option. This can for
instance be used to modify the size of the plot


<a id="org940c08c"></a>

### `pyFoamPlotWatcher.py` stops scanning the file is `--end` was specified

If the `--end-time` option is specified then the solver stops
scanning if that time is reached. The plot windows are killed. To
keep them specify `--persistent`


<a id="orgf2fbe54"></a>

### Hardcopies of custom plots have more descriptive names

Instead of the `custom00xxx` name the hardcopies of custom plots
now have and additional short name that describes the content of
the plot (it is taken from the id in the `customRegexp`)


<a id="org65f6a8e"></a>

### Plotting in Gnuplot can switch between using FIFO or regular files

The plotting utilities have two new options `--gnuplot-use-fifo`
and `--gnuplot-no-use-fifo` that switches whether the plotting
windows will use a FIFO-queue or a regular file for the data of
the plot.

Until now FIFO was used. This had two problems

-   a deadlock-situation that sometimes occurred when the utility was
    stopped with Ctrl-C
-   the plots were not interactive (no zooming) or did not
    immediately repaint when the windows were resized

Now the default behavior is to use regular files. The problem with
this is that the files are not removed in the end from
`/tmp`. This shouldn't be a problem as usually that filesystem is
purged of old files at regular intervals


<a id="orgd1460d6"></a>

### `pyFoamPrepareCase.py` calls script after copying initial conditions

A script `postCopy.sh` is called after the initial conditions are
copied from `0.org`


<a id="org9e7c677"></a>

### `--stop-after-template` and `--keep-zero` improve control in `pyFoamPrepareCaseParameters.py`

The combination of these two parameters allow "just" changing
something in the templates without running other lengthy
operations


<a id="orgd5dd8a6"></a>

### `pyFoamPVSnapshot.py` allows specification of the image quality

The option `--quality` now allows specifying the quality of the
image with a value of \(0\) being worst (but producing the smallest
pictures) and \(100\) best (but producing huge pictures). The
default is \(50\)


<a id="org6eef3ba"></a>

### Image size specification for `pyFoamPVSnapshot.py`

The options `--x-resolution` and `--y-resolution` allow specifying
the resolution of the image. If only one of them is set the image
is scaled proportionally. This only works for Paraview versions
bigger than 5.4


<a id="org2be4504"></a>

### Setting separation of views and background transparency in `pyFoamPVSnapshot.py`

Two new options were added that allow setting a separation between
different views and making the background transparent. This only
works for Paraview versions bigger than 5.4


<a id="org430a1aa"></a>

### `pyFoamPVLoadState.py` automatically uses decomposed or reconstructed data

Depending which of the two sets has more timesteps that state is
set to this before loading. So if more parallel timesteps are
present then these are used even if the state file uses the
reconstructed times. The behavior can be changed with the
`--decompoes-mode`-option


<a id="org8a2f1f9"></a>

### Change directory for `pyFoamPrepareCase.py` to target

The option `--extecute-in-case-directory` changes the working
directory to the target directory. THis allows specifying
parameter files that are in that directory without a full path


<a id="org7cc16b5"></a>

### `pyFoamPrepareCase.py` can create an example case

A command like

    pyFoamPrepareCase.py exampleCase --paramter-file=parameters.base --build-example --clone-case=originalCase

creates an example case `exampleCase` from a template case
`originalCase` using the parameter file `parameter.base`. It
creates a script `Allrun` that allows executing the case without
`PyFoam` (if none of the scripts uses `PyFoam`-scripts)

This may not work for all configurations (especially cases that use `postTemplate`)


<a id="org6fcc9dc"></a>

### `pyFoamPrepareCase` prints derived values

The same way that the utility printed the used values it now
prints the derived values as well


<a id="org4c9de57"></a>

### `pyFoamPVSnapshot` allows specifying different colors for different views

The option `--color-for-filers` now allows specifying a different
color for the same filter in different view. This is done by
specifying a dictionary


<a id="org60b9dfb"></a>

### `alternateLogscale` for custom plots

This is analog to `logscale` but for the values that are specified
with `alternateAxis`


<a id="org1c20b9e"></a>

### `pyFoamBinarySize.py` now calculates documentation size as well

If there is `html` documentation then this is counted as well


<a id="orgd749f00"></a>

### `pyFoamCompareDictionary.py` allows specification of significant digits

When comparing numbers now the number of significant digits can be
specified. This only works for single numbers. Not compound types
like lists and vectors


<a id="org7c6085e"></a>

## Enhancements to the Library


<a id="org5cea91d"></a>

### `progress`-data is automatically converted to `float`

When using format-strings for the `progress`-entry then the
library automatically attempts to convert the data to `float`
(otherwise it keeps it as `str`)


<a id="org9882302"></a>

### Additional directories in `FoamInformation`

Two functions `foamCaseDicts()` and `foamPostProcessing()` have
been added that return the paths to these directories inside
`$FOAM_ETC`


<a id="org6d4ad46"></a>

### `BoolProxy` now works correctly with `!=`

Added a method `__ne__` so that the results of the `!=` operator
are consistent with `==`


<a id="orga1cac94"></a>

## Bug fixes


<a id="org97cc4d8"></a>

### With dynamic plots names with `_slave` are problematic

This made the slave plots that had `_slave` in the name fail


<a id="orgee69615"></a>

### New-style dimensioned scalars fail

As reported in
<https://sourceforge.net/p/openfoam-extend/ticketspyfoam/223/> by
Rodrigo Leite Prates parsing certain constructs that involve
dimension sets fail. This is because of a problem with the
comparison of `Dimension` that assumes that the other side is a
`Dimension` as well. Fixed


<a id="orgd62d349"></a>

### `pyFoamPVSnapshot.py` not working with Paraview 5.6

The API now has to be called through a different module. Otherwise
it will fail


<a id="orgcb690ac"></a>

### `customRegexp` farthes away was used

When looking automatically for a `customRegexp` the one furtherest
up in the directory tree was used. Now instead all the
`customRegexp` are used with the lower ones overriding the other
ones


<a id="orgcfd9719"></a>

### `ParameterFile`-class got confused by commented lines

One of the oldest classes in PyFoam had the problem that it
"found" parameters that were commented out with `//`. This has been fixed


<a id="org2cfa48d"></a>

### `pyFoamBinarySize.py` did not count files in `build`

Some distros have a directory `build` with the intermediate object
files. This has not been counted until now


<a id="orgf4bf8ba"></a>

### Binary files with `ParsedParameterFile` not working in PYthon 3

Because Python 3 tries to encode read files as Unicode strings and
certain byte combinations are not valid UTF-8 encodings.

Hopefully fixed by reading the file as binary and then create a
`latin-1` encoded string

Reported in
<https://sourceforge.net/p/openfoam-extend/ticketspyfoam/225/> by
Johan Hidding


<a id="org57f3dbc"></a>

## Infrastructure


<a id="org1046e67"></a>

## ThirdParty


<a id="org36b92c7"></a>

# Version 0.6.10 - 2018-08-12

This is only a minor release with the main purpose to recognize
OpenFOAM 6 installations with their new numbering scheme


<a id="orge225361"></a>

## Incompatibilities


<a id="org645bbc1"></a>

### `pyFoamPrepareCase.py` does not execute decomposition scripts for single processor cases

If `numberOfProcessors` is smaller than 2 then the decomposition
scripts are ignored. This may cause problems in the unlikely case
that the setup process relied on these scripts being always
executed


<a id="org790d1fa"></a>

## New feature/utilities


<a id="orgce8148a"></a>

### Utility `pyFoamFunkyDoCalc.py` to compare data from `funkyDoCalc`

This utility compares data written by the `funkyDoCalc`-utility from
`swak4Foam` (this data is written with the `-writeDict`-switch

For details on the usage see the online help of the utility


<a id="org94bc4a8"></a>

## Enhancements to Utilities


<a id="orgb40d3d5"></a>

### Recursive searching for `pyFoamListCases.py`

The `--recursive`-option now recursively searches the specified
directories for cases. Without the option it behaves the way it
did before


<a id="org64a7f8c"></a>

### Look for `customRegexp` in parent directories

The plotting utilities now look for `customRegexp`-files in parent
directories of the case directory. This allows to use one file for
a number of cases. The file in the directory is still used. The
behavior can be switched off with the
`--no-parent-customRegexp`-option


<a id="org6482de5"></a>

### `pyFoamPrepareCase.py` does not execute decomposition scripts for single processor cases

If `numberOfProcessors` is smaller than 2 then the decomposition
scripts are ignored


<a id="org9b738a6"></a>

### `pyFoamPrepareCase.py` checks for proper decomposition

At the end the utility now checks if the number of processor
directories is consistent with the specified `--number-of-processors`


<a id="org12dda64"></a>

### `pyFoamPlotWatcher.py` automatically uses newest logfile

If a logfile `auto` is specified then the utility uses the newest
file with the extension `.logfile` in the current directory.

Like any automatism this might produce unexpected results. So use
with care


<a id="org83c9a38"></a>

## Enhancements to the Library


<a id="orgc3269fd"></a>

### `FoamFileGenerator` handles `OrderedDict`

The class now preserves the order if an instance of `OrderedDict`
is found (instead of the usual behaviour of sorting the keys to
always get the same output)


<a id="org9e4bac4"></a>

### `#sinclude` handled as an alias to `#includeIfPresent`

OpenFOAM v1812 introduces this as an alias. It is now handled by
the parser similarly


<a id="orgec04024"></a>

### OpenFOAM 6 correctly recognized

With OpenFOAM 6 the naming scheme changed again. Instead of 6.0
(which PyFoam would have recognized) it is now plain 6. PyFoam now
recognizes both forms in the directory name


<a id="org077cb49"></a>

## Bug fixes


<a id="org26e29a4"></a>

### `pyFoamPrepareCase.py` did not remove `processor`-directories


<a id="orgaf17c68"></a>

## Infrastructure


<a id="org2f61d6f"></a>

### Single digit version numbers supported

Now installations with names like `OpenFOAM-6` are recognized


<a id="org9b4299d"></a>

# Version 0.6.9 - 2018-02-25


<a id="orgc16f8ae"></a>

## Major changes


<a id="org8c83c28"></a>

### Add `curses`-output to Utilities

On terminals that support it there is now an additional option
`--curses` that enhances the output of the utility. It adds a
header and a footer-line and colors the output if it finds special
strings like the current time.

Some utilities enhance the output event further: the Runner and
Watches utilities color lines that match regular expressions that
are sought for: the line is colored differently and data items
(which are usually plotted) are colored even more
differently. There is also an additional footer-line with the
string that is usally printed by the `--progress`-option

Output can be paused by pressing `space` and resumed by pressing
`space` again. This behavior may be overridden by some utilities

Caution: on some terminal implementations resizing the terminal
causes a segmentation fault of Python which may stop your
simulation


<a id="org0fdb5ba"></a>

## Incompatibilities


<a id="org24cd8d5"></a>

### `pyFoamPrepareCase.py` creates `.foam`-file

The utility now automatically creates a file that allows Paraview
to open the case


<a id="org92516b9"></a>

### Hardcoded Foam-Version upgraded to `4.0`

The hardcoded Foam-version that is used if the
`WM_PROJECT_VERSION` environment variable is not set is set to
`4.0` from the rather ancient version `1.5`


<a id="orgd78b3c9"></a>

### `none` no longer parsed as an equivalent for `false`

This breaks the parsing of cases where `none` is used as a word.


<a id="org69be120"></a>

## New features/utilities


<a id="orgbe9eace"></a>

### `pyFoamJoinTimelines.py` to join Timelines from restarts

This utility joins timeline files from different restarts. The
lines from times that will be in the next file are discarded


<a id="orgcb06231"></a>

### `pyFoamRestartRunner.py` to automatically restart runs

For cases that fail strangely (mostly due to problems in the
linear solver) but restart successfully this utility helps running
them.

The utility tries to restart the solver until either the `endTime`
is reached or no new time-step is written to disk (in this case it
makes no sense to run again)


<a id="org293562d"></a>

## Enhancements to Utilities


<a id="orga3c1ed2"></a>

### Special snapshot utilities to use MESA

There have been variations of the regular `pyFoamPVSnapshot.py`
added. The only difference they have is that they set a option that
enforces the used `OpenGL`-implementation (especially Mesa). Use this run
the script on a machine that don't have hardware support for 3D-graphics


<a id="orgf54541a"></a>

### Automated plotting of film properties

For the surface film solvers there now properties like the mass,
covered surface, thickness and velocity are automatically plotted


<a id="org4ff56ff"></a>

### `pyFoamClearCase.py` automatically executes an existing `Allclean`

If present the script (which is usually found in tutorial cases)
is executed before other cleaning takes places


<a id="org465f949"></a>

### `pyFoamPrepareCase.py` executes tutorial scripts if available

If there are scripts present from the original tutorials that do
**only** case preparation (like `Allrun.pre`) but no solver running
and no special scripts are present then the original scripts are
executed


<a id="org9581ee4"></a>

### Script for clearing in `pyFoamPrepareCase.py`

If a special script `clearCase.sh` is found this is used for
additional clearing. If instead a script `Allclean` is found then
this is used


<a id="orgfdb6512"></a>

### `pyFoamPlotWatcher.py` now can handle multiple files

If the utility gets more than one file it tries to concatenate the
data from theses files. It assumes:

-   that the files are Log-files by a solver. It orders the files by
    the time that the mesh was created. If noo string `Create mesh
          for time =` appears in the file it is assumed that this file is
    the last one in the sequence
-   that all files except for the last one finished writing (this
    basically follows from the previous condition)

If only one file is specified and matching logdfiles from restarts
are found then these are automatically added (there is an option
to prohibit this)


<a id="org77e1322"></a>

### `pyFoamPrepareCase.py` now allows separate decomposition scripts

After three of the phases

-   mesh creation
-   copying of the `.org` files
-   case setup

the utility executes a script (`decomposeMesh.sh`,
`decomposeFields.sh` and `decomposeCase.sh`) if found. This allows
to adapt for different situations (for instance: the mesh already
being generated in parallel)


<a id="org1e4d8ab"></a>

### Runner-utilities now create seperate logfiles on restart

If PyFoam thinks that a run is restarted (old time-files exist and
there already exists a logfile) it creates logfiles with
`.restart` appended. This allows joining the original log and the
restart log


<a id="org135884d"></a>

### `pyFoamPVSnapshot.py` improves rewriting of state-files

The utility now allows changing properties before loading it into
paraview. There is also a number of options that allow setting up
this process.

First the available sources can be listed with
`--analyze-state-file`. From these sources the properties (with
values) for one of these sources can be listed like this

    pyFoamPVSnapshot.py . --list-prop=probeCSV

then one propery can be changed like this

    pyFoamPVSnapshot.py . --set-property=probeCSV:FileName=probes.csv

`--set-property` can be used more than once


<a id="org9fd5484"></a>

### `pyFoamPackCase.py` adds parallel data

With the option `--parallel` now adds parallel data


<a id="orgc9a51a4"></a>

### `--replacement`-option in `pyFoamPVSnapshot.py` supports Foam-format

The option can now alternatively use Foam-format instead of Python-format


<a id="org67823a4"></a>

### `pyFoamPVSnapshot.py` improved error messages with problems in replacement

Instead of a stack trace there is now an output of the template
string and the available values


<a id="org6552dea"></a>

### `customRegexp` now searched in parent directories

If in the directory of the log-file no `customRegexp` and the
log-file is not in the current directory then PyFoam looks for it
in all directories up to the current directories


<a id="org793ee52"></a>

## Enhancements to the Library


<a id="org6bf356e"></a>

### `Paraview.StateFile` extended

This module has been extended to allow more flexible manipulations
of the state-file


<a id="org733a062"></a>

### `BasicRunner` now checks for regular End

The `BasicRunner` now checks whether the string `End` was seen and
**no** time-information after that. This means that the simulation
reached its "regular" end and is also reported in the
`PyFoamState.TheState`-file


<a id="orgab00fa8"></a>

## Bug fixes


<a id="org1d50962"></a>

### `pyFoamPrepareCaser.py` ran out of memory for large script outputs

Because all the output from scripts was stored in memory before
being written to a log it was possible that the utility ran out of
memory when there was much output. The output is now written
directly to disk


<a id="orgb6bbeb1"></a>

### No Courant number plottet if `WM_PROJECT_VERSION` is unset

Scanning for the Courant number defaulted to the versy old
version. This has been fixed


<a id="orgb0602de"></a>

### Rescale does not work for streamlines in `pyFoamPVSnapshot.py`

`--rescale-color-to-source` did not work for sources that have no
cell values (like streamlines). Fixed.


<a id="org7c2278d"></a>

### Server not correctly running on Python 2.7 with `socketserver`

Some installations of Python 2.7 already have the
`socketserver`-module which does not have the required
`BaseServer`-module. Fixed


<a id="orgc6e6588"></a>

# Version 0.6.8.1 - 2017-08-03


<a id="org8c6638c"></a>

## Bug fixes


<a id="org8a792d7"></a>

### Fork not correctly detected for `v1706`

As the `+` is not present in the `WM_PROJECT_VERSION` this distro
was detected as the Foundation fork


<a id="org0555746"></a>

# Version 0.6.8 - 2017-07-06


<a id="org17d70de"></a>

## Major changes


<a id="org58fd6f1"></a>

### `pyFoamNet`-utilities now work without a Meta-Server

As described in other changenotes below the Server process now
announces its presence with ZeroConf. This means that a central
Meta-Server is no longer necessary. But the `zeroconf` library has
to be present on all involved machines (server and client). It is
installed with

    pip install zeroconf


<a id="org7a9e456"></a>

## New features/utilities


<a id="org106028f"></a>

### Added module `PyFoam.Infrastructure.Authentication`

This module implements a simple public key authentication. For
authentication a username and a challenge are sent. If the
username is in the set of authenticated keys (or is the own
username) then this key is used to check the challenge.


<a id="orgbb901de"></a>

## Enhancements to Utilities


<a id="orgac7bb71"></a>

### `pyFoamClearCase.py` now has `-dry-run` option

This option doesn't clear anything but prints the things that will
be erased


<a id="org0c03634"></a>

### New option `--keep-time` for `pyFoamClearCase.py`

This option (which can be specified more than once) allows
specifying single time-steps that should be kept


<a id="org1be3164"></a>

### `pyFoamNetList.py` no longer needs a meta-server to work

Due to the addition of `ZeroConf` this utility no longer needs a
Meta-Server to find running calculations in the same subnet


<a id="org093457b"></a>

## Enhancements to the Library


<a id="org4cf2f23"></a>

### Better calculation of used memory in runs

If the `psutil`-library is installed then the memory used by
parallel runs is calculated as well


<a id="org97deaf9"></a>

### Pre and post-hooks are now also searched in `PyFoam.Site`

`module` specified in `preRunHook_` and `postRunHook_` is now
searched in `PyFoam.Site.` as well. This module is the
`lib`-directory in the directory specified by the environment
variable `PYFOAM_SITE_DIR` (which allows adding user-scripts and
modules)


<a id="org22c626c"></a>

### Adapted to correctly detect `OpenFOAM+ v1706`

This fork has changed its numbering scheme (dropped the `+` in the
version string). This broke a regular expression and a function to
detect the number


<a id="orgbe7391a"></a>

## Infrastructure


<a id="orgde222f0"></a>

### The `Runner`-utilities now register as `ZeroConf`-services

Unless switched off every `pyFoam(Plot)Runner.py`-controlled run
already had a server process that allowed controlling the
process. Now the process also advertises itself via `ZeroConf`
(aka `Avahi`, `Bonjour`, `mDNS`. See
<https://www.wikiwand.com/en/Zero-configuration_networking>)

This allows the `Net`-utilities to operate without a
meta-server.

Due to the limitation of the protocol this only works reliable in
the same broadcast-subnet


<a id="org02969bc"></a>

## Bug fixes


<a id="orgb32b504"></a>

### `--keep-interval` in `pyFoamClearCase.py` not working for parallel-cases

Due to a copy/past error this option did not work for parallel
cases. This is now fixed


<a id="org90f5e54"></a>

# Version 0.6.7 - 2017-06-04


<a id="org5722e2d"></a>

## Requirements


<a id="orgcecc454"></a>

### Now at least Python 2.6 required

The new `PLY`-version and `six` now at least requires this
Python-version. If your system has Python 2.5 or older stick with
PyFoam 0.6.6


<a id="org4f0ed16"></a>

## Incompatibilities


<a id="orgfa6c766"></a>

### Names of files generated by `pyFoamPVSnapshot.py` differ

Due to changes in the time-step numbering the names of the
generated files differ. If your work-flow depends on the old names
add the options `--consecutive-index-for-timesteps` and
`--duplicate-times`


<a id="orgcca0dd5"></a>

## New features/utilities


<a id="org2095586"></a>

### Utility `pyFoamListProfilingInfo.py` to print profiling data

The utility reads the profiling info written by

-   foam-extend
-   OpenFOAM+ v1606 (and higher)
-   or the patch found at <https://sourceforge.net/p/openfoam-extend/svn/HEAD/tree/trunk/Breeder_2.3/distroPatches/applicationLevelProfiling/>

and prints it in a human-readable form


<a id="orgc939fa6"></a>

### Utility `pyFoamBlockMeshConverter.py` to convert a 2D-mesh to 3D

This utility (and the required Libraries) was written by Hasan
Shetabivash (original at <https://github.com/hasansh/blockMeshConverter.git>)

This utility takes a file that is written in a similar syntax as
the regular `blockMeshDict` but with the third dimension
missing. It then converts this file to a regular `blockMershDict`
by either extruding in the $z$-direction or by rotating around the
\(x\) or the $y$-axis


<a id="org26e0cda"></a>

## Enhancements to Utilities


<a id="org7c15240"></a>

### `customRegexp` now can scan for texts

Until now data items (groups) in the regular expression had to be
valid numbers. Otherwise a warning was issued. This behavior is
still the default but if a list-variable `stringValues` is added
then the items (whose numbers are specified in the list) are not
being plotted. They are written to disk with `--write-files` and
they can be used in `progress`


<a id="org537e5ac"></a>

### Lines in `PyFoamHistory` escaped

Additions to the history file where arguments contain whitespaces
and/or quotes are quoted and quotes inside are escaped. This
allows these command lines to be copy/pasted to the command line


<a id="org4b4b3d4"></a>

### `--values-string` of `pyFoamPrepareCase.py` now accepts OpenFOAM-format

These strings are now parsed as OpenFOAM-strings if there is no
starting `{` and no ending `}`. With these the old behavior
(parsing as a Python-dictionary) is used


<a id="orgd6335a7"></a>

### `pyFoamRunner.py` and `pyFoamPlotRunner.py` allow automatic selection of solver

If for those utilities the word `auto` is written in place of a
proper solver (like `interFoam`) then the utility looks into
`controlDict` for the `application`-entry and uses that


<a id="orgab479ce"></a>

### Calculations (data transformations) in `customRegexp`

If an entry `dataTransformations` is specified in the dictionary
then the results of these transformations is are for
writing/plotting instead of the real data.

`dataTransformations` is a list with valid single-line
python-expressions. The groups from the regular expression `expr`
are inserted textually into the expression before it is
evaluated. `$1` is the first group, `$2` the second and so on
(this convention is the same as for the `progress`-string.

The `titles`-entry corresponds to these results. If the "raw"
(untransformed) data should be plotted as well you'll have to add
identity-transformations of the form `"$1"`


<a id="org626d9f0"></a>

### Multi-part `idNr` for `dynamic` in `customRegexp`

`idNr` can now alternatively be a list of integers (instead of a
single integer). In that case the corresponding matches are
concatenated (with a `_` between them) to generate the data id.

If only a number is specified it has the old behavior.

As usual the indexes of the matches stat with \(1\) (not \(0\))


<a id="orgd330c7f"></a>

### `pyFoamListCases.py` detects dead runs

If a run has not had any output in the last hour it is listed as
dead. This threshold can be customized


<a id="org7deb9d1"></a>

### Improved time-handling of `pyFoamPVSnapshot.py`

The utility now numbers the time-steps by the order in the
solution directory. Before that the used time-steps were numbered
consecutively (from \(0\) to \(N-1\) if \(N\) time-steps were specified).

Also: by default each time-step is only processed once

The old behaviour can be reproduced with
`--consecutive-index-for-timesteps` and `--duplicate-times`


<a id="org9c378ae"></a>

### Default plots can be set in configuration

Whether or not plots are plotted automatically (for instance the
execution time) can be set in the `[Plotting]`-section of the
configuration. So it can be set per-case in the
`LocalConfigPyFoam`-file. If a plot is on by default it can be
switched off with the corresponding `--no`-option. If off by
default the `--with`-option switches it on


<a id="orgcb6efe0"></a>

### `derivedParameters.py`-script called from `pyFoamPrepareCase.py` allows error reporting

In that script that calculates new parameters and also can do
parameter checking there now is a function `error` available that
makes the script and the complete execution fail


<a id="org366ed9f"></a>

## Enhancements to the Library


<a id="orgfeaa12a"></a>

### Detection of new versions of OpenFOAM-foundation and OpenFOAM+

Both distros changed their scheme for the version numbers and the
regular expressions have been adapted to detect them


<a id="orgb6a17e9"></a>

### `SpreadsheetData` now handles string data

If one of the columns is string data then the `()`-operator
returns string values (when interpolating the next value)


<a id="orga849b29"></a>

### `TimelineData` tolerates string values

The class can now read strings without spaces (OpenFOAM `words`)
and pass them to `SpreadsheetData`


<a id="org996cd21"></a>

### `()` operator of `SpreadsheetData` works without name

If no `name` parameter is given then the method returns a
dictionary with all the values


<a id="org68ed43a"></a>

### New function `setCurrentTimeline` in `PyFoam.Paraview.Data` to get data at time

This function reads timeline data at a specified position. Return
the interpolated values from the current simulation time as a
table

Use in `Programmable Filter`. Set output type to `vtkTable`.  To
get the values from a timeline
`postProcessing/swakExpression_pseudoTime/0/pseudoTime` use

    from PyFoam.Paraview.Data import setCurrentTimeline
    setCurrentTimeline(self.GetOutput(),"swakExpression_pseudoTime","pseudoTime")

To print the values pipe into a `PythonAnnotation`-filter. Set
ArrayAssociation to `Row Data` and use an Expression like

    "Time = %.1f (%.1f)" % (average,t_value)

(this assumes that there is a column `average`)

Hint: this reads string values as well. But in that case the value has to be
converted with `val.GetValue(0)` in the expression


<a id="orgb366b79"></a>

### User-specific temporary directory

The method `PyFoam.FoamInformation.getUserTempDir` makes sure that
a user specific temporary directory exists and returns the path to
that directory


<a id="org83801cd"></a>

### `Gnuplot`-plots now get better titles

Instead of `Gnuplo` the window titles are now set to `pyFoam` and
the actual title of the plots. This should make it easier to find
plot windows in the window manager


<a id="org8c2c21b"></a>

### `ParsedParameterFile` now supports `#includeFunc`

In case of a `#includeFunc`-entry the file is either searched
relative to the current file (this is where the semantics differ
from how OpenFOAM because that searches in the
`system`-directory. But as this entry is usually called from
`system/controlDict` the result is the same) and if not it looks
for it in `$FOAM_ETC`


<a id="org8e0f5b0"></a>

### New utility function `findFileInDir`

This function in `PyFoam.Basics.Utilities` looks recursively for a
file in a directory


<a id="org4f3569a"></a>

### `humandReadableDuration` added to `PyFoam.Basics.Utilities`

This function takes a duration (in seconds) and prints it in a
human-readable form


<a id="orgedfedbb"></a>

## Infrastructure


<a id="org4953bec"></a>

### `pyFoamVersion.py` now reports the versions of the `ThirdParty`-packages

Now these versions are reported as well for quick reference


<a id="orga723922"></a>

## Bug Fixes


<a id="org50bab27"></a>

### Application classes fail in Paraview

The class `PyFoamApplication` assumes that the module `sys` has an
element `argv`. This is not the case inside Paraview


<a id="orgd09113b"></a>

### Scripts in `pyFoamPrepareCaseParameters.sh` not working on Mac OS X

Because newer versions of Mac OS X remove `LD_LIBRARY_PATH` from
the environment passed to scripts (for security reasons)
additional libraries (for instance `swak4Foam`) were not correctly
loaded. This has been fixed by generating a special script that
exports `LD_LIBRARY_PATH` before executing the rest


<a id="org0b4d996"></a>

### Processor-directories unsorted in `SolutionDirectory`

The class assumed that `processorX` directories were added in the
numeric order which is not necessarily the case. This caused
problems with `pyFoamCaseReport.py`


<a id="orgb8757a5"></a>

### Deleting failed if a file did't exist

The utility function to delete directories failed if the directory
didn't exist. Fixed


<a id="org9bd0471"></a>

### Missing files in `RegionCases`

When creating a `RegionCase` only the "known" files were
symlinked. This causes some programs to fail. Now everything from
`system` in the master-case is symlinked if there is not already a
file of that name there


<a id="org9daea85"></a>

### Wrong `solver` in `pyFoamListCase.py`

If another utility was run in the mean-time the wrong solver is
listed by the utility. Fixed


<a id="orgf589280"></a>

## ThirdParty


<a id="org84edc71"></a>

### Updated `tqdm` to version 4.8.4

No reason. Just because there was an update


<a id="org1ff561c"></a>

### Updated `PLY` to version 3.9

This breaks compatibility with Python 2.5 or older


<a id="org5d78905"></a>

### Updated `six` to 1.10.0

This also breaks compatibiliy with Python 2.5 or older


<a id="orgc9a6c22"></a>

# Version 0.6.6 - 2016-07-15


<a id="orge5b3247"></a>

## Incompatibilities


<a id="orgdf09416"></a>

### Changes in `IPython`-notebooks 3.0

With IPython 3.0 the names of the Widget classes lost the `Widget`
in the name (for instance `DropdownWidget` becomes
`Dropdown`). `PyFoam` has been changed to conform with this but as
a consequence won't work with old version of the `IPython`
notebooks


<a id="org99e069c"></a>

## Enhancements to Utilities


<a id="orgf993d12"></a>

### `pyFoamPrepareCase.py` executes `setFields` if appropriate

If no setup-script is specified and if there is a `setFieldsDict`
present then `setFields` is automatically executed


<a id="org6b9970c"></a>

### Plotting utilities now automatically add custom plots depending on the solver name

The configuration system now has a section `Autoplots`. The
entries there are all dictionaries with two entries:

-   **solvers:** a list of regular expressions. If the name of the
    currently used solver matches any of these
    expressions then this entry is used
-   **plotinfo:** a dictionary with the plot information known from
    regular `customRegexp`: `expr`, `titles` etc

If the solver matches `solvers` then a custom plot based on
`plotinfo` is automatically added.

If the solver does not fit the plot is **not** added (this helps
avoid processing of unused `expr`. This is important because
processing the `expr` is one of the things `PyFoam` uses the most
computation time for)

Some common plots (phase fractions for instance or most of the
output of `chtMultiRegionFoam`) are hardcoded into `PyFoam`

Also there is a new section `[SolverBase]` in the
configuration. It is checked whether the current solver name
**begins** with any of the keys there. If it does then the list of
solvers is assumed to be the solvers this solver was based on and
`Autoplots` for those solvers are added as well. For instance

    [SolverBase]
    myReactingCht: ["chtMultiRegionFoam","reactingFoam"]

assumes that a solver `myReactingChtFoam` is based on these two
solvers and automatically adds their `Autoplots`

In addition if a setting like

    [Plotting]
    autoplots: cloudNumberMass

is set (for instance through `LocalConfigPyFoam` in the case) then
the autoplot `cloudnumbermass` is used regardless of the solver
name


<a id="org9157e1c"></a>

### `alternateAxis`-entries now can be regular expressions

This allows specifying plots generated with `type dynamic` on the
alternate axis


<a id="org2281397"></a>

### Plotting utilities now allow choice of Gnuplot terminal

These utilities now allow with the option `--gnuplot-terminal` to
choose the terminal. Otherwise the terminal specified in the
configuration (usually `x11`) is used


<a id="org9dd160a"></a>

### Plotting utilities now sort legend by name

Names in the legend are now sorted. This improves readability for
large numbers of lines in the plot


<a id="orgcbe8d5e"></a>

### `pyFoamExecute.py` allows calling with debugger

The option `--run-with-debugger` runs the command in the
debugger. The arguments are appropriately handled


<a id="orgf9e5052"></a>

### `pyFoamPrepareCase.py` fails if execution of a script fails

If the execution of a script fails (the status code returned by
the script is not \(0\)) then execution of the utility fails (before
the utility just continued). This behavior can be overridden with
the option `--continue-on-script-failure`.

It is up to the script to ensure that the failure of a utility
called in the script is forwarded to `pyFoamPrepareCase.py`. For
instance with

    set -e

in a `bash`-script


<a id="org3373ec8"></a>

### `--hardcopy` in plotting library now allows modification of `gnuplot`-terminals

This option allows setting the options for the terminal selected
with `--format-of-hardcopy`. This overrides any default set in
configuration section `[Plotting]` under the name
`hardcopyOptions_<term>` with `<term>` being the name of the
terminal (for instance for `png` the option is `hardcopyOptions_png`.


<a id="org7918a49"></a>

### `pyFoamPrepareCase.py` writes state information about what it is currently doing

It writes to the usual state file. This way `pyFoamListCases.py`
will list this information. If the scripts call `pyFoamRunner.py`
then this information will be overwritten


<a id="org74cb96f"></a>

### `pyFoamBinarySize.py` can handle new location of binaries in OpenFOAM 3.0

Since that foam version all binaries (and object files are located
in the directory `platforms`. The utility now finds them there


<a id="orgf86b1d5"></a>

### `Runner`-utilites now can signal on `blink(1)`-devices

With the option `--use-blink1` these utilities now flash on a
plugged in `blink(1)` USB-device for every time-step


<a id="org77ab9c9"></a>

### `pyFoamExecute.py` can flash a `blink(1)`

To indicate that the utility is still running it is able to play a pattern on a
`blink(1)`-device. This is switched on with `-use-blink`


<a id="orgb51b8e8"></a>

### `pyFoamDecompose.py` allows using a template file

With the option `--template-dict` it is possible to initialize the
output with an existing file. With this file it is possible to add
'complicated' settings.


<a id="org1ee5c2e"></a>

### `pyFoamTimelinePlot.py` now handles new format of probe files

Probe files now have one comment line per probe to specify the
position. This format is now correctly detected and plotted. Old
probe files are also handled


<a id="org6249067"></a>

### `ReST`-report of `pyFoamPrepareCase.py` now reports derived parameters

The `.rst`-file written by the utility now adds a section on
derived parameters if such parameters were specified in a script


<a id="org720ce29"></a>

### `pyFoamPrepareCase` can now ignore directories

It is now possible to specify directories that should be ignored
when looking for templates. Some sensible defaults like
`postProcessing`, `processor*` and `VTK` are already set


<a id="org90acc18"></a>

### `pyFoamConvertToCSV.py` allows adding formulas to XLSX-files

The option `--add-formula-to-sheet` allows adding formulas to the
Excel-sheet. Something like

    --add-formula="massflow:::'inlet'-'outlet'"

adds a column `massflow` that subtracts the columns `inlet` and `outlet`


<a id="orge30c165"></a>

### `pyFoamListCases.py` now displays mercurial info

For those who use mercurial to keep track of their cases the
utility now has the option `-hg-info` that displays the mercurial
hash-ID, the local id and the branch name


<a id="org35d2f48"></a>

### Progress bar added to utilities with long run-time

Using the library `lqdm` progress bars have been added to
utilities that have a long run-time and where the progress bars
are not disturbing the regular output. These utilities are

-   `pyFoamListCases.py`
-   `pyFoamBinarySize.py`

Bars can be switched off with `--no-progress-bar`


<a id="org7bf29ae"></a>

### Utilities that clear data can now report what is cleared

`pyFoamCleasCase.py` and all utilities that have a `--clear`
option now also have a `--verbose-clear` option that reports
**what** is being cleared


<a id="org0c1b4e8"></a>

### `pyFoamConvertToCSV.py` now allows manipulating the input

The utility now has two new options:

-   **&#x2013;strip-characters:** This allows removing characters before the
    file is actually read
-   **&#x2013;replace-first-line:** Replaces the first line (for instance if
    the header does not match the data


<a id="org9f61ff6"></a>

## Enhancements to the Library


<a id="org399af66"></a>

### Detection of `OpenFOAM-dev`

A development installation is now also detected and it is assumed
that this uses the new calling convention. Also: PyFoam reports
this as version `9.9.9` (as this is larger than any version in the
foreseeable future


<a id="org5f72765"></a>

### Add `OpenFOAM+` as a fork

An additional fork type `openfoamplus` has been added (in addition
to `openfoam` and `extend`). Installations of the form
`OpenFOAM-vX.X+` (with `X.X` being the version number) are added
to this fork. Also `OpenFOAM-plus` is added as the development
version of this fork


<a id="org7ffbe95"></a>

### Accept new convention for location of `blockMeshDict`

In newer OpenFOAM-versions `blockMeshDict` may be located in
`system`. PyFoam detects it either there or in the old
`constant/polyMesh`-location


<a id="org8eb5c56"></a>

### Handling of complex data by `Configuration`

Lists and dictionaries now can also be specified. Have to be
correctly formatted if they are longer than one line (indented by
at least one space - convention for configuration files)


<a id="org52590ec"></a>

### `Configuration` has method `getArch` for architecture dependent settings

If an option `opt` is requested with this option then it is
checked whether an architecture-dependent setting exists.
Architecture `arch` is the output of the `uname`-command. The
architecture-dependent name is `opt_arch`.


<a id="org64aecbf"></a>

### `execute`-method from `PyFoam.Basics.Utilities` returns status-code

This function now has an option that makes it return the status of
the execution as well as the output of the execution.


<a id="orgcd17a34"></a>

### `BasicRunner` now supports more ways of stopping runs

In the past this class (and the utilities based on it) looked for
a file `stop` and stopped the run (with writing) if it was
found. Now two additional files are looked for

-   **stopWrite:** this waits for the next scheduled write and then stops the run
-   **kill:** gracefully stops the run without any writing


<a id="org5d67cff"></a>

### Added `Blink1` class to support `blink(1)` devices

This class assumes that a `blink(1)` USB-device is present and the
API-server (from the `Blink1Control`-program for this is
running. It wraps these calls so that utilities can use them
conveniently


<a id="orgb20db51"></a>

### `ParsedParameterFiles` now supports `includeEtc`

`#includeEtc` is now supported


<a id="orgb335211"></a>

### Parses uniform fields correctly

Uniform fields of the form `1002{42.5}` (Field with 1002 values
\(42.5\)) are now correctly parsed


<a id="org28e490a"></a>

### `toNumpy`-method added to `Unparsed` and `Field`

These two classes have a method `toNumpy` added that transformed
the data into a structured `NumPy`-array. There are no
applications for this in `PyFoam` yet but an application will be
the parsing of lagrangian data


<a id="orgee03d64"></a>

### Added module `PyFoam.RunDictionary.LagrangianPatchData` to read data from patch function object

This module reads data written by the cloud function-object that
writes particle data as particles hit the patches and transforms
it into `numpy`-array. Which can also be returned as `pandas`
`DataFrames`

It adds some properties to the data

-   the patch name
-   the time at which this data was written
-   a `globalId` constructed from `origId` and `origProcId`


<a id="orgf4aa34a"></a>

### Added module `PyFoam.RunDictionary.LagrangianCloudData` to read cloud data

This gets

-   a case
-   a cloud name
-   a time name and reads the lagrangian data from the specified
    time and converts it to a pandas `DataFrame`

A `globalId` that is consistent with the one in `LagrangianPatchData` is set


<a id="org9e92b8d"></a>

### Method `code` added to =RestructuredTextHelper

This method formats a string assuming that it is a program
code. Default value is `python`


<a id="org31c9b7c"></a>

### `ParsedParameterFile` now parses new dimension format correctly

Newer OpenFOAM-versions allow dimensions in symbolic format (for
example `[ m s^-1 ]`). These are now correctly parsed


<a id="org96e2f2c"></a>

### `ParsedParameterFiel` now parses uniform fields correctly

Fields of the form `23 { 4.2 }` (meaning "23 times 4.2") are now
correctly parsed


<a id="org5993005"></a>

## Infrastructure


<a id="org3a5ee18"></a>

### Change of documentation from `epydoc` to `sphinx`

As `expydoc` is discontinued the API-documentation is now generated
with `sphinx`. Just run

    make docu

to do so.

Advantage is that now with

    make docset

a document set for offline searching with `Dash` (for Mac OS X) or
clones (on other OSes) can be generated


<a id="orgacd4454"></a>

### Adaptions to the unittests

Untitests only used to run correctly if the OpenFOAM-version was
1.7. Are changed to run with OF 3.0. No effort has been made to
support intermediate versions as the changes are mainly about
changed tutorials


<a id="org4ade042"></a>

## Bug fixes


<a id="org114861f"></a>

### Wrong format of `ExecutionTime` breaks plotting utilities

If the `ExecutionTime` is not as expected `pyFoamPlotWatcher.py`
and `pyFoamPlotRunner.py` finish with an error. This is now more
robust


<a id="org6ed440b"></a>

### `phases` not working with dynamic plots

For dynamic plots the addition of the phase name did not work. Fixed


<a id="orgf79d535"></a>

### Phase name added to function object output

If `phase` was set the output of the function objects got it added
to the names even though the function objects do not belong to the
phase. This is fixed


<a id="org2ff6ee3"></a>

### One region mesh too many in utilities that change the boundary

When working with regions one region too many was added in
`pyFoamChangeBoundaryType.py` and `pyFoamChangeBoundaryName.py`. Fixed


<a id="org37a73db"></a>

### `pyFoamClearCase.py` fails on write-protected case

If a case is write protected then the utility failed. Now it only
issues a warning and continues cleaning


<a id="orgb8e828b"></a>

### Copying of directories in `pyFoamPrepareCase.py` confused by zipped files

When copying one file to another and one of them is zipped then
copying doesn't replace the destination correctly but adds the
zipped/unzipped variant


<a id="orga0b8a60"></a>

### Wrong times for multi-view layouts in `pyFoamPVSnapshots.py`

If snapshots were taken from state files with multiple layouts
then some of the views had the wrong time (either that from the
state-file or from the timestep before). Fixed


<a id="org1248f36"></a>

### First timestep not plotted (and not stored)

The data from the first timestep was not plotted under certain
circumstances. This has been fixed


<a id="org5afd363"></a>

### `DYLD_LIBRARY_PATH` not passed on *Mac OS X 10.11*

Starting with this OS-version as a security feature the system
does not pass `LD_LIBRARY_PATH` and `DYLD_LIBRARY_PATH` to a
shell. `PyFoam` detects this and creates these variables and makes
sure they are passed to the processes


<a id="org34a14ec"></a>

### Newer versions of `pandas` broke the writing of excel files with `pyFoamConvertToCSV.py`

The reason is that the old way of making axis data unique did not
work anymore. This has been fixed


<a id="org4b8dd89"></a>

### Capital `E` in exponential notation for floats breaks parser

This problem has been reported at
<https://sourceforge.net/p/openfoam-extend/ticketspyfoam/220/>
(the number `1E-2` is not correctly parsed to `0.01`) and has been fixed


<a id="orgceb54d5"></a>

### `Runner`-utilities clear processor directories if first time in parallel data differs

In cases where the parallel data has a different start directory
than \(0\) the `pyFoamRunner.py` and similar utilities cleared that
data and made a restart impossible. This has been fixed


<a id="org08add87"></a>

### Utilities `pvpython` not working when installed through `distutils`

As the `distutils` (and all mechanisms built on these like `pip`)
replace the used python in scripts the necessary `pvpython` was
removed. This has been fixed by generating a temporary script file
that is actually executed with =pvpython)


<a id="org706f5c2"></a>

## ThirdParty


<a id="orgb4bedb7"></a>

### Added `tqdm` for progress bars

Add the library `tqdm` (<https://github.com/tqdm/tqdm>) for adding
progress bars to utilities.

Library is under `MIT` License


<a id="org90befcc"></a>

# Version 0.6.5 - 2015-06-01


<a id="org837f805"></a>

## Major changes


<a id="org06c5fa8"></a>

### PyFoam now on *Python Package Index*

PyFoam is now found at <https://pypi.python.org/pypi/PyFoam>

Recommended way of installing is using <https://pip.pypa.io/en/latest/> :

    pip install PyFoam

This will also make sure that the required `numpy`-package is
installed


<a id="org9e30c7f"></a>

## Incompatibilities


<a id="orgcc85f9c"></a>

### `ArchiveDir` in `SolutionDirectory` discouraged

As this was never really used it is discouraged (the option is
still there).

If you don't understand what this means it probably doesn't
concern you


<a id="orgeb7e24d"></a>

### Pickled data files now written as binary

All pickled files are now written and read in binary mode (as this
was the only way that works consistently in Python 3). This **may**
cause problems with old cases (but no effort has been made to
check whether this problem actually exists)


<a id="orgc1d5ca5"></a>

### The `PlotRunner` and `PlotWatcher` now don't strip spaces

These two utilities now don't strip leading spaces from the read
lines. This preserves formatting in the output but might break
scripts that rely on these spaces.

The old behaviour may be reset by overriding `stripSpaces` in
section `SolverOutput` with a value `True`


<a id="orgbf372b4"></a>

### Different column names in `pyFoamConvertToCSV.py`

The enhanced naming of the columns might break scripts that rely
on the old naming


<a id="org8b1cdcd"></a>

### `pyFoamChangeBoundaryName.py` and `pyFoamChangeBoundaryType.py` automatically modify `processorX`

In previous versions these boundary files were not modified. Now
they are. Scripts that rely on unchanged `boundary`-files in the
`processorX`-directories might fail. Old behavior can be set with
the `--no-processor`-option


<a id="orgb5857ee"></a>

## Bugfixes


<a id="org0cce517"></a>

### Arbitrary commands in `TemplateFile` passed to file

Lines with `$$` are passed to the file and make it syntactically incorrect.
Fixed


<a id="orgfbe2cc9"></a>

### Pickled files not opened in binary mode

This caused problems in Python 3 were binary strings were not
correctly written (actually: attempts to write them to a
pickle-file made the application fail)


<a id="org964af14"></a>

### Additional fixes for Python 3

In a number of classes/applications semantic differences between
Python 2 and 3 makes these fail on Python 3. Changes are

-   Replace `map` with list comprehension where possible
-   Modify wrappings in `CTestRun` to work with Python3
-   Replace `print` with `print_`
-   Semantic difference in division of two integers: Python3 gives a
    floating point number as a result


<a id="org97dd460"></a>

### `ParsedParameterFile` fails if "complete" dictionary is `#include` ed

If an included dictionary has a header parsing failed. This is
fixed by retrying the parsing with the header


<a id="org256d391"></a>

### `ParsedParameterFile` fails if there is more info after `#include`

If there is for instance a `;` after an `#include` statement the
regular OpenFOAM-parser ignores it. The PyFoam-parser failed. This
has been fixed and the parser behaves like regular OpenFOAM


<a id="org4da5f8c"></a>

### `pyFoamDisplayBlockMesh.py` not working with VTK 6

Due to changes in the API the program did not work. This is now
fixed and the program works with VTK 6 as well as VTK 5


<a id="org3cd7c90"></a>

### `pyFoamCreateModuleFile.py` failed with environment variables containing `=`

In that case an overeager `split` created lists.

Fix provided by Martin Beaudoin


<a id="org69da715"></a>

### Fix import in `GeneralVCSInterface`

Change in the syntax of imports in Python 3 broke this
one. Fixed. But doesn't matter as Mercurial doesn't support
Python3


<a id="org52157fe"></a>

### Support of old format in `ParsedBlockMeshDict` broken

Wrong usage of indexes. Fixed


<a id="org5b04cc2"></a>

### `TemplateFile` not correctly working in Python 3

Reason was a different calling convention to the `exec`-function
of Python. Fixed


<a id="orgb4d8ec4"></a>

### Certain things not done by `pyFoamPrepareCase` in `--quiet` was set

This was due to actions being on the same level as the
debug-output. Fixed


<a id="org65639cc"></a>

### Annoying warning at the start of the run

For certain solvers the plot utilities issued a warning during a
phase when no information about the current time is
available. This is now fixed


<a id="org2743fd9"></a>

### Redirected values

not used when iterating over dictionaries
    When iterating over dictionaries with redirects the values in the
    redirected dictionaries were not used. This is now fixed


<a id="org67bb9e5"></a>

### Behavior of Template-engine not consistent in Python3 and Python2

Due to a difference in the behavior of the `eval`-function in
Python 3 certain expressions (especially with list comprehension)
failed. Fixed


<a id="orga8fdd14"></a>

### Braces, brackets, parentheses in column name broke `RunDatabase`

These characters were stripped out by *SQLite*. They are thus
normalized to special character combinations (which will be
denormalized after reading)


<a id="org286fab7"></a>

### Finding of installations in alternate locations broken

The algorithm to find (Open)FOAM-installations in alternate
locations was broken. Now working again


<a id="orgb8a7b40"></a>

### Failing on 3.x if socket for server thread already occupied

Due to a a change in the socket API if the socket for the network
thread (usually port 18000) was already notified the program
failed. Fixed. Tested on 2.7 as well


<a id="org37810e6"></a>

## Enhancements to Utilities


<a id="org17d86a3"></a>

### `pyFoamPrepareCase` recognizes multi-region cases

If there are multiple regions and no `prepareMesh.sh` then it will
try to execute `blockMesh` for the regions


<a id="org3a4f32d"></a>

### `pyFoamPrepareCase` adds specialized templates

With the option `--extension-addition` additional templates that
override the regular templates can be specified.

Application may be for instance special templates for
`potentialFoam`


<a id="orgc2a9315"></a>

### `pyFoamPrepareCase` keeps data generated by meshing script

If the meshing stage generates a `0`-directory then data in that
directory will be kept. This can be switched off if this is not
the desired behaviour


<a id="org5bbb50e"></a>

### `pyFoamPrepareCase` adds possibility for a file with default values

If a file `default.parameters` is found in this directory then
this file is automatically read. This file is read like a regular
parameter-file but it can also have added information about the
values:

-   if an entry is a dictionary and has the entries `description`
    and `values` then it is assumed that this is a *group of
    values*. These groups are only used for grouping in reports. The
    `values` are set in the global scope.

    Groups can be nested
-   if an entry is a dictionary and has the entries `description`
    and `default` then it is assumed that the dictionary holds
    meta-information about the value. The entry `default` is the
    value that is actually used.
-   an additional enty `options` in that dictionary specifies a list
    of valid values for that parameter. The utility fails if the set
    value is not in that list. This is useful for setting boundary
    condition types or similar entries where only a limited number
    of words is valid

It is recommended that **all** used values are specified in this
file as this will be used for reporting


<a id="org08a0dcf"></a>

### `pyFoamPrepareCase` writes report about the variables

The utility now writes a *Restructured Text* file with a report
about the variables. Information from `default.parameters` like
groupings and `description` are used in this report. Also the
default value and the actual value are reported.

The file can be converted with a utility like `rst2pdf`


<a id="org0e9f5f5"></a>

### Gnuplot can be styled with default commands

For all utilities that use Gnuplot as the backend for plotting
there is now a configuration option `gnuplotCommands` in the
`Plotting`-section with the usual `set` commands of Gnuplot. This
is preset to display a grid and the y-axis.

The settings can be reset with the `gnuplotCommands`-list in the
`customRegexp`-entries


<a id="orgfbf177f"></a>

### `pyFoamPVSnapshot.py` now supports Paraview 4.2 and later

The API for screenshots changed with Paraview 4.2 and later. This
API now supports layouts if multiple views were specified. The
default behaviour is now to make only one screenshot per
layout. The old behaviour (one screenshot per view) can now be
switched on with the `-no-layouts`-option.

This allows screenshots exactly the way they look on screen


<a id="orgd3f9c72"></a>

### `pyFoamPVSnapshot.py` allows switching between decomposed and reconstructed data

The utility now rewrites the state file so that either decomposed
or reconstructed data is read. The default is that the data set
for which more timesteps exist is selected


<a id="org76523c4"></a>

### `pyFoamPVSnapshot.py` allows changing the field for sources

It is now possible to specify a dictionary with source names and
the fields that should be set for them. This allows quickly
coloring the same layout with different fields.

This works for

-   3D (rendered) filters
-   bar charts


<a id="org0396936"></a>

### `pyFoamPVSnapshot.py` allows rescaling the color-legend

There are now two ways to rescale the color-transfer functions

-   by specifying a dictionary with the ranges
-   by specifying a source. The range of the data on that source
    will be used to scale the data
    -   when specifying a source percentiles can be specified for the
        highest and lowest percent of the cells to be ignored

The first method will override the second


<a id="org4e2173a"></a>

### `pyFoamPVsnapshot` reads parameters written by `pyFoamPrepareCase.py`

An option allows specifying that these parameters should be
read. They are then available for substitution in the *Text*
source


<a id="org52ddd13"></a>

### `pyFoamListCases.py` allows filtering

The utility now has options to select the cases that should be
considered by name of the case. Either substrings or globs can be
used. Ignore patterns can be specified as well


<a id="org50525aa"></a>

### `pyFoamRunParametervariation.py` now allows dictionaries

The format of the parameter-file has been extended so that instead
of values variations can be dictionaries. The contents of the
dictionary are then used instead of a single value. An example
would look like this

    defaults {
             a 1;
             b 2;
             c 3;
    }

    values {
           solver (
                  interFoam
           );
           inVel ( 1 2 );
           outP ( 0 1 );
           sets (
                { name foo; a 3; }
                { name bar; b 4; c 5; }
           );
    }

where sets has two variations. Values unset in `sets` will be used
from `defaults`


<a id="orgf0b422d"></a>

### `pyFoamConvertToCSV.py` now has all functionality of `pyFoamJoinCSV.py`

Now all functionality of the `Join`-utility is present in the `Convert`
utility (including interpolating times)

`pyFoamJoinCSV.py` will be removed in future versions of `PyFoam`


<a id="orgf85b209"></a>

### `dynamic` in `customRegexp` now allows composition from multiple match-groups

If `idNr` is a list then now the actual id is composed from all
the match groups specified in that list. If `idNr` is an integer
then it behaves like it used to.

Application for the new behavior would be for instance to have the
flow of different species on different patches in one plot


<a id="orgad21b17"></a>

### New type `dynamicslave` in `customRegexp`

This combines the properties of the types `dynamic` and `slave`:
dynamically generated data sets that are added to another plot


<a id="org62e1e49"></a>

### Additional profiling option `--profile-line-profiler`

Uses the library `line_profiler` for profiling. Only of interest
for developers. Experimental


<a id="org91e5241"></a>

### Utilities that use templates can be customized with the configuration

The section `Template` in the configuration now allows modifying
the behavior of the templating engine (how templates are processed
and syntax details)


<a id="orgd547be9"></a>

### `LocalConfigPyFoam` now can be read **before** argument parsing

This allows overruling options before they are set be command line
options. This has to be enabled by the application (it doesn't
make sense for all).

An example is the `pyFoamPrepareCase.py`-utility where the local
configuration file can overrule the default behavior of the
template engine


<a id="orgc4e2b31"></a>

### `pyFoamConvertToCSV.py` automatically selects the output format with `--automatic-format`

Now if that option is selected and the extension of the output is
`xls` the option `-write-excel-file` doesn't have to be set
anymore


<a id="orgcb7e94f"></a>

### `pyFoamConvertToCSV.py` allows adding original data as separate sheets

The input data files now can be added to an excel-file as separate
sheets with the `--add-sheets`-option


<a id="org8e37034"></a>

### `pyFoamConvertToCSV.py` has improved naming of columns

Now if there is more than one source file then the columns from
the first source also get a unique prefix.

It is also possible to clean the column names before writing them
to file. The time name can be changed with
`-write-time-name`. Substrings can be replaced with
`--column-name-replace` and simple functions can be applied with
`--column-name-transformation`


<a id="org8398d5c"></a>

### `pyFoamConvertToCSV.py` now supports sets-files

The utility now can read these files and determine the field names
from the filename. `--automatic` assumes that files with the
extension `.xy` are of this format


<a id="orgfa94678"></a>

### `pyFoamPrepareCase.py` can calculate derived values with a script

If a script `derivedParameters.py` is present then it is executed
and values set in that script can be used in the templates as well


<a id="org1da6355"></a>

### `pyFoamPrepareCase.py` adds a variable `numberOfProcessors`

If unspecified by the user this variable is automatically \(1\). It
can be used by the templates to distinguish between different cases

The `PrepareCaseJob`-class in `ClusterJob` automatically sets the
values according to the number of processors in the cluster job


<a id="orgfcde9a5"></a>

### `pyFoamChangeBoundaryName.py` and `pyFoamChangeBoundaryType.py` now support decomposed cases

Both utilities now also modify the boundary files in the
`processorX`-direcories. This behaviour can be switched off from the command line


<a id="orgda2ac0f"></a>

### `pyFoamPrepareCase.py` has possibility for templates after the final stage

Templates with the extension `.finalTemplate` are executed after
the `caseSetup.sh`-script.


<a id="orge24a012"></a>

### `pyFoamRunParameterVariation` allows adding postfix to cloned cases

The option `--cloned-case-postfix` adds a postfix to the cloned
directory names. This can be used if the results from multiple
variations with the same parameter file should be kept (for
instance when comparing OpenFOAM-versions)


<a id="org6fa9fd7"></a>

### `pyFoamConvertToCSV` now allows setting of default input file format

The option `--default-read-format` now allows setting a different
format than `csv` as the default format for input files


<a id="org822780f"></a>

### `pyFoamListCases.py` adds the hostname to the printed information

The utility tries to determine from the pickled data the host the
simulation was run on and prints it (can be switched off with an
option)


<a id="orgb727e4b"></a>

### `pyFoamPrepareCase.py` allows cloning

The utility now has an option `--clone-case` to clone a new case
before starting instead of working in the specified directory (in
this case the case will be cloned to this directory). The name of
the created directory **can** be constructed from the specified
parameters with the `--automatic-casename`-option


<a id="org3d1facc"></a>

## Enhancements to the Library


<a id="orgeeebf0b"></a>

### `SolutionDirectory` detects multiple regions

Valid regions are sub-directories of `constant` that have a
`polyMesh`-directory


<a id="orgbb3a827"></a>

### `BoolProxy` now compares like builtin `bool`

Comparison used to fail for types where it was not explicitly
implemented like `None`


<a id="org36667ea"></a>

### `PyFoamApplication`-class now supports `pvpython` for debugging

Now `--interactive-after-exception` also works in the utilities
that use `pvpython`


<a id="org57b05b6"></a>

### `TemplateFile` now allows more flexible assignments

In the mode where executions are allowed now more flexible
assignments to variables are possible. To be specific:

-   array assignments like

    $$ a["t"] = 2

-   multiple assignments like

    $$ a,b = 2,3


<a id="org207f5b1"></a>

### `ThirdParty`-library `six` upgraded to 1.9.0

This library has been upgraded to the latest released version


<a id="org5b6cb06"></a>

### Additional markup in `RestructuredTextHelper`

There are additional methods `emphasis`, `strong` and `literal`
that wrap their arguments in the appropriate markup

The methods `bulletList`, `enumerateList` and `definitionList`
take lists or dictionaries and mark them as lists


<a id="org91bb0d7"></a>

### `SpreadsheetData` can now read files produced by the `sets`-functionObject

If the option `isSampleFile` is set then it is assumed that the
field names are in the filename and there is no header with field
names in the file


<a id="orge4868bf"></a>

## Infrastructure


<a id="org5af9bae"></a>

### Adaption of Debian packaging to new conventions

By Oliver Borm. The building of Debian packages for Python
libraries has changes. Necessary adaptions were done by Oliver Borm


<a id="org7ee55d6"></a>

## Development changes


<a id="org61fc291"></a>

### Now uses `pytest` for unittesting

The `nose`-library had problems and all the unit-tests run
out-of-the-box with `pytest`


<a id="orgadf4fc4"></a>

# Version 0.6.4 - 2014-11-24


<a id="orgc444f6f"></a>

## Requirements

The only requirement is a python-installation. The main testing and
development has been done with 2.7 and 2.6. Python 2.5 should work
but not for all utilities. Currently 2.6, 2.7 and 3.4 are used
during development.

Certain functionalities need special Python-libraries. The main one
is `numpy` for plotting. Other libraries that might be of interest
are `matplotlib`, `pandas` and `IPython`. For
`pyFoamDisplayBlockmesh.py` the libraries `PyQt4` and `vtk` are
needed. Other libraries are tested for and reported by
`pyFoamVersion.py` but not required (only install if you're sure
that you need it)


<a id="org3d4e387"></a>

## Future changes


<a id="org2a473dc"></a>

### Redundant utilities `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py` unified

These two utilities are almost indistinguishable and will be
unified into one


<a id="org6d9eac0"></a>

## Major changes


<a id="orga62f6f8"></a>

### Multi-line regular expressions in `customRegexp`

If in `customRegexp` an `expr` is found with `\n` then this
expression is matched over multiple consecutive lines. Types like
`dynamic` work as usual.

This makes it possible to match for instance the output of the
`forces`-function objects


<a id="org4b34ec9"></a>

### Enhancement of `pyFoamPrepare.py`

The utility which was introduced in the last version is becomong
more usable and will be central to all things that set up the case
(for instance a special `ClusterJob`)


<a id="org54e8f52"></a>

### Enhancements of the CSV-utilities

These utilities are now more flexible and allow writing and
reading of Excel-files too


<a id="org154001d"></a>

### Environment variable `PYFOAM_SITE_DIR` and `PYFOAM_DIR`

Both variables are not necessary but `PYFOAM_SITE_DIR` allows
consistent insertion of site-specific libraries and utilities.

`PYFOAM_DIR` is set by some Foam-distributions and tested for by
`pyFoamVersion.py`. It is supposed to point to the currents
PyFoam-installation.

`PYFOAM_SITE_DIR` points to a directory with site-specific scripts
and configurations. The sub-directories supported (and thested py
`pyFoamVersion.py`) are

-   **bin:** directory with scripts. It has to be added to the `PATH`
    outside of PyFoam (for instance in the `.bashrc`)
-   **etc:** Optional directory which is searched for configuration
    files. Priority is below the user settings and above the
    global settings
-   **lib:** Optional directory to allow mixing in site-specific
    library files. Imported as `PyFoam.Site`: For instance if
    a file `Foo.py` is present in `lib` it can be imported as
    `PyFoam.Site.Foo`. This directory does not have to be (in
    fact: it **shouldn't**) added to `PYTHONPATH`

Purpose of `PYFOAM_SITE_DIR` is to allow administrators to provide
site-wide scripts and settings for all users on a site


<a id="org83ddbb6"></a>

## Incompatibilities


<a id="org156e8e9"></a>

### Option `--silent` removed from `pyFoamPrepareCase.py`

Option has been renamed to `--no-complain`


<a id="orgc40d03b"></a>

### Keys in `RunDatabase` with column-names that contain upper-case letters change

SQLite does not support case-sensitive column-names (`s_max` and
`S_max` are the same). To change this the upper case letters in
the column names are replaced by an underscore and the letter
(`S_max` becomes `_s__max`)

This means that old databases might not be read correctly


<a id="org064d808"></a>

### Change in unique variable names in `pyFoamConvertToCSV.py`

The algorithm to make variable names unique has changed (basically
it uses the part of the filenames that differ) and scripts relying
on these names might fail


<a id="orgcf4f4c2"></a>

### `PyFoam.IPython`-module renamed to `PyFoam.IPythonHelpers`

The name of the module crashed in certain instances (especially
unit-testing) with the regular `IPython`-library. To avoid these
crashes it has been renamed to `IPythonHelpers`. This raises two
potential problems:

-   scripts that `import` the module have to be adapted to the new name
-   IPython-notebooks created with `pyFoamIPythonNotebook.py` have
    two imports pointing to this module. These notebooks have to be
    adapted to be usable again


<a id="orgbf99e07"></a>

## Bugfixes


<a id="org3b869aa"></a>

### Templates in `pyFoamPrepareCase.py` did not keep permissions

This was a problem for script-templates which were not executable
any more. Fixed


<a id="org3b1f15e"></a>

### `pyFoamComparator.py` failed due to circular dependency

This has been fixed by adding an import in `BasicRunner.py`


<a id="orga360801"></a>

### `pyFoamDumpRunDatabaseToCSV.py` fails if Pandas-data is requested

This is now fixed


<a id="orgcc9ef74"></a>

### `sort` for list broke code on Python 3

Some calls for `sort` still used the `cmp`-parameter which does
not exist for Python3 anymore. These calls have been replaced with
`key` and `reverse`


<a id="orgff0ead5"></a>

### Changing the OF-version does not work in Python 3

Because the output of `subprocess` is now *binary* instead of a
regular string. Fixed


<a id="org407a0b2"></a>

### `addData` in `PyFoamDataFrame` extrapolates for invalid values

This was due to incorrect use of the `interpolate`-method


<a id="org6b31e0c"></a>

### `--keep-last` did not work for `pyFoamClearCase.py` and parallel cases

This was because there was a problem in the library code and the
utility did not consider the parallel time-steps. Fixed


<a id="org251553a"></a>

### `pyFoamDumpRunDatabaseToCSV.py` does not add basic run information

Basic run information was not added to the file. Now it is with
the prefix `runInfo//`


<a id="org01c5894"></a>

### Restore of `FileBasisBackup` did not work

The logic for checking whether a file was "backupable" was
wrong. This affected the proper restore of files with utilities
for instance for `--write-all`


<a id="org5e94bd0"></a>

### Remove circular dependency in `DataStructures`

According to the bug
<http://sourceforge.net/p/openfoam-extend/ticketspyfoam/219/> it was
not possible to import `DataStructures` because of a circular
dependency with `FoamFileGenerator`. Fixed by moving an import to
the back of the file


<a id="org237943c"></a>

## New features/Utilities


<a id="orgcb1ac46"></a>

### `pyFoamRunParameterVariation.py`

This utility takes a template case and a file specifying the
parameter variation and creates cases with the
`pyFoamPrepareCase.py`-engine, runs a solver on these cases and
collects the data into a database. The database can then be
extracted with `pyFoamDumpRunDatabaseToCSV.py`


<a id="org615335e"></a>

### `pyFoamBinarySize.py`

Calculates the size of the binaries in an OpenFOAM-installation
separated by compile-option


<a id="orgcd3d92d"></a>

### `pyFoamBlockMeshRewrite.py`

Assists the user in rewriting the `blockMeshDict` by doing simple,
but error-prone transformations. Assumes "sensible" formatting:
one block/vertex etc per line.

Sub-commands are:

-   **refine:** refines mesh by multiplying cell numbers in the blocks
-   **number:** Adds comments with the vertex numbers. Should help the
    user when editing/modifying the mesh
-   **stripNumber:** Remove the comments added by `number`
-   **mergeVertices:** Adds vertices from other blockMeshes that
    are not present in the current blockMesh
-   **renumberVertices:** Take another `blockMeshDict`, copy over the
    `vertices`-section of that mesh and rewrite `blocks` and
    `patches` so that they conform to these `vertices`. The
    original `vertices` have to be a sub-set of the `vertices` in
    the other mesh
-   **normalizePatches:** Rotates patches so that the lowest number is
    in front


<a id="org2d467dd"></a>

## Enhancements to Utilities


<a id="orgcb34fd4"></a>

### `pyFoamChangeBoundaryType.py` allows setting additional values

The option `--additional-values` allows specifying a dictionary
with additional values for the boundary (stuff that is needed by
`mappedWall` etc)


<a id="org347f336"></a>

### `pyFoamPrepareCase.py` now has OF-version and fork as defined variables

This allows to write case-templates that can distinguish between
different OF-versions


<a id="org63afcbd"></a>

### `pyFoamPrepareCase.py` now allows "overloading" another directory

Before doing anything else the contents of different directories
are copied into the current case. This allows for instance to use
tutorial cases as the basis for a case


<a id="orgcf2e1f9"></a>

### `pyFoamIPythonNotebook.py` adds improvements to the notebook

Additional code added to the generated notebook:

-   Code to change the default size of the plots
-   Distribution-directories in subdirectories `distributions`
    (generated by some `swak`-function objects) added


<a id="org4cd1198"></a>

### `pyFoamListCases.py` more tolerant to faulty `controlDict`

If the `controlDict` is acceptable to OpenFOAM but syntactically
incorrect for PyFoam (for instance because of a missing semicolon)
the utility does not fail anymore (but no data is collected for
that case).


<a id="orgf09c121"></a>

### `pyFoamDumpConfiguration.py` prints sections and keys alphabetically

This should make it easier to find items


<a id="org8750c1e"></a>

### `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py` read and write Excel-files

Both utilities now allow writing Excel-files

In addition to regular text files the first sheet from `xls`-files
can be read


<a id="org1f79484"></a>

### Flexible variable filtering in `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py`

Now it is possible to filter for regular expressions

The functionality of the two utilities now is very similar and it
is possible that one of them will be discontinued


<a id="org722b4d6"></a>

### Columns in `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py` can be recalculated

The two utilities now can add columns or recalculate columns
based on the existing column values


<a id="orge839bc4"></a>

### Testing for `Numeric` removed from `pyFoamVersion.py`

Testing for the library `Numeric` library removed as it is no
longer supported as a fallback for `numpy`. Test also removed from
`setup.py`


<a id="org56f1593"></a>

## Enhancements to the Library


<a id="org006c877"></a>

### Subclass of `ClusterJob` that support `PrepareCase`

The class `PrepareCaseJob` supports cases that are set up with
`pyFoamPrepareCase.py`. Additional parameters to the constructor are

-   the name of the parameter-file
-   a list with the parameters. The list is composed of
    name/value-pairs


<a id="org0520fe4"></a>

### Subclass of `ClusterJob` that support `RunParameterVariation`

The class `VariationCaseJob` supports cases that are set up with
`pyFoamRunParameterVariation.py`. Additional parameters to the constructor are

-   the name of the parameter-file
-   the name of the variations-file


<a id="org917d6f1"></a>

### `execute` in `PyFoam/Utilities` fails if script is not executable

The function checks if the file exists and is **not**
executable. The program fails in that case


<a id="org84c078a"></a>

### `foamVersion` uses a separate wrapper class for `tuple`

This ensures that it is printed in a form that is valid in
OF-dictionaries


<a id="org1371fd8"></a>

### Move calculation of disk usage to `Utilities`

This has until now only been used in `ListCases` but moved to a
separate method/function `diskUsage` in the `Utilities`-module


<a id="org8af6285"></a>

### Enhancement of `--help`

Added the possibility to have an epilog and usage examples with
the `epilog` and  `examples`-keyword arguments for applications.

These and descriptions now have the possibility for line-breaks:
if two line-breaks are encountered in the text a new paragraph is
created


<a id="org26b14d6"></a>

### `which`-routine in `Utitlities` uses native Python-routine

For Python-version where `shutil` has a `which`-function this is
used instead of calling an external program


<a id="org5e1a0f2"></a>

### `FileBasis` now allows file handles instead of the filename

This currently only works for reading, Backups, zipping etc won't
work but it makes algorithms more flexible


<a id="orgbc8489f"></a>

### `BlockMesh` doesn't force writing to file anymore

Instead content is stored in memory. Old behaviour is the default
to preserve compatibility with old scripts


<a id="org8a697e9"></a>

### Additional methods for `BlockMesh`-class

-   **numberVertices:** Adds comments with the vertex numbers to the
    vertices


<a id="org87f6e7e"></a>

### `LineReader` allows keeping spaces on left

Previous behaviour was stripping all spaces from the lines. Now
the left hand spaces can be ket. Old behaviour is still default
for compatibility


<a id="org9cf54da"></a>

### `TemplateFile` now allows writing of assignment-results in file

This allows faster debugging of template-files. This can be
enabled with a switch in the utilities using templates


<a id="orgb91d014"></a>

### `SolverJob` now allows passing of parameters to the solver

And additional parameter `solverArgs` will now be passed to the
solver (if the solver accepts arguments)


<a id="orgb48f232"></a>

### `SpreadsheetData` now allows reading from an Excel file

During construction if an Excel-file is specified and the
`xlrd`-library and `pandas` are installed then the first sheet in
the file is read


<a id="org3fb4a0d"></a>

### `SpreadsheetData` allows recalculating columns

Columns can be recalculated using expressions. This includes other
data items. Currently present column names are available as
variables. There is also a variable `data` that can be subscripted
for items that are not valid variable names. A variable `this`
points to the item to be recalculated


<a id="orgf43d83b"></a>

## Known bugs


<a id="orga403ece"></a>

### Timelines not forgotten for multiple runner calls

This manifests with `pyFoamRunParameterVariation.py`. The custom
timelines are still kept in memory. Not a problem. Just annoying


<a id="org017701f"></a>

# Version 0.6.3 - 2014-06-23


<a id="orged77a1d"></a>

## Requirements

The only requirement is a python-installation. The main testing and
development has been done with 2.7 and 2.6. Python 2.5 should work
but not for all utilities. Unit tests run on Python 3.4 but it is
currently not used in a production environment (reports of success
or failure most welcome)

Certain functionalities need special Python-libraries. The main one
is `numpy` for plotting. Other libraries that might be of interest
are `matplotlib`, `pandas` and `IPython`. For
`pyFoamDisplayBlockmesh.py` the libraries `PyQt4` and `vtk` are
needed. Other libraries are tested for and reported by
`pyFoamVersion.py` but not required (only install if you're sure
that you need it)


<a id="orgcc80bb8"></a>

## Major changes


<a id="orge28a831"></a>

### Version changing supports forks of OpenFOAM

Now `pyFoam` supports different versions of OpenFOAM for switching.
Out of the box `openfoam` and `extend` are supported. If only the
version number is specified (for instance by `--foamVersion=1.7.x`)
and such a version exists only for one fork it is correctly
expanded with the correct fork( in the example with
`openfoam-1.7.x`). If more than one fork has the same version then
the fork name has to be specified as well

Note: additional forks can be easily specified with the
configurations. In section `OpenFOAM` the parameter `forks` has to
be extended. For each new fork a `dirpatterns` and
`installation`-parameter has to be specified


<a id="orga5eefde"></a>

## Incompatibilities


<a id="org1794e8e"></a>

### Change of command interface of `pyFoamSTLUtility.py`

The selection of what is to be done is now selected by subcommands
instead of options. This will break scripts using this


<a id="org6c8e094"></a>

### If `0.org` is present `pyFoamCloneCase.py` and `pyFoamPackCase.py` ignore `0`

The reason is that the utilities assume that this directory is
produced from `0.org`


<a id="orga0c764a"></a>

## Bugfixes


<a id="org1b0149d"></a>

### PlotWatcher has long times between updates if pickling takes long

The reason was that it used the same throttling that made sense
for the PlotRunner. Fixed


<a id="orgdd092e9"></a>

### `pyFoamPVSnapshot.py` fails for newer paraview-versions

Reason is that the class `vtkPythonStdStreamCaptureHelper` does
not support `isatty`


<a id="org9406646"></a>

### SamplePlot failed when valueNames are unspecified

Reported in
<https://sourceforge.net/apps/mantisbt/openfoam-extend/view.php?id=208>
and fixed


<a id="orgd7c097c"></a>

### `pyFoamTimelinePlot.py` failed Numpy/Pandas output of vector fields

Vector fields only were added to the data fields if they were the
first in the list. Fixed


<a id="org87ee89f"></a>

### `alternateAxis` ignored for slave

This is now fixed. The alternate values have to be specified in
the master (specifying in the slave gives an error)


<a id="org805e442"></a>

### `pyFoamCaseReport.py` more stable for binary `boundary`-files

Usually these files are `ascii` (even if the header says
`binary`). In some cases the parsing failed for these. Fixed by
enforcing reading as `ascii`. Can be switched off


<a id="orgfd5ec9f"></a>

### `SpreadsheetData` returns data which breaks certain Pandas-operations

The reason was that if there were duplicate times in the table the
index was non-unique which certain Pandas-operations don't
appreciate. Solved by dropping duplicate times. Can be switched off


<a id="org1ff4c14"></a>

### `pyFoamCloneCase.py` added duplicates to the archive

If things are specified twice they were added twice. Now it is
checked whether the item already exists in the tar-file before
adding them


<a id="orgc8eaa3b"></a>

### `nonuniform` of length 3 not correctly printed

The reason was that this was interpreted as a vector and the
numeric prefix was removed. Reported at
<http://sourceforge.net/apps/mantisbt/openfoam-extend/view.php?id=218>

Fixed by introducing an extra parameter to `FoamFileGenerator`


<a id="orgd29b618"></a>

## New features/Utilities


<a id="orgd75aa43"></a>

### `pyFoamPrepareCase.py` for case preparation

This utility aims to reduce the need for boilerplate scripts to
set up cases. The steps it executes are

1.  Clear old data from the case (including processor directories)
2.  if a folder `0.org` is present remove the `0` folder too
3.  go through all folders and for every found file with the
    extension `.template` do template expansion using the
    pyratemp-engine
4.  create a mesh (either by using a script or if a `blockMeshDict`
    is present by running blockMesh. If none of these is present
    assume that there is a valid mesh present)
5.  copy every `foo.org` that is found to to `foo` (recursively if directory)
6.  do template replacement for every `.postTemplate`
7.  execute another preparation script


<a id="org18f28ab"></a>

### `pyFoamIPythonNotebook.py` for generating and manipulating IPython-notebooks

This utility creates and manipulates IPython-notebooks for
analyzing OpenFOAM cases. It has a number of subcommands:

-   **create:** this is the main command. All other commands assume
    that the notebooks they work with were created with
    this.

    The utility looks at the case specified and creates a
    notebook that has the capabilities to quickly build a
    report about the case:

    -   reporting general properties of the case. This
        basically is the capability of the
        `pyFoamCaseReport.py`-utility
    -   It searches for data that can be visualized by
        `pyFoamTimelinePlot.py` or `pyFoamSamplePlot.py` and
        generates selectors that allow the user to select
        which data to import. The selectors import the data as
        Pandas-`DataFrames` and create the commands
        necessary to do this. It is recommended to erase the
        selector afterwards
    -   Selectors for pickled case data and pickled plot
        generated by PyFoam
    -   Capability to store read data **in** the notebook
        file. This feature is experimental and has
        performance issues for medium to large datasets

    The created notebook can be executed but needs to be
    edited to be useful
-   **clear:** removes selected cells (but only cells created with
    `create`) or output from the notebook.
-   **info:** prints information about the notebook
-   **copy:** copies notebook to a different case and rewrites it so
    that data is read from that case

Recommended way of working with this utility is

1.  Create notebook with utility
2.  Edit it to contain standardized evaluations
3.  Copy it over to another, similar case


<a id="org9ae8ff2"></a>

### Additional sub-module `PyFoam.IPython`

The purpose of this submodule is to support
`pyFoamIPythonNotebook.py`. It has the classes

-   **Notebook:** read a file and interpret it as an
    IPython-notebook. Do manipulations on this notebook
-   **PermanentStorage:** Implements permanent storage in an
    IPython-notebook. Only works inside a notebook and allows
    only one instance at once. Passing the data from the notebook
    (through JavaScript) to Python currently is a performance
    bottleneck
-   **Case:** Convenience object that exposes the functionality of
    some of the PyFoam-utilities through a simple interface


<a id="org64737a4"></a>

### Additional sub-module `PyFoam.Wrappers`

Wraps popular Python-libraries to add functions that make it
easier to work with OpenFOAM-data.

Currently only one Wrapper is implemented:

1.  `Pandas`-wrappers

    This provides `PyFoamDataFrame` as a wrapper for `DataFrame`. The
    functionality added is

    -   **addData:** Conveniently add new data from different `Series`,
        `DataFrames`. It is assumed that the index is the
        same property (time or for samples the distance) but
        with a different resolution. The indexes are joined
        and missing data is interpolated
    -   **integrate, validLength, weightedAverage:** uses the index as
        the $x$-axis and calculates these properties for a
        `Series`. `validLength` is the extent on which data is
        defined (`weightedAverage` is basically `integrate` divided
        by `validLength`). For `integrate` the trapezoid-rule is used
    -   **describe:** adds the three above quantities to the regular
        `describe`-command


<a id="org9add3db"></a>

## Enhancements to Utilities


<a id="org6f440d2"></a>

### `pyFoamSampleplot` has option to use index instead of time in filenames

The option `-index-instead-of-filename` switches this on. This
makes it easier to generate movies from the files


<a id="org685a706"></a>

### `pyFoamListCases.py` Allows addition of custom data

The option `--custom-data` now allows the specification of custom
data items. These are read from the `pickledData`-files and
displayed in the table like regular data items


<a id="orge4ebf39"></a>

### Switch compiler versions

Now all utilities allow switching the compiler version (for
instance from `Gcc47` to `Gcc48`). The relevant options are
`--force-system-compiler`, `--force-openfoam-compiler` and
`--force-compiler`


<a id="org06414b0"></a>

### `pyFoamVersion.py` reports the installed versions better

Now the location of the installations is reported as well


<a id="orge5d9aaf"></a>

### Offscreen rendering can be switched off in `pyFoamPVSnapshot.py`

This is a workaround where the writer produces a segmentation
fault


<a id="orgd404e8f"></a>

### Write 3D-data in `pyFoamPVSnapshot.py`

In addition to writing out bitmaps allows writing out 3D-data (for
importing into other applications). Sources can be selected by name


<a id="org4d3d3d3"></a>

### Added capabilities to `pyFoamSTLUtility`

The utility can now also:

-   erase selected patches
-   merge selected patches into one


<a id="org5955867"></a>

### `pyFoamDecomposer.py` switches off function objects

This now automatically happens for OF-versions that support
it (2.0 and greater). They can be switched on again


<a id="org17a3786"></a>

### `pyFoamCloneCase.py` clones more stuff

Files that are assumed to be used by `pyFoamPrepareCase.py` are
automatically added to the clone. This includes all files (and
directories) with the extensions `.sh`, `.template` and
`.org`. Also IPython notebooks (extension `.ipynb` are added)


<a id="orge109e86"></a>

## Enhancements to the Library


<a id="org25f72e0"></a>

### `BasicRunner` now can print the command line that is actually used

This should help with diagnosing problems with MPI etc.

Can be switched on in some utilities with `--echo-command-prefix`


<a id="orgb4a7043"></a>

### `ClusterJob` now can live without a machinefile

Using the machine-file now can be switched off for job-schedulers
with a tight integration


<a id="org5068755"></a>

### Enhanced treatment of symlinks during cloning

If a item in the case itself is a symlink then it used to be a
copy of the file the symlink is pointing to. Now it is created as
a symlink to the target the original symlink. If the
`--follow-symlink`-option is used the old behaviour is used
(copying). In this case the option `noForceSymlink` in the
`Cloning`-section of the configuration can be used to change this
behaviour for selected files


<a id="org040a19a"></a>

### `AnalyzedCommon` clears the `analyzed`-directory

The directory is cleared if it exits from a previous run.


<a id="org8daa4d8"></a>

### `TimelineDirectory` is more tolerant

Used to fail if incompatible data types were used. Now ignores
them


<a id="org7c707fc"></a>

### Possibility of a subcommand-interface for utilities

The subclass `SubclassFoamOptionParser` now allows the parsing of
subclasses. The base class for utilities `PyFoamApplication` now
supports this as an option. As an example this is implemented in
`pyFoamSTLUtilities.py`


<a id="orgdaf026a"></a>

### `STLUtility` accepts file-handles

The class checks whether arguments are filehandles and in this
case doesn't try to open a file for reading or writing but uses
the handle


<a id="org2fed06f"></a>

### `addClone` in `SolutionDirectory` accepts glob patterns

If no file matching the name is found it is assumed that this is a
glob-pattern and all matching files are added. This affects all
utilities that use that method (especially `pyFoamCloneCase.py`)


<a id="org704211e"></a>

### `execute` in `Utilities` allows specification of working directory and echoing of output

This method now allows the specification of a working
directory. Before executing the command the method changes to the
working directory. Afterwards it changes back to the regular
working directory.

There is also an option `echo` that immediately prints the output
to the screen


<a id="org754309f"></a>

### `rmtree` and `copytree` more tolerant

`rmtree` now also works if the "tree" is a file.

`copytree` now has a parameter `force` that allows removing the
destination directory if it exists


<a id="org948e00f"></a>

### Enhanced support for booleans in the parser

Strings that are usually interpreted as boolean in OF-dictionaries
(for instance `on`, `yes`, &#x2026;) are now stored as a special type
that allows treating them like 'real' booleans.

For instance an expression `test no;` in a dictionary now allows
things like `if d['test']:` in the script


<a id="org3bbd08c"></a>

### Application classes now allow specifying options as keyword parameters

Until now the options to be used had to be specified as a list of
string modeled on the way the command line looked like. This is
still possible. In addition it is now possible to specify these
things as keyword parameters on the command line. Rudimentary type
checking is done. The names of the parameters are generated from
the command line options: the `-` are removed and the words are
converted to CamelCase. So for instance `--list-custom-Regexp =
    becomes =listCustomRegexp`. Also for switches like these a boolean
value has to be passed. So the correct usage in a call would be
`listCustomRegexp=True`.


<a id="orgb982259"></a>

### `SolutionDirector` now can classify directories in the `postProcessing`-directory

A number of properties has been added that list data generated by
function objects:

-   **timelines:** timeline data (like `propes`) that can be
    visualized by `pyFoamTimelinePlot.py`
-   **samples:** data from `set` (assuming it is in `raw`-format) that
    can be processed by `pyFoamSamplePlot.py`
-   **surfaces:** data from `surface` (assumes `VTK`-format) that can
    be used by `pyFoamSurfacePlot.py`
-   **distributions:** special cases of `sample` with distribution
    data

These properties only list the subdirectories of the case with
that data

Additional properties are

-   **pickledData:** a list of pickled data files that are found
-   **pickledPlots:** list of found pickled plots

These lists are sorted in descending temporal order (newest first)


<a id="org2e3d373"></a>

### `pyFoamSamplePlot.py` now more flexible for distributions

Tries to determine the names of the values from the first line in
the files


<a id="orge7f8a5c"></a>

### `DictProxy` now has a `dict`-like `update`-method

This also allows enforcing string values


<a id="org550293a"></a>

### `FoamFileGenerator` automatically quotes strings

If strings are unquoted but contain characters that make it
illegal as a word then the string is quoted before output


<a id="orgd2e184c"></a>

### Children of `FileBasis` now can be used with the `with`-statement

This mainly concerns `ParsedParameterFile`


<a id="org47681e4"></a>

# Version 0.6.2 - 2013-11-03


<a id="org0da9ff9"></a>

## Major changes


<a id="orgb7c0f5d"></a>

### Use of `pandas`-library

Starting with this version the `pandas`-library is used for
data-analysis. When possible and appropriate classes return
`pandas`-objects. Currently these are:

-   `CSVCollection`. With a call-operator this class returns the
    collected data as a `DataFrame` of the collected data
-   `SpreadsheetData` now has methods to return `Series` and
    `DataFrame` objects

It is not necessary to install `pandas` if these classes are not
used (and even then most of their functionality works)


<a id="org3d63a95"></a>

## Incompatibilities


<a id="orgad13a0b"></a>

### Different separator for databases in CSV-files

The class `RunDatabase` (and therefor also the utility
`pyFoamDumpRunDatabaseToCSV.py`) now write as a separator for data
from sub-tables a `//` instead of the space. This especially means
that scripts that rely on a data-item `foo` in `analyzed` might
break because this is now called `analyzed//foo` instead of
`analyzed foo`. On the other hand this makes the names more
consistent and easier to parse as `//` is the saperator for other
levels of dictionaries


<a id="orgd27a16f"></a>

### Change of independent variable name in sample data

Instead of `col0` this is now `coord`. This could cause problems
with scripts that use that column name in the resulting
`SpreadsheetData`-object


<a id="orgf8a3cd1"></a>

## Bugfixes


<a id="org5be4202"></a>

### `pyFoamPackCase.py` does not handle symbolic links correctly

Symbolic links were copied as is and did not work correctly
afterwards. This is fixed. If the symbolic link is an absolute
path or points outside the case directory it is replaced with the
file it points to. Otherwise it is preserved as a symbolic link


<a id="org1689779"></a>

### `pyFoamPotentialRunner.py` not working with OpenFOAM 2.0 or newer

These versions require an entry `potentialFlow` in the
`fvSolution`-file instead of the old `SIMPLE`


<a id="orga9a7d27"></a>

### `pyFoamListCase.py` fails with `controlDict` that use preprocessing

Fixed by first trying to read that with preprocessing. Without if
that fails


<a id="orga5051a7"></a>

### Cloning fails in symlink-mode if files are specified twice

Now using a `set` instead of a `list` makes sure that no file is
cloned twice


<a id="org86a0a2f"></a>

## Utilities


<a id="orgf506478"></a>

### `pyFoamPotentialRunner.py` now allows removing of `functions` and `libs`

The utility now allows removing these entries in case that they
don't work with `potentialFoam`


<a id="orgc09249d"></a>

### The Runner-utilities now have more options for clearing

Some of the options of `pyFoamClearCase.py` for clearing cases
(for instance specifying additional files) have been ported to the
`Runner`-utilities. Also is the `postProcessing`-directory
removed by default


<a id="orga3a01ed"></a>

## Library


<a id="org67ba29c"></a>

### `SolutionDirectory` and `TimeDirectory` are more tolerant

If there are field files and their zipped counterpart than
instead of an error a warning **can** be given


<a id="orgb4b3041"></a>

### `ClusterJob` now handles template files

A new method `templateFile` gets the name of a file which is
constructed from a template of the same name plus the extension
`.template`


<a id="org40b6596"></a>

### Additional parameters in `ClusterJob`

The method `additionalParameters` can return a dictionary with
additional parameters


<a id="org2426708"></a>

### Custom data in directory easier accessible

In the written data in the sub-dictionary `analyzed` there is now
a subdictionary `Custom` with the values of the custom expressions
with the prefix `CustomXX_` removed. This means that values that
were available as

    data['Custom02_velCheck']['min']

are now available as

    data['Custom']['velCheck']['min']

The advantage is that the number part which was dependent on the
order the expressions were specified is now no longer necessary
(this should make scripts more stable)

The old notation is still available but deprecated


<a id="org854459d"></a>

### `SolverJob` now allows compression of output

The parameter `solverLogCompress` compresses the log-file while
writing it to disc. **Attention:** This may lead to corrupted
log-files if the run crashes


<a id="org6c4878e"></a>

### `PyFoamApplication`-class now allows quick access to data

The dictionary returned by `getData()` now allows access to all
the elements as attributes.


<a id="org662f88e"></a>

## New features/Utilities


<a id="org1aaae5d"></a>

### Post-run hook that sends mail at the end of run

The hook-module `MailToAddress` sends a mail at the end of a
run. Prerequisite is an SMTP-Server that doesn't need
authentication


<a id="org72cb81e"></a>

### New utility `pyFoamCompressCases.py`

This utility goes through cases and compresses single files. The
cases can be searched recursively to.

Purpose of this utility is to shrink cases where
`writeCompression` was not turned on during the run


<a id="org815bdf3"></a>

### Paraview-module to read additional data

A new module `PyFoam.Paraview.Data` reads additional data usually
written by OpenFOAM. These are converted to `vtkArray` using the
following functions and can be used in `Programmable filters`:

-   **setSampleData:** reads the data from sampled sets
-   **setTimelineData:** reads data from a timeline directory
-   **setPlotData:** reads pickled plot data using `RedoPlot`


<a id="org2abe3ac"></a>

## Enhancements


<a id="orgd99f4a9"></a>

### `pyFoamRedoPlot.py` can plot in XKCD-mode

When used with the option `--implementation=xkcd` and version of
`matplotlib` that supports it is installed then plots are done in
the style of the webcomics <http://xkcd.com>


<a id="orgf15c6e1"></a>

### `pyFoamListCases.py` now displays disk usage in human readable form

If the disk usage of the cases is calculated then it is displayed
in human readable form (as KB, MB, GB or TB) for sizes larger than
one Kilobyte


<a id="org771360c"></a>

### `pyFoamClearCase.py` more flexible in selection of data to be removed

Options to be more flexible in removing data are added:

-   **keep-interval:** keep timesteps at a specified interval. For
    instance `--keep-interval=0.1` will keep times
    like \(1\), \(1.1\) etc but remove \(1.05\)
-   **keep-parallel:** this will not remove any times in the
    `processor`-directories. Also are things like
    `keep-last` now honored for processor directories
-   **remove-analyzed:** Remove the directories with the analyzed data
    too. Old behavior was to remove them. Now they are kept by default


<a id="orgd0a0e62"></a>

### `pyFoamFromTemplate.py` automatically chooses template and default values

If an output file `foo` is specified and no template then the
utility looks for a file `foo.template` as a template.

If a file `foo.defaults` is present then this file is read and
used as default parameter values. Other specifications override
these defaults


<a id="orga239dc6"></a>

### `pyFoamDumpRunDatabaseToCSV.py` can disable standard-fields

Additional option `--disable-run-data`


<a id="org9dca4e4"></a>

### `pyFoamDumpRunDatabaseToCSV.py` prints `pandas`-object

With the `-pandas-print`-option a `DataFrame` is generated and
printed


<a id="org0a276bf"></a>

### Better debugging with `ipdb`

If the `ipdb`-package (basically `pdb` with `IPython`-additions)
is installed then it is used. This gives additions like
tab-completion


<a id="org896ecb8"></a>

### Interactive shell after execution for utilities

The option `--interactive-after-execution` drops the user to an
interactive shell where the namespace can be inspected. If present
`IPython` will be used, otherwise the regular shell is used


<a id="org0a0d8c1"></a>

### Utilities that read quantitative data convert to `pandas`-data and/or `numpy`

This is mainly to be used on the interactive shell to do further
analysis or write this data out. The utilities are:

-   **pyDumpRunDatabaseToCSV.py:** add an item `dump` with the whole
    data as a `DataFrame`
-   **pyFoamTimelinePlot.py:** add element `series` with all the data
    as `Series` and `dataFrame` with the same data as a `DataFrame`
-   **pyFoamSamplePlot.py:** Like `pyFoamTimelinePlot.py`
-   **pyFoamRedoPlot.py:** Now can get series and the whole plot data
    as pandas-objects


<a id="orgc9afb9e"></a>

### Utilities that read quantitative data write Excel files

The utilities `pyDumpRunDatabaseToCSV.py`,
`pyFoamTimelinePlot.py`, `pyFoamSamplePlot.py` and
`pyFoamRedoPlot.py` now have options to write Excel-files


<a id="org217700b"></a>

### Specify additional settings for `GnuPlot` in `customRegexp`

If an item in `customRegexp` has an item `gnuplotCommands` then
it is assumed that this is a list of strings which are executed
before the first plotting. For instance

    gnuplotCommands (
       "set format y '%.2e'"
     );

changes the number format on the y-axis


<a id="org4badce1"></a>

### More flexible data specification for `pyFoamSamplePlot.py`

Instead of determining the names of the fields and lines form the
filenames it is now also possible to specify them through options.

The option `--is-distribution` is a shorthand that sets these
options for distribution files


<a id="orgdd48a3e"></a>

### `pyFoamSamplePlot.py` now allows specification of x-range

The range of the x-axis of the plots can either be set by
automatically scaling to the domains of all the data sets with
`--scale-domain` or by specifying them with `--domain-minimum` or
`--domain-maximum`.

These domains are set for **all** plots


<a id="orga41e16c"></a>

# Version 0.6.1 - 2013-05-24


<a id="org3fa3bfd"></a>

## Major changes


<a id="org490fe11"></a>

## Bugfixes


<a id="orgab82433"></a>

### Restoring of `controlDict` after `write`

When activating an on-demand write the `constrolDict` was not
restored because the output-line about the file being read was not
recognized (due to a change in the output in recent
OF-versions). Now a number of different formats is recognized


<a id="org0784c9d"></a>

### Custom-plot type `slave` not working if no `master` defined

That plot-type needs a `master`. Fixed to fail if none is defined


<a id="org5d9d14b"></a>

### `-list-only` did not correctly parse lists with a numeric prefix

This did affect all utilities that use that option and also calls
with `listOnly` to the library class


<a id="orgd03557b"></a>

## Utilities


<a id="org06f52fc"></a>

### `pyFoamBuildHelper.py` now allow more than one action

If multiple actions like `--update` and `--build` are specified
they are executed in a sensible order (update before build etc)


<a id="orgc45da84"></a>

### Utilities warn if OpenFOAM-version is unset

If the environment variable that determines the OpenFOAM-version
is unset a warning is issued by the utilities


<a id="org85625e1"></a>

### `pyFoamUpgradeDictionariesTo20.py` allows single files

If  single file is specified then the action to transform it has
can be specified


<a id="org2d30227"></a>

### `pyFoamUpgradeDictionariesTo20.py` transforms reaction-schemes

Now knows how to transform "old" reaction files (where the
`reactions`-entry was a list) to the new format (where it is a
dictionary). Only a limited number of reaction types is supported.


<a id="orgd3c4558"></a>

### `pyFoamUpgradeDictionariesTo20.py` transforms thermophysical data

Now the old form of thermophysical data (lists) is transformed
into the new dictionary-form


<a id="org4cddfe8"></a>

### `pyFoamCloneCase` now allows creating directory that symlinks to the original

Now with the option `--symlink-mode` instead of copying the
directories from the original new directories art created and
populated with symlinks to the files in the original. The depth
until which no symlinks to directories are created can be
specified. This allows the clone to share the configuration files
with the original


<a id="org1d7b676"></a>

### `pyFoamClearCase.py` now removes `postProcessing` and allows removal of additional files

The directory `postProcessing` is now automatically removed (can be
switched off with `--keep-postprocessing`). Also with the
`--additional`-option patterns with additional files to remove
can be specified.


<a id="orge35c691"></a>

### Improvements to `pyFoamVersion.py`

-   Now reports the location of the `python`-executable
-   Reports locations of used libraries


<a id="org17ad99d"></a>

### Additional files automatically cloned

The files `Allrun`, `Allclean` and `0.org` are automatically
added during cloning as these are often used by the standard-utilities


<a id="org53f1f07"></a>

### `pyFoamDisplayBlockMesh.py` uses the same options for template format as `pyFoamFromTemplate.py`

This makes sure that templates are handled consistently and also
allows different delimiters in the `blockMeshDict.template`


<a id="orga97ea30"></a>

## Library


<a id="org7ce956b"></a>

### Improvements in syntax of `ParsedParameterFile`

-   Now the new relative scoping that was introduced in OF 2.2 is
    supported


<a id="org2acdff1"></a>

### `Utilities`-class now function to find files matching a pattern

Added a function `find` that approxiamtes the `find`-command


<a id="orgfe7c1e1"></a>

### VCS ignores more files

Some more patterns have been added that will be ignored in a
VSC-controlled case. All of them concerning files that PyFoam
creates during operation


<a id="orgeeecaa3"></a>

## New features/Utilities


<a id="org33cc91a"></a>

### New Utility `pyFoamSymlinkToFile.py`

This utility replaces a symlink with a copy of the
file/directories it points to. To be used after a
`pyFoamCloneCase.py` in `--symlink-mode`


<a id="orge4489b2"></a>

# Version 0.6.0 - 2013-03-14


<a id="org4dee8d3"></a>

## Major changes


<a id="org337c89e"></a>

### Adaption to work with Python3

Sources are adapted so that `PyFoam` works with Python3 too. This
breaks support for Python 2.4 and earlier (possibly also Python
2.5)

Some of the Libraries in `PyFoam.ThirdParty` had to be adapted to
work with Python3:

-   **Gnuplot.py:** The original version 1.8 is quite old. It was
    adapted with the help of the `six`-library (see
    below) to work with Python2 and Python3 (inspired
    by
    [<https://github.com/oblalex/gnuplot.py-py3k/commits/master>]
    which is a pure port to Python3 without backwards
    compatibility)


<a id="org63f6fe5"></a>

### New ThirdParty-Libraries

-   **six:** Library that helps supporting Python 2 and Python 3 in
    the same source code. Currently version 1.2 from
    [<https://bitbucket.org/gutworth/six>] is used
-   **pyratemp:** Templating library to support the new templating
    format. Version 0.2.0 from
    [<http://www.simple-is-better.org/template/pyratemp.html>]
    is used


<a id="org95468f8"></a>

### Porting to `Windows`

Port to allow running PyFoam on Windows was done by Bruno Santos
of blueCAPE (bruno.santos@bluecape.com.pt)

Patch was originally posted at
<http://sourceforge.net/apps/mantisbt/openfoam-extend/view.php?id=166>

**Note**: many of PyFoam's features are not yet fully functional on
Windows.


<a id="org6876252"></a>

### Experimental port to `pypy`

Sources are executed in `pypy` but it seems there are problems
with `numpy` and also with code like `for l in open(f).readlines()`


<a id="org194d82f"></a>

## Third-Party


<a id="org77d31ae"></a>

### Upgraded `ply` to 3.4

This brings virtually no changes. `README` with copyright
information has been added


<a id="org90f2281"></a>

## Infrastructure


<a id="orgf445a68"></a>

### Parameters can't be modified in `CTestRun` after initialization

This should help to avoid side-effects


<a id="orgcf15253"></a>

### Treat timeouts in the `MetaServer` right

Due to a previous workaround timeouts when collecting information
about new machines was not treated correctly


<a id="org5525e90"></a>

### Add `execute`-method to `ClusterJob`

This allows the execution of a shell-script in the directory of
the case


<a id="orga7ad368"></a>

### Add possibility to run specific modules before or after the solver

These modules are found in `PyFoam.Infrastructure.RunHooks`. Two
concrete implementations:

-   **`PrintMessageHook`:** to print a text to the terminal
-   **`SendToWebservice`:** encode an URL and send it to a webservice
    (example for `pushover.net` added)

Hooks are automatically instantiated from the configuration data
(examples are hardcoded))


<a id="org2716d1a"></a>

### Parameters added to the info about the run

The Runner-classes now have a parameter `parameters`. This data
(usually it would be a dictionary) is added verbatim to the run
info.

Most runner applications now have the possibility to add this
info.

Purpose of this facility is to identify different runs in the
database better.


<a id="orgde696ef"></a>

### Parameter handling in `ClusterJob` extended

Parameter values are now handed to the actual job. Also a
dictionary with parameters can be handed to the constructor and
will be used in the relevant callbacks


<a id="orgf3a3305"></a>

### Run data written alongside `PickledPlots`

During the run whenever the `PickledPlots`-file is written a file
`pickledUnfinishedData` gets written. This has the current solver
data and is similar to `pickledData`.

Also a file `pickledStartData` gets written that has the data that
is available at the start of the run.


<a id="org399a0c6"></a>

### `BasicRunner` collects error and warning texts

The runner collects

-   at every warning the next 20 lines of the output until a total
    of 500 lines is reached (this avoids filling disk and memory if
    the solver produces too many warnings)
-   All output from an error message until the end

And stores them in the application data


<a id="org53931dd"></a>

## Library


<a id="org60df394"></a>

### `TemplateFile` now uses `pyratemp`

The class `TempalteFile` now uses an enhanced templating
engine. The  old implementation is in the class
`TemplateFileOldFormat`


<a id="orge71d3e2"></a>

### Clearer error message in Application-classes

If used as classes (not as utilities) these classes print the
class name instead of the calling utilities name


<a id="org19d12a5"></a>

### Output is only colored if it goes to the terminal

Error and warning messages don't decorate the output if it goes to
files or other non-terminal streams


<a id="org0669553"></a>

### `error`-method of application classes now raises an exception

An exception is now raised by `self.error()`. This makes it easier
to handle such errors if the application class is used. The
exception is passed up until there is a "real" application


<a id="org366d5be"></a>

### `ParsedParameterFile` now knows how to handle binary files

When the format of a file is `binary` lists with a length prefix
are being read as binary blobs.

For reading the blobs a simple heuristics is used: a multiple of
the length in bytes is read. If the next character is a `)` and
the characters after that are a certain combination of characters
(newlines and `;`) then it is assumed that the blob has
ended. This may fail on certain occasions:

-   if the combination of characters appears at these places
-   if the objects inside the binary data are of different sizes

It would be hard to work around these restrictions without
reprogramming the full functionality of OpenFOAM


<a id="orga9bd89f"></a>

### `LabledReSTTable` for more flexible table generation

New class in the `RestructuredTextHelper` allows more flexible
generation of tables. Items are added with `column` and `row` and
if these don't exist in the first row/column the table is extended
appropriately


<a id="org0411108"></a>

### Plotting classes now allow setting of `xlabel`

This is implemented for `Gnuplot` and `Matplotlib`. Default for
the label on the x-Axis is now "Time [s]"


<a id="orgf3b7711"></a>

## Utilities


<a id="orgeb9b864"></a>

### `pyFoamFromTemplate.py` with new templating engine

The utility can now use the pyratemp-templating engine which
allows templates with loops, conditions and other  fancy stuff


<a id="orga7c06f8"></a>

### `pyFoamSamplePlot.py` allows using the reference data as basis for comparison

Instead of using the x-values from the original data the y-values
of the reference data can be used for comparing (with the
`--use-reference`-option)

Same for `pyFoamTimelimePlot.py`


<a id="orgf12beb5"></a>

### Scaling and offsets are now used in plots of `pyFoamSamplePlot.py`

If scales not equal to \(1\) and offsets not equal to \(0\) are
specified they are used in the `gnuplot`-output


<a id="org0600484"></a>

### `pyFoamPrintData2DStatistics.py` prints relative average error

With the `--relative-average-error`-option


<a id="org71e938a"></a>

### Enhancements to `pyFoamVersion.py`

-   More tolerant if no library was found
-   Reports the location of the PyFoam-Library
-   Checks whether utility version is consistent the library found


<a id="org331179e"></a>

### `pyFoamRunner.py` allows hooks

Hooks can be added at the start and the end of a run


<a id="orgc7c1720"></a>

### `pyFoamRedoPlots.py` supports range for plots

Added `-end` and `-start`-option to select a range that should be
plotted.

Currently not working with the Matplotlib-implementation (only gnuplot)


<a id="org9b32884"></a>

### `pyFoamDisplayBlockMesh.py` no supports templates

If a file with values is specified then the utility assumes you're
editing a template file and will evaluate it before displaying it


<a id="org711a356"></a>

### `pyFoamCaseReport.py` is tolerant towards binary files

New switch that makes the parser treat files that are declared
`binary` in the header as if they were `ascii`


<a id="org0b8d8f0"></a>

### `pyFoamSamplePlot.py` and `pyFoamTimelinePlot.py` raise error if no plots are generated

This makes it easier to catch faulty specifications (or empty
timeline-files)


<a id="orgd3c6d1e"></a>

### `pyFoamSurfacePlot.py` can wait for a key

An option `--wait` has been added that makes the utility wait
before displaying the next picture


<a id="org5e71adf"></a>

### `pyFoamEchoDictionary.py` is more flexible with binary files

Switch allows forcing it to read a binary File as an ASCII


<a id="org1331150"></a>

### All utilities now have a switch that starts the debugger even with syntax-errors

Previously the option `--interactive-debug` only started the
debugger if the error was **no** syntax error. This is still the
default behavior, but can be overruled


<a id="org8dcba13"></a>

### Utilities now can be killed with `USR1` and will give a traceback

The option `--catch-USR1-signal` now installs a signal-handler
that prints a traceback and finishes the run. If the interactive
debugger is enabled then it goes to the debugger-shell.

Option `--keyboard-interrupt-trace` triggers the same behaviour
for keyboard interrupts with `<Ctrl>-C`


<a id="org00a972e"></a>

### Switch to switch on **all** debug options

For the purpose of developing a switch `--i-am-a-developer` has
been added.


<a id="org5400710"></a>

### Plotting utilities now allow specification of x-Axis label

With the option `xlabel` in the `customRegexp`-file the label on
the x-axis of the plot can be changed. Setting `ylabel` and
`y2label` (for the secondary axis) was already possible


<a id="org1a391ca"></a>

### Metrics and compare for `pyFoamTimelinePlot.py` and `pyFoamSamplePlot.py` support time ranges

Now the options `--min-time` and `--max-time` are supported by
`--metrics` and `--compare`


<a id="orgda13303"></a>

### `pyFoamDisplayBlockMesh.py` allows graphical selection of blocks and patches

New addition by Marc Immer allows the graphical selection of
blocks and patches and adds them to the `blockMeshDict`


<a id="org24b279b"></a>

### `pyFoamCloneCase.py` and `pyFoamPackCase.py` accept additional parameters

The file `LocalConfigPyFoam` is read by these utilities and if
there is a parameter `addItem` in the section `Cloning` defined
then these files are cloned/packed automatically (no user
specification required)


<a id="org267feda"></a>

### `pyFoamListCases.py` now calculates estimated end-times

Additional option to print the estimated end times. These can be
wrong if the case did not start from the `startTime` in the
`controlDict`.

Also now allows printing the end and the start-time according to
the `controlDict`


<a id="org1878022"></a>

## New features


<a id="org95ca548"></a>

### Different "phases" for multi-region solvers

Plots of type `phase` in `customRegexp` don't actually plot
anything. The set a phase-name that is used for subsequent values
(for instance to distinguish the different residuals)


<a id="org2c35065"></a>

### `pyFoamChangeBoundaryType.py` allows selection of region and time

Options `--region` and `--time-directory` added that allow
selecting different `boundary`-files


<a id="org9f2b8a5"></a>

### New class for storing case data in a sqlite-database and associated utilities

The class `RunDatabase` stores the data from runs. Utility
`pyFoamAddCaseDataToDatabase.py` is one way to populate the
database. `pyFoamDumpRunDatabaseToCSV.py` allows dumping that
data to a file for further processing (in a spreadsheet for
instance)

Database can also be populated using a special post-run hook


<a id="org5bdf7ea"></a>

## Bugfixes


<a id="orgffd236d"></a>

### Only binary packages of 1.x were found

Pattern had to start with 1 (now every digit is possible))


<a id="org9c38a73"></a>

### Option group *Regular expressions* was listed twice

No harm done. But fixed


<a id="orga4a2fcc"></a>

### `--clear`-option for `pyFoamDecompose.py` not working

Reason was that `rmtree` does not allow wildcards. Fixed


<a id="org6a2fdf4"></a>

### `pyFoamDisplayBlockmesh.py` not working with variable substitution

The `DictRedirect` would not convert to float. Fixed. Although it
might happen again for other data types


<a id="orgba3b908"></a>

### Option `--function-object-data` of `pyFoamClearCase.py` not working with directories

The option was only implemented for the list-form of the
`functions` entry in `controlDict`

Now fixed to also work with the dictionary-form


<a id="orgaca12e4"></a>

### `nonuniform` of length 0 not correctly printed

Seems like the length was interpreted as the name of the
list. Fixed


<a id="org81c06f7"></a>

### Building of pseudocases with `pyFoamRunner.py` broken

Only worked if no region was specified (= not at all). Fixed


<a id="orgc35a6d1"></a>

### `pyFoamRedoPlot.py` did not correctly honor `--end` and `--start`

Plots were over the whole data range. This is now fix (also the
issue that `--end` alone did not work)


<a id="org099790c"></a>

### `WriteParameterFile` does not preserve the order of additions

Contents was "only" set as a dictionary which does not preserve
the order in which entries are added. Replaced with a `DictProxy`


<a id="orgf267061"></a>

### Wrong number of arguments when using `TimelinePlot` in `positions`-mode

Problem that was introduced by changes in the `fields`-mode


<a id="orgd40a214"></a>

### `ClusterJob` uses only `metis` for decomposition

For OpenFOAM-versions 1.6 and higher the automatic decomposition
used is now `scotch`


<a id="orga9f9b04"></a>

### `pyFoamSamplePlot.py` and `pyFoamTimelinePlot.py` produced no pictures for regions

As regions have their own subdirectories the `/` from the
directory name was inserted into the filename and if the
subdirectory did not exist `gnuplot` did not create the picture


<a id="org2d32b20"></a>

### Barplots in `pyFoamTimelinePlot.py` not working if value is a vector

The base class didn't correctly handle the `(` and `)`. Fixed


<a id="orga2d7c00"></a>

### Mysterious deadlocks while plotting long logfiles

The problem was that during splitting the timeline data an exception was
raised. This exception was caught by another part of PyFoam. This
left a lock on the data structure locked and the next access to
the structure was held indefinitely. Fixed


<a id="org716c979"></a>

### Scanning linear expressions form the block coupled solver failed

As there is a tuple of residuals the scanner did not analyze the
output of the output of the block-coupled solver from `1.6-ext`
correctly. This is now treated as a special case and each residual
is plotted separately (distinguished by a `[x]` with `x` being the
number of the component)


<a id="org005209b"></a>

### `#include` not correctly working with macros in the included file

Macros `$var` were not correctly expanded. Fixed


<a id="orgc1f90d6"></a>

### Macros not correctly expanded to strings

When being expanded to string form macros were not correctly
expanded


<a id="org2c537b8"></a>

### `pyFoamPackCase.py` in the working directory produces 'invisible' tar

If the utility was used in the form

    pyFoamPackCase.py .

then an 'invisible' tar `..tgz` was produced. Fixed


<a id="org1956e3f"></a>

### String at the end of a linear solver output makes parsing fail

Reported in
[<http://www.cfd-online.com/Forums/openfoam-solving/112278-pyfoam-struggles-adopted-solver-post403990.html>]
the string is assumed to be part of the iteration number. Fixed


<a id="org959755c"></a>

### Paraview utilities not working with higher Paraview versions

At least for PV 3.14 and 3.98 the way the version number is
determined has changed and the PV-utilities failed. This has been
fixed but is untested with old versions


<a id="orga899b7f"></a>

### Camera settings not honored with `pyFoamPVSnapshot.py`

For the first rendered view Paraview automatically resets the
camera. This has now been switched off (so the snapshot is
rendered correctly)


<a id="orgfa30d27"></a>

# Version 0.5.7 - 2012-04-13


<a id="orgc539561"></a>

## Parser improvements

-   Problem with nested comments
-   Parse code streams
-   Preserving of comments can be switched off
-   Ignore extra semicolons
-   Allows parsing lists of length 3 and 9 as lists and not as
    vectors and tensors
-   "lookup redirection" in OF-dictionaries now works


<a id="orga9d4c12"></a>

## Utility improvements

-   pyFoamSamplePlot.py stops if the same directory is compared
-   pyFoamSamplePlot.py shows the location of the biggest difference
-   pyFoamSamplePlot.py allows only same ranges for comparisons
-   Generation of pickled-files can be switched of for runner-utilities
-   Frequency with which the pickled file is written is adapted (so
    that it doesn't use ALL the CPU-time)
-   pyFoamVersion.py improved (Version of Python is checked etc)
-   pyFoamRedoPlot.py: fixed parameter checking
-   pyFoamPotentialRunner.py: temporarily disable libs and functions
-   Only write last N loglines from Runner-utility
-   pyFoamClearCase.py: allow local specification of additional files
    that should be cleared
-   Runner utilities can report data about the run
-   pyFoamConvertToCSV.py now allows selection of columns
-   Utilities for quantative analysis now can return data
-   Utilities for quantative now correctly return data for multiple places
-   pyFoamSamplePlot.py now allows specification of valid variable pre and
    postfixes to allow correct parsing of variable names with a \_
-   endTime can be specified by the runner-utilities
-   Utilities now allow piping (using pickled data)
-   pyFoamSamplePlot.py now allows the specification of a reference time
-   Nomenclature of pyFoamSamplePlot.py and pyFoamTimelinePlots.py
    now similar (both call it fields)
-   pyFoamDecompose.py now can use the -region-option ifthe
    OF-version is right
-   Forcing debug-mode fixed for older OF-versions
-   pyFoamDecomposer.py now accepts globalFaceZones in Python or
    OpenFOAM-syntax
-   Plot-utilities now don't interpret \_ in names not as LaTeX


<a id="org35fbea6"></a>

## New Utilities

-   pyFoamEchoPickledApplicationData to output pickled data
-   pyFoamPrintData2DStatistics.py to output data from comparisons
-   pyFoamBuildHelper.py to build project and its prerequisites (work
    in progress)
-   pyFoamCreateModuleFile.py to create files for
    <http://modules.sourceforge.net/> (by Martin Beaudoin)
-   pyFoamSTLUtility.py to join STL-files


<a id="org10b8650"></a>

## Library improvements

-   stabler comparisons
-   Paraview-Utilities work with 1.x and 2.x
-   Runner classes return a dictionary with data
-   TimelineDirectory ignores dot-files
-   Application-objects can now be used like dictionaries to access
    data
-   New class TableData for simple data tables
-   New class Data2DStatistics for statistics about tables
-   new class CTestRun as basis for automated testing
-   FoamOptionParser now resets environment variables so that
    application-classes can call other application classes
-   Improvements to HgInterface
-   Additional VCS-subclasses for git, svn and svk (implementation
    only as needed)
-   SolutionDir now uses 0.org as initial directory if no valid
    initial directory is present (this affects clearing and cloning)
-   FoamFileGenerator now more flexible for long lists
-   ParsedBlockMeshDict now doesn't introduce prefixes for 'long' lists


<a id="org6772fc3"></a>

## Removed utilities

-   pyFoamAPoMaFoX.py
-   pyFoamPlotResiduals.py


<a id="orgba388d5"></a>

## Thirdparty

-   Got rid of Numeric-support in Gnuplot-library


<a id="org9f63d55"></a>

## Other

-   script to generate man-pages for the utilities
-   Paraview3-example probeDisplay.py now renamed to
    probeAndSetDisplay.py and reads sampledSets from controlDict and
    sampleDict


<a id="orgdcf54b9"></a>

# Older Versions

The changes for older versions can be found on
[the Wiki-page](http://openfoamwiki.net/index.php/Contrib_PyFoam#History)
