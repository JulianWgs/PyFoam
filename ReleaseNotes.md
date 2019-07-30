# Table of Contents

1.  [Version 0.6.11 - Not yet released](#orga45ca8d)
    1.  [Major changes](#org5dcdb7c)
    2.  [Incompatibilities](#org85a22f3)
        1.  [Behaviour reading `customRegexp`](#org947dfa7)
        2.  [Gnuplot does not use `FIFO` as the default anymore](#orgaaa6c9f)
    3.  [New feature/utilities](#orge3fb473)
    4.  [Enhancements to Utilities](#org71f9fe7)
        1.  [Replay data-files in `customRegexp`](#orgadcfdbe)
        2.  [Macro expansion in `customRegexp`](#org3404693)
        3.  [`progress` entry in `customRegexp` now allows `format` strings](#org670e9ba)
        4.  [`pyFoamRedoPlot.py` allows passing terminal options](#org4cb8408)
        5.  [`pyFoamPlotWatcher.py` stops scanning the file is `--end` was specified](#orga41ac2f)
        6.  [Hardcopies of custom plots have more descriptive names](#orgb1ebf8e)
        7.  [Plotting in Gnuplot can switch between using FIFO or regular files](#org1de8eda)
        8.  [`pyFoamPrepareCase.py` calls script after copying initial conditions](#orgaa133a1)
        9.  [`--stop-after-template` and `--keep-zero` improve control in `pyFoamPrepareCaseParameters.py`](#orge33ffe2)
        10. [`pyFoamPVSnapshot.py` allows specification of the image quality](#orgc625c60)
        11. [Image size specification for `pyFoamPVSnapshot.py`](#orgeb6ff15)
        12. [Setting separation of views and background transparency in `pyFoamPVSnapshot.py`](#org11d72f7)
        13. [`pyFoamPVLoadState.py` automatically uses decomposed or reconstructed data](#orga46be89)
        14. [Change directory for `pyFoamPrepareCase.py` to target](#org4930732)
        15. [`pyFoamPrepareCase.py` can create an example case](#org04ec85c)
        16. [`pyFoamPrepareCase` prints derived values](#org52696c9)
        17. [`pyFoamPVSnapshot` allows specifying different colors for different views](#org251069e)
        18. [`alternateLogscale` for custom plots](#org349ca70)
        19. [`pyFoamBinarySize.py` now calculates documentation size as well](#org2a8a918)
    5.  [Enhancements to the Library](#org1173124)
        1.  [`progress`-data is automatically converted to `float`](#org276182e)
    6.  [Bug fixes](#org53c86ab)
        1.  [With dynamic plots names with `_slave` are problematic](#orge80151f)
        2.  [New-style dimensioned scalars fail](#org49774d8)
        3.  [`pyFoamPVSnapshot.py` not working with Paraview 5.6](#orgcac24b0)
        4.  [`customRegexp` farthes away was used](#org7a30c1c)
        5.  [`ParameterFile`-class got confused by commented lines](#org99a5a46)
        6.  [`pyFoamBinarySize.py` did not count files in `build`](#org34ae69b)
    7.  [Infrastructure](#orgf7ce561)
    8.  [ThirdParty](#org2d1d97b)
2.  [Version 0.6.10 - 2018-08-12](#org50d1fa7)
    1.  [Incompatibilities](#orgce47b79)
        1.  [`pyFoamPrepareCase.py` does not execute decomposition scripts for single processor cases](#org03e7525)
    2.  [New feature/utilities](#orgffa713b)
        1.  [Utility `pyFoamFunkyDoCalc.py` to compare data from `funkyDoCalc`](#org786baa3)
    3.  [Enhancements to Utilities](#org849e7e3)
        1.  [Recursive searching for `pyFoamListCases.py`](#org3308338)
        2.  [Look for `customRegexp` in parent directories](#orgca9a5dd)
        3.  [`pyFoamPrepareCase.py` does not execute decomposition scripts for single processor cases](#org6752191)
        4.  [`pyFoamPrepareCase.py` checks for proper decomposition](#org421ac20)
        5.  [`pyFoamPlotWatcher.py` automatically uses newest logfile](#org951038a)
    4.  [Enhancements to the Library](#org8f9ea32)
        1.  [`FoamFileGenerator` handles `OrderedDict`](#org2d8134f)
        2.  [`#sinclude` handled as an alias to `#includeIfPresent`](#org7ed1e97)
        3.  [OpenFOAM 6 correctly recognized](#org64f2d21)
    5.  [Bug fixes](#orgc59a74a)
        1.  [`pyFoamPrepareCase.py` did not remove `processor`-directories](#orgc9bd235)
    6.  [Infrastructure](#org5bc25c7)
        1.  [Single digit version numbers supported](#orga0e5fdf)
3.  [Version 0.6.9 - 2018-02-25](#org55981fa)
    1.  [Major changes](#org0a97015)
        1.  [Add `curses`-output to Utilities](#org113c2a5)
    2.  [Incompatibilities](#orgc8acde3)
        1.  [`pyFoamPrepareCase.py` creates `.foam`-file](#org1ba00ee)
        2.  [Hardcoded Foam-Version upgraded to `4.0`](#orgd6917b3)
        3.  [`none` no longer parsed as an equivalent for `false`](#org0eab5a1)
    3.  [New features/utilities](#org732a1d7)
        1.  [`pyFoamJoinTimelines.py` to join Timelines from restarts](#orge30c63e)
        2.  [`pyFoamRestartRunner.py` to automatically restart runs](#org00b6bcb)
    4.  [Enhancements to Utilities](#orga703f7f)
        1.  [Special snapshot utilities to use MESA](#orgc03f213)
        2.  [Automated plotting of film properties](#orgafe2943)
        3.  [`pyFoamClearCase.py` automatically executes an existing `Allclean`](#org648679d)
        4.  [`pyFoamPrepareCase.py` executes tutorial scripts if available](#org51b8eea)
        5.  [Script for clearing in `pyFoamPrepareCase.py`](#orge0fdcaa)
        6.  [`pyFoamPlotWatcher.py` now can handle multiple files](#orgd390cc0)
        7.  [`pyFoamPrepareCase.py` now allows separate decomposition scripts](#org9a59bd7)
        8.  [Runner-utilities now create seperate logfiles on restart](#org1595d94)
        9.  [`pyFoamPVSnapshot.py` improves rewriting of state-files](#org3d73757)
        10. [`pyFoamPackCase.py` adds parallel data](#org7bddb40)
        11. [`--replacement`-option in `pyFoamPVSnapshot.py` supports Foam-format](#org0fcf0d7)
        12. [`pyFoamPVSnapshot.py` improved error messages with problems in replacement](#org490d894)
        13. [`customRegexp` now searched in parent directories](#orgd125964)
    5.  [Enhancements to the Library](#org9e4457c)
        1.  [`Paraview.StateFile` extended](#org2da29d4)
        2.  [`BasicRunner` now checks for regular End](#org3eae458)
    6.  [Bug fixes](#org2bf07fb)
        1.  [`pyFoamPrepareCaser.py` ran out of memory for large script outputs](#org245f119)
        2.  [No Courant number plottet if `WM_PROJECT_VERSION` is unset](#orgba2f106)
        3.  [Rescale does not work for streamlines in `pyFoamPVSnapshot.py`](#org6fb6adc)
        4.  [Server not correctly running on Python 2.7 with `socketserver`](#orgdda6927)
4.  [Version 0.6.8.1 - 2017-08-03](#orge652309)
    1.  [Bug fixes](#orgdb76ad3)
        1.  [Fork not correctly detected for `v1706`](#orgcb83bdb)
5.  [Version 0.6.8 - 2017-07-06](#org8aae348)
    1.  [Major changes](#org8ec411f)
        1.  [`pyFoamNet`-utilities now work without a Meta-Server](#orgcd5cfbd)
    2.  [New features/utilities](#org3975116)
        1.  [Added module `PyFoam.Infrastructure.Authentication`](#orgffeca4a)
    3.  [Enhancements to Utilities](#orge8f51a9)
        1.  [`pyFoamClearCase.py` now has `-dry-run` option](#orgb0f7246)
        2.  [New option `--keep-time` for `pyFoamClearCase.py`](#org4c8db55)
        3.  [`pyFoamNetList.py` no longer needs a meta-server to work](#org63a60c3)
    4.  [Enhancements to the Library](#org4bf7352)
        1.  [Better calculation of used memory in runs](#org6aebde0)
        2.  [Pre and post-hooks are now also searched in `PyFoam.Site`](#orgdf1c369)
        3.  [Adapted to correctly detect `OpenFOAM+ v1706`](#orgc413802)
    5.  [Infrastructure](#org9c571fd)
        1.  [The `Runner`-utilities now register as `ZeroConf`-services](#org9e17472)
    6.  [Bug fixes](#org26853ab)
        1.  [`--keep-interval` in `pyFoamClearCase.py` not working for parallel-cases](#org072dfc4)
6.  [Version 0.6.7 - 2017-06-04](#org01969b2)
    1.  [Requirements](#orgce134c0)
        1.  [Now at least Python 2.6 required](#org40b1902)
    2.  [Incompatibilities](#orgfc55571)
        1.  [Names of files generated by `pyFoamPVSnapshot.py` differ](#org478cb30)
    3.  [New features/utilities](#org24965f0)
        1.  [Utility `pyFoamListProfilingInfo.py` to print profiling data](#org64e952b)
        2.  [Utility `pyFoamBlockMeshConverter.py` to convert a 2D-mesh to 3D](#orgbfefdc1)
    4.  [Enhancements to Utilities](#orgfb4d04e)
        1.  [`customRegexp` now can scan for texts](#orgdab48a6)
        2.  [Lines in `PyFoamHistory` escaped](#org0bbca63)
        3.  [`--values-string` of `pyFoamPrepareCase.py` now accepts OpenFOAM-format](#orga54aa9b)
        4.  [`pyFoamRunner.py` and `pyFoamPlotRunner.py` allow automatic selection of solver](#orgac58bfc)
        5.  [Calculations (data transformations) in `customRegexp`](#org405b6eb)
        6.  [Multi-part `idNr` for `dynamic` in `customRegexp`](#org109fb1c)
        7.  [`pyFoamListCases.py` detects dead runs](#org0dc3b0e)
        8.  [Improved time-handling of `pyFoamPVSnapshot.py`](#orgb35315f)
        9.  [Default plots can be set in configuration](#org45da957)
        10. [`derivedParameters.py`-script called from `pyFoamPrepareCase.py` allows error reporting](#orgf3786c1)
    5.  [Enhancements to the Library](#org3079b4f)
        1.  [Detection of new versions of OpenFOAM-foundation and OpenFOAM+](#orga300113)
        2.  [`SpreadsheetData` now handles string data](#org9aedadb)
        3.  [`TimelineData` tolerates string values](#org7ccf962)
        4.  [`()` operator of `SpreadsheetData` works without name](#orgd08d4db)
        5.  [New function `setCurrentTimeline` in `PyFoam.Paraview.Data` to get data at time](#orgb01ea5b)
        6.  [User-specific temporary directory](#orga8640fb)
        7.  [`Gnuplot`-plots now get better titles](#orgc8cd31a)
        8.  [`ParsedParameterFile` now supports `#includeFunc`](#orgbb40158)
        9.  [New utility function `findFileInDir`](#orgc0e6098)
        10. [`humandReadableDuration` added to `PyFoam.Basics.Utilities`](#orgac7b425)
    6.  [Infrastructure](#orge5a21a8)
        1.  [`pyFoamVersion.py` now reports the versions of the `ThirdParty`-packages](#org8c1ed36)
    7.  [Bug Fixes](#org3395561)
        1.  [Application classes fail in Paraview](#orgf37d2c9)
        2.  [Scripts in `pyFoamPrepareCaseParameters.sh` not working on Mac OS X](#orgc9bd6dc)
        3.  [Processor-directories unsorted in `SolutionDirectory`](#orgd62e23a)
        4.  [Deleting failed if a file did't exist](#org95e2213)
        5.  [Missing files in `RegionCases`](#org1e2dc7a)
        6.  [Wrong `solver` in `pyFoamListCase.py`](#org931673a)
    8.  [ThirdParty](#org31f0233)
        1.  [Updated `tqdm` to version 4.8.4](#org254e576)
        2.  [Updated `PLY` to version 3.9](#org34dc94d)
        3.  [Updated `six` to 1.10.0](#orgac0288b)
7.  [Version 0.6.6 - 2016-07-15](#orgc559817)
    1.  [Incompatibilities](#org4cca3ff)
        1.  [Changes in `IPython`-notebooks 3.0](#org0eb92a6)
    2.  [Enhancements to Utilities](#orgdc9b36b)
        1.  [`pyFoamPrepareCase.py` executes `setFields` if appropriate](#orgd0bda2f)
        2.  [Plotting utilities now automatically add custom plots depending on the solver name](#orgd1de42b)
        3.  [`alternateAxis`-entries now can be regular expressions](#orgc4a6c42)
        4.  [Plotting utilities now allow choice of Gnuplot terminal](#orgc0d0330)
        5.  [Plotting utilities now sort legend by name](#orgc2cd98e)
        6.  [`pyFoamExecute.py` allows calling with debugger](#org5f8efd8)
        7.  [`pyFoamPrepareCase.py` fails if execution of a script fails](#org145020c)
        8.  [`--hardcopy` in plotting library now allows modification of `gnuplot`-terminals](#orgb537c58)
        9.  [`pyFoamPrepareCase.py` writes state information about what it is currently doing](#orgc8daafc)
        10. [`pyFoamBinarySize.py` can handle new location of binaries in OpenFOAM 3.0](#org43065d6)
        11. [`Runner`-utilites now can signal on `blink(1)`-devices](#org2c31b6d)
        12. [`pyFoamExecute.py` can flash a `blink(1)`](#org2761b66)
        13. [`pyFoamDecompose.py` allows using a template file](#orgdea1714)
        14. [`pyFoamTimelinePlot.py` now handles new format of probe files](#org5ae9edf)
        15. [`ReST`-report of `pyFoamPrepareCase.py` now reports derived parameters](#org5e260d2)
        16. [`pyFoamPrepareCase` can now ignore directories](#orgb519f32)
        17. [`pyFoamConvertToCSV.py` allows adding formulas to XLSX-files](#org8c48d63)
        18. [`pyFoamListCases.py` now displays mercurial info](#org0c36b40)
        19. [Progress bar added to utilities with long run-time](#org4706a75)
        20. [Utilities that clear data can now report what is cleared](#orgfbdadaa)
        21. [`pyFoamConvertToCSV.py` now allows manipulating the input](#org30b469f)
    3.  [Enhancements to the Library](#orgd4112e7)
        1.  [Detection of `OpenFOAM-dev`](#orgdcdf5df)
        2.  [Add `OpenFOAM+` as a fork](#org5b817ee)
        3.  [Accept new convention for location of `blockMeshDict`](#orgae5385d)
        4.  [Handling of complex data by `Configuration`](#org33c818e)
        5.  [`Configuration` has method `getArch` for architecture dependent settings](#org6a97783)
        6.  [`execute`-method from `PyFoam.Basics.Utilities` returns status-code](#org510fd36)
        7.  [`BasicRunner` now supports more ways of stopping runs](#orge80db8c)
        8.  [Added `Blink1` class to support `blink(1)` devices](#org6895a0c)
        9.  [`ParsedParameterFiles` now supports `includeEtc`](#org6697771)
        10. [Parses uniform fields correctly](#orgfc5c3dc)
        11. [`toNumpy`-method added to `Unparsed` and `Field`](#org52a804e)
        12. [Added module `PyFoam.RunDictionary.LagrangianPatchData` to read data from patch function object](#org7abe3d3)
        13. [Added module `PyFoam.RunDictionary.LagrangianCloudData` to read cloud data](#org75609f4)
        14. [Method `code` added to =RestructuredTextHelper](#org9e687ae)
        15. [`ParsedParameterFile` now parses new dimension format correctly](#org9c9c045)
        16. [`ParsedParameterFiel` now parses uniform fields correctly](#org4728689)
    4.  [Infrastructure](#org1481866)
        1.  [Change of documentation from `epydoc` to `sphinx`](#orgedf8119)
        2.  [Adaptions to the unittests](#org91202f0)
    5.  [Bug fixes](#orgbd30472)
        1.  [Wrong format of `ExecutionTime` breaks plotting utilities](#orgb81897c)
        2.  [`phases` not working with dynamic plots](#org623aa9f)
        3.  [Phase name added to function object output](#org64f71a4)
        4.  [One region mesh too many in utilities that change the boundary](#org3625bce)
        5.  [`pyFoamClearCase.py` fails on write-protected case](#org66bfeb3)
        6.  [Copying of directories in `pyFoamPrepareCase.py` confused by zipped files](#org270e925)
        7.  [Wrong times for multi-view layouts in `pyFoamPVSnapshots.py`](#orgcbc8c9e)
        8.  [First timestep not plotted (and not stored)](#org4a69423)
        9.  [`DYLD_LIBRARY_PATH` not passed on *Mac OS X 10.11*](#org2c08321)
        10. [Newer versions of `pandas` broke the writing of excel files with `pyFoamConvertToCSV.py`](#org0424de8)
        11. [Capital `E` in exponential notation for floats breaks parser](#org9521803)
        12. [`Runner`-utilities clear processor directories if first time in parallel data differs](#orgf76fa1e)
        13. [Utilities `pvpython` not working when installed through `distutils`](#orgd197c4c)
    6.  [ThirdParty](#org34e907e)
        1.  [Added `tqdm` for progress bars](#orgef61a93)
8.  [Version 0.6.5 - 2015-06-01](#orgdb008d5)
    1.  [Major changes](#org828b500)
        1.  [PyFoam now on *Python Package Index*](#org7776c27)
    2.  [Incompatibilities](#org112878a)
        1.  [`ArchiveDir` in `SolutionDirectory` discouraged](#orga1c0c07)
        2.  [Pickled data files now written as binary](#org919d8c5)
        3.  [The `PlotRunner` and `PlotWatcher` now don't strip spaces](#org1d627a3)
        4.  [Different column names in `pyFoamConvertToCSV.py`](#org201c50c)
        5.  [`pyFoamChangeBoundaryName.py` and `pyFoamChangeBoundaryType.py` automatically modify `processorX`](#org705cf96)
    3.  [Bugfixes](#org215dc45)
        1.  [Arbitrary commands in `TemplateFile` passed to file](#orga568e9e)
        2.  [Pickled files not opened in binary mode](#orgd9afd42)
        3.  [Additional fixes for Python 3](#orgc176a64)
        4.  [`ParsedParameterFile` fails if "complete" dictionary is `#include` ed](#org644f1f4)
        5.  [`ParsedParameterFile` fails if there is more info after `#include`](#org2d334e6)
        6.  [`pyFoamDisplayBlockMesh.py` not working with VTK 6](#org4e15ee3)
        7.  [`pyFoamCreateModuleFile.py` failed with environment variables containing `=`](#orge2964b2)
        8.  [Fix import in `GeneralVCSInterface`](#orgf5bd6f5)
        9.  [Support of old format in `ParsedBlockMeshDict` broken](#orgdc29ce6)
        10. [`TemplateFile` not correctly working in Python 3](#org6d4b29d)
        11. [Certain things not done by `pyFoamPrepareCase` in `--quiet` was set](#org481426b)
        12. [Annoying warning at the start of the run](#org19fc44f)
        13. [Redirected values](#org74582b1)
        14. [Behavior of Template-engine not consistent in Python3 and Python2](#orga789957)
        15. [Braces, brackets, parentheses in column name broke `RunDatabase`](#orgecf4921)
        16. [Finding of installations in alternate locations broken](#org90a2465)
        17. [Failing on 3.x if socket for server thread already occupied](#orgf49aa34)
    4.  [Enhancements to Utilities](#org8457d5f)
        1.  [`pyFoamPrepareCase` recognizes multi-region cases](#orgd16ba6d)
        2.  [`pyFoamPrepareCase` adds specialized templates](#org2552e86)
        3.  [`pyFoamPrepareCase` keeps data generated by meshing script](#org301faec)
        4.  [`pyFoamPrepareCase` adds possibility for a file with default values](#org35d97c0)
        5.  [`pyFoamPrepareCase` writes report about the variables](#org7c227c5)
        6.  [Gnuplot can be styled with default commands](#org6279f13)
        7.  [`pyFoamPVSnapshot.py` now supports Paraview 4.2 and later](#org0b9fb7f)
        8.  [`pyFoamPVSnapshot.py` allows switching between decomposed and reconstructed data](#org7476d85)
        9.  [`pyFoamPVSnapshot.py` allows changing the field for sources](#org6a3f9cb)
        10. [`pyFoamPVSnapshot.py` allows rescaling the color-legend](#org81545b4)
        11. [`pyFoamPVsnapshot` reads parameters written by `pyFoamPrepareCase.py`](#orge78ea31)
        12. [`pyFoamListCases.py` allows filtering](#orgee162d0)
        13. [`pyFoamRunParametervariation.py` now allows dictionaries](#org4747ed3)
        14. [`pyFoamConvertToCSV.py` now has all functionality of `pyFoamJoinCSV.py`](#org9bed1d5)
        15. [`dynamic` in `customRegexp` now allows composition from multiple match-groups](#org8ae045d)
        16. [New type `dynamicslave` in `customRegexp`](#orge3c94d5)
        17. [Additional profiling option `--profile-line-profiler`](#org15beb41)
        18. [Utilities that use templates can be customized with the configuration](#org0ee45d0)
        19. [`LocalConfigPyFoam` now can be read **before** argument parsing](#orge4a688d)
        20. [`pyFoamConvertToCSV.py` automatically selects the output format with `--automatic-format`](#org97ea21f)
        21. [`pyFoamConvertToCSV.py` allows adding original data as separate sheets](#org84f320c)
        22. [`pyFoamConvertToCSV.py` has improved naming of columns](#orgc85fbb8)
        23. [`pyFoamConvertToCSV.py` now supports sets-files](#org3f11a91)
        24. [`pyFoamPrepareCase.py` can calculate derived values with a script](#org3ab663b)
        25. [`pyFoamPrepareCase.py` adds a variable `numberOfProcessors`](#orga88a5ba)
        26. [`pyFoamChangeBoundaryName.py` and `pyFoamChangeBoundaryType.py` now support decomposed cases](#org9f0a893)
        27. [`pyFoamPrepareCase.py` has possibility for templates after the final stage](#org449107f)
        28. [`pyFoamRunParameterVariation` allows adding postfix to cloned cases](#org8753a89)
        29. [`pyFoamConvertToCSV` now allows setting of default input file format](#org43d53ce)
        30. [`pyFoamListCases.py` adds the hostname to the printed information](#org9e91179)
        31. [`pyFoamPrepareCase.py` allows cloning](#orgc9e07f4)
    5.  [Enhancements to the Library](#orga53692c)
        1.  [`SolutionDirectory` detects multiple regions](#orga413508)
        2.  [`BoolProxy` now compares like builtin `bool`](#org6e73584)
        3.  [`PyFoamApplication`-class now supports `pvpython` for debugging](#orgb77a169)
        4.  [`TemplateFile` now allows more flexible assignments](#orge38c04c)
        5.  [`ThirdParty`-library `six` upgraded to 1.9.0](#org2f2dc8d)
        6.  [Additional markup in `RestructuredTextHelper`](#orgc97b44a)
        7.  [`SpreadsheetData` can now read files produced by the `sets`-functionObject](#org4ed352e)
    6.  [Infrastructure](#org4fc6612)
        1.  [Adaption of Debian packaging to new conventions](#org273fcdc)
    7.  [Development changes](#orga95a340)
        1.  [Now uses `pytest` for unittesting](#orgeb75acf)
9.  [Version 0.6.4 - 2014-11-24](#org34fc571)
    1.  [Requirements](#org34bfb89)
    2.  [Future changes](#org5afe7fe)
        1.  [Redundant utilities `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py` unified](#org4d4da64)
    3.  [Major changes](#orgeed81cb)
        1.  [Multi-line regular expressions in `customRegexp`](#org3f7436d)
        2.  [Enhancement of `pyFoamPrepare.py`](#orgd11a928)
        3.  [Enhancements of the CSV-utilities](#org1ff2850)
        4.  [Environment variable `PYFOAM_SITE_DIR` and `PYFOAM_DIR`](#orgd59d3e1)
    4.  [Incompatibilities](#org023e076)
        1.  [Option `--silent` removed from `pyFoamPrepareCase.py`](#org7ed78af)
        2.  [Keys in `RunDatabase` with column-names that contain upper-case letters change](#org38ab82e)
        3.  [Change in unique variable names in `pyFoamConvertToCSV.py`](#org45ac628)
        4.  [`PyFoam.IPython`-module renamed to `PyFoam.IPythonHelpers`](#org15331fe)
    5.  [Bugfixes](#orgeaf348a)
        1.  [Templates in `pyFoamPrepareCase.py` did not keep permissions](#org7dd9887)
        2.  [`pyFoamComparator.py` failed due to circular dependency](#org007578b)
        3.  [`pyFoamDumpRunDatabaseToCSV.py` fails if Pandas-data is requested](#orgcddb577)
        4.  [`sort` for list broke code on Python 3](#orgc5ba637)
        5.  [Changing the OF-version does not work in Python 3](#org345d247)
        6.  [`addData` in `PyFoamDataFrame` extrapolates for invalid values](#org2ed355b)
        7.  [`--keep-last` did not work for `pyFoamClearCase.py` and parallel cases](#org49a0251)
        8.  [`pyFoamDumpRunDatabaseToCSV.py` does not add basic run information](#org8fc5413)
        9.  [Restore of `FileBasisBackup` did not work](#org7de82a2)
        10. [Remove circular dependency in `DataStructures`](#org44f9adb)
    6.  [New features/Utilities](#orgcd94b27)
        1.  [`pyFoamRunParameterVariation.py`](#org090f0c1)
        2.  [`pyFoamBinarySize.py`](#orga774375)
        3.  [`pyFoamBlockMeshRewrite.py`](#org8bdbb83)
    7.  [Enhancements to Utilities](#org5a81cd1)
        1.  [`pyFoamChangeBoundaryType.py` allows setting additional values](#org6855baa)
        2.  [`pyFoamPrepareCase.py` now has OF-version and fork as defined variables](#org10c8829)
        3.  [`pyFoamPrepareCase.py` now allows "overloading" another directory](#orge8e1790)
        4.  [`pyFoamIPythonNotebook.py` adds improvements to the notebook](#org3480e7b)
        5.  [`pyFoamListCases.py` more tolerant to faulty `controlDict`](#orgc19b7a0)
        6.  [`pyFoamDumpConfiguration.py` prints sections and keys alphabetically](#orgb96bd80)
        7.  [`pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py` read and write Excel-files](#org6336c7b)
        8.  [Flexible variable filtering in `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py`](#org4d7a955)
        9.  [Columns in `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py` can be recalculated](#org0df41d3)
        10. [Testing for `Numeric` removed from `pyFoamVersion.py`](#orge55f190)
    8.  [Enhancements to the Library](#orga426405)
        1.  [Subclass of `ClusterJob` that support `PrepareCase`](#org9adfe4a)
        2.  [Subclass of `ClusterJob` that support `RunParameterVariation`](#orga94c0fd)
        3.  [`execute` in `PyFoam/Utilities` fails if script is not executable](#orgdd09bd8)
        4.  [`foamVersion` uses a separate wrapper class for `tuple`](#orgc17d6c4)
        5.  [Move calculation of disk usage to `Utilities`](#orgea3514c)
        6.  [Enhancement of `--help`](#org78d9c9d)
        7.  [`which`-routine in `Utitlities` uses native Python-routine](#org3004432)
        8.  [`FileBasis` now allows file handles instead of the filename](#orgf6cb3bc)
        9.  [`BlockMesh` doesn't force writing to file anymore](#org6c01a7a)
        10. [Additional methods for `BlockMesh`-class](#org953ba64)
        11. [`LineReader` allows keeping spaces on left](#orgbea18ee)
        12. [`TemplateFile` now allows writing of assignment-results in file](#org6b2c518)
        13. [`SolverJob` now allows passing of parameters to the solver](#orgdbcb3f6)
        14. [`SpreadsheetData` now allows reading from an Excel file](#orge5aad9c)
        15. [`SpreadsheetData` allows recalculating columns](#orgdd34465)
    9.  [Known bugs](#org647c84d)
        1.  [Timelines not forgotten for multiple runner calls](#org3f67eb2)
10. [Version 0.6.3 - 2014-06-23](#orgde142e8)
    1.  [Requirements](#org1423902)
    2.  [Major changes](#org71c3571)
        1.  [Version changing supports forks of OpenFOAM](#orgc51a56f)
    3.  [Incompatibilities](#org5a25539)
        1.  [Change of command interface of `pyFoamSTLUtility.py`](#orge4f17f8)
        2.  [If `0.org` is present `pyFoamCloneCase.py` and `pyFoamPackCase.py` ignore `0`](#orgf8a575a)
    4.  [Bugfixes](#orgb9b14a4)
        1.  [PlotWatcher has long times between updates if pickling takes long](#orge3ae087)
        2.  [`pyFoamPVSnapshot.py` fails for newer paraview-versions](#org3c63b29)
        3.  [SamplePlot failed when valueNames are unspecified](#org2605682)
        4.  [`pyFoamTimelinePlot.py` failed Numpy/Pandas output of vector fields](#orge0c280f)
        5.  [`alternateAxis` ignored for slave](#orga39227d)
        6.  [`pyFoamCaseReport.py` more stable for binary `boundary`-files](#org04c943d)
        7.  [`SpreadsheetData` returns data which breaks certain Pandas-operations](#orga3b5f19)
        8.  [`pyFoamCloneCase.py` added duplicates to the archive](#orgd587679)
        9.  [`nonuniform` of length 3 not correctly printed](#orge708a91)
    5.  [New features/Utilities](#orgca52a69)
        1.  [`pyFoamPrepareCase.py` for case preparation](#org806531c)
        2.  [`pyFoamIPythonNotebook.py` for generating and manipulating IPython-notebooks](#org5131915)
        3.  [Additional sub-module `PyFoam.IPython`](#org71c02d6)
        4.  [Additional sub-module `PyFoam.Wrappers`](#org152f42b)
    6.  [Enhancements to Utilities](#orgc94cc9d)
        1.  [`pyFoamSampleplot` has option to use index instead of time in filenames](#org7753fe5)
        2.  [`pyFoamListCases.py` Allows addition of custom data](#orgf647750)
        3.  [Switch compiler versions](#org687e654)
        4.  [`pyFoamVersion.py` reports the installed versions better](#org2c58d2c)
        5.  [Offscreen rendering can be switched off in `pyFoamPVSnapshot.py`](#org41e7140)
        6.  [Write 3D-data in `pyFoamPVSnapshot.py`](#orgc2adb85)
        7.  [Added capabilities to `pyFoamSTLUtility`](#org45256b3)
        8.  [`pyFoamDecomposer.py` switches off function objects](#orga712726)
        9.  [`pyFoamCloneCase.py` clones more stuff](#org2c30017)
    7.  [Enhancements to the Library](#orgce3a6a8)
        1.  [`BasicRunner` now can print the command line that is actually used](#org690194a)
        2.  [`ClusterJob` now can live without a machinefile](#org7048c31)
        3.  [Enhanced treatment of symlinks during cloning](#org3840fc7)
        4.  [`AnalyzedCommon` clears the `analyzed`-directory](#orgb67fcdc)
        5.  [`TimelineDirectory` is more tolerant](#org6ba4260)
        6.  [Possibility of a subcommand-interface for utilities](#org3ce6203)
        7.  [`STLUtility` accepts file-handles](#orgc181b85)
        8.  [`addClone` in `SolutionDirectory` accepts glob patterns](#org13eaa40)
        9.  [`execute` in `Utilities` allows specification of working directory and echoing of output](#org766d761)
        10. [`rmtree` and `copytree` more tolerant](#org5193523)
        11. [Enhanced support for booleans in the parser](#org9acb77f)
        12. [Application classes now allow specifying options as keyword parameters](#org55c99dd)
        13. [`SolutionDirector` now can classify directories in the `postProcessing`-directory](#org163dbcc)
        14. [`pyFoamSamplePlot.py` now more flexible for distributions](#orgcf8205c)
        15. [`DictProxy` now has a `dict`-like `update`-method](#org3b65818)
        16. [`FoamFileGenerator` automatically quotes strings](#orga2eb483)
        17. [Children of `FileBasis` now can be used with the `with`-statement](#orgebaa677)
11. [Version 0.6.2 - 2013-11-03](#orga3eb1cd)
    1.  [Major changes](#org68963fa)
        1.  [Use of `pandas`-library](#orgd90c07b)
    2.  [Incompatibilities](#org51bb2b0)
        1.  [Different separator for databases in CSV-files](#org2c957c7)
        2.  [Change of independent variable name in sample data](#org5c07ed4)
    3.  [Bugfixes](#org2e141f0)
        1.  [`pyFoamPackCase.py` does not handle symbolic links correctly](#org26d1068)
        2.  [`pyFoamPotentialRunner.py` not working with OpenFOAM 2.0 or newer](#org2295455)
        3.  [`pyFoamListCase.py` fails with `controlDict` that use preprocessing](#orgf21f376)
        4.  [Cloning fails in symlink-mode if files are specified twice](#org332dd2d)
    4.  [Utilities](#org374bf0a)
        1.  [`pyFoamPotentialRunner.py` now allows removing of `functions` and `libs`](#org6616dc0)
        2.  [The Runner-utilities now have more options for clearing](#orgd2e4f21)
    5.  [Library](#org5d10e27)
        1.  [`SolutionDirectory` and `TimeDirectory` are more tolerant](#org3c842fb)
        2.  [`ClusterJob` now handles template files](#orgbcb0b8e)
        3.  [Additional parameters in `ClusterJob`](#orgd06ae27)
        4.  [Custom data in directory easier accessible](#org97f03b9)
        5.  [`SolverJob` now allows compression of output](#org2d1acb2)
        6.  [`PyFoamApplication`-class now allows quick access to data](#org4316534)
    6.  [New features/Utilities](#orgc823b76)
        1.  [Post-run hook that sends mail at the end of run](#orgd2c79ea)
        2.  [New utility `pyFoamCompressCases.py`](#org94c6af4)
        3.  [Paraview-module to read additional data](#orgf049384)
    7.  [Enhancements](#org4bd23a7)
        1.  [`pyFoamRedoPlot.py` can plot in XKCD-mode](#orgb9a77d5)
        2.  [`pyFoamListCases.py` now displays disk usage in human readable form](#org8193e67)
        3.  [`pyFoamClearCase.py` more flexible in selection of data to be removed](#org15b307e)
        4.  [`pyFoamFromTemplate.py` automatically chooses template and default values](#orga35d2d1)
        5.  [`pyFoamDumpRunDatabaseToCSV.py` can disable standard-fields](#org5ba0a8d)
        6.  [`pyFoamDumpRunDatabaseToCSV.py` prints `pandas`-object](#org8a184e8)
        7.  [Better debugging with `ipdb`](#org0e695b7)
        8.  [Interactive shell after execution for utilities](#orgc69c7af)
        9.  [Utilities that read quantitative data convert to `pandas`-data and/or `numpy`](#org97e8b58)
        10. [Utilities that read quantitative data write Excel files](#orgcfb41e3)
        11. [Specify additional settings for `GnuPlot` in `customRegexp`](#orgccce9dc)
        12. [More flexible data specification for `pyFoamSamplePlot.py`](#org6b1f371)
        13. [`pyFoamSamplePlot.py` now allows specification of x-range](#org093dcdc)
12. [Version 0.6.1 - 2013-05-24](#orgfa6191f)
    1.  [Major changes](#org047f1d2)
    2.  [Bugfixes](#org8a808de)
        1.  [Restoring of `controlDict` after `write`](#org7ead729)
        2.  [Custom-plot type `slave` not working if no `master` defined](#org16b0c9d)
        3.  [`-list-only` did not correctly parse lists with a numeric prefix](#orgda1d5fa)
    3.  [Utilities](#org9040c46)
        1.  [`pyFoamBuildHelper.py` now allow more than one action](#org6cf61f9)
        2.  [Utilities warn if OpenFOAM-version is unset](#org94b6cee)
        3.  [`pyFoamUpgradeDictionariesTo20.py` allows single files](#org4f38a4f)
        4.  [`pyFoamUpgradeDictionariesTo20.py` transforms reaction-schemes](#org15b862d)
        5.  [`pyFoamUpgradeDictionariesTo20.py` transforms thermophysical data](#org7c5a8dd)
        6.  [`pyFoamCloneCase` now allows creating directory that symlinks to the original](#org22d33ca)
        7.  [`pyFoamClearCase.py` now removes `postProcessing` and allows removal of additional files](#orgc7c0bd9)
        8.  [Improvements to `pyFoamVersion.py`](#org3a89c3c)
        9.  [Additional files automatically cloned](#orga1c4df8)
        10. [`pyFoamDisplayBlockMesh.py` uses the same options for template format as `pyFoamFromTemplate.py`](#org25c4142)
    4.  [Library](#org292b20d)
        1.  [Improvements in syntax of `ParsedParameterFile`](#orgafab9bf)
        2.  [`Utilities`-class now function to find files matching a pattern](#org6425cc5)
        3.  [VCS ignores more files](#org28c32de)
    5.  [New features/Utilities](#org866a78b)
        1.  [New Utility `pyFoamSymlinkToFile.py`](#org2bd243c)
13. [Version 0.6.0 - 2013-03-14](#orga3c53cf)
    1.  [Major changes](#orgb9163b0)
        1.  [Adaption to work with Python3](#org1bbc153)
        2.  [New ThirdParty-Libraries](#org91cf73a)
        3.  [Porting to `Windows`](#org36dde8f)
        4.  [Experimental port to `pypy`](#orgef37903)
    2.  [Third-Party](#orgc59f049)
        1.  [Upgraded `ply` to 3.4](#org861d7ca)
    3.  [Infrastructure](#org2d3cce8)
        1.  [Parameters can't be modified in `CTestRun` after initialization](#org543198f)
        2.  [Treat timeouts in the `MetaServer` right](#org46ea309)
        3.  [Add `execute`-method to `ClusterJob`](#org97e4b2d)
        4.  [Add possibility to run specific modules before or after the solver](#org1dd4ced)
        5.  [Parameters added to the info about the run](#orga0be15d)
        6.  [Parameter handling in `ClusterJob` extended](#org2f9966c)
        7.  [Run data written alongside `PickledPlots`](#org887b902)
        8.  [`BasicRunner` collects error and warning texts](#org23af3d7)
    4.  [Library](#orga721d40)
        1.  [`TemplateFile` now uses `pyratemp`](#org105653d)
        2.  [Clearer error message in Application-classes](#org17cd919)
        3.  [Output is only colored if it goes to the terminal](#orgbbbfe4e)
        4.  [`error`-method of application classes now raises an exception](#org5f04f7d)
        5.  [`ParsedParameterFile` now knows how to handle binary files](#orgf3f5135)
        6.  [`LabledReSTTable` for more flexible table generation](#org1f496a6)
        7.  [Plotting classes now allow setting of `xlabel`](#org0d1962b)
    5.  [Utilities](#org118d859)
        1.  [`pyFoamFromTemplate.py` with new templating engine](#org5d56a27)
        2.  [`pyFoamSamplePlot.py` allows using the reference data as basis for comparison](#orge580fcc)
        3.  [Scaling and offsets are now used in plots of `pyFoamSamplePlot.py`](#orga158ced)
        4.  [`pyFoamPrintData2DStatistics.py` prints relative average error](#org2a801c0)
        5.  [Enhancements to `pyFoamVersion.py`](#org0f26174)
        6.  [`pyFoamRunner.py` allows hooks](#org61dc57d)
        7.  [`pyFoamRedoPlots.py` supports range for plots](#org4157937)
        8.  [`pyFoamDisplayBlockMesh.py` no supports templates](#orge3c4f64)
        9.  [`pyFoamCaseReport.py` is tolerant towards binary files](#orgbda38e3)
        10. [`pyFoamSamplePlot.py` and `pyFoamTimelinePlot.py` raise error if no plots are generated](#org52e66f8)
        11. [`pyFoamSurfacePlot.py` can wait for a key](#org1bde25d)
        12. [`pyFoamEchoDictionary.py` is more flexible with binary files](#org07e2d9d)
        13. [All utilities now have a switch that starts the debugger even with syntax-errors](#org63c1fcd)
        14. [Utilities now can be killed with `USR1` and will give a traceback](#org390143b)
        15. [Switch to switch on **all** debug options](#org5d8f17d)
        16. [Plotting utilities now allow specification of x-Axis label](#org2e75473)
        17. [Metrics and compare for `pyFoamTimelinePlot.py` and `pyFoamSamplePlot.py` support time ranges](#org4de27a1)
        18. [`pyFoamDisplayBlockMesh.py` allows graphical selection of blocks and patches](#orgc6a43ba)
        19. [`pyFoamCloneCase.py` and `pyFoamPackCase.py` accept additional parameters](#orgc59ffb0)
        20. [`pyFoamListCases.py` now calculates estimated end-times](#orge36404b)
    6.  [New features](#org39bd427)
        1.  [Different "phases" for multi-region solvers](#org5d62f6a)
        2.  [`pyFoamChangeBoundaryType.py` allows selection of region and time](#orgcb5925f)
        3.  [New class for storing case data in a sqlite-database and associated utilities](#orga129994)
    7.  [Bugfixes](#orgefe66fe)
        1.  [Only binary packages of 1.x were found](#orged4cff6)
        2.  [Option group *Regular expressions* was listed twice](#orgaefb6e8)
        3.  [`--clear`-option for `pyFoamDecompose.py` not working](#org7dcef9e)
        4.  [`pyFoamDisplayBlockmesh.py` not working with variable substitution](#orgb9c0183)
        5.  [Option `--function-object-data` of `pyFoamClearCase.py` not working with directories](#orgd460fcf)
        6.  [`nonuniform` of length 0 not correctly printed](#org9263fec)
        7.  [Building of pseudocases with `pyFoamRunner.py` broken](#org4488a30)
        8.  [`pyFoamRedoPlot.py` did not correctly honor `--end` and `--start`](#orga41eb28)
        9.  [`WriteParameterFile` does not preserve the order of additions](#org9d4fc4e)
        10. [Wrong number of arguments when using `TimelinePlot` in `positions`-mode](#org2351cfc)
        11. [`ClusterJob` uses only `metis` for decomposition](#org74474ea)
        12. [`pyFoamSamplePlot.py` and `pyFoamTimelinePlot.py` produced no pictures for regions](#org605a17b)
        13. [Barplots in `pyFoamTimelinePlot.py` not working if value is a vector](#org07adf67)
        14. [Mysterious deadlocks while plotting long logfiles](#orge0d5389)
        15. [Scanning linear expressions form the block coupled solver failed](#org499bd88)
        16. [`#include` not correctly working with macros in the included file](#org32980a2)
        17. [Macros not correctly expanded to strings](#orgc47ca3e)
        18. [`pyFoamPackCase.py` in the working directory produces 'invisible' tar](#org7b563a7)
        19. [String at the end of a linear solver output makes parsing fail](#org87542d3)
        20. [Paraview utilities not working with higher Paraview versions](#org06e0333)
        21. [Camera settings not honored with `pyFoamPVSnapshot.py`](#org9257528)
14. [Version 0.5.7 - 2012-04-13](#org0777681)
    1.  [Parser improvements](#orgf5422e4)
    2.  [Utility improvements](#org611ad70)
    3.  [New Utilities](#org8d746f6)
    4.  [Library improvements](#org60bf06d)
    5.  [Removed utilities](#org27c589a)
    6.  [Thirdparty](#org838765e)
    7.  [Other](#org42ae195)
15. [Older Versions](#orgc8efab8)


<a id="orga45ca8d"></a>

# Version 0.6.11 - Not yet released


<a id="org5dcdb7c"></a>

## Major changes


<a id="org85a22f3"></a>

## Incompatibilities


<a id="org947dfa7"></a>

### Behaviour reading `customRegexp`

Macro expansion in the `customRegexp` might break it for some
cases


<a id="orgaaa6c9f"></a>

### Gnuplot does not use `FIFO` as the default anymore

See the relevant entry in *Enhancements to Utilities*

A potential problem is that the new implementation leaves files in
the `/tmp` filesystem


<a id="orge3fb473"></a>

## New feature/utilities


<a id="org71f9fe7"></a>

## Enhancements to Utilities


<a id="orgadcfdbe"></a>

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


<a id="org3404693"></a>

### Macro expansion in `customRegexp`

In the `customRegexp` it is now possible to use the usual
OpenFOAM-macro-expansions with `$` etc. This makes


<a id="org670e9ba"></a>

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


<a id="org4cb8408"></a>

### `pyFoamRedoPlot.py` allows passing terminal options

The utility now allows passing options to the plotting
implementation with the `--terminal-options`-option. This can for
instance be used to modify the size of the plot


<a id="orga41ac2f"></a>

### `pyFoamPlotWatcher.py` stops scanning the file is `--end` was specified

If the `--end-time` option is specified then the solver stops
scanning if that time is reached. The plot windows are killed. To
keep them specify `--persistent`


<a id="orgb1ebf8e"></a>

### Hardcopies of custom plots have more descriptive names

Instead of the `custom00xxx` name the hardcopies of custom plots
now have and additional short name that describes the content of
the plot (it is taken from the id in the `customRegexp`)


<a id="org1de8eda"></a>

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


<a id="orgaa133a1"></a>

### `pyFoamPrepareCase.py` calls script after copying initial conditions

A script `postCopy.sh` is called after the initial conditions are
copied from `0.org`


<a id="orge33ffe2"></a>

### `--stop-after-template` and `--keep-zero` improve control in `pyFoamPrepareCaseParameters.py`

The combination of these two parameters allow "just" changing
something in the templates without running other lengthy
operations


<a id="orgc625c60"></a>

### `pyFoamPVSnapshot.py` allows specification of the image quality

The option `--quality` now allows specifying the quality of the
image with a value of \(0\) being worst (but producing the smallest
pictures) and \(100\) best (but producing huge pictures). The
default is \(50\)


<a id="orgeb6ff15"></a>

### Image size specification for `pyFoamPVSnapshot.py`

The options `--x-resolution` and `--y-resolution` allow specifying
the resolution of the image. If only one of them is set the image
is scaled proportionally. This only works for Paraview versions
bigger than 5.4


<a id="org11d72f7"></a>

### Setting separation of views and background transparency in `pyFoamPVSnapshot.py`

Two new options were added that allow setting a separation between
different views and making the background transparent. This only
works for Paraview versions bigger than 5.4


<a id="orga46be89"></a>

### `pyFoamPVLoadState.py` automatically uses decomposed or reconstructed data

Depending which of the two sets has more timesteps that state is
set to this before loading. So if more parallel timesteps are
present then these are used even if the state file uses the
reconstructed times. The behavior can be changed with the
`--decompoes-mode`-option


<a id="org4930732"></a>

### Change directory for `pyFoamPrepareCase.py` to target

The option `--extecute-in-case-directory` changes the working
directory to the target directory. THis allows specifying
parameter files that are in that directory without a full path


<a id="org04ec85c"></a>

### `pyFoamPrepareCase.py` can create an example case

A command like

    pyFoamPrepareCase.py exampleCase --paramter-file=parameters.base --build-example --clone-case=originalCase

creates an example case `exampleCase` from a template case
`originalCase` using the parameter file `parameter.base`. It
creates a script `Allrun` that allows executing the case without
`PyFoam` (if none of the scripts uses `PyFoam`-scripts)

This may not work for all configurations (especially cases that use `postTemplate`)


<a id="org52696c9"></a>

### `pyFoamPrepareCase` prints derived values

The same way that the utility printed the used values it now
prints the derived values as well


<a id="org251069e"></a>

### `pyFoamPVSnapshot` allows specifying different colors for different views

The option `--color-for-filers` now allows specifying a different
color for the same filter in different view. This is done by
specifying a dictionary


<a id="org349ca70"></a>

### `alternateLogscale` for custom plots

This is analog to `logscale` but for the values that are specified
with `alternateAxis`


<a id="org2a8a918"></a>

### `pyFoamBinarySize.py` now calculates documentation size as well

If there is `html` documentation then this is counted as well


<a id="org1173124"></a>

## Enhancements to the Library


<a id="org276182e"></a>

### `progress`-data is automatically converted to `float`

When using format-strings for the `progress`-entry then the
library automatically attempts to convert the data to `float`
(otherwise it keeps it as `str`)


<a id="org53c86ab"></a>

## Bug fixes


<a id="orge80151f"></a>

### With dynamic plots names with `_slave` are problematic

This made the slave plots that had `_slave` in the name fail


<a id="org49774d8"></a>

### New-style dimensioned scalars fail

As reported in
<https://sourceforge.net/p/openfoam-extend/ticketspyfoam/223/> by
Rodrigo Leite Prates parsing certain constructs that involve
dimension sets fail. This is because of a problem with the
comparison of `Dimension` that assumes that the other side is a
`Dimension` as well. Fixed


<a id="orgcac24b0"></a>

### `pyFoamPVSnapshot.py` not working with Paraview 5.6

The API now has to be called through a different module. Otherwise
it will fail


<a id="org7a30c1c"></a>

### `customRegexp` farthes away was used

When looking automatically for a `customRegexp` the one furtherest
up in the directory tree was used. Now instead all the
`customRegexp` are used with the lower ones overriding the other
ones


<a id="org99a5a46"></a>

### `ParameterFile`-class got confused by commented lines

One of the oldest classes in PyFoam had the problem that it
"found" parameters that were commented out with `//`. This has been fixed


<a id="org34ae69b"></a>

### `pyFoamBinarySize.py` did not count files in `build`

Some distros have a directory `build` with the intermediate object
files. This has not been counted until now


<a id="orgf7ce561"></a>

## Infrastructure


<a id="org2d1d97b"></a>

## ThirdParty


<a id="org50d1fa7"></a>

# Version 0.6.10 - 2018-08-12

This is only a minor release with the main purpose to recognize
OpenFOAM 6 installations with their new numbering scheme


<a id="orgce47b79"></a>

## Incompatibilities


<a id="org03e7525"></a>

### `pyFoamPrepareCase.py` does not execute decomposition scripts for single processor cases

If `numberOfProcessors` is smaller than 2 then the decomposition
scripts are ignored. This may cause problems in the unlikely case
that the setup process relied on these scripts being always
executed


<a id="orgffa713b"></a>

## New feature/utilities


<a id="org786baa3"></a>

### Utility `pyFoamFunkyDoCalc.py` to compare data from `funkyDoCalc`

This utility compares data written by the `funkyDoCalc`-utility from
`swak4Foam` (this data is written with the `-writeDict`-switch

For details on the usage see the online help of the utility


<a id="org849e7e3"></a>

## Enhancements to Utilities


<a id="org3308338"></a>

### Recursive searching for `pyFoamListCases.py`

The `--recursive`-option now recursively searches the specified
directories for cases. Without the option it behaves the way it
did before


<a id="orgca9a5dd"></a>

### Look for `customRegexp` in parent directories

The plotting utilities now look for `customRegexp`-files in parent
directories of the case directory. This allows to use one file for
a number of cases. The file in the directory is still used. The
behavior can be switched off with the
`--no-parent-customRegexp`-option


<a id="org6752191"></a>

### `pyFoamPrepareCase.py` does not execute decomposition scripts for single processor cases

If `numberOfProcessors` is smaller than 2 then the decomposition
scripts are ignored


<a id="org421ac20"></a>

### `pyFoamPrepareCase.py` checks for proper decomposition

At the end the utility now checks if the number of processor
directories is consistent with the specified `--number-of-processors`


<a id="org951038a"></a>

### `pyFoamPlotWatcher.py` automatically uses newest logfile

If a logfile `auto` is specified then the utility uses the newest
file with the extension `.logfile` in the current directory.

Like any automatism this might produce unexpected results. So use
with care


<a id="org8f9ea32"></a>

## Enhancements to the Library


<a id="org2d8134f"></a>

### `FoamFileGenerator` handles `OrderedDict`

The class now preserves the order if an instance of `OrderedDict`
is found (instead of the usual behaviour of sorting the keys to
always get the same output)


<a id="org7ed1e97"></a>

### `#sinclude` handled as an alias to `#includeIfPresent`

OpenFOAM v1812 introduces this as an alias. It is now handled by
the parser similarly


<a id="org64f2d21"></a>

### OpenFOAM 6 correctly recognized

With OpenFOAM 6 the naming scheme changed again. Instead of 6.0
(which PyFoam would have recognized) it is now plain 6. PyFoam now
recognizes both forms in the directory name


<a id="orgc59a74a"></a>

## Bug fixes


<a id="orgc9bd235"></a>

### `pyFoamPrepareCase.py` did not remove `processor`-directories


<a id="org5bc25c7"></a>

## Infrastructure


<a id="orga0e5fdf"></a>

### Single digit version numbers supported

Now installations with names like `OpenFOAM-6` are recognized


<a id="org55981fa"></a>

# Version 0.6.9 - 2018-02-25


<a id="org0a97015"></a>

## Major changes


<a id="org113c2a5"></a>

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


<a id="orgc8acde3"></a>

## Incompatibilities


<a id="org1ba00ee"></a>

### `pyFoamPrepareCase.py` creates `.foam`-file

The utility now automatically creates a file that allows Paraview
to open the case


<a id="orgd6917b3"></a>

### Hardcoded Foam-Version upgraded to `4.0`

The hardcoded Foam-version that is used if the
`WM_PROJECT_VERSION` environment variable is not set is set to
`4.0` from the rather ancient version `1.5`


<a id="org0eab5a1"></a>

### `none` no longer parsed as an equivalent for `false`

This breaks the parsing of cases where `none` is used as a word.


<a id="org732a1d7"></a>

## New features/utilities


<a id="orge30c63e"></a>

### `pyFoamJoinTimelines.py` to join Timelines from restarts

This utility joins timeline files from different restarts. The
lines from times that will be in the next file are discarded


<a id="org00b6bcb"></a>

### `pyFoamRestartRunner.py` to automatically restart runs

For cases that fail strangely (mostly due to problems in the
linear solver) but restart successfully this utility helps running
them.

The utility tries to restart the solver until either the `endTime`
is reached or no new time-step is written to disk (in this case it
makes no sense to run again)


<a id="orga703f7f"></a>

## Enhancements to Utilities


<a id="orgc03f213"></a>

### Special snapshot utilities to use MESA

There have been variations of the regular `pyFoamPVSnapshot.py`
added. The only difference they have is that they set a option that
enforces the used `OpenGL`-implementation (especially Mesa). Use this run
the script on a machine that don't have hardware support for 3D-graphics


<a id="orgafe2943"></a>

### Automated plotting of film properties

For the surface film solvers there now properties like the mass,
covered surface, thickness and velocity are automatically plotted


<a id="org648679d"></a>

### `pyFoamClearCase.py` automatically executes an existing `Allclean`

If present the script (which is usually found in tutorial cases)
is executed before other cleaning takes places


<a id="org51b8eea"></a>

### `pyFoamPrepareCase.py` executes tutorial scripts if available

If there are scripts present from the original tutorials that do
**only** case preparation (like `Allrun.pre`) but no solver running
and no special scripts are present then the original scripts are
executed


<a id="orge0fdcaa"></a>

### Script for clearing in `pyFoamPrepareCase.py`

If a special script `clearCase.sh` is found this is used for
additional clearing. If instead a script `Allclean` is found then
this is used


<a id="orgd390cc0"></a>

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


<a id="org9a59bd7"></a>

### `pyFoamPrepareCase.py` now allows separate decomposition scripts

After three of the phases

-   mesh creation
-   copying of the `.org` files
-   case setup

the utility executes a script (`decomposeMesh.sh`,
`decomposeFields.sh` and `decomposeCase.sh`) if found. This allows
to adapt for different situations (for instance: the mesh already
being generated in parallel)


<a id="org1595d94"></a>

### Runner-utilities now create seperate logfiles on restart

If PyFoam thinks that a run is restarted (old time-files exist and
there already exists a logfile) it creates logfiles with
`.restart` appended. This allows joining the original log and the
restart log


<a id="org3d73757"></a>

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


<a id="org7bddb40"></a>

### `pyFoamPackCase.py` adds parallel data

With the option `--parallel` now adds parallel data


<a id="org0fcf0d7"></a>

### `--replacement`-option in `pyFoamPVSnapshot.py` supports Foam-format

The option can now alternatively use Foam-format instead of Python-format


<a id="org490d894"></a>

### `pyFoamPVSnapshot.py` improved error messages with problems in replacement

Instead of a stack trace there is now an output of the template
string and the available values


<a id="orgd125964"></a>

### `customRegexp` now searched in parent directories

If in the directory of the log-file no `customRegexp` and the
log-file is not in the current directory then PyFoam looks for it
in all directories up to the current directories


<a id="org9e4457c"></a>

## Enhancements to the Library


<a id="org2da29d4"></a>

### `Paraview.StateFile` extended

This module has been extended to allow more flexible manipulations
of the state-file


<a id="org3eae458"></a>

### `BasicRunner` now checks for regular End

The `BasicRunner` now checks whether the string `End` was seen and
**no** time-information after that. This means that the simulation
reached its "regular" end and is also reported in the
`PyFoamState.TheState`-file


<a id="org2bf07fb"></a>

## Bug fixes


<a id="org245f119"></a>

### `pyFoamPrepareCaser.py` ran out of memory for large script outputs

Because all the output from scripts was stored in memory before
being written to a log it was possible that the utility ran out of
memory when there was much output. The output is now written
directly to disk


<a id="orgba2f106"></a>

### No Courant number plottet if `WM_PROJECT_VERSION` is unset

Scanning for the Courant number defaulted to the versy old
version. This has been fixed


<a id="org6fb6adc"></a>

### Rescale does not work for streamlines in `pyFoamPVSnapshot.py`

`--rescale-color-to-source` did not work for sources that have no
cell values (like streamlines). Fixed.


<a id="orgdda6927"></a>

### Server not correctly running on Python 2.7 with `socketserver`

Some installations of Python 2.7 already have the
`socketserver`-module which does not have the required
`BaseServer`-module. Fixed


<a id="orge652309"></a>

# Version 0.6.8.1 - 2017-08-03


<a id="orgdb76ad3"></a>

## Bug fixes


<a id="orgcb83bdb"></a>

### Fork not correctly detected for `v1706`

As the `+` is not present in the `WM_PROJECT_VERSION` this distro
was detected as the Foundation fork


<a id="org8aae348"></a>

# Version 0.6.8 - 2017-07-06


<a id="org8ec411f"></a>

## Major changes


<a id="orgcd5cfbd"></a>

### `pyFoamNet`-utilities now work without a Meta-Server

As described in other changenotes below the Server process now
announces its presence with ZeroConf. This means that a central
Meta-Server is no longer necessary. But the `zeroconf` library has
to be present on all involved machines (server and client). It is
installed with

    pip install zeroconf


<a id="org3975116"></a>

## New features/utilities


<a id="orgffeca4a"></a>

### Added module `PyFoam.Infrastructure.Authentication`

This module implements a simple public key authentication. For
authentication a username and a challenge are sent. If the
username is in the set of authenticated keys (or is the own
username) then this key is used to check the challenge.


<a id="orge8f51a9"></a>

## Enhancements to Utilities


<a id="orgb0f7246"></a>

### `pyFoamClearCase.py` now has `-dry-run` option

This option doesn't clear anything but prints the things that will
be erased


<a id="org4c8db55"></a>

### New option `--keep-time` for `pyFoamClearCase.py`

This option (which can be specified more than once) allows
specifying single time-steps that should be kept


<a id="org63a60c3"></a>

### `pyFoamNetList.py` no longer needs a meta-server to work

Due to the addition of `ZeroConf` this utility no longer needs a
Meta-Server to find running calculations in the same subnet


<a id="org4bf7352"></a>

## Enhancements to the Library


<a id="org6aebde0"></a>

### Better calculation of used memory in runs

If the `psutil`-library is installed then the memory used by
parallel runs is calculated as well


<a id="orgdf1c369"></a>

### Pre and post-hooks are now also searched in `PyFoam.Site`

`module` specified in `preRunHook_` and `postRunHook_` is now
searched in `PyFoam.Site.` as well. This module is the
`lib`-directory in the directory specified by the environment
variable `PYFOAM_SITE_DIR` (which allows adding user-scripts and
modules)


<a id="orgc413802"></a>

### Adapted to correctly detect `OpenFOAM+ v1706`

This fork has changed its numbering scheme (dropped the `+` in the
version string). This broke a regular expression and a function to
detect the number


<a id="org9c571fd"></a>

## Infrastructure


<a id="org9e17472"></a>

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


<a id="org26853ab"></a>

## Bug fixes


<a id="org072dfc4"></a>

### `--keep-interval` in `pyFoamClearCase.py` not working for parallel-cases

Due to a copy/past error this option did not work for parallel
cases. This is now fixed


<a id="org01969b2"></a>

# Version 0.6.7 - 2017-06-04


<a id="orgce134c0"></a>

## Requirements


<a id="org40b1902"></a>

### Now at least Python 2.6 required

The new `PLY`-version and `six` now at least requires this
Python-version. If your system has Python 2.5 or older stick with
PyFoam 0.6.6


<a id="orgfc55571"></a>

## Incompatibilities


<a id="org478cb30"></a>

### Names of files generated by `pyFoamPVSnapshot.py` differ

Due to changes in the time-step numbering the names of the
generated files differ. If your work-flow depends on the old names
add the options `--consecutive-index-for-timesteps` and
`--duplicate-times`


<a id="org24965f0"></a>

## New features/utilities


<a id="org64e952b"></a>

### Utility `pyFoamListProfilingInfo.py` to print profiling data

The utility reads the profiling info written by

-   foam-extend
-   OpenFOAM+ v1606 (and higher)
-   or the patch found at <https://sourceforge.net/p/openfoam-extend/svn/HEAD/tree/trunk/Breeder_2.3/distroPatches/applicationLevelProfiling/>

and prints it in a human-readable form


<a id="orgbfefdc1"></a>

### Utility `pyFoamBlockMeshConverter.py` to convert a 2D-mesh to 3D

This utility (and the required Libraries) was written by Hasan
Shetabivash (original at <https://github.com/hasansh/blockMeshConverter.git>)

This utility takes a file that is written in a similar syntax as
the regular `blockMeshDict` but with the third dimension
missing. It then converts this file to a regular `blockMershDict`
by either extruding in the $z$-direction or by rotating around the
\(x\) or the $y$-axis


<a id="orgfb4d04e"></a>

## Enhancements to Utilities


<a id="orgdab48a6"></a>

### `customRegexp` now can scan for texts

Until now data items (groups) in the regular expression had to be
valid numbers. Otherwise a warning was issued. This behavior is
still the default but if a list-variable `stringValues` is added
then the items (whose numbers are specified in the list) are not
being plotted. They are written to disk with `--write-files` and
they can be used in `progress`


<a id="org0bbca63"></a>

### Lines in `PyFoamHistory` escaped

Additions to the history file where arguments contain whitespaces
and/or quotes are quoted and quotes inside are escaped. This
allows these command lines to be copy/pasted to the command line


<a id="orga54aa9b"></a>

### `--values-string` of `pyFoamPrepareCase.py` now accepts OpenFOAM-format

These strings are now parsed as OpenFOAM-strings if there is no
starting `{` and no ending `}`. With these the old behavior
(parsing as a Python-dictionary) is used


<a id="orgac58bfc"></a>

### `pyFoamRunner.py` and `pyFoamPlotRunner.py` allow automatic selection of solver

If for those utilities the word `auto` is written in place of a
proper solver (like `interFoam`) then the utility looks into
`controlDict` for the `application`-entry and uses that


<a id="org405b6eb"></a>

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


<a id="org109fb1c"></a>

### Multi-part `idNr` for `dynamic` in `customRegexp`

`idNr` can now alternatively be a list of integers (instead of a
single integer). In that case the corresponding matches are
concatenated (with a `_` between them) to generate the data id.

If only a number is specified it has the old behavior.

As usual the indexes of the matches stat with \(1\) (not \(0\))


<a id="org0dc3b0e"></a>

### `pyFoamListCases.py` detects dead runs

If a run has not had any output in the last hour it is listed as
dead. This threshold can be customized


<a id="orgb35315f"></a>

### Improved time-handling of `pyFoamPVSnapshot.py`

The utility now numbers the time-steps by the order in the
solution directory. Before that the used time-steps were numbered
consecutively (from \(0\) to \(N-1\) if \(N\) time-steps were specified).

Also: by default each time-step is only processed once

The old behaviour can be reproduced with
`--consecutive-index-for-timesteps` and `--duplicate-times`


<a id="org45da957"></a>

### Default plots can be set in configuration

Whether or not plots are plotted automatically (for instance the
execution time) can be set in the `[Plotting]`-section of the
configuration. So it can be set per-case in the
`LocalConfigPyFoam`-file. If a plot is on by default it can be
switched off with the corresponding `--no`-option. If off by
default the `--with`-option switches it on


<a id="orgf3786c1"></a>

### `derivedParameters.py`-script called from `pyFoamPrepareCase.py` allows error reporting

In that script that calculates new parameters and also can do
parameter checking there now is a function `error` available that
makes the script and the complete execution fail


<a id="org3079b4f"></a>

## Enhancements to the Library


<a id="orga300113"></a>

### Detection of new versions of OpenFOAM-foundation and OpenFOAM+

Both distros changed their scheme for the version numbers and the
regular expressions have been adapted to detect them


<a id="org9aedadb"></a>

### `SpreadsheetData` now handles string data

If one of the columns is string data then the `()`-operator
returns string values (when interpolating the next value)


<a id="org7ccf962"></a>

### `TimelineData` tolerates string values

The class can now read strings without spaces (OpenFOAM `words`)
and pass them to `SpreadsheetData`


<a id="orgd08d4db"></a>

### `()` operator of `SpreadsheetData` works without name

If no `name` parameter is given then the method returns a
dictionary with all the values


<a id="orgb01ea5b"></a>

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


<a id="orga8640fb"></a>

### User-specific temporary directory

The method `PyFoam.FoamInformation.getUserTempDir` makes sure that
a user specific temporary directory exists and returns the path to
that directory


<a id="orgc8cd31a"></a>

### `Gnuplot`-plots now get better titles

Instead of `Gnuplo` the window titles are now set to `pyFoam` and
the actual title of the plots. This should make it easier to find
plot windows in the window manager


<a id="orgbb40158"></a>

### `ParsedParameterFile` now supports `#includeFunc`

In case of a `#includeFunc`-entry the file is either searched
relative to the current file (this is where the semantics differ
from how OpenFOAM because that searches in the
`system`-directory. But as this entry is usually called from
`system/controlDict` the result is the same) and if not it looks
for it in `$FOAM_ETC`


<a id="orgc0e6098"></a>

### New utility function `findFileInDir`

This function in `PyFoam.Basics.Utilities` looks recursively for a
file in a directory


<a id="orgac7b425"></a>

### `humandReadableDuration` added to `PyFoam.Basics.Utilities`

This function takes a duration (in seconds) and prints it in a
human-readable form


<a id="orge5a21a8"></a>

## Infrastructure


<a id="org8c1ed36"></a>

### `pyFoamVersion.py` now reports the versions of the `ThirdParty`-packages

Now these versions are reported as well for quick reference


<a id="org3395561"></a>

## Bug Fixes


<a id="orgf37d2c9"></a>

### Application classes fail in Paraview

The class `PyFoamApplication` assumes that the module `sys` has an
element `argv`. This is not the case inside Paraview


<a id="orgc9bd6dc"></a>

### Scripts in `pyFoamPrepareCaseParameters.sh` not working on Mac OS X

Because newer versions of Mac OS X remove `LD_LIBRARY_PATH` from
the environment passed to scripts (for security reasons)
additional libraries (for instance `swak4Foam`) were not correctly
loaded. This has been fixed by generating a special script that
exports `LD_LIBRARY_PATH` before executing the rest


<a id="orgd62e23a"></a>

### Processor-directories unsorted in `SolutionDirectory`

The class assumed that `processorX` directories were added in the
numeric order which is not necessarily the case. This caused
problems with `pyFoamCaseReport.py`


<a id="org95e2213"></a>

### Deleting failed if a file did't exist

The utility function to delete directories failed if the directory
didn't exist. Fixed


<a id="org1e2dc7a"></a>

### Missing files in `RegionCases`

When creating a `RegionCase` only the "known" files were
symlinked. This causes some programs to fail. Now everything from
`system` in the master-case is symlinked if there is not already a
file of that name there


<a id="org931673a"></a>

### Wrong `solver` in `pyFoamListCase.py`

If another utility was run in the mean-time the wrong solver is
listed by the utility. Fixed


<a id="org31f0233"></a>

## ThirdParty


<a id="org254e576"></a>

### Updated `tqdm` to version 4.8.4

No reason. Just because there was an update


<a id="org34dc94d"></a>

### Updated `PLY` to version 3.9

This breaks compatibility with Python 2.5 or older


<a id="orgac0288b"></a>

### Updated `six` to 1.10.0

This also breaks compatibiliy with Python 2.5 or older


<a id="orgc559817"></a>

# Version 0.6.6 - 2016-07-15


<a id="org4cca3ff"></a>

## Incompatibilities


<a id="org0eb92a6"></a>

### Changes in `IPython`-notebooks 3.0

With IPython 3.0 the names of the Widget classes lost the `Widget`
in the name (for instance `DropdownWidget` becomes
`Dropdown`). `PyFoam` has been changed to conform with this but as
a consequence won't work with old version of the `IPython`
notebooks


<a id="orgdc9b36b"></a>

## Enhancements to Utilities


<a id="orgd0bda2f"></a>

### `pyFoamPrepareCase.py` executes `setFields` if appropriate

If no setup-script is specified and if there is a `setFieldsDict`
present then `setFields` is automatically executed


<a id="orgd1de42b"></a>

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


<a id="orgc4a6c42"></a>

### `alternateAxis`-entries now can be regular expressions

This allows specifying plots generated with `type dynamic` on the
alternate axis


<a id="orgc0d0330"></a>

### Plotting utilities now allow choice of Gnuplot terminal

These utilities now allow with the option `--gnuplot-terminal` to
choose the terminal. Otherwise the terminal specified in the
configuration (usually `x11`) is used


<a id="orgc2cd98e"></a>

### Plotting utilities now sort legend by name

Names in the legend are now sorted. This improves readability for
large numbers of lines in the plot


<a id="org5f8efd8"></a>

### `pyFoamExecute.py` allows calling with debugger

The option `--run-with-debugger` runs the command in the
debugger. The arguments are appropriately handled


<a id="org145020c"></a>

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


<a id="orgb537c58"></a>

### `--hardcopy` in plotting library now allows modification of `gnuplot`-terminals

This option allows setting the options for the terminal selected
with `--format-of-hardcopy`. This overrides any default set in
configuration section `[Plotting]` under the name
`hardcopyOptions_<term>` with `<term>` being the name of the
terminal (for instance for `png` the option is `hardcopyOptions_png`.


<a id="orgc8daafc"></a>

### `pyFoamPrepareCase.py` writes state information about what it is currently doing

It writes to the usual state file. This way `pyFoamListCases.py`
will list this information. If the scripts call `pyFoamRunner.py`
then this information will be overwritten


<a id="org43065d6"></a>

### `pyFoamBinarySize.py` can handle new location of binaries in OpenFOAM 3.0

Since that foam version all binaries (and object files are located
in the directory `platforms`. The utility now finds them there


<a id="org2c31b6d"></a>

### `Runner`-utilites now can signal on `blink(1)`-devices

With the option `--use-blink1` these utilities now flash on a
plugged in `blink(1)` USB-device for every time-step


<a id="org2761b66"></a>

### `pyFoamExecute.py` can flash a `blink(1)`

To indicate that the utility is still running it is able to play a pattern on a
`blink(1)`-device. This is switched on with `-use-blink`


<a id="orgdea1714"></a>

### `pyFoamDecompose.py` allows using a template file

With the option `--template-dict` it is possible to initialize the
output with an existing file. With this file it is possible to add
'complicated' settings.


<a id="org5ae9edf"></a>

### `pyFoamTimelinePlot.py` now handles new format of probe files

Probe files now have one comment line per probe to specify the
position. This format is now correctly detected and plotted. Old
probe files are also handled


<a id="org5e260d2"></a>

### `ReST`-report of `pyFoamPrepareCase.py` now reports derived parameters

The `.rst`-file written by the utility now adds a section on
derived parameters if such parameters were specified in a script


<a id="orgb519f32"></a>

### `pyFoamPrepareCase` can now ignore directories

It is now possible to specify directories that should be ignored
when looking for templates. Some sensible defaults like
`postProcessing`, `processor*` and `VTK` are already set


<a id="org8c48d63"></a>

### `pyFoamConvertToCSV.py` allows adding formulas to XLSX-files

The option `--add-formula-to-sheet` allows adding formulas to the
Excel-sheet. Something like

    --add-formula="massflow:::'inlet'-'outlet'"

adds a column `massflow` that subtracts the columns `inlet` and `outlet`


<a id="org0c36b40"></a>

### `pyFoamListCases.py` now displays mercurial info

For those who use mercurial to keep track of their cases the
utility now has the option `-hg-info` that displays the mercurial
hash-ID, the local id and the branch name


<a id="org4706a75"></a>

### Progress bar added to utilities with long run-time

Using the library `lqdm` progress bars have been added to
utilities that have a long run-time and where the progress bars
are not disturbing the regular output. These utilities are

-   `pyFoamListCases.py`
-   `pyFoamBinarySize.py`

Bars can be switched off with `--no-progress-bar`


<a id="orgfbdadaa"></a>

### Utilities that clear data can now report what is cleared

`pyFoamCleasCase.py` and all utilities that have a `--clear`
option now also have a `--verbose-clear` option that reports
**what** is being cleared


<a id="org30b469f"></a>

### `pyFoamConvertToCSV.py` now allows manipulating the input

The utility now has two new options:

-   **&#x2013;strip-characters:** This allows removing characters before the
    file is actually read
-   **&#x2013;replace-first-line:** Replaces the first line (for instance if
    the header does not match the data


<a id="orgd4112e7"></a>

## Enhancements to the Library


<a id="orgdcdf5df"></a>

### Detection of `OpenFOAM-dev`

A development installation is now also detected and it is assumed
that this uses the new calling convention. Also: PyFoam reports
this as version `9.9.9` (as this is larger than any version in the
foreseeable future


<a id="org5b817ee"></a>

### Add `OpenFOAM+` as a fork

An additional fork type `openfoamplus` has been added (in addition
to `openfoam` and `extend`). Installations of the form
`OpenFOAM-vX.X+` (with `X.X` being the version number) are added
to this fork. Also `OpenFOAM-plus` is added as the development
version of this fork


<a id="orgae5385d"></a>

### Accept new convention for location of `blockMeshDict`

In newer OpenFOAM-versions `blockMeshDict` may be located in
`system`. PyFoam detects it either there or in the old
`constant/polyMesh`-location


<a id="org33c818e"></a>

### Handling of complex data by `Configuration`

Lists and dictionaries now can also be specified. Have to be
correctly formatted if they are longer than one line (indented by
at least one space - convention for configuration files)


<a id="org6a97783"></a>

### `Configuration` has method `getArch` for architecture dependent settings

If an option `opt` is requested with this option then it is
checked whether an architecture-dependent setting exists.
Architecture `arch` is the output of the `uname`-command. The
architecture-dependent name is `opt_arch`.


<a id="org510fd36"></a>

### `execute`-method from `PyFoam.Basics.Utilities` returns status-code

This function now has an option that makes it return the status of
the execution as well as the output of the execution.


<a id="orge80db8c"></a>

### `BasicRunner` now supports more ways of stopping runs

In the past this class (and the utilities based on it) looked for
a file `stop` and stopped the run (with writing) if it was
found. Now two additional files are looked for

-   **stopWrite:** this waits for the next scheduled write and then stops the run
-   **kill:** gracefully stops the run without any writing


<a id="org6895a0c"></a>

### Added `Blink1` class to support `blink(1)` devices

This class assumes that a `blink(1)` USB-device is present and the
API-server (from the `Blink1Control`-program for this is
running. It wraps these calls so that utilities can use them
conveniently


<a id="org6697771"></a>

### `ParsedParameterFiles` now supports `includeEtc`

`#includeEtc` is now supported


<a id="orgfc5c3dc"></a>

### Parses uniform fields correctly

Uniform fields of the form `1002{42.5}` (Field with 1002 values
\(42.5\)) are now correctly parsed


<a id="org52a804e"></a>

### `toNumpy`-method added to `Unparsed` and `Field`

These two classes have a method `toNumpy` added that transformed
the data into a structured `NumPy`-array. There are no
applications for this in `PyFoam` yet but an application will be
the parsing of lagrangian data


<a id="org7abe3d3"></a>

### Added module `PyFoam.RunDictionary.LagrangianPatchData` to read data from patch function object

This module reads data written by the cloud function-object that
writes particle data as particles hit the patches and transforms
it into `numpy`-array. Which can also be returned as `pandas`
`DataFrames`

It adds some properties to the data

-   the patch name
-   the time at which this data was written
-   a `globalId` constructed from `origId` and `origProcId`


<a id="org75609f4"></a>

### Added module `PyFoam.RunDictionary.LagrangianCloudData` to read cloud data

This gets

-   a case
-   a cloud name
-   a time name and reads the lagrangian data from the specified
    time and converts it to a pandas `DataFrame`

A `globalId` that is consistent with the one in `LagrangianPatchData` is set


<a id="org9e687ae"></a>

### Method `code` added to =RestructuredTextHelper

This method formats a string assuming that it is a program
code. Default value is `python`


<a id="org9c9c045"></a>

### `ParsedParameterFile` now parses new dimension format correctly

Newer OpenFOAM-versions allow dimensions in symbolic format (for
example `[ m s^-1 ]`). These are now correctly parsed


<a id="org4728689"></a>

### `ParsedParameterFiel` now parses uniform fields correctly

Fields of the form `23 { 4.2 }` (meaning "23 times 4.2") are now
correctly parsed


<a id="org1481866"></a>

## Infrastructure


<a id="orgedf8119"></a>

### Change of documentation from `epydoc` to `sphinx`

As `expydoc` is discontinued the API-documentation is now generated
with `sphinx`. Just run

    make docu

to do so.

Advantage is that now with

    make docset

a document set for offline searching with `Dash` (for Mac OS X) or
clones (on other OSes) can be generated


<a id="org91202f0"></a>

### Adaptions to the unittests

Untitests only used to run correctly if the OpenFOAM-version was
1.7. Are changed to run with OF 3.0. No effort has been made to
support intermediate versions as the changes are mainly about
changed tutorials


<a id="orgbd30472"></a>

## Bug fixes


<a id="orgb81897c"></a>

### Wrong format of `ExecutionTime` breaks plotting utilities

If the `ExecutionTime` is not as expected `pyFoamPlotWatcher.py`
and `pyFoamPlotRunner.py` finish with an error. This is now more
robust


<a id="org623aa9f"></a>

### `phases` not working with dynamic plots

For dynamic plots the addition of the phase name did not work. Fixed


<a id="org64f71a4"></a>

### Phase name added to function object output

If `phase` was set the output of the function objects got it added
to the names even though the function objects do not belong to the
phase. This is fixed


<a id="org3625bce"></a>

### One region mesh too many in utilities that change the boundary

When working with regions one region too many was added in
`pyFoamChangeBoundaryType.py` and `pyFoamChangeBoundaryName.py`. Fixed


<a id="org66bfeb3"></a>

### `pyFoamClearCase.py` fails on write-protected case

If a case is write protected then the utility failed. Now it only
issues a warning and continues cleaning


<a id="org270e925"></a>

### Copying of directories in `pyFoamPrepareCase.py` confused by zipped files

When copying one file to another and one of them is zipped then
copying doesn't replace the destination correctly but adds the
zipped/unzipped variant


<a id="orgcbc8c9e"></a>

### Wrong times for multi-view layouts in `pyFoamPVSnapshots.py`

If snapshots were taken from state files with multiple layouts
then some of the views had the wrong time (either that from the
state-file or from the timestep before). Fixed


<a id="org4a69423"></a>

### First timestep not plotted (and not stored)

The data from the first timestep was not plotted under certain
circumstances. This has been fixed


<a id="org2c08321"></a>

### `DYLD_LIBRARY_PATH` not passed on *Mac OS X 10.11*

Starting with this OS-version as a security feature the system
does not pass `LD_LIBRARY_PATH` and `DYLD_LIBRARY_PATH` to a
shell. `PyFoam` detects this and creates these variables and makes
sure they are passed to the processes


<a id="org0424de8"></a>

### Newer versions of `pandas` broke the writing of excel files with `pyFoamConvertToCSV.py`

The reason is that the old way of making axis data unique did not
work anymore. This has been fixed


<a id="org9521803"></a>

### Capital `E` in exponential notation for floats breaks parser

This problem has been reported at
<https://sourceforge.net/p/openfoam-extend/ticketspyfoam/220/>
(the number `1E-2` is not correctly parsed to `0.01`) and has been fixed


<a id="orgf76fa1e"></a>

### `Runner`-utilities clear processor directories if first time in parallel data differs

In cases where the parallel data has a different start directory
than \(0\) the `pyFoamRunner.py` and similar utilities cleared that
data and made a restart impossible. This has been fixed


<a id="orgd197c4c"></a>

### Utilities `pvpython` not working when installed through `distutils`

As the `distutils` (and all mechanisms built on these like `pip`)
replace the used python in scripts the necessary `pvpython` was
removed. This has been fixed by generating a temporary script file
that is actually executed with =pvpython)


<a id="org34e907e"></a>

## ThirdParty


<a id="orgef61a93"></a>

### Added `tqdm` for progress bars

Add the library `tqdm` (<https://github.com/tqdm/tqdm>) for adding
progress bars to utilities.

Library is under `MIT` License


<a id="orgdb008d5"></a>

# Version 0.6.5 - 2015-06-01


<a id="org828b500"></a>

## Major changes


<a id="org7776c27"></a>

### PyFoam now on *Python Package Index*

PyFoam is now found at <https://pypi.python.org/pypi/PyFoam>

Recommended way of installing is using <https://pip.pypa.io/en/latest/> :

    pip install PyFoam

This will also make sure that the required `numpy`-package is
installed


<a id="org112878a"></a>

## Incompatibilities


<a id="orga1c0c07"></a>

### `ArchiveDir` in `SolutionDirectory` discouraged

As this was never really used it is discouraged (the option is
still there).

If you don't understand what this means it probably doesn't
concern you


<a id="org919d8c5"></a>

### Pickled data files now written as binary

All pickled files are now written and read in binary mode (as this
was the only way that works consistently in Python 3). This **may**
cause problems with old cases (but no effort has been made to
check whether this problem actually exists)


<a id="org1d627a3"></a>

### The `PlotRunner` and `PlotWatcher` now don't strip spaces

These two utilities now don't strip leading spaces from the read
lines. This preserves formatting in the output but might break
scripts that rely on these spaces.

The old behaviour may be reset by overriding `stripSpaces` in
section `SolverOutput` with a value `True`


<a id="org201c50c"></a>

### Different column names in `pyFoamConvertToCSV.py`

The enhanced naming of the columns might break scripts that rely
on the old naming


<a id="org705cf96"></a>

### `pyFoamChangeBoundaryName.py` and `pyFoamChangeBoundaryType.py` automatically modify `processorX`

In previous versions these boundary files were not modified. Now
they are. Scripts that rely on unchanged `boundary`-files in the
`processorX`-directories might fail. Old behavior can be set with
the `--no-processor`-option


<a id="org215dc45"></a>

## Bugfixes


<a id="orga568e9e"></a>

### Arbitrary commands in `TemplateFile` passed to file

Lines with `$$` are passed to the file and make it syntactically incorrect.
Fixed


<a id="orgd9afd42"></a>

### Pickled files not opened in binary mode

This caused problems in Python 3 were binary strings were not
correctly written (actually: attempts to write them to a
pickle-file made the application fail)


<a id="orgc176a64"></a>

### Additional fixes for Python 3

In a number of classes/applications semantic differences between
Python 2 and 3 makes these fail on Python 3. Changes are

-   Replace `map` with list comprehension where possible
-   Modify wrappings in `CTestRun` to work with Python3
-   Replace `print` with `print_`
-   Semantic difference in division of two integers: Python3 gives a
    floating point number as a result


<a id="org644f1f4"></a>

### `ParsedParameterFile` fails if "complete" dictionary is `#include` ed

If an included dictionary has a header parsing failed. This is
fixed by retrying the parsing with the header


<a id="org2d334e6"></a>

### `ParsedParameterFile` fails if there is more info after `#include`

If there is for instance a `;` after an `#include` statement the
regular OpenFOAM-parser ignores it. The PyFoam-parser failed. This
has been fixed and the parser behaves like regular OpenFOAM


<a id="org4e15ee3"></a>

### `pyFoamDisplayBlockMesh.py` not working with VTK 6

Due to changes in the API the program did not work. This is now
fixed and the program works with VTK 6 as well as VTK 5


<a id="orge2964b2"></a>

### `pyFoamCreateModuleFile.py` failed with environment variables containing `=`

In that case an overeager `split` created lists.

Fix provided by Martin Beaudoin


<a id="orgf5bd6f5"></a>

### Fix import in `GeneralVCSInterface`

Change in the syntax of imports in Python 3 broke this
one. Fixed. But doesn't matter as Mercurial doesn't support
Python3


<a id="orgdc29ce6"></a>

### Support of old format in `ParsedBlockMeshDict` broken

Wrong usage of indexes. Fixed


<a id="org6d4b29d"></a>

### `TemplateFile` not correctly working in Python 3

Reason was a different calling convention to the `exec`-function
of Python. Fixed


<a id="org481426b"></a>

### Certain things not done by `pyFoamPrepareCase` in `--quiet` was set

This was due to actions being on the same level as the
debug-output. Fixed


<a id="org19fc44f"></a>

### Annoying warning at the start of the run

For certain solvers the plot utilities issued a warning during a
phase when no information about the current time is
available. This is now fixed


<a id="org74582b1"></a>

### Redirected values

not used when iterating over dictionaries
    When iterating over dictionaries with redirects the values in the
    redirected dictionaries were not used. This is now fixed


<a id="orga789957"></a>

### Behavior of Template-engine not consistent in Python3 and Python2

Due to a difference in the behavior of the `eval`-function in
Python 3 certain expressions (especially with list comprehension)
failed. Fixed


<a id="orgecf4921"></a>

### Braces, brackets, parentheses in column name broke `RunDatabase`

These characters were stripped out by *SQLite*. They are thus
normalized to special character combinations (which will be
denormalized after reading)


<a id="org90a2465"></a>

### Finding of installations in alternate locations broken

The algorithm to find (Open)FOAM-installations in alternate
locations was broken. Now working again


<a id="orgf49aa34"></a>

### Failing on 3.x if socket for server thread already occupied

Due to a a change in the socket API if the socket for the network
thread (usually port 18000) was already notified the program
failed. Fixed. Tested on 2.7 as well


<a id="org8457d5f"></a>

## Enhancements to Utilities


<a id="orgd16ba6d"></a>

### `pyFoamPrepareCase` recognizes multi-region cases

If there are multiple regions and no `prepareMesh.sh` then it will
try to execute `blockMesh` for the regions


<a id="org2552e86"></a>

### `pyFoamPrepareCase` adds specialized templates

With the option `--extension-addition` additional templates that
override the regular templates can be specified.

Application may be for instance special templates for
`potentialFoam`


<a id="org301faec"></a>

### `pyFoamPrepareCase` keeps data generated by meshing script

If the meshing stage generates a `0`-directory then data in that
directory will be kept. This can be switched off if this is not
the desired behaviour


<a id="org35d97c0"></a>

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


<a id="org7c227c5"></a>

### `pyFoamPrepareCase` writes report about the variables

The utility now writes a *Restructured Text* file with a report
about the variables. Information from `default.parameters` like
groupings and `description` are used in this report. Also the
default value and the actual value are reported.

The file can be converted with a utility like `rst2pdf`


<a id="org6279f13"></a>

### Gnuplot can be styled with default commands

For all utilities that use Gnuplot as the backend for plotting
there is now a configuration option `gnuplotCommands` in the
`Plotting`-section with the usual `set` commands of Gnuplot. This
is preset to display a grid and the y-axis.

The settings can be reset with the `gnuplotCommands`-list in the
`customRegexp`-entries


<a id="org0b9fb7f"></a>

### `pyFoamPVSnapshot.py` now supports Paraview 4.2 and later

The API for screenshots changed with Paraview 4.2 and later. This
API now supports layouts if multiple views were specified. The
default behaviour is now to make only one screenshot per
layout. The old behaviour (one screenshot per view) can now be
switched on with the `-no-layouts`-option.

This allows screenshots exactly the way they look on screen


<a id="org7476d85"></a>

### `pyFoamPVSnapshot.py` allows switching between decomposed and reconstructed data

The utility now rewrites the state file so that either decomposed
or reconstructed data is read. The default is that the data set
for which more timesteps exist is selected


<a id="org6a3f9cb"></a>

### `pyFoamPVSnapshot.py` allows changing the field for sources

It is now possible to specify a dictionary with source names and
the fields that should be set for them. This allows quickly
coloring the same layout with different fields.

This works for

-   3D (rendered) filters
-   bar charts


<a id="org81545b4"></a>

### `pyFoamPVSnapshot.py` allows rescaling the color-legend

There are now two ways to rescale the color-transfer functions

-   by specifying a dictionary with the ranges
-   by specifying a source. The range of the data on that source
    will be used to scale the data
    -   when specifying a source percentiles can be specified for the
        highest and lowest percent of the cells to be ignored

The first method will override the second


<a id="orge78ea31"></a>

### `pyFoamPVsnapshot` reads parameters written by `pyFoamPrepareCase.py`

An option allows specifying that these parameters should be
read. They are then available for substitution in the *Text*
source


<a id="orgee162d0"></a>

### `pyFoamListCases.py` allows filtering

The utility now has options to select the cases that should be
considered by name of the case. Either substrings or globs can be
used. Ignore patterns can be specified as well


<a id="org4747ed3"></a>

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


<a id="org9bed1d5"></a>

### `pyFoamConvertToCSV.py` now has all functionality of `pyFoamJoinCSV.py`

Now all functionality of the `Join`-utility is present in the `Convert`
utility (including interpolating times)

`pyFoamJoinCSV.py` will be removed in future versions of `PyFoam`


<a id="org8ae045d"></a>

### `dynamic` in `customRegexp` now allows composition from multiple match-groups

If `idNr` is a list then now the actual id is composed from all
the match groups specified in that list. If `idNr` is an integer
then it behaves like it used to.

Application for the new behavior would be for instance to have the
flow of different species on different patches in one plot


<a id="orge3c94d5"></a>

### New type `dynamicslave` in `customRegexp`

This combines the properties of the types `dynamic` and `slave`:
dynamically generated data sets that are added to another plot


<a id="org15beb41"></a>

### Additional profiling option `--profile-line-profiler`

Uses the library `line_profiler` for profiling. Only of interest
for developers. Experimental


<a id="org0ee45d0"></a>

### Utilities that use templates can be customized with the configuration

The section `Template` in the configuration now allows modifying
the behavior of the templating engine (how templates are processed
and syntax details)


<a id="orge4a688d"></a>

### `LocalConfigPyFoam` now can be read **before** argument parsing

This allows overruling options before they are set be command line
options. This has to be enabled by the application (it doesn't
make sense for all).

An example is the `pyFoamPrepareCase.py`-utility where the local
configuration file can overrule the default behavior of the
template engine


<a id="org97ea21f"></a>

### `pyFoamConvertToCSV.py` automatically selects the output format with `--automatic-format`

Now if that option is selected and the extension of the output is
`xls` the option `-write-excel-file` doesn't have to be set
anymore


<a id="org84f320c"></a>

### `pyFoamConvertToCSV.py` allows adding original data as separate sheets

The input data files now can be added to an excel-file as separate
sheets with the `--add-sheets`-option


<a id="orgc85fbb8"></a>

### `pyFoamConvertToCSV.py` has improved naming of columns

Now if there is more than one source file then the columns from
the first source also get a unique prefix.

It is also possible to clean the column names before writing them
to file. The time name can be changed with
`-write-time-name`. Substrings can be replaced with
`--column-name-replace` and simple functions can be applied with
`--column-name-transformation`


<a id="org3f11a91"></a>

### `pyFoamConvertToCSV.py` now supports sets-files

The utility now can read these files and determine the field names
from the filename. `--automatic` assumes that files with the
extension `.xy` are of this format


<a id="org3ab663b"></a>

### `pyFoamPrepareCase.py` can calculate derived values with a script

If a script `derivedParameters.py` is present then it is executed
and values set in that script can be used in the templates as well


<a id="orga88a5ba"></a>

### `pyFoamPrepareCase.py` adds a variable `numberOfProcessors`

If unspecified by the user this variable is automatically \(1\). It
can be used by the templates to distinguish between different cases

The `PrepareCaseJob`-class in `ClusterJob` automatically sets the
values according to the number of processors in the cluster job


<a id="org9f0a893"></a>

### `pyFoamChangeBoundaryName.py` and `pyFoamChangeBoundaryType.py` now support decomposed cases

Both utilities now also modify the boundary files in the
`processorX`-direcories. This behaviour can be switched off from the command line


<a id="org449107f"></a>

### `pyFoamPrepareCase.py` has possibility for templates after the final stage

Templates with the extension `.finalTemplate` are executed after
the `caseSetup.sh`-script.


<a id="org8753a89"></a>

### `pyFoamRunParameterVariation` allows adding postfix to cloned cases

The option `--cloned-case-postfix` adds a postfix to the cloned
directory names. This can be used if the results from multiple
variations with the same parameter file should be kept (for
instance when comparing OpenFOAM-versions)


<a id="org43d53ce"></a>

### `pyFoamConvertToCSV` now allows setting of default input file format

The option `--default-read-format` now allows setting a different
format than `csv` as the default format for input files


<a id="org9e91179"></a>

### `pyFoamListCases.py` adds the hostname to the printed information

The utility tries to determine from the pickled data the host the
simulation was run on and prints it (can be switched off with an
option)


<a id="orgc9e07f4"></a>

### `pyFoamPrepareCase.py` allows cloning

The utility now has an option `--clone-case` to clone a new case
before starting instead of working in the specified directory (in
this case the case will be cloned to this directory). The name of
the created directory **can** be constructed from the specified
parameters with the `--automatic-casename`-option


<a id="orga53692c"></a>

## Enhancements to the Library


<a id="orga413508"></a>

### `SolutionDirectory` detects multiple regions

Valid regions are sub-directories of `constant` that have a
`polyMesh`-directory


<a id="org6e73584"></a>

### `BoolProxy` now compares like builtin `bool`

Comparison used to fail for types where it was not explicitly
implemented like `None`


<a id="orgb77a169"></a>

### `PyFoamApplication`-class now supports `pvpython` for debugging

Now `--interactive-after-exception` also works in the utilities
that use `pvpython`


<a id="orge38c04c"></a>

### `TemplateFile` now allows more flexible assignments

In the mode where executions are allowed now more flexible
assignments to variables are possible. To be specific:

-   array assignments like

    $$ a["t"] = 2

-   multiple assignments like

    $$ a,b = 2,3


<a id="org2f2dc8d"></a>

### `ThirdParty`-library `six` upgraded to 1.9.0

This library has been upgraded to the latest released version


<a id="orgc97b44a"></a>

### Additional markup in `RestructuredTextHelper`

There are additional methods `emphasis`, `strong` and `literal`
that wrap their arguments in the appropriate markup

The methods `bulletList`, `enumerateList` and `definitionList`
take lists or dictionaries and mark them as lists


<a id="org4ed352e"></a>

### `SpreadsheetData` can now read files produced by the `sets`-functionObject

If the option `isSampleFile` is set then it is assumed that the
field names are in the filename and there is no header with field
names in the file


<a id="org4fc6612"></a>

## Infrastructure


<a id="org273fcdc"></a>

### Adaption of Debian packaging to new conventions

By Oliver Borm. The building of Debian packages for Python
libraries has changes. Necessary adaptions were done by Oliver Borm


<a id="orga95a340"></a>

## Development changes


<a id="orgeb75acf"></a>

### Now uses `pytest` for unittesting

The `nose`-library had problems and all the unit-tests run
out-of-the-box with `pytest`


<a id="org34fc571"></a>

# Version 0.6.4 - 2014-11-24


<a id="org34bfb89"></a>

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


<a id="org5afe7fe"></a>

## Future changes


<a id="org4d4da64"></a>

### Redundant utilities `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py` unified

These two utilities are almost indistinguishable and will be
unified into one


<a id="orgeed81cb"></a>

## Major changes


<a id="org3f7436d"></a>

### Multi-line regular expressions in `customRegexp`

If in `customRegexp` an `expr` is found with `\n` then this
expression is matched over multiple consecutive lines. Types like
`dynamic` work as usual.

This makes it possible to match for instance the output of the
`forces`-function objects


<a id="orgd11a928"></a>

### Enhancement of `pyFoamPrepare.py`

The utility which was introduced in the last version is becomong
more usable and will be central to all things that set up the case
(for instance a special `ClusterJob`)


<a id="org1ff2850"></a>

### Enhancements of the CSV-utilities

These utilities are now more flexible and allow writing and
reading of Excel-files too


<a id="orgd59d3e1"></a>

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


<a id="org023e076"></a>

## Incompatibilities


<a id="org7ed78af"></a>

### Option `--silent` removed from `pyFoamPrepareCase.py`

Option has been renamed to `--no-complain`


<a id="org38ab82e"></a>

### Keys in `RunDatabase` with column-names that contain upper-case letters change

SQLite does not support case-sensitive column-names (`s_max` and
`S_max` are the same). To change this the upper case letters in
the column names are replaced by an underscore and the letter
(`S_max` becomes `_s__max`)

This means that old databases might not be read correctly


<a id="org45ac628"></a>

### Change in unique variable names in `pyFoamConvertToCSV.py`

The algorithm to make variable names unique has changed (basically
it uses the part of the filenames that differ) and scripts relying
on these names might fail


<a id="org15331fe"></a>

### `PyFoam.IPython`-module renamed to `PyFoam.IPythonHelpers`

The name of the module crashed in certain instances (especially
unit-testing) with the regular `IPython`-library. To avoid these
crashes it has been renamed to `IPythonHelpers`. This raises two
potential problems:

-   scripts that `import` the module have to be adapted to the new name
-   IPython-notebooks created with `pyFoamIPythonNotebook.py` have
    two imports pointing to this module. These notebooks have to be
    adapted to be usable again


<a id="orgeaf348a"></a>

## Bugfixes


<a id="org7dd9887"></a>

### Templates in `pyFoamPrepareCase.py` did not keep permissions

This was a problem for script-templates which were not executable
any more. Fixed


<a id="org007578b"></a>

### `pyFoamComparator.py` failed due to circular dependency

This has been fixed by adding an import in `BasicRunner.py`


<a id="orgcddb577"></a>

### `pyFoamDumpRunDatabaseToCSV.py` fails if Pandas-data is requested

This is now fixed


<a id="orgc5ba637"></a>

### `sort` for list broke code on Python 3

Some calls for `sort` still used the `cmp`-parameter which does
not exist for Python3 anymore. These calls have been replaced with
`key` and `reverse`


<a id="org345d247"></a>

### Changing the OF-version does not work in Python 3

Because the output of `subprocess` is now *binary* instead of a
regular string. Fixed


<a id="org2ed355b"></a>

### `addData` in `PyFoamDataFrame` extrapolates for invalid values

This was due to incorrect use of the `interpolate`-method


<a id="org49a0251"></a>

### `--keep-last` did not work for `pyFoamClearCase.py` and parallel cases

This was because there was a problem in the library code and the
utility did not consider the parallel time-steps. Fixed


<a id="org8fc5413"></a>

### `pyFoamDumpRunDatabaseToCSV.py` does not add basic run information

Basic run information was not added to the file. Now it is with
the prefix `runInfo//`


<a id="org7de82a2"></a>

### Restore of `FileBasisBackup` did not work

The logic for checking whether a file was "backupable" was
wrong. This affected the proper restore of files with utilities
for instance for `--write-all`


<a id="org44f9adb"></a>

### Remove circular dependency in `DataStructures`

According to the bug
<http://sourceforge.net/p/openfoam-extend/ticketspyfoam/219/> it was
not possible to import `DataStructures` because of a circular
dependency with `FoamFileGenerator`. Fixed by moving an import to
the back of the file


<a id="orgcd94b27"></a>

## New features/Utilities


<a id="org090f0c1"></a>

### `pyFoamRunParameterVariation.py`

This utility takes a template case and a file specifying the
parameter variation and creates cases with the
`pyFoamPrepareCase.py`-engine, runs a solver on these cases and
collects the data into a database. The database can then be
extracted with `pyFoamDumpRunDatabaseToCSV.py`


<a id="orga774375"></a>

### `pyFoamBinarySize.py`

Calculates the size of the binaries in an OpenFOAM-installation
separated by compile-option


<a id="org8bdbb83"></a>

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


<a id="org5a81cd1"></a>

## Enhancements to Utilities


<a id="org6855baa"></a>

### `pyFoamChangeBoundaryType.py` allows setting additional values

The option `--additional-values` allows specifying a dictionary
with additional values for the boundary (stuff that is needed by
`mappedWall` etc)


<a id="org10c8829"></a>

### `pyFoamPrepareCase.py` now has OF-version and fork as defined variables

This allows to write case-templates that can distinguish between
different OF-versions


<a id="orge8e1790"></a>

### `pyFoamPrepareCase.py` now allows "overloading" another directory

Before doing anything else the contents of different directories
are copied into the current case. This allows for instance to use
tutorial cases as the basis for a case


<a id="org3480e7b"></a>

### `pyFoamIPythonNotebook.py` adds improvements to the notebook

Additional code added to the generated notebook:

-   Code to change the default size of the plots
-   Distribution-directories in subdirectories `distributions`
    (generated by some `swak`-function objects) added


<a id="orgc19b7a0"></a>

### `pyFoamListCases.py` more tolerant to faulty `controlDict`

If the `controlDict` is acceptable to OpenFOAM but syntactically
incorrect for PyFoam (for instance because of a missing semicolon)
the utility does not fail anymore (but no data is collected for
that case).


<a id="orgb96bd80"></a>

### `pyFoamDumpConfiguration.py` prints sections and keys alphabetically

This should make it easier to find items


<a id="org6336c7b"></a>

### `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py` read and write Excel-files

Both utilities now allow writing Excel-files

In addition to regular text files the first sheet from `xls`-files
can be read


<a id="org4d7a955"></a>

### Flexible variable filtering in `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py`

Now it is possible to filter for regular expressions

The functionality of the two utilities now is very similar and it
is possible that one of them will be discontinued


<a id="org0df41d3"></a>

### Columns in `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py` can be recalculated

The two utilities now can add columns or recalculate columns
based on the existing column values


<a id="orge55f190"></a>

### Testing for `Numeric` removed from `pyFoamVersion.py`

Testing for the library `Numeric` library removed as it is no
longer supported as a fallback for `numpy`. Test also removed from
`setup.py`


<a id="orga426405"></a>

## Enhancements to the Library


<a id="org9adfe4a"></a>

### Subclass of `ClusterJob` that support `PrepareCase`

The class `PrepareCaseJob` supports cases that are set up with
`pyFoamPrepareCase.py`. Additional parameters to the constructor are

-   the name of the parameter-file
-   a list with the parameters. The list is composed of
    name/value-pairs


<a id="orga94c0fd"></a>

### Subclass of `ClusterJob` that support `RunParameterVariation`

The class `VariationCaseJob` supports cases that are set up with
`pyFoamRunParameterVariation.py`. Additional parameters to the constructor are

-   the name of the parameter-file
-   the name of the variations-file


<a id="orgdd09bd8"></a>

### `execute` in `PyFoam/Utilities` fails if script is not executable

The function checks if the file exists and is **not**
executable. The program fails in that case


<a id="orgc17d6c4"></a>

### `foamVersion` uses a separate wrapper class for `tuple`

This ensures that it is printed in a form that is valid in
OF-dictionaries


<a id="orgea3514c"></a>

### Move calculation of disk usage to `Utilities`

This has until now only been used in `ListCases` but moved to a
separate method/function `diskUsage` in the `Utilities`-module


<a id="org78d9c9d"></a>

### Enhancement of `--help`

Added the possibility to have an epilog and usage examples with
the `epilog` and  `examples`-keyword arguments for applications.

These and descriptions now have the possibility for line-breaks:
if two line-breaks are encountered in the text a new paragraph is
created


<a id="org3004432"></a>

### `which`-routine in `Utitlities` uses native Python-routine

For Python-version where `shutil` has a `which`-function this is
used instead of calling an external program


<a id="orgf6cb3bc"></a>

### `FileBasis` now allows file handles instead of the filename

This currently only works for reading, Backups, zipping etc won't
work but it makes algorithms more flexible


<a id="org6c01a7a"></a>

### `BlockMesh` doesn't force writing to file anymore

Instead content is stored in memory. Old behaviour is the default
to preserve compatibility with old scripts


<a id="org953ba64"></a>

### Additional methods for `BlockMesh`-class

-   **numberVertices:** Adds comments with the vertex numbers to the
    vertices


<a id="orgbea18ee"></a>

### `LineReader` allows keeping spaces on left

Previous behaviour was stripping all spaces from the lines. Now
the left hand spaces can be ket. Old behaviour is still default
for compatibility


<a id="org6b2c518"></a>

### `TemplateFile` now allows writing of assignment-results in file

This allows faster debugging of template-files. This can be
enabled with a switch in the utilities using templates


<a id="orgdbcb3f6"></a>

### `SolverJob` now allows passing of parameters to the solver

And additional parameter `solverArgs` will now be passed to the
solver (if the solver accepts arguments)


<a id="orge5aad9c"></a>

### `SpreadsheetData` now allows reading from an Excel file

During construction if an Excel-file is specified and the
`xlrd`-library and `pandas` are installed then the first sheet in
the file is read


<a id="orgdd34465"></a>

### `SpreadsheetData` allows recalculating columns

Columns can be recalculated using expressions. This includes other
data items. Currently present column names are available as
variables. There is also a variable `data` that can be subscripted
for items that are not valid variable names. A variable `this`
points to the item to be recalculated


<a id="org647c84d"></a>

## Known bugs


<a id="org3f67eb2"></a>

### Timelines not forgotten for multiple runner calls

This manifests with `pyFoamRunParameterVariation.py`. The custom
timelines are still kept in memory. Not a problem. Just annoying


<a id="orgde142e8"></a>

# Version 0.6.3 - 2014-06-23


<a id="org1423902"></a>

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


<a id="org71c3571"></a>

## Major changes


<a id="orgc51a56f"></a>

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


<a id="org5a25539"></a>

## Incompatibilities


<a id="orge4f17f8"></a>

### Change of command interface of `pyFoamSTLUtility.py`

The selection of what is to be done is now selected by subcommands
instead of options. This will break scripts using this


<a id="orgf8a575a"></a>

### If `0.org` is present `pyFoamCloneCase.py` and `pyFoamPackCase.py` ignore `0`

The reason is that the utilities assume that this directory is
produced from `0.org`


<a id="orgb9b14a4"></a>

## Bugfixes


<a id="orge3ae087"></a>

### PlotWatcher has long times between updates if pickling takes long

The reason was that it used the same throttling that made sense
for the PlotRunner. Fixed


<a id="org3c63b29"></a>

### `pyFoamPVSnapshot.py` fails for newer paraview-versions

Reason is that the class `vtkPythonStdStreamCaptureHelper` does
not support `isatty`


<a id="org2605682"></a>

### SamplePlot failed when valueNames are unspecified

Reported in
<https://sourceforge.net/apps/mantisbt/openfoam-extend/view.php?id=208>
and fixed


<a id="orge0c280f"></a>

### `pyFoamTimelinePlot.py` failed Numpy/Pandas output of vector fields

Vector fields only were added to the data fields if they were the
first in the list. Fixed


<a id="orga39227d"></a>

### `alternateAxis` ignored for slave

This is now fixed. The alternate values have to be specified in
the master (specifying in the slave gives an error)


<a id="org04c943d"></a>

### `pyFoamCaseReport.py` more stable for binary `boundary`-files

Usually these files are `ascii` (even if the header says
`binary`). In some cases the parsing failed for these. Fixed by
enforcing reading as `ascii`. Can be switched off


<a id="orga3b5f19"></a>

### `SpreadsheetData` returns data which breaks certain Pandas-operations

The reason was that if there were duplicate times in the table the
index was non-unique which certain Pandas-operations don't
appreciate. Solved by dropping duplicate times. Can be switched off


<a id="orgd587679"></a>

### `pyFoamCloneCase.py` added duplicates to the archive

If things are specified twice they were added twice. Now it is
checked whether the item already exists in the tar-file before
adding them


<a id="orge708a91"></a>

### `nonuniform` of length 3 not correctly printed

The reason was that this was interpreted as a vector and the
numeric prefix was removed. Reported at
<http://sourceforge.net/apps/mantisbt/openfoam-extend/view.php?id=218>

Fixed by introducing an extra parameter to `FoamFileGenerator`


<a id="orgca52a69"></a>

## New features/Utilities


<a id="org806531c"></a>

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


<a id="org5131915"></a>

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


<a id="org71c02d6"></a>

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


<a id="org152f42b"></a>

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


<a id="orgc94cc9d"></a>

## Enhancements to Utilities


<a id="org7753fe5"></a>

### `pyFoamSampleplot` has option to use index instead of time in filenames

The option `-index-instead-of-filename` switches this on. This
makes it easier to generate movies from the files


<a id="orgf647750"></a>

### `pyFoamListCases.py` Allows addition of custom data

The option `--custom-data` now allows the specification of custom
data items. These are read from the `pickledData`-files and
displayed in the table like regular data items


<a id="org687e654"></a>

### Switch compiler versions

Now all utilities allow switching the compiler version (for
instance from `Gcc47` to `Gcc48`). The relevant options are
`--force-system-compiler`, `--force-openfoam-compiler` and
`--force-compiler`


<a id="org2c58d2c"></a>

### `pyFoamVersion.py` reports the installed versions better

Now the location of the installations is reported as well


<a id="org41e7140"></a>

### Offscreen rendering can be switched off in `pyFoamPVSnapshot.py`

This is a workaround where the writer produces a segmentation
fault


<a id="orgc2adb85"></a>

### Write 3D-data in `pyFoamPVSnapshot.py`

In addition to writing out bitmaps allows writing out 3D-data (for
importing into other applications). Sources can be selected by name


<a id="org45256b3"></a>

### Added capabilities to `pyFoamSTLUtility`

The utility can now also:

-   erase selected patches
-   merge selected patches into one


<a id="orga712726"></a>

### `pyFoamDecomposer.py` switches off function objects

This now automatically happens for OF-versions that support
it (2.0 and greater). They can be switched on again


<a id="org2c30017"></a>

### `pyFoamCloneCase.py` clones more stuff

Files that are assumed to be used by `pyFoamPrepareCase.py` are
automatically added to the clone. This includes all files (and
directories) with the extensions `.sh`, `.template` and
`.org`. Also IPython notebooks (extension `.ipynb` are added)


<a id="orgce3a6a8"></a>

## Enhancements to the Library


<a id="org690194a"></a>

### `BasicRunner` now can print the command line that is actually used

This should help with diagnosing problems with MPI etc.

Can be switched on in some utilities with `--echo-command-prefix`


<a id="org7048c31"></a>

### `ClusterJob` now can live without a machinefile

Using the machine-file now can be switched off for job-schedulers
with a tight integration


<a id="org3840fc7"></a>

### Enhanced treatment of symlinks during cloning

If a item in the case itself is a symlink then it used to be a
copy of the file the symlink is pointing to. Now it is created as
a symlink to the target the original symlink. If the
`--follow-symlink`-option is used the old behaviour is used
(copying). In this case the option `noForceSymlink` in the
`Cloning`-section of the configuration can be used to change this
behaviour for selected files


<a id="orgb67fcdc"></a>

### `AnalyzedCommon` clears the `analyzed`-directory

The directory is cleared if it exits from a previous run.


<a id="org6ba4260"></a>

### `TimelineDirectory` is more tolerant

Used to fail if incompatible data types were used. Now ignores
them


<a id="org3ce6203"></a>

### Possibility of a subcommand-interface for utilities

The subclass `SubclassFoamOptionParser` now allows the parsing of
subclasses. The base class for utilities `PyFoamApplication` now
supports this as an option. As an example this is implemented in
`pyFoamSTLUtilities.py`


<a id="orgc181b85"></a>

### `STLUtility` accepts file-handles

The class checks whether arguments are filehandles and in this
case doesn't try to open a file for reading or writing but uses
the handle


<a id="org13eaa40"></a>

### `addClone` in `SolutionDirectory` accepts glob patterns

If no file matching the name is found it is assumed that this is a
glob-pattern and all matching files are added. This affects all
utilities that use that method (especially `pyFoamCloneCase.py`)


<a id="org766d761"></a>

### `execute` in `Utilities` allows specification of working directory and echoing of output

This method now allows the specification of a working
directory. Before executing the command the method changes to the
working directory. Afterwards it changes back to the regular
working directory.

There is also an option `echo` that immediately prints the output
to the screen


<a id="org5193523"></a>

### `rmtree` and `copytree` more tolerant

`rmtree` now also works if the "tree" is a file.

`copytree` now has a parameter `force` that allows removing the
destination directory if it exists


<a id="org9acb77f"></a>

### Enhanced support for booleans in the parser

Strings that are usually interpreted as boolean in OF-dictionaries
(for instance `on`, `yes`, &#x2026;) are now stored as a special type
that allows treating them like 'real' booleans.

For instance an expression `test no;` in a dictionary now allows
things like `if d['test']:` in the script


<a id="org55c99dd"></a>

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


<a id="org163dbcc"></a>

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


<a id="orgcf8205c"></a>

### `pyFoamSamplePlot.py` now more flexible for distributions

Tries to determine the names of the values from the first line in
the files


<a id="org3b65818"></a>

### `DictProxy` now has a `dict`-like `update`-method

This also allows enforcing string values


<a id="orga2eb483"></a>

### `FoamFileGenerator` automatically quotes strings

If strings are unquoted but contain characters that make it
illegal as a word then the string is quoted before output


<a id="orgebaa677"></a>

### Children of `FileBasis` now can be used with the `with`-statement

This mainly concerns `ParsedParameterFile`


<a id="orga3eb1cd"></a>

# Version 0.6.2 - 2013-11-03


<a id="org68963fa"></a>

## Major changes


<a id="orgd90c07b"></a>

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


<a id="org51bb2b0"></a>

## Incompatibilities


<a id="org2c957c7"></a>

### Different separator for databases in CSV-files

The class `RunDatabase` (and therefor also the utility
`pyFoamDumpRunDatabaseToCSV.py`) now write as a separator for data
from sub-tables a `//` instead of the space. This especially means
that scripts that rely on a data-item `foo` in `analyzed` might
break because this is now called `analyzed//foo` instead of
`analyzed foo`. On the other hand this makes the names more
consistent and easier to parse as `//` is the saperator for other
levels of dictionaries


<a id="org5c07ed4"></a>

### Change of independent variable name in sample data

Instead of `col0` this is now `coord`. This could cause problems
with scripts that use that column name in the resulting
`SpreadsheetData`-object


<a id="org2e141f0"></a>

## Bugfixes


<a id="org26d1068"></a>

### `pyFoamPackCase.py` does not handle symbolic links correctly

Symbolic links were copied as is and did not work correctly
afterwards. This is fixed. If the symbolic link is an absolute
path or points outside the case directory it is replaced with the
file it points to. Otherwise it is preserved as a symbolic link


<a id="org2295455"></a>

### `pyFoamPotentialRunner.py` not working with OpenFOAM 2.0 or newer

These versions require an entry `potentialFlow` in the
`fvSolution`-file instead of the old `SIMPLE`


<a id="orgf21f376"></a>

### `pyFoamListCase.py` fails with `controlDict` that use preprocessing

Fixed by first trying to read that with preprocessing. Without if
that fails


<a id="org332dd2d"></a>

### Cloning fails in symlink-mode if files are specified twice

Now using a `set` instead of a `list` makes sure that no file is
cloned twice


<a id="org374bf0a"></a>

## Utilities


<a id="org6616dc0"></a>

### `pyFoamPotentialRunner.py` now allows removing of `functions` and `libs`

The utility now allows removing these entries in case that they
don't work with `potentialFoam`


<a id="orgd2e4f21"></a>

### The Runner-utilities now have more options for clearing

Some of the options of `pyFoamClearCase.py` for clearing cases
(for instance specifying additional files) have been ported to the
`Runner`-utilities. Also is the `postProcessing`-directory
removed by default


<a id="org5d10e27"></a>

## Library


<a id="org3c842fb"></a>

### `SolutionDirectory` and `TimeDirectory` are more tolerant

If there are field files and their zipped counterpart than
instead of an error a warning **can** be given


<a id="orgbcb0b8e"></a>

### `ClusterJob` now handles template files

A new method `templateFile` gets the name of a file which is
constructed from a template of the same name plus the extension
`.template`


<a id="orgd06ae27"></a>

### Additional parameters in `ClusterJob`

The method `additionalParameters` can return a dictionary with
additional parameters


<a id="org97f03b9"></a>

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


<a id="org2d1acb2"></a>

### `SolverJob` now allows compression of output

The parameter `solverLogCompress` compresses the log-file while
writing it to disc. **Attention:** This may lead to corrupted
log-files if the run crashes


<a id="org4316534"></a>

### `PyFoamApplication`-class now allows quick access to data

The dictionary returned by `getData()` now allows access to all
the elements as attributes.


<a id="orgc823b76"></a>

## New features/Utilities


<a id="orgd2c79ea"></a>

### Post-run hook that sends mail at the end of run

The hook-module `MailToAddress` sends a mail at the end of a
run. Prerequisite is an SMTP-Server that doesn't need
authentication


<a id="org94c6af4"></a>

### New utility `pyFoamCompressCases.py`

This utility goes through cases and compresses single files. The
cases can be searched recursively to.

Purpose of this utility is to shrink cases where
`writeCompression` was not turned on during the run


<a id="orgf049384"></a>

### Paraview-module to read additional data

A new module `PyFoam.Paraview.Data` reads additional data usually
written by OpenFOAM. These are converted to `vtkArray` using the
following functions and can be used in `Programmable filters`:

-   **setSampleData:** reads the data from sampled sets
-   **setTimelineData:** reads data from a timeline directory
-   **setPlotData:** reads pickled plot data using `RedoPlot`


<a id="org4bd23a7"></a>

## Enhancements


<a id="orgb9a77d5"></a>

### `pyFoamRedoPlot.py` can plot in XKCD-mode

When used with the option `--implementation=xkcd` and version of
`matplotlib` that supports it is installed then plots are done in
the style of the webcomics <http://xkcd.com>


<a id="org8193e67"></a>

### `pyFoamListCases.py` now displays disk usage in human readable form

If the disk usage of the cases is calculated then it is displayed
in human readable form (as KB, MB, GB or TB) for sizes larger than
one Kilobyte


<a id="org15b307e"></a>

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


<a id="orga35d2d1"></a>

### `pyFoamFromTemplate.py` automatically chooses template and default values

If an output file `foo` is specified and no template then the
utility looks for a file `foo.template` as a template.

If a file `foo.defaults` is present then this file is read and
used as default parameter values. Other specifications override
these defaults


<a id="org5ba0a8d"></a>

### `pyFoamDumpRunDatabaseToCSV.py` can disable standard-fields

Additional option `--disable-run-data`


<a id="org8a184e8"></a>

### `pyFoamDumpRunDatabaseToCSV.py` prints `pandas`-object

With the `-pandas-print`-option a `DataFrame` is generated and
printed


<a id="org0e695b7"></a>

### Better debugging with `ipdb`

If the `ipdb`-package (basically `pdb` with `IPython`-additions)
is installed then it is used. This gives additions like
tab-completion


<a id="orgc69c7af"></a>

### Interactive shell after execution for utilities

The option `--interactive-after-execution` drops the user to an
interactive shell where the namespace can be inspected. If present
`IPython` will be used, otherwise the regular shell is used


<a id="org97e8b58"></a>

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


<a id="orgcfb41e3"></a>

### Utilities that read quantitative data write Excel files

The utilities `pyDumpRunDatabaseToCSV.py`,
`pyFoamTimelinePlot.py`, `pyFoamSamplePlot.py` and
`pyFoamRedoPlot.py` now have options to write Excel-files


<a id="orgccce9dc"></a>

### Specify additional settings for `GnuPlot` in `customRegexp`

If an item in `customRegexp` has an item `gnuplotCommands` then
it is assumed that this is a list of strings which are executed
before the first plotting. For instance

    gnuplotCommands (
       "set format y '%.2e'"
     );

changes the number format on the y-axis


<a id="org6b1f371"></a>

### More flexible data specification for `pyFoamSamplePlot.py`

Instead of determining the names of the fields and lines form the
filenames it is now also possible to specify them through options.

The option `--is-distribution` is a shorthand that sets these
options for distribution files


<a id="org093dcdc"></a>

### `pyFoamSamplePlot.py` now allows specification of x-range

The range of the x-axis of the plots can either be set by
automatically scaling to the domains of all the data sets with
`--scale-domain` or by specifying them with `--domain-minimum` or
`--domain-maximum`.

These domains are set for **all** plots


<a id="orgfa6191f"></a>

# Version 0.6.1 - 2013-05-24


<a id="org047f1d2"></a>

## Major changes


<a id="org8a808de"></a>

## Bugfixes


<a id="org7ead729"></a>

### Restoring of `controlDict` after `write`

When activating an on-demand write the `constrolDict` was not
restored because the output-line about the file being read was not
recognized (due to a change in the output in recent
OF-versions). Now a number of different formats is recognized


<a id="org16b0c9d"></a>

### Custom-plot type `slave` not working if no `master` defined

That plot-type needs a `master`. Fixed to fail if none is defined


<a id="orgda1d5fa"></a>

### `-list-only` did not correctly parse lists with a numeric prefix

This did affect all utilities that use that option and also calls
with `listOnly` to the library class


<a id="org9040c46"></a>

## Utilities


<a id="org6cf61f9"></a>

### `pyFoamBuildHelper.py` now allow more than one action

If multiple actions like `--update` and `--build` are specified
they are executed in a sensible order (update before build etc)


<a id="org94b6cee"></a>

### Utilities warn if OpenFOAM-version is unset

If the environment variable that determines the OpenFOAM-version
is unset a warning is issued by the utilities


<a id="org4f38a4f"></a>

### `pyFoamUpgradeDictionariesTo20.py` allows single files

If  single file is specified then the action to transform it has
can be specified


<a id="org15b862d"></a>

### `pyFoamUpgradeDictionariesTo20.py` transforms reaction-schemes

Now knows how to transform "old" reaction files (where the
`reactions`-entry was a list) to the new format (where it is a
dictionary). Only a limited number of reaction types is supported.


<a id="org7c5a8dd"></a>

### `pyFoamUpgradeDictionariesTo20.py` transforms thermophysical data

Now the old form of thermophysical data (lists) is transformed
into the new dictionary-form


<a id="org22d33ca"></a>

### `pyFoamCloneCase` now allows creating directory that symlinks to the original

Now with the option `--symlink-mode` instead of copying the
directories from the original new directories art created and
populated with symlinks to the files in the original. The depth
until which no symlinks to directories are created can be
specified. This allows the clone to share the configuration files
with the original


<a id="orgc7c0bd9"></a>

### `pyFoamClearCase.py` now removes `postProcessing` and allows removal of additional files

The directory `postProcessing` is now automatically removed (can be
switched off with `--keep-postprocessing`). Also with the
`--additional`-option patterns with additional files to remove
can be specified.


<a id="org3a89c3c"></a>

### Improvements to `pyFoamVersion.py`

-   Now reports the location of the `python`-executable
-   Reports locations of used libraries


<a id="orga1c4df8"></a>

### Additional files automatically cloned

The files `Allrun`, `Allclean` and `0.org` are automatically
added during cloning as these are often used by the standard-utilities


<a id="org25c4142"></a>

### `pyFoamDisplayBlockMesh.py` uses the same options for template format as `pyFoamFromTemplate.py`

This makes sure that templates are handled consistently and also
allows different delimiters in the `blockMeshDict.template`


<a id="org292b20d"></a>

## Library


<a id="orgafab9bf"></a>

### Improvements in syntax of `ParsedParameterFile`

-   Now the new relative scoping that was introduced in OF 2.2 is
    supported


<a id="org6425cc5"></a>

### `Utilities`-class now function to find files matching a pattern

Added a function `find` that approxiamtes the `find`-command


<a id="org28c32de"></a>

### VCS ignores more files

Some more patterns have been added that will be ignored in a
VSC-controlled case. All of them concerning files that PyFoam
creates during operation


<a id="org866a78b"></a>

## New features/Utilities


<a id="org2bd243c"></a>

### New Utility `pyFoamSymlinkToFile.py`

This utility replaces a symlink with a copy of the
file/directories it points to. To be used after a
`pyFoamCloneCase.py` in `--symlink-mode`


<a id="orga3c53cf"></a>

# Version 0.6.0 - 2013-03-14


<a id="orgb9163b0"></a>

## Major changes


<a id="org1bbc153"></a>

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


<a id="org91cf73a"></a>

### New ThirdParty-Libraries

-   **six:** Library that helps supporting Python 2 and Python 3 in
    the same source code. Currently version 1.2 from
    [<https://bitbucket.org/gutworth/six>] is used
-   **pyratemp:** Templating library to support the new templating
    format. Version 0.2.0 from
    [<http://www.simple-is-better.org/template/pyratemp.html>]
    is used


<a id="org36dde8f"></a>

### Porting to `Windows`

Port to allow running PyFoam on Windows was done by Bruno Santos
of blueCAPE (bruno.santos@bluecape.com.pt)

Patch was originally posted at
<http://sourceforge.net/apps/mantisbt/openfoam-extend/view.php?id=166>

**Note**: many of PyFoam's features are not yet fully functional on
Windows.


<a id="orgef37903"></a>

### Experimental port to `pypy`

Sources are executed in `pypy` but it seems there are problems
with `numpy` and also with code like `for l in open(f).readlines()`


<a id="orgc59f049"></a>

## Third-Party


<a id="org861d7ca"></a>

### Upgraded `ply` to 3.4

This brings virtually no changes. `README` with copyright
information has been added


<a id="org2d3cce8"></a>

## Infrastructure


<a id="org543198f"></a>

### Parameters can't be modified in `CTestRun` after initialization

This should help to avoid side-effects


<a id="org46ea309"></a>

### Treat timeouts in the `MetaServer` right

Due to a previous workaround timeouts when collecting information
about new machines was not treated correctly


<a id="org97e4b2d"></a>

### Add `execute`-method to `ClusterJob`

This allows the execution of a shell-script in the directory of
the case


<a id="org1dd4ced"></a>

### Add possibility to run specific modules before or after the solver

These modules are found in `PyFoam.Infrastructure.RunHooks`. Two
concrete implementations:

-   **`PrintMessageHook`:** to print a text to the terminal
-   **`SendToWebservice`:** encode an URL and send it to a webservice
    (example for `pushover.net` added)

Hooks are automatically instantiated from the configuration data
(examples are hardcoded))


<a id="orga0be15d"></a>

### Parameters added to the info about the run

The Runner-classes now have a parameter `parameters`. This data
(usually it would be a dictionary) is added verbatim to the run
info.

Most runner applications now have the possibility to add this
info.

Purpose of this facility is to identify different runs in the
database better.


<a id="org2f9966c"></a>

### Parameter handling in `ClusterJob` extended

Parameter values are now handed to the actual job. Also a
dictionary with parameters can be handed to the constructor and
will be used in the relevant callbacks


<a id="org887b902"></a>

### Run data written alongside `PickledPlots`

During the run whenever the `PickledPlots`-file is written a file
`pickledUnfinishedData` gets written. This has the current solver
data and is similar to `pickledData`.

Also a file `pickledStartData` gets written that has the data that
is available at the start of the run.


<a id="org23af3d7"></a>

### `BasicRunner` collects error and warning texts

The runner collects

-   at every warning the next 20 lines of the output until a total
    of 500 lines is reached (this avoids filling disk and memory if
    the solver produces too many warnings)
-   All output from an error message until the end

And stores them in the application data


<a id="orga721d40"></a>

## Library


<a id="org105653d"></a>

### `TemplateFile` now uses `pyratemp`

The class `TempalteFile` now uses an enhanced templating
engine. The  old implementation is in the class
`TemplateFileOldFormat`


<a id="org17cd919"></a>

### Clearer error message in Application-classes

If used as classes (not as utilities) these classes print the
class name instead of the calling utilities name


<a id="orgbbbfe4e"></a>

### Output is only colored if it goes to the terminal

Error and warning messages don't decorate the output if it goes to
files or other non-terminal streams


<a id="org5f04f7d"></a>

### `error`-method of application classes now raises an exception

An exception is now raised by `self.error()`. This makes it easier
to handle such errors if the application class is used. The
exception is passed up until there is a "real" application


<a id="orgf3f5135"></a>

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


<a id="org1f496a6"></a>

### `LabledReSTTable` for more flexible table generation

New class in the `RestructuredTextHelper` allows more flexible
generation of tables. Items are added with `column` and `row` and
if these don't exist in the first row/column the table is extended
appropriately


<a id="org0d1962b"></a>

### Plotting classes now allow setting of `xlabel`

This is implemented for `Gnuplot` and `Matplotlib`. Default for
the label on the x-Axis is now "Time [s]"


<a id="org118d859"></a>

## Utilities


<a id="org5d56a27"></a>

### `pyFoamFromTemplate.py` with new templating engine

The utility can now use the pyratemp-templating engine which
allows templates with loops, conditions and other  fancy stuff


<a id="orge580fcc"></a>

### `pyFoamSamplePlot.py` allows using the reference data as basis for comparison

Instead of using the x-values from the original data the y-values
of the reference data can be used for comparing (with the
`--use-reference`-option)

Same for `pyFoamTimelimePlot.py`


<a id="orga158ced"></a>

### Scaling and offsets are now used in plots of `pyFoamSamplePlot.py`

If scales not equal to \(1\) and offsets not equal to \(0\) are
specified they are used in the `gnuplot`-output


<a id="org2a801c0"></a>

### `pyFoamPrintData2DStatistics.py` prints relative average error

With the `--relative-average-error`-option


<a id="org0f26174"></a>

### Enhancements to `pyFoamVersion.py`

-   More tolerant if no library was found
-   Reports the location of the PyFoam-Library
-   Checks whether utility version is consistent the library found


<a id="org61dc57d"></a>

### `pyFoamRunner.py` allows hooks

Hooks can be added at the start and the end of a run


<a id="org4157937"></a>

### `pyFoamRedoPlots.py` supports range for plots

Added `-end` and `-start`-option to select a range that should be
plotted.

Currently not working with the Matplotlib-implementation (only gnuplot)


<a id="orge3c4f64"></a>

### `pyFoamDisplayBlockMesh.py` no supports templates

If a file with values is specified then the utility assumes you're
editing a template file and will evaluate it before displaying it


<a id="orgbda38e3"></a>

### `pyFoamCaseReport.py` is tolerant towards binary files

New switch that makes the parser treat files that are declared
`binary` in the header as if they were `ascii`


<a id="org52e66f8"></a>

### `pyFoamSamplePlot.py` and `pyFoamTimelinePlot.py` raise error if no plots are generated

This makes it easier to catch faulty specifications (or empty
timeline-files)


<a id="org1bde25d"></a>

### `pyFoamSurfacePlot.py` can wait for a key

An option `--wait` has been added that makes the utility wait
before displaying the next picture


<a id="org07e2d9d"></a>

### `pyFoamEchoDictionary.py` is more flexible with binary files

Switch allows forcing it to read a binary File as an ASCII


<a id="org63c1fcd"></a>

### All utilities now have a switch that starts the debugger even with syntax-errors

Previously the option `--interactive-debug` only started the
debugger if the error was **no** syntax error. This is still the
default behavior, but can be overruled


<a id="org390143b"></a>

### Utilities now can be killed with `USR1` and will give a traceback

The option `--catch-USR1-signal` now installs a signal-handler
that prints a traceback and finishes the run. If the interactive
debugger is enabled then it goes to the debugger-shell.

Option `--keyboard-interrupt-trace` triggers the same behaviour
for keyboard interrupts with `<Ctrl>-C`


<a id="org5d8f17d"></a>

### Switch to switch on **all** debug options

For the purpose of developing a switch `--i-am-a-developer` has
been added.


<a id="org2e75473"></a>

### Plotting utilities now allow specification of x-Axis label

With the option `xlabel` in the `customRegexp`-file the label on
the x-axis of the plot can be changed. Setting `ylabel` and
`y2label` (for the secondary axis) was already possible


<a id="org4de27a1"></a>

### Metrics and compare for `pyFoamTimelinePlot.py` and `pyFoamSamplePlot.py` support time ranges

Now the options `--min-time` and `--max-time` are supported by
`--metrics` and `--compare`


<a id="orgc6a43ba"></a>

### `pyFoamDisplayBlockMesh.py` allows graphical selection of blocks and patches

New addition by Marc Immer allows the graphical selection of
blocks and patches and adds them to the `blockMeshDict`


<a id="orgc59ffb0"></a>

### `pyFoamCloneCase.py` and `pyFoamPackCase.py` accept additional parameters

The file `LocalConfigPyFoam` is read by these utilities and if
there is a parameter `addItem` in the section `Cloning` defined
then these files are cloned/packed automatically (no user
specification required)


<a id="orge36404b"></a>

### `pyFoamListCases.py` now calculates estimated end-times

Additional option to print the estimated end times. These can be
wrong if the case did not start from the `startTime` in the
`controlDict`.

Also now allows printing the end and the start-time according to
the `controlDict`


<a id="org39bd427"></a>

## New features


<a id="org5d62f6a"></a>

### Different "phases" for multi-region solvers

Plots of type `phase` in `customRegexp` don't actually plot
anything. The set a phase-name that is used for subsequent values
(for instance to distinguish the different residuals)


<a id="orgcb5925f"></a>

### `pyFoamChangeBoundaryType.py` allows selection of region and time

Options `--region` and `--time-directory` added that allow
selecting different `boundary`-files


<a id="orga129994"></a>

### New class for storing case data in a sqlite-database and associated utilities

The class `RunDatabase` stores the data from runs. Utility
`pyFoamAddCaseDataToDatabase.py` is one way to populate the
database. `pyFoamDumpRunDatabaseToCSV.py` allows dumping that
data to a file for further processing (in a spreadsheet for
instance)

Database can also be populated using a special post-run hook


<a id="orgefe66fe"></a>

## Bugfixes


<a id="orged4cff6"></a>

### Only binary packages of 1.x were found

Pattern had to start with 1 (now every digit is possible))


<a id="orgaefb6e8"></a>

### Option group *Regular expressions* was listed twice

No harm done. But fixed


<a id="org7dcef9e"></a>

### `--clear`-option for `pyFoamDecompose.py` not working

Reason was that `rmtree` does not allow wildcards. Fixed


<a id="orgb9c0183"></a>

### `pyFoamDisplayBlockmesh.py` not working with variable substitution

The `DictRedirect` would not convert to float. Fixed. Although it
might happen again for other data types


<a id="orgd460fcf"></a>

### Option `--function-object-data` of `pyFoamClearCase.py` not working with directories

The option was only implemented for the list-form of the
`functions` entry in `controlDict`

Now fixed to also work with the dictionary-form


<a id="org9263fec"></a>

### `nonuniform` of length 0 not correctly printed

Seems like the length was interpreted as the name of the
list. Fixed


<a id="org4488a30"></a>

### Building of pseudocases with `pyFoamRunner.py` broken

Only worked if no region was specified (= not at all). Fixed


<a id="orga41eb28"></a>

### `pyFoamRedoPlot.py` did not correctly honor `--end` and `--start`

Plots were over the whole data range. This is now fix (also the
issue that `--end` alone did not work)


<a id="org9d4fc4e"></a>

### `WriteParameterFile` does not preserve the order of additions

Contents was "only" set as a dictionary which does not preserve
the order in which entries are added. Replaced with a `DictProxy`


<a id="org2351cfc"></a>

### Wrong number of arguments when using `TimelinePlot` in `positions`-mode

Problem that was introduced by changes in the `fields`-mode


<a id="org74474ea"></a>

### `ClusterJob` uses only `metis` for decomposition

For OpenFOAM-versions 1.6 and higher the automatic decomposition
used is now `scotch`


<a id="org605a17b"></a>

### `pyFoamSamplePlot.py` and `pyFoamTimelinePlot.py` produced no pictures for regions

As regions have their own subdirectories the `/` from the
directory name was inserted into the filename and if the
subdirectory did not exist `gnuplot` did not create the picture


<a id="org07adf67"></a>

### Barplots in `pyFoamTimelinePlot.py` not working if value is a vector

The base class didn't correctly handle the `(` and `)`. Fixed


<a id="orge0d5389"></a>

### Mysterious deadlocks while plotting long logfiles

The problem was that during splitting the timeline data an exception was
raised. This exception was caught by another part of PyFoam. This
left a lock on the data structure locked and the next access to
the structure was held indefinitely. Fixed


<a id="org499bd88"></a>

### Scanning linear expressions form the block coupled solver failed

As there is a tuple of residuals the scanner did not analyze the
output of the output of the block-coupled solver from `1.6-ext`
correctly. This is now treated as a special case and each residual
is plotted separately (distinguished by a `[x]` with `x` being the
number of the component)


<a id="org32980a2"></a>

### `#include` not correctly working with macros in the included file

Macros `$var` were not correctly expanded. Fixed


<a id="orgc47ca3e"></a>

### Macros not correctly expanded to strings

When being expanded to string form macros were not correctly
expanded


<a id="org7b563a7"></a>

### `pyFoamPackCase.py` in the working directory produces 'invisible' tar

If the utility was used in the form

    pyFoamPackCase.py .

then an 'invisible' tar `..tgz` was produced. Fixed


<a id="org87542d3"></a>

### String at the end of a linear solver output makes parsing fail

Reported in
[<http://www.cfd-online.com/Forums/openfoam-solving/112278-pyfoam-struggles-adopted-solver-post403990.html>]
the string is assumed to be part of the iteration number. Fixed


<a id="org06e0333"></a>

### Paraview utilities not working with higher Paraview versions

At least for PV 3.14 and 3.98 the way the version number is
determined has changed and the PV-utilities failed. This has been
fixed but is untested with old versions


<a id="org9257528"></a>

### Camera settings not honored with `pyFoamPVSnapshot.py`

For the first rendered view Paraview automatically resets the
camera. This has now been switched off (so the snapshot is
rendered correctly)


<a id="org0777681"></a>

# Version 0.5.7 - 2012-04-13


<a id="orgf5422e4"></a>

## Parser improvements

-   Problem with nested comments
-   Parse code streams
-   Preserving of comments can be switched off
-   Ignore extra semicolons
-   Allows parsing lists of length 3 and 9 as lists and not as
    vectors and tensors
-   "lookup redirection" in OF-dictionaries now works


<a id="org611ad70"></a>

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


<a id="org8d746f6"></a>

## New Utilities

-   pyFoamEchoPickledApplicationData to output pickled data
-   pyFoamPrintData2DStatistics.py to output data from comparisons
-   pyFoamBuildHelper.py to build project and its prerequisites (work
    in progress)
-   pyFoamCreateModuleFile.py to create files for
    <http://modules.sourceforge.net/> (by Martin Beaudoin)
-   pyFoamSTLUtility.py to join STL-files


<a id="org60bf06d"></a>

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


<a id="org27c589a"></a>

## Removed utilities

-   pyFoamAPoMaFoX.py
-   pyFoamPlotResiduals.py


<a id="org838765e"></a>

## Thirdparty

-   Got rid of Numeric-support in Gnuplot-library


<a id="org42ae195"></a>

## Other

-   script to generate man-pages for the utilities
-   Paraview3-example probeDisplay.py now renamed to
    probeAndSetDisplay.py and reads sampledSets from controlDict and
    sampleDict


<a id="orgc8efab8"></a>

# Older Versions

The changes for older versions can be found on
[the Wiki-page](http://openfoamwiki.net/index.php/Contrib_PyFoam#History)
