# Table of Contents

1.  [Version 0.6.12 - Not releases](#orgce2577d)
    1.  [New features/utilities](#org2085bc5)
    2.  [Enhancements to the utilities](#org1c6a97d)
        1.  [Paraview-utilities now work in Paraviews that use Python 3](#org2da9c6e)
        2.  [`pyFoamPrepareCase.py` allows automatically zipping template results](#org1ceb094)
        3.  [`customRegexp` has a type `mark` to add marks to the plots](#orgae12578)
        4.  [Plotting utilities now plot progress of `snappyHexMesh`](#orgbe95a54)
        5.  [Plotting utilities now plot progress of `foamyHexMesh`](#org1c2b928)
        6.  [Plotting utilities now print available values of `type`](#org892ffa0)
        7.  [Missing attributes in `customRegexp`-specifications now give better error messages](#org1712edc)
        8.  [Option `--quiet-plot` for plotting utilities swallows output of the plotting program](#org4d8ee50)
        9.  [Colored markers in `pyFoamPlotWatcher` for logfiles from restarts](#orga56de1d)
        10. [`writeFiles` in a `customRegexp`-entry writes scanned output to file](#org51b9b5e)
        11. [Modifying splitting behavior for plot data](#org8efebcb)
    3.  [Enhancements to the library](#orgf0f734c)
        1.  [Paraview-classes now work with Python 3](#org349ee4f)
        2.  [`TemplateFile` now can write the result as zipped](#orgce668d0)
        3.  [Mechanism to have `alternateTime` in single `customRegexp`](#orga95f690)
        4.  [`quiet`-option added to plotting implementations](#org2153c93)
        5.  [The `[]`-operator of the `PyFoamDataFrame` is now more flexible](#orgc509d10)
        6.  [Each run started by `BasicRunner` has a unique ID](#orgf0042a2)
        7.  [`pyFoamAddCaseDataToDatabase.py` allows updating data](#org2f79c6a)
        8.  [`RunDatabase` gets method `modify`](#orgf82621d)
    4.  [Bug fixes](#org0412f84)
        1.  [`auto` for the solver does not work with compressed `controlDict`](#orga6b2069)
        2.  [`FileBasisBackup` now works with zipped file](#orgf5f1318)
        3.  [Case with zipped `controlDict` not recognized as a valid case](#org716eca8)
        4.  [`pyFoamDisplayBlockMesh.py` not working with newer VTK-versions](#org10fc8df)
    5.  [Incompatibilities](#orgb61d2c6)
        1.  [`TemplateFile` writes to zipped file if it exists](#org6ef3f5e)
        2.  [`pyFoamDisplayBlockMesh.py` not working with Python 2.x anymore](#orgac8d0dd)
        3.  [Constructor of `PyFoamDataFrame` is more restrictive](#orgbe36102)
        4.  [`[]`-operator of `PyFoamDataFrame` returns a `PyFoamDataFrame`](#org5e11a20)
        5.  [`RunDatabase` fails if the same unique ID is inserted again](#orgc0def18)
    6.  [Code structure](#orgf9da19b)
    7.  [Infrastructure](#org6554e73)
    8.  [ThirdParty](#orgbe3b04e)
        1.  [Modification to `Gnuplot`-library](#orge791c7e)
2.  [Version 0.6.11 - 2019-10-31](#orgb5b93b0)
    1.  [Code structure](#orgc73e2e2)
        1.  [Moved library into `src`-directory](#orgb0ddae6)
        2.  [Added Developer notes](#org10d1ee4)
    2.  [Incompatibilities](#org7ef15da)
        1.  [Behaviour reading `customRegexp`](#org81fe655)
        2.  [Gnuplot does not use `FIFO` as the default anymore](#orgb5d3a71)
    3.  [Enhancements to Utilities](#org1004c90)
        1.  [Replay data-files in `customRegexp`](#org6af76a6)
        2.  [Macro expansion in `customRegexp`](#org963967a)
        3.  [`progress` entry in `customRegexp` now allows `format` strings](#org021e2c4)
        4.  [`pyFoamRedoPlot.py` allows passing terminal options](#orga7412d8)
        5.  [`pyFoamPlotWatcher.py` stops scanning the file is `--end` was specified](#orgde667b6)
        6.  [Hardcopies of custom plots have more descriptive names](#org2a2c4a6)
        7.  [Plotting in Gnuplot can switch between using FIFO or regular files](#org93ddb00)
        8.  [`pyFoamPrepareCase.py` calls script after copying initial conditions](#org943ce13)
        9.  [`--stop-after-template` and `--keep-zero` improve control in `pyFoamPrepareCaseParameters.py`](#orgc050efa)
        10. [`pyFoamPVSnapshot.py` allows specification of the image quality](#orgbc19bf6)
        11. [Image size specification for `pyFoamPVSnapshot.py`](#org7eec9a6)
        12. [Setting separation of views and background transparency in `pyFoamPVSnapshot.py`](#org318545e)
        13. [`pyFoamPVLoadState.py` automatically uses decomposed or reconstructed data](#org9cb2ac9)
        14. [Change directory for `pyFoamPrepareCase.py` to target](#org4c4abe5)
        15. [`pyFoamPrepareCase.py` can create an example case](#org2c8be6c)
        16. [`pyFoamPrepareCase` prints derived values](#org4598ebd)
        17. [`pyFoamPVSnapshot` allows specifying different colors for different views](#org149e1f2)
        18. [`alternateLogscale` for custom plots](#orgfef4b89)
        19. [`pyFoamBinarySize.py` now calculates documentation size as well](#orga604b1a)
        20. [`pyFoamCompareDictionary.py` allows specification of significant digits](#orga6a7aa9)
    4.  [Enhancements to the Library](#orgca806d8)
        1.  [`progress`-data is automatically converted to `float`](#orgad9d42d)
        2.  [Additional directories in `FoamInformation`](#orgf53e21a)
        3.  [`BoolProxy` now works correctly with `!=`](#orgf7486d5)
    5.  [Bug fixes](#org9216e75)
        1.  [With dynamic plots names with `_slave` are problematic](#orge492a20)
        2.  [New-style dimensioned scalars fail](#org5a66f95)
        3.  [`pyFoamPVSnapshot.py` not working with Paraview 5.6](#orgee62991)
        4.  [`customRegexp` farthes away was used](#org05595b8)
        5.  [`ParameterFile`-class got confused by commented lines](#orgc0ee3b6)
        6.  [`pyFoamBinarySize.py` did not count files in `build`](#org88c1615)
        7.  [Binary files with `ParsedParameterFile` not working in Python 3](#org00bedbf)
        8.  [Improved handling of binary files in Python 2 and 3](#org49168cf)
3.  [Version 0.6.10 - 2018-08-12](#orgcac849c)
    1.  [Incompatibilities](#orgaf25f86)
        1.  [`pyFoamPrepareCase.py` does not execute decomposition scripts for single processor cases](#orgd16da20)
    2.  [New feature/utilities](#org0bf70a9)
        1.  [Utility `pyFoamFunkyDoCalc.py` to compare data from `funkyDoCalc`](#org7d0c5b1)
    3.  [Enhancements to Utilities](#org10abf30)
        1.  [Recursive searching for `pyFoamListCases.py`](#org83008dd)
        2.  [Look for `customRegexp` in parent directories](#org529ee7e)
        3.  [`pyFoamPrepareCase.py` does not execute decomposition scripts for single processor cases](#orge011495)
        4.  [`pyFoamPrepareCase.py` checks for proper decomposition](#orgbea19c0)
        5.  [`pyFoamPlotWatcher.py` automatically uses newest logfile](#org79d1077)
    4.  [Enhancements to the Library](#org7f3090d)
        1.  [`FoamFileGenerator` handles `OrderedDict`](#org7cbad52)
        2.  [`#sinclude` handled as an alias to `#includeIfPresent`](#orgbdf3ca6)
        3.  [OpenFOAM 6 correctly recognized](#org156f21b)
    5.  [Bug fixes](#org8a56cfb)
        1.  [`pyFoamPrepareCase.py` did not remove `processor`-directories](#orga1d93c6)
    6.  [Infrastructure](#orge69f9e5)
        1.  [Single digit version numbers supported](#orga3c306e)
4.  [Version 0.6.9 - 2018-02-25](#org8e914d1)
    1.  [Major changes](#org396fe46)
        1.  [Add `curses`-output to Utilities](#org670cbdd)
    2.  [Incompatibilities](#org982040a)
        1.  [`pyFoamPrepareCase.py` creates `.foam`-file](#orgd038931)
        2.  [Hardcoded Foam-Version upgraded to `4.0`](#org32c902d)
        3.  [`none` no longer parsed as an equivalent for `false`](#org6ae5028)
    3.  [New features/utilities](#org0740d03)
        1.  [`pyFoamJoinTimelines.py` to join Timelines from restarts](#orgbc5d39b)
        2.  [`pyFoamRestartRunner.py` to automatically restart runs](#orgc293c1d)
    4.  [Enhancements to Utilities](#orgf3ebd5d)
        1.  [Special snapshot utilities to use MESA](#org169f11e)
        2.  [Automated plotting of film properties](#org2a5ba11)
        3.  [`pyFoamClearCase.py` automatically executes an existing `Allclean`](#orgecc8d98)
        4.  [`pyFoamPrepareCase.py` executes tutorial scripts if available](#orga3fa5ce)
        5.  [Script for clearing in `pyFoamPrepareCase.py`](#orgb6ecbc6)
        6.  [`pyFoamPlotWatcher.py` now can handle multiple files](#org37f668d)
        7.  [`pyFoamPrepareCase.py` now allows separate decomposition scripts](#orgd53256f)
        8.  [Runner-utilities now create seperate logfiles on restart](#orgdd7349f)
        9.  [`pyFoamPVSnapshot.py` improves rewriting of state-files](#org6aca9d5)
        10. [`pyFoamPackCase.py` adds parallel data](#org873bfd5)
        11. [`--replacement`-option in `pyFoamPVSnapshot.py` supports Foam-format](#orgba452d3)
        12. [`pyFoamPVSnapshot.py` improved error messages with problems in replacement](#orgb4af9e6)
        13. [`customRegexp` now searched in parent directories](#org6dda1f5)
    5.  [Enhancements to the Library](#orgd8768ec)
        1.  [`Paraview.StateFile` extended](#orgf9e776a)
        2.  [`BasicRunner` now checks for regular End](#orgfd92ed4)
    6.  [Bug fixes](#org27d0a17)
        1.  [`pyFoamPrepareCaser.py` ran out of memory for large script outputs](#orgdce2e95)
        2.  [No Courant number plottet if `WM_PROJECT_VERSION` is unset](#orgc972d07)
        3.  [Rescale does not work for streamlines in `pyFoamPVSnapshot.py`](#org9128126)
        4.  [Server not correctly running on Python 2.7 with `socketserver`](#orgaff12ad)
5.  [Version 0.6.8.1 - 2017-08-03](#orgdab6d07)
    1.  [Bug fixes](#org3b02c6d)
        1.  [Fork not correctly detected for `v1706`](#org1496a05)
6.  [Version 0.6.8 - 2017-07-06](#org37140b5)
    1.  [Major changes](#org61bcc8d)
        1.  [`pyFoamNet`-utilities now work without a Meta-Server](#orgd15a4cc)
    2.  [New features/utilities](#orgbf78a98)
        1.  [Added module `PyFoam.Infrastructure.Authentication`](#org8d35ab8)
    3.  [Enhancements to Utilities](#org2f3f2d4)
        1.  [`pyFoamClearCase.py` now has `-dry-run` option](#org9cffeed)
        2.  [New option `--keep-time` for `pyFoamClearCase.py`](#org5ac307a)
        3.  [`pyFoamNetList.py` no longer needs a meta-server to work](#org69aec67)
    4.  [Enhancements to the Library](#orgf75e30c)
        1.  [Better calculation of used memory in runs](#org32f6b84)
        2.  [Pre and post-hooks are now also searched in `PyFoam.Site`](#org2da406b)
        3.  [Adapted to correctly detect `OpenFOAM+ v1706`](#org558753a)
    5.  [Infrastructure](#org3660e0d)
        1.  [The `Runner`-utilities now register as `ZeroConf`-services](#orgfb1085a)
    6.  [Bug fixes](#org3d5165f)
        1.  [`--keep-interval` in `pyFoamClearCase.py` not working for parallel-cases](#org4ad67d9)
7.  [Version 0.6.7 - 2017-06-04](#orga6a6310)
    1.  [Requirements](#org4d933d1)
        1.  [Now at least Python 2.6 required](#org1c08837)
    2.  [Incompatibilities](#orgdb7dbaa)
        1.  [Names of files generated by `pyFoamPVSnapshot.py` differ](#org69f0e3b)
    3.  [New features/utilities](#org2f1b8ec)
        1.  [Utility `pyFoamListProfilingInfo.py` to print profiling data](#orgae93ae4)
        2.  [Utility `pyFoamBlockMeshConverter.py` to convert a 2D-mesh to 3D](#org409dc21)
    4.  [Enhancements to Utilities](#orgaeff21a)
        1.  [`customRegexp` now can scan for texts](#org393a8be)
        2.  [Lines in `PyFoamHistory` escaped](#orgca71f4e)
        3.  [`--values-string` of `pyFoamPrepareCase.py` now accepts OpenFOAM-format](#org93e03ce)
        4.  [`pyFoamRunner.py` and `pyFoamPlotRunner.py` allow automatic selection of solver](#org2ab2b5d)
        5.  [Calculations (data transformations) in `customRegexp`](#orgd0aadf8)
        6.  [Multi-part `idNr` for `dynamic` in `customRegexp`](#org9e0328b)
        7.  [`pyFoamListCases.py` detects dead runs](#orgb4658c4)
        8.  [Improved time-handling of `pyFoamPVSnapshot.py`](#org37604ef)
        9.  [Default plots can be set in configuration](#org7ac0172)
        10. [`derivedParameters.py`-script called from `pyFoamPrepareCase.py` allows error reporting](#org8c8974b)
    5.  [Enhancements to the Library](#orga3c0c2d)
        1.  [Detection of new versions of OpenFOAM-foundation and OpenFOAM+](#org45c0e41)
        2.  [`SpreadsheetData` now handles string data](#org1064347)
        3.  [`TimelineData` tolerates string values](#orge5ac561)
        4.  [`()` operator of `SpreadsheetData` works without name](#orge8088c5)
        5.  [New function `setCurrentTimeline` in `PyFoam.Paraview.Data` to get data at time](#org8e3ec8a)
        6.  [User-specific temporary directory](#org4813203)
        7.  [`Gnuplot`-plots now get better titles](#org088abdd)
        8.  [`ParsedParameterFile` now supports `#includeFunc`](#org5f4301c)
        9.  [New utility function `findFileInDir`](#org3342740)
        10. [`humandReadableDuration` added to `PyFoam.Basics.Utilities`](#orgd58f2cf)
    6.  [Infrastructure](#orge74212d)
        1.  [`pyFoamVersion.py` now reports the versions of the `ThirdParty`-packages](#orga488621)
    7.  [Bug Fixes](#org7604823)
        1.  [Application classes fail in Paraview](#orgc6384a8)
        2.  [Scripts in `pyFoamPrepareCaseParameters.sh` not working on Mac OS X](#orgb486f56)
        3.  [Processor-directories unsorted in `SolutionDirectory`](#orga3200d5)
        4.  [Deleting failed if a file did't exist](#org55c7bc6)
        5.  [Missing files in `RegionCases`](#org928e1f0)
        6.  [Wrong `solver` in `pyFoamListCase.py`](#org03b566e)
    8.  [ThirdParty](#org3014b89)
        1.  [Updated `tqdm` to version 4.8.4](#org79b3864)
        2.  [Updated `PLY` to version 3.9](#orgc5d2823)
        3.  [Updated `six` to 1.10.0](#org0dceff2)
8.  [Version 0.6.6 - 2016-07-15](#orgcb780e2)
    1.  [Incompatibilities](#org44cdd37)
        1.  [Changes in `IPython`-notebooks 3.0](#org22ccbf9)
    2.  [Enhancements to Utilities](#org11b4edc)
        1.  [`pyFoamPrepareCase.py` executes `setFields` if appropriate](#org764b137)
        2.  [Plotting utilities now automatically add custom plots depending on the solver name](#org248c695)
        3.  [`alternateAxis`-entries now can be regular expressions](#org12dbede)
        4.  [Plotting utilities now allow choice of Gnuplot terminal](#org5bfe67d)
        5.  [Plotting utilities now sort legend by name](#org89c0558)
        6.  [`pyFoamExecute.py` allows calling with debugger](#org609fa23)
        7.  [`pyFoamPrepareCase.py` fails if execution of a script fails](#org01dd61a)
        8.  [`--hardcopy` in plotting library now allows modification of `gnuplot`-terminals](#orgc564ba7)
        9.  [`pyFoamPrepareCase.py` writes state information about what it is currently doing](#org61c6273)
        10. [`pyFoamBinarySize.py` can handle new location of binaries in OpenFOAM 3.0](#org7dd55ce)
        11. [`Runner`-utilites now can signal on `blink(1)`-devices](#orgf50c4c8)
        12. [`pyFoamExecute.py` can flash a `blink(1)`](#orge2a66b6)
        13. [`pyFoamDecompose.py` allows using a template file](#org0539c2a)
        14. [`pyFoamTimelinePlot.py` now handles new format of probe files](#org01eae2e)
        15. [`ReST`-report of `pyFoamPrepareCase.py` now reports derived parameters](#org3bdf420)
        16. [`pyFoamPrepareCase` can now ignore directories](#org2f1b2f4)
        17. [`pyFoamConvertToCSV.py` allows adding formulas to XLSX-files](#org78f356c)
        18. [`pyFoamListCases.py` now displays mercurial info](#orgb8317fd)
        19. [Progress bar added to utilities with long run-time](#orgb7b91c7)
        20. [Utilities that clear data can now report what is cleared](#org6e04b05)
        21. [`pyFoamConvertToCSV.py` now allows manipulating the input](#org2a11088)
    3.  [Enhancements to the Library](#orga337349)
        1.  [Detection of `OpenFOAM-dev`](#orgf8c597e)
        2.  [Add `OpenFOAM+` as a fork](#org539a5c6)
        3.  [Accept new convention for location of `blockMeshDict`](#org903eefa)
        4.  [Handling of complex data by `Configuration`](#org2a25561)
        5.  [`Configuration` has method `getArch` for architecture dependent settings](#org3e7f5c4)
        6.  [`execute`-method from `PyFoam.Basics.Utilities` returns status-code](#orgbfc9087)
        7.  [`BasicRunner` now supports more ways of stopping runs](#orgcccab0b)
        8.  [Added `Blink1` class to support `blink(1)` devices](#org52e5731)
        9.  [`ParsedParameterFiles` now supports `includeEtc`](#org66d69be)
        10. [Parses uniform fields correctly](#orgffa6268)
        11. [`toNumpy`-method added to `Unparsed` and `Field`](#org34d98bb)
        12. [Added module `PyFoam.RunDictionary.LagrangianPatchData` to read data from patch function object](#org01b6800)
        13. [Added module `PyFoam.RunDictionary.LagrangianCloudData` to read cloud data](#org93b7ceb)
        14. [Method `code` added to =RestructuredTextHelper](#org88d8d6d)
        15. [`ParsedParameterFile` now parses new dimension format correctly](#orgd5e047e)
        16. [`ParsedParameterFiel` now parses uniform fields correctly](#org459b2c6)
    4.  [Infrastructure](#org3a35dae)
        1.  [Change of documentation from `epydoc` to `sphinx`](#orga5db4f4)
        2.  [Adaptions to the unittests](#org3ff2684)
    5.  [Bug fixes](#orgff9a6a7)
        1.  [Wrong format of `ExecutionTime` breaks plotting utilities](#orgb28a347)
        2.  [`phases` not working with dynamic plots](#org12b21e6)
        3.  [Phase name added to function object output](#orge3fca8c)
        4.  [One region mesh too many in utilities that change the boundary](#org5740171)
        5.  [`pyFoamClearCase.py` fails on write-protected case](#org68c297f)
        6.  [Copying of directories in `pyFoamPrepareCase.py` confused by zipped files](#org0349cbc)
        7.  [Wrong times for multi-view layouts in `pyFoamPVSnapshots.py`](#org8fc760c)
        8.  [First timestep not plotted (and not stored)](#org1e979be)
        9.  [`DYLD_LIBRARY_PATH` not passed on *Mac OS X 10.11*](#org6e33e96)
        10. [Newer versions of `pandas` broke the writing of excel files with `pyFoamConvertToCSV.py`](#orgdd1eded)
        11. [Capital `E` in exponential notation for floats breaks parser](#org516ada1)
        12. [`Runner`-utilities clear processor directories if first time in parallel data differs](#org8813466)
        13. [Utilities `pvpython` not working when installed through `distutils`](#orga37fe0d)
    6.  [ThirdParty](#org92e51c1)
        1.  [Added `tqdm` for progress bars](#orge68f812)
9.  [Version 0.6.5 - 2015-06-01](#orgb0bb6e4)
    1.  [Major changes](#org2a64ea3)
        1.  [PyFoam now on *Python Package Index*](#orgbcba398)
    2.  [Incompatibilities](#org06c2db4)
        1.  [`ArchiveDir` in `SolutionDirectory` discouraged](#org605d6fc)
        2.  [Pickled data files now written as binary](#orgcfcc270)
        3.  [The `PlotRunner` and `PlotWatcher` now don't strip spaces](#orgda5389e)
        4.  [Different column names in `pyFoamConvertToCSV.py`](#org6272a7b)
        5.  [`pyFoamChangeBoundaryName.py` and `pyFoamChangeBoundaryType.py` automatically modify `processorX`](#orgdac5f04)
    3.  [Bugfixes](#org0a7bda4)
        1.  [Arbitrary commands in `TemplateFile` passed to file](#org58d0b2b)
        2.  [Pickled files not opened in binary mode](#org509b7e4)
        3.  [Additional fixes for Python 3](#org4aa177a)
        4.  [`ParsedParameterFile` fails if "complete" dictionary is `#include` ed](#org8c8520c)
        5.  [`ParsedParameterFile` fails if there is more info after `#include`](#orga7dd83b)
        6.  [`pyFoamDisplayBlockMesh.py` not working with VTK 6](#orgfa9e172)
        7.  [`pyFoamCreateModuleFile.py` failed with environment variables containing `=`](#org2b160ee)
        8.  [Fix import in `GeneralVCSInterface`](#org9ed8fd5)
        9.  [Support of old format in `ParsedBlockMeshDict` broken](#org0217e8b)
        10. [`TemplateFile` not correctly working in Python 3](#org008ffc3)
        11. [Certain things not done by `pyFoamPrepareCase` in `--quiet` was set](#org78a1e62)
        12. [Annoying warning at the start of the run](#org4f5ed43)
        13. [Redirected values](#org13ba9e0)
        14. [Behavior of Template-engine not consistent in Python3 and Python2](#org1fbe617)
        15. [Braces, brackets, parentheses in column name broke `RunDatabase`](#orgf0dd355)
        16. [Finding of installations in alternate locations broken](#org082e1f4)
        17. [Failing on 3.x if socket for server thread already occupied](#org44d2a19)
    4.  [Enhancements to Utilities](#orgbce9f08)
        1.  [`pyFoamPrepareCase` recognizes multi-region cases](#org3a83002)
        2.  [`pyFoamPrepareCase` adds specialized templates](#org312e53e)
        3.  [`pyFoamPrepareCase` keeps data generated by meshing script](#org78552fe)
        4.  [`pyFoamPrepareCase` adds possibility for a file with default values](#org4db90b8)
        5.  [`pyFoamPrepareCase` writes report about the variables](#org4b0ed9b)
        6.  [Gnuplot can be styled with default commands](#org59af6bb)
        7.  [`pyFoamPVSnapshot.py` now supports Paraview 4.2 and later](#orgd0fa2ed)
        8.  [`pyFoamPVSnapshot.py` allows switching between decomposed and reconstructed data](#org9943c06)
        9.  [`pyFoamPVSnapshot.py` allows changing the field for sources](#orgab5e1bf)
        10. [`pyFoamPVSnapshot.py` allows rescaling the color-legend](#orgfa6542a)
        11. [`pyFoamPVsnapshot` reads parameters written by `pyFoamPrepareCase.py`](#org307f4f9)
        12. [`pyFoamListCases.py` allows filtering](#org06ef952)
        13. [`pyFoamRunParametervariation.py` now allows dictionaries](#orgebcf6d3)
        14. [`pyFoamConvertToCSV.py` now has all functionality of `pyFoamJoinCSV.py`](#orgaadf28e)
        15. [`dynamic` in `customRegexp` now allows composition from multiple match-groups](#orgea2787a)
        16. [New type `dynamicslave` in `customRegexp`](#org2f87595)
        17. [Additional profiling option `--profile-line-profiler`](#org0f5cd56)
        18. [Utilities that use templates can be customized with the configuration](#orgb29003c)
        19. [`LocalConfigPyFoam` now can be read **before** argument parsing](#org6df8b6f)
        20. [`pyFoamConvertToCSV.py` automatically selects the output format with `--automatic-format`](#orgdedd366)
        21. [`pyFoamConvertToCSV.py` allows adding original data as separate sheets](#orgbf5b698)
        22. [`pyFoamConvertToCSV.py` has improved naming of columns](#org21ce5bd)
        23. [`pyFoamConvertToCSV.py` now supports sets-files](#org01ec699)
        24. [`pyFoamPrepareCase.py` can calculate derived values with a script](#org7dfbd21)
        25. [`pyFoamPrepareCase.py` adds a variable `numberOfProcessors`](#org3bf70ed)
        26. [`pyFoamChangeBoundaryName.py` and `pyFoamChangeBoundaryType.py` now support decomposed cases](#orgcaf1ab2)
        27. [`pyFoamPrepareCase.py` has possibility for templates after the final stage](#orgd671909)
        28. [`pyFoamRunParameterVariation` allows adding postfix to cloned cases](#orgca14fba)
        29. [`pyFoamConvertToCSV` now allows setting of default input file format](#orgdaf89fa)
        30. [`pyFoamListCases.py` adds the hostname to the printed information](#org3751fe2)
        31. [`pyFoamPrepareCase.py` allows cloning](#org9698b20)
    5.  [Enhancements to the Library](#org7d8fecd)
        1.  [`SolutionDirectory` detects multiple regions](#org5730276)
        2.  [`BoolProxy` now compares like builtin `bool`](#orge53616f)
        3.  [`PyFoamApplication`-class now supports `pvpython` for debugging](#orgd4b78aa)
        4.  [`TemplateFile` now allows more flexible assignments](#orge49a8b4)
        5.  [`ThirdParty`-library `six` upgraded to 1.9.0](#org290bb1f)
        6.  [Additional markup in `RestructuredTextHelper`](#org666561e)
        7.  [`SpreadsheetData` can now read files produced by the `sets`-functionObject](#org70b96ba)
    6.  [Infrastructure](#orgcd2d99c)
        1.  [Adaption of Debian packaging to new conventions](#org76ec865)
    7.  [Development changes](#org31d20c2)
        1.  [Now uses `pytest` for unittesting](#orgd9038ed)
10. [Version 0.6.4 - 2014-11-24](#orgb583977)
    1.  [Requirements](#org003d25d)
    2.  [Future changes](#org62af32f)
        1.  [Redundant utilities `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py` unified](#org839a772)
    3.  [Major changes](#orgaca131b)
        1.  [Multi-line regular expressions in `customRegexp`](#org8fcec76)
        2.  [Enhancement of `pyFoamPrepare.py`](#orgc2967f2)
        3.  [Enhancements of the CSV-utilities](#org77fe244)
        4.  [Environment variable `PYFOAM_SITE_DIR` and `PYFOAM_DIR`](#org8604eb9)
    4.  [Incompatibilities](#org0ed9dae)
        1.  [Option `--silent` removed from `pyFoamPrepareCase.py`](#org2eabe5e)
        2.  [Keys in `RunDatabase` with column-names that contain upper-case letters change](#orga395f9b)
        3.  [Change in unique variable names in `pyFoamConvertToCSV.py`](#org0085a21)
        4.  [`PyFoam.IPython`-module renamed to `PyFoam.IPythonHelpers`](#orgff51a8e)
    5.  [Bugfixes](#org72f141b)
        1.  [Templates in `pyFoamPrepareCase.py` did not keep permissions](#org6cade50)
        2.  [`pyFoamComparator.py` failed due to circular dependency](#org67a20e2)
        3.  [`pyFoamDumpRunDatabaseToCSV.py` fails if Pandas-data is requested](#orgc1ec398)
        4.  [`sort` for list broke code on Python 3](#org309d908)
        5.  [Changing the OF-version does not work in Python 3](#org50d04c4)
        6.  [`addData` in `PyFoamDataFrame` extrapolates for invalid values](#org9d1b9bd)
        7.  [`--keep-last` did not work for `pyFoamClearCase.py` and parallel cases](#org8f75a51)
        8.  [`pyFoamDumpRunDatabaseToCSV.py` does not add basic run information](#org18b337c)
        9.  [Restore of `FileBasisBackup` did not work](#org6e92d1c)
        10. [Remove circular dependency in `DataStructures`](#org88c5ea5)
    6.  [New features/Utilities](#orgadafbf4)
        1.  [`pyFoamRunParameterVariation.py`](#org79948ab)
        2.  [`pyFoamBinarySize.py`](#orga991c24)
        3.  [`pyFoamBlockMeshRewrite.py`](#org6322319)
    7.  [Enhancements to Utilities](#org94fec6b)
        1.  [`pyFoamChangeBoundaryType.py` allows setting additional values](#orgce5d174)
        2.  [`pyFoamPrepareCase.py` now has OF-version and fork as defined variables](#orge764967)
        3.  [`pyFoamPrepareCase.py` now allows "overloading" another directory](#orgc78f053)
        4.  [`pyFoamIPythonNotebook.py` adds improvements to the notebook](#orgf5062f5)
        5.  [`pyFoamListCases.py` more tolerant to faulty `controlDict`](#orgef968c1)
        6.  [`pyFoamDumpConfiguration.py` prints sections and keys alphabetically](#org9c3d5f9)
        7.  [`pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py` read and write Excel-files](#org86640e3)
        8.  [Flexible variable filtering in `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py`](#orge737cb9)
        9.  [Columns in `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py` can be recalculated](#org8ad3af9)
        10. [Testing for `Numeric` removed from `pyFoamVersion.py`](#org778a4d0)
    8.  [Enhancements to the Library](#org9e9cf9b)
        1.  [Subclass of `ClusterJob` that support `PrepareCase`](#org895c395)
        2.  [Subclass of `ClusterJob` that support `RunParameterVariation`](#orgd2920b9)
        3.  [`execute` in `PyFoam/Utilities` fails if script is not executable](#org214f11d)
        4.  [`foamVersion` uses a separate wrapper class for `tuple`](#orgeb59443)
        5.  [Move calculation of disk usage to `Utilities`](#org1a1a01a)
        6.  [Enhancement of `--help`](#orgeaa21e2)
        7.  [`which`-routine in `Utitlities` uses native Python-routine](#orge32158f)
        8.  [`FileBasis` now allows file handles instead of the filename](#orga9874b1)
        9.  [`BlockMesh` doesn't force writing to file anymore](#orgf523b19)
        10. [Additional methods for `BlockMesh`-class](#orgcee7e38)
        11. [`LineReader` allows keeping spaces on left](#orgee9cc94)
        12. [`TemplateFile` now allows writing of assignment-results in file](#orgdc2cbfd)
        13. [`SolverJob` now allows passing of parameters to the solver](#orgdac0a22)
        14. [`SpreadsheetData` now allows reading from an Excel file](#org0f22196)
        15. [`SpreadsheetData` allows recalculating columns](#org4015342)
    9.  [Known bugs](#orgca1f60e)
        1.  [Timelines not forgotten for multiple runner calls](#orgfc34162)
11. [Version 0.6.3 - 2014-06-23](#org23f752f)
    1.  [Requirements](#orgf8034c1)
    2.  [Major changes](#org07477c5)
        1.  [Version changing supports forks of OpenFOAM](#org328e3ac)
    3.  [Incompatibilities](#org8a6df25)
        1.  [Change of command interface of `pyFoamSTLUtility.py`](#orgc54dd56)
        2.  [If `0.org` is present `pyFoamCloneCase.py` and `pyFoamPackCase.py` ignore `0`](#org6f56424)
    4.  [Bugfixes](#org5a5719a)
        1.  [PlotWatcher has long times between updates if pickling takes long](#orgfd7cfe9)
        2.  [`pyFoamPVSnapshot.py` fails for newer paraview-versions](#org14e3955)
        3.  [SamplePlot failed when valueNames are unspecified](#org6ff7087)
        4.  [`pyFoamTimelinePlot.py` failed Numpy/Pandas output of vector fields](#org8ab7cea)
        5.  [`alternateAxis` ignored for slave](#orgcca73de)
        6.  [`pyFoamCaseReport.py` more stable for binary `boundary`-files](#org44a2314)
        7.  [`SpreadsheetData` returns data which breaks certain Pandas-operations](#org917fa9a)
        8.  [`pyFoamCloneCase.py` added duplicates to the archive](#org23fe4e7)
        9.  [`nonuniform` of length 3 not correctly printed](#org6ff5fcc)
    5.  [New features/Utilities](#org1f17340)
        1.  [`pyFoamPrepareCase.py` for case preparation](#org52435d1)
        2.  [`pyFoamIPythonNotebook.py` for generating and manipulating IPython-notebooks](#org4a8e42c)
        3.  [Additional sub-module `PyFoam.IPython`](#orgf4a4b34)
        4.  [Additional sub-module `PyFoam.Wrappers`](#org61fbd28)
    6.  [Enhancements to Utilities](#org7d81761)
        1.  [`pyFoamSampleplot` has option to use index instead of time in filenames](#org386c115)
        2.  [`pyFoamListCases.py` Allows addition of custom data](#orgc1388cd)
        3.  [Switch compiler versions](#orgf3ba76b)
        4.  [`pyFoamVersion.py` reports the installed versions better](#org776ef5e)
        5.  [Offscreen rendering can be switched off in `pyFoamPVSnapshot.py`](#org2dc39f1)
        6.  [Write 3D-data in `pyFoamPVSnapshot.py`](#org0eb4dab)
        7.  [Added capabilities to `pyFoamSTLUtility`](#org2cf8644)
        8.  [`pyFoamDecomposer.py` switches off function objects](#org33b85bf)
        9.  [`pyFoamCloneCase.py` clones more stuff](#org6e555af)
    7.  [Enhancements to the Library](#org5f09e8e)
        1.  [`BasicRunner` now can print the command line that is actually used](#org9301875)
        2.  [`ClusterJob` now can live without a machinefile](#org8461a15)
        3.  [Enhanced treatment of symlinks during cloning](#orgcbccb06)
        4.  [`AnalyzedCommon` clears the `analyzed`-directory](#org3dbbb2a)
        5.  [`TimelineDirectory` is more tolerant](#org09cfc42)
        6.  [Possibility of a subcommand-interface for utilities](#org057684a)
        7.  [`STLUtility` accepts file-handles](#org70e65c2)
        8.  [`addClone` in `SolutionDirectory` accepts glob patterns](#org6c177ef)
        9.  [`execute` in `Utilities` allows specification of working directory and echoing of output](#orgedef9ce)
        10. [`rmtree` and `copytree` more tolerant](#orgf82b9ae)
        11. [Enhanced support for booleans in the parser](#org8dada90)
        12. [Application classes now allow specifying options as keyword parameters](#orgb1148d6)
        13. [`SolutionDirector` now can classify directories in the `postProcessing`-directory](#org26bdb00)
        14. [`pyFoamSamplePlot.py` now more flexible for distributions](#orgc24b366)
        15. [`DictProxy` now has a `dict`-like `update`-method](#orgad91e46)
        16. [`FoamFileGenerator` automatically quotes strings](#org0b3e2a5)
        17. [Children of `FileBasis` now can be used with the `with`-statement](#orgdb0a996)
12. [Version 0.6.2 - 2013-11-03](#orgcf3c6ef)
    1.  [Major changes](#orgbba5797)
        1.  [Use of `pandas`-library](#org29d7d86)
    2.  [Incompatibilities](#org2df2350)
        1.  [Different separator for databases in CSV-files](#orgfd26b9d)
        2.  [Change of independent variable name in sample data](#orgdcb1ff3)
    3.  [Bugfixes](#org5afc8ef)
        1.  [`pyFoamPackCase.py` does not handle symbolic links correctly](#org586889d)
        2.  [`pyFoamPotentialRunner.py` not working with OpenFOAM 2.0 or newer](#org294699e)
        3.  [`pyFoamListCase.py` fails with `controlDict` that use preprocessing](#org7914291)
        4.  [Cloning fails in symlink-mode if files are specified twice](#org4bcacca)
    4.  [Utilities](#org4474c2b)
        1.  [`pyFoamPotentialRunner.py` now allows removing of `functions` and `libs`](#org6424e3f)
        2.  [The Runner-utilities now have more options for clearing](#org38df037)
    5.  [Library](#orgc58deae)
        1.  [`SolutionDirectory` and `TimeDirectory` are more tolerant](#orgd220fa3)
        2.  [`ClusterJob` now handles template files](#org269020f)
        3.  [Additional parameters in `ClusterJob`](#orgc53aa1d)
        4.  [Custom data in directory easier accessible](#org87c3e9a)
        5.  [`SolverJob` now allows compression of output](#org77d40cd)
        6.  [`PyFoamApplication`-class now allows quick access to data](#org09dbf20)
    6.  [New features/Utilities](#org11fca3f)
        1.  [Post-run hook that sends mail at the end of run](#org5647355)
        2.  [New utility `pyFoamCompressCases.py`](#org58e1362)
        3.  [Paraview-module to read additional data](#orgc8a1e50)
    7.  [Enhancements](#org410d311)
        1.  [`pyFoamRedoPlot.py` can plot in XKCD-mode](#org8c65d40)
        2.  [`pyFoamListCases.py` now displays disk usage in human readable form](#org9ce7042)
        3.  [`pyFoamClearCase.py` more flexible in selection of data to be removed](#orge645728)
        4.  [`pyFoamFromTemplate.py` automatically chooses template and default values](#org7cd1103)
        5.  [`pyFoamDumpRunDatabaseToCSV.py` can disable standard-fields](#orgfcf0e0b)
        6.  [`pyFoamDumpRunDatabaseToCSV.py` prints `pandas`-object](#org9191f51)
        7.  [Better debugging with `ipdb`](#org16bcdbb)
        8.  [Interactive shell after execution for utilities](#org45dc6f6)
        9.  [Utilities that read quantitative data convert to `pandas`-data and/or `numpy`](#orga17f0f9)
        10. [Utilities that read quantitative data write Excel files](#orgd41c013)
        11. [Specify additional settings for `GnuPlot` in `customRegexp`](#org4af6a1e)
        12. [More flexible data specification for `pyFoamSamplePlot.py`](#org57ba2bb)
        13. [`pyFoamSamplePlot.py` now allows specification of x-range](#orgf916f53)
13. [Version 0.6.1 - 2013-05-24](#org9fab04c)
    1.  [Major changes](#org139fdad)
    2.  [Bugfixes](#orgddd0e18)
        1.  [Restoring of `controlDict` after `write`](#org55e95de)
        2.  [Custom-plot type `slave` not working if no `master` defined](#org42302ac)
        3.  [`-list-only` did not correctly parse lists with a numeric prefix](#org41afdcd)
    3.  [Utilities](#orgb277feb)
        1.  [`pyFoamBuildHelper.py` now allow more than one action](#org6976440)
        2.  [Utilities warn if OpenFOAM-version is unset](#orgb468973)
        3.  [`pyFoamUpgradeDictionariesTo20.py` allows single files](#orgeba72a6)
        4.  [`pyFoamUpgradeDictionariesTo20.py` transforms reaction-schemes](#orgdbd9fb9)
        5.  [`pyFoamUpgradeDictionariesTo20.py` transforms thermophysical data](#org8575c44)
        6.  [`pyFoamCloneCase` now allows creating directory that symlinks to the original](#org1c75bdb)
        7.  [`pyFoamClearCase.py` now removes `postProcessing` and allows removal of additional files](#org6fd7dc0)
        8.  [Improvements to `pyFoamVersion.py`](#orgcb53b2e)
        9.  [Additional files automatically cloned](#org6a0aaf9)
        10. [`pyFoamDisplayBlockMesh.py` uses the same options for template format as `pyFoamFromTemplate.py`](#orga53001f)
    4.  [Library](#org4ca467e)
        1.  [Improvements in syntax of `ParsedParameterFile`](#orgf4d71dd)
        2.  [`Utilities`-class now function to find files matching a pattern](#org30849b4)
        3.  [VCS ignores more files](#org6e8ab7d)
    5.  [New features/Utilities](#org44b801a)
        1.  [New Utility `pyFoamSymlinkToFile.py`](#org5ac96f0)
14. [Version 0.6.0 - 2013-03-14](#orgf454d98)
    1.  [Major changes](#org5bde096)
        1.  [Adaption to work with Python3](#org11c4903)
        2.  [New ThirdParty-Libraries](#org3e8deeb)
        3.  [Porting to `Windows`](#org916aef9)
        4.  [Experimental port to `pypy`](#orgd7c7d8d)
    2.  [Third-Party](#org87ecdda)
        1.  [Upgraded `ply` to 3.4](#orgb0a3bde)
    3.  [Infrastructure](#orgb7fdb24)
        1.  [Parameters can't be modified in `CTestRun` after initialization](#org4049378)
        2.  [Treat timeouts in the `MetaServer` right](#org8993dcc)
        3.  [Add `execute`-method to `ClusterJob`](#org76f4369)
        4.  [Add possibility to run specific modules before or after the solver](#org5b7506a)
        5.  [Parameters added to the info about the run](#org3822c98)
        6.  [Parameter handling in `ClusterJob` extended](#org482fbf9)
        7.  [Run data written alongside `PickledPlots`](#org2b4f02d)
        8.  [`BasicRunner` collects error and warning texts](#org8178f8b)
    4.  [Library](#orgd866a75)
        1.  [`TemplateFile` now uses `pyratemp`](#org6fcc935)
        2.  [Clearer error message in Application-classes](#org7fb7072)
        3.  [Output is only colored if it goes to the terminal](#org8c53d89)
        4.  [`error`-method of application classes now raises an exception](#orgbcceacc)
        5.  [`ParsedParameterFile` now knows how to handle binary files](#org33ca6c1)
        6.  [`LabledReSTTable` for more flexible table generation](#org895cd5d)
        7.  [Plotting classes now allow setting of `xlabel`](#orgf9218cc)
    5.  [Utilities](#orgd4734b3)
        1.  [`pyFoamFromTemplate.py` with new templating engine](#orge6aebbe)
        2.  [`pyFoamSamplePlot.py` allows using the reference data as basis for comparison](#orga7c691f)
        3.  [Scaling and offsets are now used in plots of `pyFoamSamplePlot.py`](#org6a84dcf)
        4.  [`pyFoamPrintData2DStatistics.py` prints relative average error](#org42f5ec3)
        5.  [Enhancements to `pyFoamVersion.py`](#org8d55e08)
        6.  [`pyFoamRunner.py` allows hooks](#org33d3f40)
        7.  [`pyFoamRedoPlots.py` supports range for plots](#org63e4e44)
        8.  [`pyFoamDisplayBlockMesh.py` no supports templates](#org8e2b21d)
        9.  [`pyFoamCaseReport.py` is tolerant towards binary files](#org619595e)
        10. [`pyFoamSamplePlot.py` and `pyFoamTimelinePlot.py` raise error if no plots are generated](#org40ec20f)
        11. [`pyFoamSurfacePlot.py` can wait for a key](#org054696b)
        12. [`pyFoamEchoDictionary.py` is more flexible with binary files](#org82587da)
        13. [All utilities now have a switch that starts the debugger even with syntax-errors](#org4b4c950)
        14. [Utilities now can be killed with `USR1` and will give a traceback](#orgfaa2110)
        15. [Switch to switch on **all** debug options](#orgb009f18)
        16. [Plotting utilities now allow specification of x-Axis label](#org920ad05)
        17. [Metrics and compare for `pyFoamTimelinePlot.py` and `pyFoamSamplePlot.py` support time ranges](#orga86993e)
        18. [`pyFoamDisplayBlockMesh.py` allows graphical selection of blocks and patches](#orgd611832)
        19. [`pyFoamCloneCase.py` and `pyFoamPackCase.py` accept additional parameters](#org80a069e)
        20. [`pyFoamListCases.py` now calculates estimated end-times](#org73579dc)
    6.  [New features](#org1f281b3)
        1.  [Different "phases" for multi-region solvers](#org7ac5507)
        2.  [`pyFoamChangeBoundaryType.py` allows selection of region and time](#org2ae2760)
        3.  [New class for storing case data in a sqlite-database and associated utilities](#org7345bfc)
    7.  [Bugfixes](#orgbc68abd)
        1.  [Only binary packages of 1.x were found](#org7b6cb3e)
        2.  [Option group *Regular expressions* was listed twice](#orgefce7ad)
        3.  [`--clear`-option for `pyFoamDecompose.py` not working](#org065966f)
        4.  [`pyFoamDisplayBlockmesh.py` not working with variable substitution](#org5020891)
        5.  [Option `--function-object-data` of `pyFoamClearCase.py` not working with directories](#org705c8b3)
        6.  [`nonuniform` of length 0 not correctly printed](#org8ac13af)
        7.  [Building of pseudocases with `pyFoamRunner.py` broken](#org1697278)
        8.  [`pyFoamRedoPlot.py` did not correctly honor `--end` and `--start`](#orgf3ae7ae)
        9.  [`WriteParameterFile` does not preserve the order of additions](#orgb3881fb)
        10. [Wrong number of arguments when using `TimelinePlot` in `positions`-mode](#org58048c5)
        11. [`ClusterJob` uses only `metis` for decomposition](#org4d107fe)
        12. [`pyFoamSamplePlot.py` and `pyFoamTimelinePlot.py` produced no pictures for regions](#org65c60f2)
        13. [Barplots in `pyFoamTimelinePlot.py` not working if value is a vector](#org5246b19)
        14. [Mysterious deadlocks while plotting long logfiles](#orgaa92ea0)
        15. [Scanning linear expressions form the block coupled solver failed](#orgbc18344)
        16. [`#include` not correctly working with macros in the included file](#orgf12ed84)
        17. [Macros not correctly expanded to strings](#org6da2c3a)
        18. [`pyFoamPackCase.py` in the working directory produces 'invisible' tar](#org8898d4e)
        19. [String at the end of a linear solver output makes parsing fail](#orgdadd08e)
        20. [Paraview utilities not working with higher Paraview versions](#org31b2bf5)
        21. [Camera settings not honored with `pyFoamPVSnapshot.py`](#org9ba3bac)
15. [Version 0.5.7 - 2012-04-13](#orge80bb85)
    1.  [Parser improvements](#orgd893792)
    2.  [Utility improvements](#org8b558bd)
    3.  [New Utilities](#orgcb98381)
    4.  [Library improvements](#org0d5ccfb)
    5.  [Removed utilities](#org36307ad)
    6.  [Thirdparty](#orgbca3dce)
    7.  [Other](#org7384e0a)
16. [Older Versions](#org3b223b9)


<a id="orgce2577d"></a>

# Version 0.6.12 - Not releases


<a id="org2085bc5"></a>

## New features/utilities


<a id="org1c6a97d"></a>

## Enhancements to the utilities


<a id="org2da9c6e"></a>

### Paraview-utilities now work in Paraviews that use Python 3

Newer versions of Paraview may use Python 3 as the
Python-interpreter which made `pyFoamPVSnapshot.py` fail.

The Paraview-utiliies (and the library as well) have been adapted
to work with Python 3 **and** 2


<a id="org1ceb094"></a>

### `pyFoamPrepareCase.py` allows automatically zipping template results

The utility now allows automatically zipping the results of
template evaluations **if** the result file has no extension
(because then it can be assumed that these files are
OpenFOAM-dictionaries which are transparently unzipped).

This allows automatically ignoring this files with proper patterns
in `.gitignore` or `.hgignore`

This can be switched on via the command line or the
`LocalConfigPyFoam` file


<a id="orgae12578"></a>

### `customRegexp` has a type `mark` to add marks to the plots

Plots of `type mark` don't plot but there is a list `targets` with
names of other plots. Every time the `expr` matches a vertical
line is added to those plots.

Purpose of this type is to annotate singular events in the graphs


<a id="orgbe95a54"></a>

### Plotting utilities now plot progress of `snappyHexMesh`

The `pyFoamPlotRunner.py` and `pyFoamPlotWatcher.py` now allow
plotting the numbers of cells in different refinement levels in
`snappyHexMesh`

Different phases are annotated with vertical lines


<a id="org1c2b928"></a>

### Plotting utilities now plot progress of `foamyHexMesh`

The `pyFoamPlotRunner.py` and `pyFoamPlotWatcher.py` now allow
plotting the numbers of inserted points and the total displacement
and distance of `foamyHexMesh`


<a id="org892ffa0"></a>

### Plotting utilities now print available values of `type`

Instead of an obscure error message it now prints a list of the
available types and a short descriptions


<a id="org1712edc"></a>

### Missing attributes in `customRegexp`-specifications now give better error messages

Now the complete spec is printed (in addition to the missing attribute)


<a id="org4d8ee50"></a>

### Option `--quiet-plot` for plotting utilities swallows output of the plotting program

`gnuplot` sometimes outputs error messages which mess up the
`ncurses`-output. The `--quiet-plot`-option swallows this
output. This behaviour is **not** the default because sometimes this
output is useful


<a id="orga56de1d"></a>

### Colored markers in `pyFoamPlotWatcher` for logfiles from restarts

If following a file which has `.restartXX`-files then when the
file is changed a red marker line with the label "Restart" is
shown in all the plots


<a id="org51b9b5e"></a>

### `writeFiles` in a `customRegexp`-entry writes scanned output to file

If a line

    writeFiles yes;

is added to an entry in `customRegexp` then the data is written to
a file as well. These files are found in the `.analyzed`-folder


<a id="org8efebcb"></a>

### Modifying splitting behavior for plot data

Plotting data is reduced from time to time if the number of data
points exceeds a certain threshold. Usually this threshold
is 2048. Now for most runner utilities (and the `PlotWatcher`)
there are two additional options: `--split-data-points-threshold`
allows setting the number of data points to a different value than
2048 and `--no-split-data-points`  to switch off splitting altogether


<a id="orgf0f734c"></a>

## Enhancements to the library


<a id="org349ee4f"></a>

### Paraview-classes now work with Python 3

See above: *Paraview-utilities now work in Paraviews that use
Python 3*


<a id="orgce668d0"></a>

### `TemplateFile` now can write the result as zipped

The `writeFile`-method now has an optional parameter `gzip` that
forces the file to be written in compressed form with the
extension `.gz` added. If the file already has the extension `.gz`
it is assumed that `gzip` is set. If a file of the same name with
an extension `.gz` exists then it is assumed that this is to be
overwritten. If a file is written zipped and the same file without
`.gz` exists then it is removed to avoid confusion which file will
be used


<a id="orga95f690"></a>

### Mechanism to have `alternateTime` in single `customRegexp`

The entry `alternateTime` now allows to reference special
expressions that will serve as an alternate "time source". This
was for instance used to implement the progress graph for
`snappyHexMesh`


<a id="org2153c93"></a>

### `quiet`-option added to plotting implementations

This option tells the plotting program to not output anything to
the terminal. Currently only works for `Gnuplot`


<a id="orgc509d10"></a>

### The `[]`-operator of the `PyFoamDataFrame` is now more flexible

If that operator gets a single numeric value or a list of numbers
it gets the rows where the index (usually the time) is nearest to
the number(s) and returns a `PyFoamDataFrame`

All other keys are passed to the "usual" `[]`-operator of the
`DataFrame` but the result is converted to a `PyFoamDataFrame`


<a id="orgf0042a2"></a>

### Each run started by `BasicRunner` has a unique ID

Each run gets a unique id. This allows to easily find out whether
the data is from the same run


<a id="org2f79c6a"></a>

### `pyFoamAddCaseDataToDatabase.py` allows updating data

The `--update` switch allows updating the data for runs. Otherwise
if the run already exists in the database the utility will fail


<a id="orgf82621d"></a>

### `RunDatabase` gets method `modify`

This method allows updating a run with a unique id by specifying a
(nested) dictionary with the values


<a id="org0412f84"></a>

## Bug fixes


<a id="orga6b2069"></a>

### `auto` for the solver does not work with compressed `controlDict`

If the `controlDict` was compressed the value of the
`application`-entry could not be read. This has been fixed


<a id="orgf5f1318"></a>

### `FileBasisBackup` now works with zipped file

If a file is already zipped then the `FileBasisBackup` class could
not create a backup file and failed. This works now


<a id="org716eca8"></a>

### Case with zipped `controlDict` not recognized as a valid case

If the `controlDict` was zipped for some reason then PyFoam (and
therefor utilities like `pyFoamListCase.py`) did not recognize it
as a valid case


<a id="org10fc8df"></a>

### `pyFoamDisplayBlockMesh.py` not working with newer VTK-versions

The utility did not work with newer versions of VTK. This has been
fixed. In the process support for Python 2.x has been broken


<a id="orgb61d2c6"></a>

## Incompatibilities


<a id="org6ef3f5e"></a>

### `TemplateFile` writes to zipped file if it exists

The method `writeFile` looks for a file o the same name with `.gz`
added. If this exists then it is assumed that this should be
written (in zipped form)


<a id="orgac8d0dd"></a>

### `pyFoamDisplayBlockMesh.py` not working with Python 2.x anymore

This utility now requires Python 3.

It is not typically run on computation servers (which mostly still
have Python 2) so the extra effort to support this outdated
version of Python is not worth it


<a id="orgbe36102"></a>

### Constructor of `PyFoamDataFrame` is more restrictive

The constructor now checks if

-   the index has a number type
-   the index is strictly monothonic

because most additional algorithms (`integrate()` etc) rely on
these assumptions


<a id="org5e11a20"></a>

### `[]`-operator of `PyFoamDataFrame` returns a `PyFoamDataFrame`

The old behaviour of this was to return a `DataFrame`. Shouldn't
break existing code but makes it easier to chain indexes


<a id="orgc0def18"></a>

### `RunDatabase` fails if the same unique ID is inserted again

If a dataset with the same unique ID is added with `add` for a
second time the method fails with a `KeyError` unless the
`update_existing`-flag is set

This has the potential to beak old code (which probably wouldn't
work correctly anyway as the old behaviour was to add the data for
the rum for a second time)


<a id="orgf9da19b"></a>

## Code structure


<a id="org6554e73"></a>

## Infrastructure


<a id="orgbe3b04e"></a>

## ThirdParty


<a id="orge791c7e"></a>

### Modification to `Gnuplot`-library

There has been a `quiet`-option added that swallows all terminal
output of `gnuplot`. This only works in the
Unix/Linux-implementation. All others ignore it


<a id="orgb5b93b0"></a>

# Version 0.6.11 - 2019-10-31


<a id="orgc73e2e2"></a>

## Code structure


<a id="orgb0ddae6"></a>

### Moved library into `src`-directory

To make sure that the `tox`-tests are not affected the library is
moved into the `src`-subdirectory


<a id="org10d1ee4"></a>

### Added Developer notes

Added a file `DeveloperNotes` with hints for people who want to
contribute


<a id="org7ef15da"></a>

## Incompatibilities


<a id="org81fe655"></a>

### Behaviour reading `customRegexp`

Macro expansion in the `customRegexp` might break it for some
cases


<a id="orgb5d3a71"></a>

### Gnuplot does not use `FIFO` as the default anymore

See the relevant entry in *Enhancements to Utilities*

A potential problem is that the new implementation leaves files in
the `/tmp` filesystem


<a id="org1004c90"></a>

## Enhancements to Utilities


<a id="org6af76a6"></a>

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


<a id="org963967a"></a>

### Macro expansion in `customRegexp`

In the `customRegexp` it is now possible to use the usual
OpenFOAM-macro-expansions with `$` etc. This makes


<a id="org021e2c4"></a>

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


<a id="orga7412d8"></a>

### `pyFoamRedoPlot.py` allows passing terminal options

The utility now allows passing options to the plotting
implementation with the `--terminal-options`-option. This can for
instance be used to modify the size of the plot


<a id="orgde667b6"></a>

### `pyFoamPlotWatcher.py` stops scanning the file is `--end` was specified

If the `--end-time` option is specified then the solver stops
scanning if that time is reached. The plot windows are killed. To
keep them specify `--persistent`


<a id="org2a2c4a6"></a>

### Hardcopies of custom plots have more descriptive names

Instead of the `custom00xxx` name the hardcopies of custom plots
now have and additional short name that describes the content of
the plot (it is taken from the id in the `customRegexp`)


<a id="org93ddb00"></a>

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


<a id="org943ce13"></a>

### `pyFoamPrepareCase.py` calls script after copying initial conditions

A script `postCopy.sh` is called after the initial conditions are
copied from `0.org`


<a id="orgc050efa"></a>

### `--stop-after-template` and `--keep-zero` improve control in `pyFoamPrepareCaseParameters.py`

The combination of these two parameters allow "just" changing
something in the templates without running other lengthy
operations


<a id="orgbc19bf6"></a>

### `pyFoamPVSnapshot.py` allows specification of the image quality

The option `--quality` now allows specifying the quality of the
image with a value of \(0\) being worst (but producing the smallest
pictures) and \(100\) best (but producing huge pictures). The
default is \(50\)


<a id="org7eec9a6"></a>

### Image size specification for `pyFoamPVSnapshot.py`

The options `--x-resolution` and `--y-resolution` allow specifying
the resolution of the image. If only one of them is set the image
is scaled proportionally. This only works for Paraview versions
bigger than 5.4


<a id="org318545e"></a>

### Setting separation of views and background transparency in `pyFoamPVSnapshot.py`

Two new options were added that allow setting a separation between
different views and making the background transparent. This only
works for Paraview versions bigger than 5.4


<a id="org9cb2ac9"></a>

### `pyFoamPVLoadState.py` automatically uses decomposed or reconstructed data

Depending which of the two sets has more timesteps that state is
set to this before loading. So if more parallel timesteps are
present then these are used even if the state file uses the
reconstructed times. The behavior can be changed with the
`--decompoes-mode`-option


<a id="org4c4abe5"></a>

### Change directory for `pyFoamPrepareCase.py` to target

The option `--extecute-in-case-directory` changes the working
directory to the target directory. THis allows specifying
parameter files that are in that directory without a full path


<a id="org2c8be6c"></a>

### `pyFoamPrepareCase.py` can create an example case

A command like

    pyFoamPrepareCase.py exampleCase --paramter-file=parameters.base --build-example --clone-case=originalCase

creates an example case `exampleCase` from a template case
`originalCase` using the parameter file `parameter.base`. It
creates a script `Allrun` that allows executing the case without
`PyFoam` (if none of the scripts uses `PyFoam`-scripts)

This may not work for all configurations (especially cases that use `postTemplate`)


<a id="org4598ebd"></a>

### `pyFoamPrepareCase` prints derived values

The same way that the utility printed the used values it now
prints the derived values as well


<a id="org149e1f2"></a>

### `pyFoamPVSnapshot` allows specifying different colors for different views

The option `--color-for-filers` now allows specifying a different
color for the same filter in different view. This is done by
specifying a dictionary


<a id="orgfef4b89"></a>

### `alternateLogscale` for custom plots

This is analog to `logscale` but for the values that are specified
with `alternateAxis`


<a id="orga604b1a"></a>

### `pyFoamBinarySize.py` now calculates documentation size as well

If there is `html` documentation then this is counted as well


<a id="orga6a7aa9"></a>

### `pyFoamCompareDictionary.py` allows specification of significant digits

When comparing numbers now the number of significant digits can be
specified. This only works for single numbers. Not compound types
like lists and vectors


<a id="orgca806d8"></a>

## Enhancements to the Library


<a id="orgad9d42d"></a>

### `progress`-data is automatically converted to `float`

When using format-strings for the `progress`-entry then the
library automatically attempts to convert the data to `float`
(otherwise it keeps it as `str`)


<a id="orgf53e21a"></a>

### Additional directories in `FoamInformation`

Two functions `foamCaseDicts()` and `foamPostProcessing()` have
been added that return the paths to these directories inside
`$FOAM_ETC`


<a id="orgf7486d5"></a>

### `BoolProxy` now works correctly with `!=`

Added a method `__ne__` so that the results of the `!=` operator
are consistent with `==`


<a id="org9216e75"></a>

## Bug fixes


<a id="orge492a20"></a>

### With dynamic plots names with `_slave` are problematic

This made the slave plots that had `_slave` in the name fail


<a id="org5a66f95"></a>

### New-style dimensioned scalars fail

As reported in
<https://sourceforge.net/p/openfoam-extend/ticketspyfoam/223/> by
Rodrigo Leite Prates parsing certain constructs that involve
dimension sets fail. This is because of a problem with the
comparison of `Dimension` that assumes that the other side is a
`Dimension` as well. Fixed


<a id="orgee62991"></a>

### `pyFoamPVSnapshot.py` not working with Paraview 5.6

The API now has to be called through a different module. Otherwise
it will fail


<a id="org05595b8"></a>

### `customRegexp` farthes away was used

When looking automatically for a `customRegexp` the one furtherest
up in the directory tree was used. Now instead all the
`customRegexp` are used with the lower ones overriding the other
ones


<a id="orgc0ee3b6"></a>

### `ParameterFile`-class got confused by commented lines

One of the oldest classes in PyFoam had the problem that it
"found" parameters that were commented out with `//`. This has been fixed


<a id="org88c1615"></a>

### `pyFoamBinarySize.py` did not count files in `build`

Some distros have a directory `build` with the intermediate object
files. This has not been counted until now


<a id="org00bedbf"></a>

### Binary files with `ParsedParameterFile` not working in Python 3

Because Python 3 tries to encode read files as Unicode strings and
certain byte combinations are not valid UTF-8 encodings.

Hopefully fixed by reading the file as binary and then create a
`latin-1` encoded string

Reported in
<https://sourceforge.net/p/openfoam-extend/ticketspyfoam/225/> by
Johan Hidding


<a id="org49168cf"></a>

### Improved handling of binary files in Python 2 and 3

Parts of the `FileBasis` class were not working correctly in
Python 3 because there strings are no longer 'lists of
bytes'. This has been adapted so that these parts work correctly
in Python 2 **and** 3 and unit tests have been added


<a id="orgcac849c"></a>

# Version 0.6.10 - 2018-08-12

This is only a minor release with the main purpose to recognize
OpenFOAM 6 installations with their new numbering scheme


<a id="orgaf25f86"></a>

## Incompatibilities


<a id="orgd16da20"></a>

### `pyFoamPrepareCase.py` does not execute decomposition scripts for single processor cases

If `numberOfProcessors` is smaller than 2 then the decomposition
scripts are ignored. This may cause problems in the unlikely case
that the setup process relied on these scripts being always
executed


<a id="org0bf70a9"></a>

## New feature/utilities


<a id="org7d0c5b1"></a>

### Utility `pyFoamFunkyDoCalc.py` to compare data from `funkyDoCalc`

This utility compares data written by the `funkyDoCalc`-utility from
`swak4Foam` (this data is written with the `-writeDict`-switch

For details on the usage see the online help of the utility


<a id="org10abf30"></a>

## Enhancements to Utilities


<a id="org83008dd"></a>

### Recursive searching for `pyFoamListCases.py`

The `--recursive`-option now recursively searches the specified
directories for cases. Without the option it behaves the way it
did before


<a id="org529ee7e"></a>

### Look for `customRegexp` in parent directories

The plotting utilities now look for `customRegexp`-files in parent
directories of the case directory. This allows to use one file for
a number of cases. The file in the directory is still used. The
behavior can be switched off with the
`--no-parent-customRegexp`-option


<a id="orge011495"></a>

### `pyFoamPrepareCase.py` does not execute decomposition scripts for single processor cases

If `numberOfProcessors` is smaller than 2 then the decomposition
scripts are ignored


<a id="orgbea19c0"></a>

### `pyFoamPrepareCase.py` checks for proper decomposition

At the end the utility now checks if the number of processor
directories is consistent with the specified `--number-of-processors`


<a id="org79d1077"></a>

### `pyFoamPlotWatcher.py` automatically uses newest logfile

If a logfile `auto` is specified then the utility uses the newest
file with the extension `.logfile` in the current directory.

Like any automatism this might produce unexpected results. So use
with care


<a id="org7f3090d"></a>

## Enhancements to the Library


<a id="org7cbad52"></a>

### `FoamFileGenerator` handles `OrderedDict`

The class now preserves the order if an instance of `OrderedDict`
is found (instead of the usual behaviour of sorting the keys to
always get the same output)


<a id="orgbdf3ca6"></a>

### `#sinclude` handled as an alias to `#includeIfPresent`

OpenFOAM v1812 introduces this as an alias. It is now handled by
the parser similarly


<a id="org156f21b"></a>

### OpenFOAM 6 correctly recognized

With OpenFOAM 6 the naming scheme changed again. Instead of 6.0
(which PyFoam would have recognized) it is now plain 6. PyFoam now
recognizes both forms in the directory name


<a id="org8a56cfb"></a>

## Bug fixes


<a id="orga1d93c6"></a>

### `pyFoamPrepareCase.py` did not remove `processor`-directories


<a id="orge69f9e5"></a>

## Infrastructure


<a id="orga3c306e"></a>

### Single digit version numbers supported

Now installations with names like `OpenFOAM-6` are recognized


<a id="org8e914d1"></a>

# Version 0.6.9 - 2018-02-25


<a id="org396fe46"></a>

## Major changes


<a id="org670cbdd"></a>

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


<a id="org982040a"></a>

## Incompatibilities


<a id="orgd038931"></a>

### `pyFoamPrepareCase.py` creates `.foam`-file

The utility now automatically creates a file that allows Paraview
to open the case


<a id="org32c902d"></a>

### Hardcoded Foam-Version upgraded to `4.0`

The hardcoded Foam-version that is used if the
`WM_PROJECT_VERSION` environment variable is not set is set to
`4.0` from the rather ancient version `1.5`


<a id="org6ae5028"></a>

### `none` no longer parsed as an equivalent for `false`

This breaks the parsing of cases where `none` is used as a word.


<a id="org0740d03"></a>

## New features/utilities


<a id="orgbc5d39b"></a>

### `pyFoamJoinTimelines.py` to join Timelines from restarts

This utility joins timeline files from different restarts. The
lines from times that will be in the next file are discarded


<a id="orgc293c1d"></a>

### `pyFoamRestartRunner.py` to automatically restart runs

For cases that fail strangely (mostly due to problems in the
linear solver) but restart successfully this utility helps running
them.

The utility tries to restart the solver until either the `endTime`
is reached or no new time-step is written to disk (in this case it
makes no sense to run again)


<a id="orgf3ebd5d"></a>

## Enhancements to Utilities


<a id="org169f11e"></a>

### Special snapshot utilities to use MESA

There have been variations of the regular `pyFoamPVSnapshot.py`
added. The only difference they have is that they set a option that
enforces the used `OpenGL`-implementation (especially Mesa). Use this run
the script on a machine that don't have hardware support for 3D-graphics


<a id="org2a5ba11"></a>

### Automated plotting of film properties

For the surface film solvers there now properties like the mass,
covered surface, thickness and velocity are automatically plotted


<a id="orgecc8d98"></a>

### `pyFoamClearCase.py` automatically executes an existing `Allclean`

If present the script (which is usually found in tutorial cases)
is executed before other cleaning takes places


<a id="orga3fa5ce"></a>

### `pyFoamPrepareCase.py` executes tutorial scripts if available

If there are scripts present from the original tutorials that do
**only** case preparation (like `Allrun.pre`) but no solver running
and no special scripts are present then the original scripts are
executed


<a id="orgb6ecbc6"></a>

### Script for clearing in `pyFoamPrepareCase.py`

If a special script `clearCase.sh` is found this is used for
additional clearing. If instead a script `Allclean` is found then
this is used


<a id="org37f668d"></a>

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


<a id="orgd53256f"></a>

### `pyFoamPrepareCase.py` now allows separate decomposition scripts

After three of the phases

-   mesh creation
-   copying of the `.org` files
-   case setup

the utility executes a script (`decomposeMesh.sh`,
`decomposeFields.sh` and `decomposeCase.sh`) if found. This allows
to adapt for different situations (for instance: the mesh already
being generated in parallel)


<a id="orgdd7349f"></a>

### Runner-utilities now create seperate logfiles on restart

If PyFoam thinks that a run is restarted (old time-files exist and
there already exists a logfile) it creates logfiles with
`.restart` appended. This allows joining the original log and the
restart log


<a id="org6aca9d5"></a>

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


<a id="org873bfd5"></a>

### `pyFoamPackCase.py` adds parallel data

With the option `--parallel` now adds parallel data


<a id="orgba452d3"></a>

### `--replacement`-option in `pyFoamPVSnapshot.py` supports Foam-format

The option can now alternatively use Foam-format instead of Python-format


<a id="orgb4af9e6"></a>

### `pyFoamPVSnapshot.py` improved error messages with problems in replacement

Instead of a stack trace there is now an output of the template
string and the available values


<a id="org6dda1f5"></a>

### `customRegexp` now searched in parent directories

If in the directory of the log-file no `customRegexp` and the
log-file is not in the current directory then PyFoam looks for it
in all directories up to the current directories


<a id="orgd8768ec"></a>

## Enhancements to the Library


<a id="orgf9e776a"></a>

### `Paraview.StateFile` extended

This module has been extended to allow more flexible manipulations
of the state-file


<a id="orgfd92ed4"></a>

### `BasicRunner` now checks for regular End

The `BasicRunner` now checks whether the string `End` was seen and
**no** time-information after that. This means that the simulation
reached its "regular" end and is also reported in the
`PyFoamState.TheState`-file


<a id="org27d0a17"></a>

## Bug fixes


<a id="orgdce2e95"></a>

### `pyFoamPrepareCaser.py` ran out of memory for large script outputs

Because all the output from scripts was stored in memory before
being written to a log it was possible that the utility ran out of
memory when there was much output. The output is now written
directly to disk


<a id="orgc972d07"></a>

### No Courant number plottet if `WM_PROJECT_VERSION` is unset

Scanning for the Courant number defaulted to the versy old
version. This has been fixed


<a id="org9128126"></a>

### Rescale does not work for streamlines in `pyFoamPVSnapshot.py`

`--rescale-color-to-source` did not work for sources that have no
cell values (like streamlines). Fixed.


<a id="orgaff12ad"></a>

### Server not correctly running on Python 2.7 with `socketserver`

Some installations of Python 2.7 already have the
`socketserver`-module which does not have the required
`BaseServer`-module. Fixed


<a id="orgdab6d07"></a>

# Version 0.6.8.1 - 2017-08-03


<a id="org3b02c6d"></a>

## Bug fixes


<a id="org1496a05"></a>

### Fork not correctly detected for `v1706`

As the `+` is not present in the `WM_PROJECT_VERSION` this distro
was detected as the Foundation fork


<a id="org37140b5"></a>

# Version 0.6.8 - 2017-07-06


<a id="org61bcc8d"></a>

## Major changes


<a id="orgd15a4cc"></a>

### `pyFoamNet`-utilities now work without a Meta-Server

As described in other changenotes below the Server process now
announces its presence with ZeroConf. This means that a central
Meta-Server is no longer necessary. But the `zeroconf` library has
to be present on all involved machines (server and client). It is
installed with

    pip install zeroconf


<a id="orgbf78a98"></a>

## New features/utilities


<a id="org8d35ab8"></a>

### Added module `PyFoam.Infrastructure.Authentication`

This module implements a simple public key authentication. For
authentication a username and a challenge are sent. If the
username is in the set of authenticated keys (or is the own
username) then this key is used to check the challenge.


<a id="org2f3f2d4"></a>

## Enhancements to Utilities


<a id="org9cffeed"></a>

### `pyFoamClearCase.py` now has `-dry-run` option

This option doesn't clear anything but prints the things that will
be erased


<a id="org5ac307a"></a>

### New option `--keep-time` for `pyFoamClearCase.py`

This option (which can be specified more than once) allows
specifying single time-steps that should be kept


<a id="org69aec67"></a>

### `pyFoamNetList.py` no longer needs a meta-server to work

Due to the addition of `ZeroConf` this utility no longer needs a
Meta-Server to find running calculations in the same subnet


<a id="orgf75e30c"></a>

## Enhancements to the Library


<a id="org32f6b84"></a>

### Better calculation of used memory in runs

If the `psutil`-library is installed then the memory used by
parallel runs is calculated as well


<a id="org2da406b"></a>

### Pre and post-hooks are now also searched in `PyFoam.Site`

`module` specified in `preRunHook_` and `postRunHook_` is now
searched in `PyFoam.Site.` as well. This module is the
`lib`-directory in the directory specified by the environment
variable `PYFOAM_SITE_DIR` (which allows adding user-scripts and
modules)


<a id="org558753a"></a>

### Adapted to correctly detect `OpenFOAM+ v1706`

This fork has changed its numbering scheme (dropped the `+` in the
version string). This broke a regular expression and a function to
detect the number


<a id="org3660e0d"></a>

## Infrastructure


<a id="orgfb1085a"></a>

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


<a id="org3d5165f"></a>

## Bug fixes


<a id="org4ad67d9"></a>

### `--keep-interval` in `pyFoamClearCase.py` not working for parallel-cases

Due to a copy/past error this option did not work for parallel
cases. This is now fixed


<a id="orga6a6310"></a>

# Version 0.6.7 - 2017-06-04


<a id="org4d933d1"></a>

## Requirements


<a id="org1c08837"></a>

### Now at least Python 2.6 required

The new `PLY`-version and `six` now at least requires this
Python-version. If your system has Python 2.5 or older stick with
PyFoam 0.6.6


<a id="orgdb7dbaa"></a>

## Incompatibilities


<a id="org69f0e3b"></a>

### Names of files generated by `pyFoamPVSnapshot.py` differ

Due to changes in the time-step numbering the names of the
generated files differ. If your work-flow depends on the old names
add the options `--consecutive-index-for-timesteps` and
`--duplicate-times`


<a id="org2f1b8ec"></a>

## New features/utilities


<a id="orgae93ae4"></a>

### Utility `pyFoamListProfilingInfo.py` to print profiling data

The utility reads the profiling info written by

-   foam-extend
-   OpenFOAM+ v1606 (and higher)
-   or the patch found at <https://sourceforge.net/p/openfoam-extend/svn/HEAD/tree/trunk/Breeder_2.3/distroPatches/applicationLevelProfiling/>

and prints it in a human-readable form


<a id="org409dc21"></a>

### Utility `pyFoamBlockMeshConverter.py` to convert a 2D-mesh to 3D

This utility (and the required Libraries) was written by Hasan
Shetabivash (original at <https://github.com/hasansh/blockMeshConverter.git>)

This utility takes a file that is written in a similar syntax as
the regular `blockMeshDict` but with the third dimension
missing. It then converts this file to a regular `blockMershDict`
by either extruding in the $z$-direction or by rotating around the
\(x\) or the $y$-axis


<a id="orgaeff21a"></a>

## Enhancements to Utilities


<a id="org393a8be"></a>

### `customRegexp` now can scan for texts

Until now data items (groups) in the regular expression had to be
valid numbers. Otherwise a warning was issued. This behavior is
still the default but if a list-variable `stringValues` is added
then the items (whose numbers are specified in the list) are not
being plotted. They are written to disk with `--write-files` and
they can be used in `progress`


<a id="orgca71f4e"></a>

### Lines in `PyFoamHistory` escaped

Additions to the history file where arguments contain whitespaces
and/or quotes are quoted and quotes inside are escaped. This
allows these command lines to be copy/pasted to the command line


<a id="org93e03ce"></a>

### `--values-string` of `pyFoamPrepareCase.py` now accepts OpenFOAM-format

These strings are now parsed as OpenFOAM-strings if there is no
starting `{` and no ending `}`. With these the old behavior
(parsing as a Python-dictionary) is used


<a id="org2ab2b5d"></a>

### `pyFoamRunner.py` and `pyFoamPlotRunner.py` allow automatic selection of solver

If for those utilities the word `auto` is written in place of a
proper solver (like `interFoam`) then the utility looks into
`controlDict` for the `application`-entry and uses that


<a id="orgd0aadf8"></a>

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


<a id="org9e0328b"></a>

### Multi-part `idNr` for `dynamic` in `customRegexp`

`idNr` can now alternatively be a list of integers (instead of a
single integer). In that case the corresponding matches are
concatenated (with a `_` between them) to generate the data id.

If only a number is specified it has the old behavior.

As usual the indexes of the matches stat with \(1\) (not \(0\))


<a id="orgb4658c4"></a>

### `pyFoamListCases.py` detects dead runs

If a run has not had any output in the last hour it is listed as
dead. This threshold can be customized


<a id="org37604ef"></a>

### Improved time-handling of `pyFoamPVSnapshot.py`

The utility now numbers the time-steps by the order in the
solution directory. Before that the used time-steps were numbered
consecutively (from \(0\) to \(N-1\) if \(N\) time-steps were specified).

Also: by default each time-step is only processed once

The old behaviour can be reproduced with
`--consecutive-index-for-timesteps` and `--duplicate-times`


<a id="org7ac0172"></a>

### Default plots can be set in configuration

Whether or not plots are plotted automatically (for instance the
execution time) can be set in the `[Plotting]`-section of the
configuration. So it can be set per-case in the
`LocalConfigPyFoam`-file. If a plot is on by default it can be
switched off with the corresponding `--no`-option. If off by
default the `--with`-option switches it on


<a id="org8c8974b"></a>

### `derivedParameters.py`-script called from `pyFoamPrepareCase.py` allows error reporting

In that script that calculates new parameters and also can do
parameter checking there now is a function `error` available that
makes the script and the complete execution fail


<a id="orga3c0c2d"></a>

## Enhancements to the Library


<a id="org45c0e41"></a>

### Detection of new versions of OpenFOAM-foundation and OpenFOAM+

Both distros changed their scheme for the version numbers and the
regular expressions have been adapted to detect them


<a id="org1064347"></a>

### `SpreadsheetData` now handles string data

If one of the columns is string data then the `()`-operator
returns string values (when interpolating the next value)


<a id="orge5ac561"></a>

### `TimelineData` tolerates string values

The class can now read strings without spaces (OpenFOAM `words`)
and pass them to `SpreadsheetData`


<a id="orge8088c5"></a>

### `()` operator of `SpreadsheetData` works without name

If no `name` parameter is given then the method returns a
dictionary with all the values


<a id="org8e3ec8a"></a>

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


<a id="org4813203"></a>

### User-specific temporary directory

The method `PyFoam.FoamInformation.getUserTempDir` makes sure that
a user specific temporary directory exists and returns the path to
that directory


<a id="org088abdd"></a>

### `Gnuplot`-plots now get better titles

Instead of `Gnuplo` the window titles are now set to `pyFoam` and
the actual title of the plots. This should make it easier to find
plot windows in the window manager


<a id="org5f4301c"></a>

### `ParsedParameterFile` now supports `#includeFunc`

In case of a `#includeFunc`-entry the file is either searched
relative to the current file (this is where the semantics differ
from how OpenFOAM because that searches in the
`system`-directory. But as this entry is usually called from
`system/controlDict` the result is the same) and if not it looks
for it in `$FOAM_ETC`


<a id="org3342740"></a>

### New utility function `findFileInDir`

This function in `PyFoam.Basics.Utilities` looks recursively for a
file in a directory


<a id="orgd58f2cf"></a>

### `humandReadableDuration` added to `PyFoam.Basics.Utilities`

This function takes a duration (in seconds) and prints it in a
human-readable form


<a id="orge74212d"></a>

## Infrastructure


<a id="orga488621"></a>

### `pyFoamVersion.py` now reports the versions of the `ThirdParty`-packages

Now these versions are reported as well for quick reference


<a id="org7604823"></a>

## Bug Fixes


<a id="orgc6384a8"></a>

### Application classes fail in Paraview

The class `PyFoamApplication` assumes that the module `sys` has an
element `argv`. This is not the case inside Paraview


<a id="orgb486f56"></a>

### Scripts in `pyFoamPrepareCaseParameters.sh` not working on Mac OS X

Because newer versions of Mac OS X remove `LD_LIBRARY_PATH` from
the environment passed to scripts (for security reasons)
additional libraries (for instance `swak4Foam`) were not correctly
loaded. This has been fixed by generating a special script that
exports `LD_LIBRARY_PATH` before executing the rest


<a id="orga3200d5"></a>

### Processor-directories unsorted in `SolutionDirectory`

The class assumed that `processorX` directories were added in the
numeric order which is not necessarily the case. This caused
problems with `pyFoamCaseReport.py`


<a id="org55c7bc6"></a>

### Deleting failed if a file did't exist

The utility function to delete directories failed if the directory
didn't exist. Fixed


<a id="org928e1f0"></a>

### Missing files in `RegionCases`

When creating a `RegionCase` only the "known" files were
symlinked. This causes some programs to fail. Now everything from
`system` in the master-case is symlinked if there is not already a
file of that name there


<a id="org03b566e"></a>

### Wrong `solver` in `pyFoamListCase.py`

If another utility was run in the mean-time the wrong solver is
listed by the utility. Fixed


<a id="org3014b89"></a>

## ThirdParty


<a id="org79b3864"></a>

### Updated `tqdm` to version 4.8.4

No reason. Just because there was an update


<a id="orgc5d2823"></a>

### Updated `PLY` to version 3.9

This breaks compatibility with Python 2.5 or older


<a id="org0dceff2"></a>

### Updated `six` to 1.10.0

This also breaks compatibiliy with Python 2.5 or older


<a id="orgcb780e2"></a>

# Version 0.6.6 - 2016-07-15


<a id="org44cdd37"></a>

## Incompatibilities


<a id="org22ccbf9"></a>

### Changes in `IPython`-notebooks 3.0

With IPython 3.0 the names of the Widget classes lost the `Widget`
in the name (for instance `DropdownWidget` becomes
`Dropdown`). `PyFoam` has been changed to conform with this but as
a consequence won't work with old version of the `IPython`
notebooks


<a id="org11b4edc"></a>

## Enhancements to Utilities


<a id="org764b137"></a>

### `pyFoamPrepareCase.py` executes `setFields` if appropriate

If no setup-script is specified and if there is a `setFieldsDict`
present then `setFields` is automatically executed


<a id="org248c695"></a>

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


<a id="org12dbede"></a>

### `alternateAxis`-entries now can be regular expressions

This allows specifying plots generated with `type dynamic` on the
alternate axis


<a id="org5bfe67d"></a>

### Plotting utilities now allow choice of Gnuplot terminal

These utilities now allow with the option `--gnuplot-terminal` to
choose the terminal. Otherwise the terminal specified in the
configuration (usually `x11`) is used


<a id="org89c0558"></a>

### Plotting utilities now sort legend by name

Names in the legend are now sorted. This improves readability for
large numbers of lines in the plot


<a id="org609fa23"></a>

### `pyFoamExecute.py` allows calling with debugger

The option `--run-with-debugger` runs the command in the
debugger. The arguments are appropriately handled


<a id="org01dd61a"></a>

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


<a id="orgc564ba7"></a>

### `--hardcopy` in plotting library now allows modification of `gnuplot`-terminals

This option allows setting the options for the terminal selected
with `--format-of-hardcopy`. This overrides any default set in
configuration section `[Plotting]` under the name
`hardcopyOptions_<term>` with `<term>` being the name of the
terminal (for instance for `png` the option is `hardcopyOptions_png`.


<a id="org61c6273"></a>

### `pyFoamPrepareCase.py` writes state information about what it is currently doing

It writes to the usual state file. This way `pyFoamListCases.py`
will list this information. If the scripts call `pyFoamRunner.py`
then this information will be overwritten


<a id="org7dd55ce"></a>

### `pyFoamBinarySize.py` can handle new location of binaries in OpenFOAM 3.0

Since that foam version all binaries (and object files are located
in the directory `platforms`. The utility now finds them there


<a id="orgf50c4c8"></a>

### `Runner`-utilites now can signal on `blink(1)`-devices

With the option `--use-blink1` these utilities now flash on a
plugged in `blink(1)` USB-device for every time-step


<a id="orge2a66b6"></a>

### `pyFoamExecute.py` can flash a `blink(1)`

To indicate that the utility is still running it is able to play a pattern on a
`blink(1)`-device. This is switched on with `-use-blink`


<a id="org0539c2a"></a>

### `pyFoamDecompose.py` allows using a template file

With the option `--template-dict` it is possible to initialize the
output with an existing file. With this file it is possible to add
'complicated' settings.


<a id="org01eae2e"></a>

### `pyFoamTimelinePlot.py` now handles new format of probe files

Probe files now have one comment line per probe to specify the
position. This format is now correctly detected and plotted. Old
probe files are also handled


<a id="org3bdf420"></a>

### `ReST`-report of `pyFoamPrepareCase.py` now reports derived parameters

The `.rst`-file written by the utility now adds a section on
derived parameters if such parameters were specified in a script


<a id="org2f1b2f4"></a>

### `pyFoamPrepareCase` can now ignore directories

It is now possible to specify directories that should be ignored
when looking for templates. Some sensible defaults like
`postProcessing`, `processor*` and `VTK` are already set


<a id="org78f356c"></a>

### `pyFoamConvertToCSV.py` allows adding formulas to XLSX-files

The option `--add-formula-to-sheet` allows adding formulas to the
Excel-sheet. Something like

    --add-formula="massflow:::'inlet'-'outlet'"

adds a column `massflow` that subtracts the columns `inlet` and `outlet`


<a id="orgb8317fd"></a>

### `pyFoamListCases.py` now displays mercurial info

For those who use mercurial to keep track of their cases the
utility now has the option `-hg-info` that displays the mercurial
hash-ID, the local id and the branch name


<a id="orgb7b91c7"></a>

### Progress bar added to utilities with long run-time

Using the library `lqdm` progress bars have been added to
utilities that have a long run-time and where the progress bars
are not disturbing the regular output. These utilities are

-   `pyFoamListCases.py`
-   `pyFoamBinarySize.py`

Bars can be switched off with `--no-progress-bar`


<a id="org6e04b05"></a>

### Utilities that clear data can now report what is cleared

`pyFoamCleasCase.py` and all utilities that have a `--clear`
option now also have a `--verbose-clear` option that reports
**what** is being cleared


<a id="org2a11088"></a>

### `pyFoamConvertToCSV.py` now allows manipulating the input

The utility now has two new options:

-   **&#x2013;strip-characters:** This allows removing characters before the
    file is actually read
-   **&#x2013;replace-first-line:** Replaces the first line (for instance if
    the header does not match the data


<a id="orga337349"></a>

## Enhancements to the Library


<a id="orgf8c597e"></a>

### Detection of `OpenFOAM-dev`

A development installation is now also detected and it is assumed
that this uses the new calling convention. Also: PyFoam reports
this as version `9.9.9` (as this is larger than any version in the
foreseeable future


<a id="org539a5c6"></a>

### Add `OpenFOAM+` as a fork

An additional fork type `openfoamplus` has been added (in addition
to `openfoam` and `extend`). Installations of the form
`OpenFOAM-vX.X+` (with `X.X` being the version number) are added
to this fork. Also `OpenFOAM-plus` is added as the development
version of this fork


<a id="org903eefa"></a>

### Accept new convention for location of `blockMeshDict`

In newer OpenFOAM-versions `blockMeshDict` may be located in
`system`. PyFoam detects it either there or in the old
`constant/polyMesh`-location


<a id="org2a25561"></a>

### Handling of complex data by `Configuration`

Lists and dictionaries now can also be specified. Have to be
correctly formatted if they are longer than one line (indented by
at least one space - convention for configuration files)


<a id="org3e7f5c4"></a>

### `Configuration` has method `getArch` for architecture dependent settings

If an option `opt` is requested with this option then it is
checked whether an architecture-dependent setting exists.
Architecture `arch` is the output of the `uname`-command. The
architecture-dependent name is `opt_arch`.


<a id="orgbfc9087"></a>

### `execute`-method from `PyFoam.Basics.Utilities` returns status-code

This function now has an option that makes it return the status of
the execution as well as the output of the execution.


<a id="orgcccab0b"></a>

### `BasicRunner` now supports more ways of stopping runs

In the past this class (and the utilities based on it) looked for
a file `stop` and stopped the run (with writing) if it was
found. Now two additional files are looked for

-   **stopWrite:** this waits for the next scheduled write and then stops the run
-   **kill:** gracefully stops the run without any writing


<a id="org52e5731"></a>

### Added `Blink1` class to support `blink(1)` devices

This class assumes that a `blink(1)` USB-device is present and the
API-server (from the `Blink1Control`-program for this is
running. It wraps these calls so that utilities can use them
conveniently


<a id="org66d69be"></a>

### `ParsedParameterFiles` now supports `includeEtc`

`#includeEtc` is now supported


<a id="orgffa6268"></a>

### Parses uniform fields correctly

Uniform fields of the form `1002{42.5}` (Field with 1002 values
\(42.5\)) are now correctly parsed


<a id="org34d98bb"></a>

### `toNumpy`-method added to `Unparsed` and `Field`

These two classes have a method `toNumpy` added that transformed
the data into a structured `NumPy`-array. There are no
applications for this in `PyFoam` yet but an application will be
the parsing of lagrangian data


<a id="org01b6800"></a>

### Added module `PyFoam.RunDictionary.LagrangianPatchData` to read data from patch function object

This module reads data written by the cloud function-object that
writes particle data as particles hit the patches and transforms
it into `numpy`-array. Which can also be returned as `pandas`
`DataFrames`

It adds some properties to the data

-   the patch name
-   the time at which this data was written
-   a `globalId` constructed from `origId` and `origProcId`


<a id="org93b7ceb"></a>

### Added module `PyFoam.RunDictionary.LagrangianCloudData` to read cloud data

This gets

-   a case
-   a cloud name
-   a time name and reads the lagrangian data from the specified
    time and converts it to a pandas `DataFrame`

A `globalId` that is consistent with the one in `LagrangianPatchData` is set


<a id="org88d8d6d"></a>

### Method `code` added to =RestructuredTextHelper

This method formats a string assuming that it is a program
code. Default value is `python`


<a id="orgd5e047e"></a>

### `ParsedParameterFile` now parses new dimension format correctly

Newer OpenFOAM-versions allow dimensions in symbolic format (for
example `[ m s^-1 ]`). These are now correctly parsed


<a id="org459b2c6"></a>

### `ParsedParameterFiel` now parses uniform fields correctly

Fields of the form `23 { 4.2 }` (meaning "23 times 4.2") are now
correctly parsed


<a id="org3a35dae"></a>

## Infrastructure


<a id="orga5db4f4"></a>

### Change of documentation from `epydoc` to `sphinx`

As `expydoc` is discontinued the API-documentation is now generated
with `sphinx`. Just run

    make docu

to do so.

Advantage is that now with

    make docset

a document set for offline searching with `Dash` (for Mac OS X) or
clones (on other OSes) can be generated


<a id="org3ff2684"></a>

### Adaptions to the unittests

Untitests only used to run correctly if the OpenFOAM-version was
1.7. Are changed to run with OF 3.0. No effort has been made to
support intermediate versions as the changes are mainly about
changed tutorials


<a id="orgff9a6a7"></a>

## Bug fixes


<a id="orgb28a347"></a>

### Wrong format of `ExecutionTime` breaks plotting utilities

If the `ExecutionTime` is not as expected `pyFoamPlotWatcher.py`
and `pyFoamPlotRunner.py` finish with an error. This is now more
robust


<a id="org12b21e6"></a>

### `phases` not working with dynamic plots

For dynamic plots the addition of the phase name did not work. Fixed


<a id="orge3fca8c"></a>

### Phase name added to function object output

If `phase` was set the output of the function objects got it added
to the names even though the function objects do not belong to the
phase. This is fixed


<a id="org5740171"></a>

### One region mesh too many in utilities that change the boundary

When working with regions one region too many was added in
`pyFoamChangeBoundaryType.py` and `pyFoamChangeBoundaryName.py`. Fixed


<a id="org68c297f"></a>

### `pyFoamClearCase.py` fails on write-protected case

If a case is write protected then the utility failed. Now it only
issues a warning and continues cleaning


<a id="org0349cbc"></a>

### Copying of directories in `pyFoamPrepareCase.py` confused by zipped files

When copying one file to another and one of them is zipped then
copying doesn't replace the destination correctly but adds the
zipped/unzipped variant


<a id="org8fc760c"></a>

### Wrong times for multi-view layouts in `pyFoamPVSnapshots.py`

If snapshots were taken from state files with multiple layouts
then some of the views had the wrong time (either that from the
state-file or from the timestep before). Fixed


<a id="org1e979be"></a>

### First timestep not plotted (and not stored)

The data from the first timestep was not plotted under certain
circumstances. This has been fixed


<a id="org6e33e96"></a>

### `DYLD_LIBRARY_PATH` not passed on *Mac OS X 10.11*

Starting with this OS-version as a security feature the system
does not pass `LD_LIBRARY_PATH` and `DYLD_LIBRARY_PATH` to a
shell. `PyFoam` detects this and creates these variables and makes
sure they are passed to the processes


<a id="orgdd1eded"></a>

### Newer versions of `pandas` broke the writing of excel files with `pyFoamConvertToCSV.py`

The reason is that the old way of making axis data unique did not
work anymore. This has been fixed


<a id="org516ada1"></a>

### Capital `E` in exponential notation for floats breaks parser

This problem has been reported at
<https://sourceforge.net/p/openfoam-extend/ticketspyfoam/220/>
(the number `1E-2` is not correctly parsed to `0.01`) and has been fixed


<a id="org8813466"></a>

### `Runner`-utilities clear processor directories if first time in parallel data differs

In cases where the parallel data has a different start directory
than \(0\) the `pyFoamRunner.py` and similar utilities cleared that
data and made a restart impossible. This has been fixed


<a id="orga37fe0d"></a>

### Utilities `pvpython` not working when installed through `distutils`

As the `distutils` (and all mechanisms built on these like `pip`)
replace the used python in scripts the necessary `pvpython` was
removed. This has been fixed by generating a temporary script file
that is actually executed with =pvpython)


<a id="org92e51c1"></a>

## ThirdParty


<a id="orge68f812"></a>

### Added `tqdm` for progress bars

Add the library `tqdm` (<https://github.com/tqdm/tqdm>) for adding
progress bars to utilities.

Library is under `MIT` License


<a id="orgb0bb6e4"></a>

# Version 0.6.5 - 2015-06-01


<a id="org2a64ea3"></a>

## Major changes


<a id="orgbcba398"></a>

### PyFoam now on *Python Package Index*

PyFoam is now found at <https://pypi.python.org/pypi/PyFoam>

Recommended way of installing is using <https://pip.pypa.io/en/latest/> :

    pip install PyFoam

This will also make sure that the required `numpy`-package is
installed


<a id="org06c2db4"></a>

## Incompatibilities


<a id="org605d6fc"></a>

### `ArchiveDir` in `SolutionDirectory` discouraged

As this was never really used it is discouraged (the option is
still there).

If you don't understand what this means it probably doesn't
concern you


<a id="orgcfcc270"></a>

### Pickled data files now written as binary

All pickled files are now written and read in binary mode (as this
was the only way that works consistently in Python 3). This **may**
cause problems with old cases (but no effort has been made to
check whether this problem actually exists)


<a id="orgda5389e"></a>

### The `PlotRunner` and `PlotWatcher` now don't strip spaces

These two utilities now don't strip leading spaces from the read
lines. This preserves formatting in the output but might break
scripts that rely on these spaces.

The old behaviour may be reset by overriding `stripSpaces` in
section `SolverOutput` with a value `True`


<a id="org6272a7b"></a>

### Different column names in `pyFoamConvertToCSV.py`

The enhanced naming of the columns might break scripts that rely
on the old naming


<a id="orgdac5f04"></a>

### `pyFoamChangeBoundaryName.py` and `pyFoamChangeBoundaryType.py` automatically modify `processorX`

In previous versions these boundary files were not modified. Now
they are. Scripts that rely on unchanged `boundary`-files in the
`processorX`-directories might fail. Old behavior can be set with
the `--no-processor`-option


<a id="org0a7bda4"></a>

## Bugfixes


<a id="org58d0b2b"></a>

### Arbitrary commands in `TemplateFile` passed to file

Lines with `$$` are passed to the file and make it syntactically incorrect.
Fixed


<a id="org509b7e4"></a>

### Pickled files not opened in binary mode

This caused problems in Python 3 were binary strings were not
correctly written (actually: attempts to write them to a
pickle-file made the application fail)


<a id="org4aa177a"></a>

### Additional fixes for Python 3

In a number of classes/applications semantic differences between
Python 2 and 3 makes these fail on Python 3. Changes are

-   Replace `map` with list comprehension where possible
-   Modify wrappings in `CTestRun` to work with Python3
-   Replace `print` with `print_`
-   Semantic difference in division of two integers: Python3 gives a
    floating point number as a result


<a id="org8c8520c"></a>

### `ParsedParameterFile` fails if "complete" dictionary is `#include` ed

If an included dictionary has a header parsing failed. This is
fixed by retrying the parsing with the header


<a id="orga7dd83b"></a>

### `ParsedParameterFile` fails if there is more info after `#include`

If there is for instance a `;` after an `#include` statement the
regular OpenFOAM-parser ignores it. The PyFoam-parser failed. This
has been fixed and the parser behaves like regular OpenFOAM


<a id="orgfa9e172"></a>

### `pyFoamDisplayBlockMesh.py` not working with VTK 6

Due to changes in the API the program did not work. This is now
fixed and the program works with VTK 6 as well as VTK 5


<a id="org2b160ee"></a>

### `pyFoamCreateModuleFile.py` failed with environment variables containing `=`

In that case an overeager `split` created lists.

Fix provided by Martin Beaudoin


<a id="org9ed8fd5"></a>

### Fix import in `GeneralVCSInterface`

Change in the syntax of imports in Python 3 broke this
one. Fixed. But doesn't matter as Mercurial doesn't support
Python3


<a id="org0217e8b"></a>

### Support of old format in `ParsedBlockMeshDict` broken

Wrong usage of indexes. Fixed


<a id="org008ffc3"></a>

### `TemplateFile` not correctly working in Python 3

Reason was a different calling convention to the `exec`-function
of Python. Fixed


<a id="org78a1e62"></a>

### Certain things not done by `pyFoamPrepareCase` in `--quiet` was set

This was due to actions being on the same level as the
debug-output. Fixed


<a id="org4f5ed43"></a>

### Annoying warning at the start of the run

For certain solvers the plot utilities issued a warning during a
phase when no information about the current time is
available. This is now fixed


<a id="org13ba9e0"></a>

### Redirected values

not used when iterating over dictionaries
    When iterating over dictionaries with redirects the values in the
    redirected dictionaries were not used. This is now fixed


<a id="org1fbe617"></a>

### Behavior of Template-engine not consistent in Python3 and Python2

Due to a difference in the behavior of the `eval`-function in
Python 3 certain expressions (especially with list comprehension)
failed. Fixed


<a id="orgf0dd355"></a>

### Braces, brackets, parentheses in column name broke `RunDatabase`

These characters were stripped out by *SQLite*. They are thus
normalized to special character combinations (which will be
denormalized after reading)


<a id="org082e1f4"></a>

### Finding of installations in alternate locations broken

The algorithm to find (Open)FOAM-installations in alternate
locations was broken. Now working again


<a id="org44d2a19"></a>

### Failing on 3.x if socket for server thread already occupied

Due to a a change in the socket API if the socket for the network
thread (usually port 18000) was already notified the program
failed. Fixed. Tested on 2.7 as well


<a id="orgbce9f08"></a>

## Enhancements to Utilities


<a id="org3a83002"></a>

### `pyFoamPrepareCase` recognizes multi-region cases

If there are multiple regions and no `prepareMesh.sh` then it will
try to execute `blockMesh` for the regions


<a id="org312e53e"></a>

### `pyFoamPrepareCase` adds specialized templates

With the option `--extension-addition` additional templates that
override the regular templates can be specified.

Application may be for instance special templates for
`potentialFoam`


<a id="org78552fe"></a>

### `pyFoamPrepareCase` keeps data generated by meshing script

If the meshing stage generates a `0`-directory then data in that
directory will be kept. This can be switched off if this is not
the desired behaviour


<a id="org4db90b8"></a>

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


<a id="org4b0ed9b"></a>

### `pyFoamPrepareCase` writes report about the variables

The utility now writes a *Restructured Text* file with a report
about the variables. Information from `default.parameters` like
groupings and `description` are used in this report. Also the
default value and the actual value are reported.

The file can be converted with a utility like `rst2pdf`


<a id="org59af6bb"></a>

### Gnuplot can be styled with default commands

For all utilities that use Gnuplot as the backend for plotting
there is now a configuration option `gnuplotCommands` in the
`Plotting`-section with the usual `set` commands of Gnuplot. This
is preset to display a grid and the y-axis.

The settings can be reset with the `gnuplotCommands`-list in the
`customRegexp`-entries


<a id="orgd0fa2ed"></a>

### `pyFoamPVSnapshot.py` now supports Paraview 4.2 and later

The API for screenshots changed with Paraview 4.2 and later. This
API now supports layouts if multiple views were specified. The
default behaviour is now to make only one screenshot per
layout. The old behaviour (one screenshot per view) can now be
switched on with the `-no-layouts`-option.

This allows screenshots exactly the way they look on screen


<a id="org9943c06"></a>

### `pyFoamPVSnapshot.py` allows switching between decomposed and reconstructed data

The utility now rewrites the state file so that either decomposed
or reconstructed data is read. The default is that the data set
for which more timesteps exist is selected


<a id="orgab5e1bf"></a>

### `pyFoamPVSnapshot.py` allows changing the field for sources

It is now possible to specify a dictionary with source names and
the fields that should be set for them. This allows quickly
coloring the same layout with different fields.

This works for

-   3D (rendered) filters
-   bar charts


<a id="orgfa6542a"></a>

### `pyFoamPVSnapshot.py` allows rescaling the color-legend

There are now two ways to rescale the color-transfer functions

-   by specifying a dictionary with the ranges
-   by specifying a source. The range of the data on that source
    will be used to scale the data
    -   when specifying a source percentiles can be specified for the
        highest and lowest percent of the cells to be ignored

The first method will override the second


<a id="org307f4f9"></a>

### `pyFoamPVsnapshot` reads parameters written by `pyFoamPrepareCase.py`

An option allows specifying that these parameters should be
read. They are then available for substitution in the *Text*
source


<a id="org06ef952"></a>

### `pyFoamListCases.py` allows filtering

The utility now has options to select the cases that should be
considered by name of the case. Either substrings or globs can be
used. Ignore patterns can be specified as well


<a id="orgebcf6d3"></a>

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


<a id="orgaadf28e"></a>

### `pyFoamConvertToCSV.py` now has all functionality of `pyFoamJoinCSV.py`

Now all functionality of the `Join`-utility is present in the `Convert`
utility (including interpolating times)

`pyFoamJoinCSV.py` will be removed in future versions of `PyFoam`


<a id="orgea2787a"></a>

### `dynamic` in `customRegexp` now allows composition from multiple match-groups

If `idNr` is a list then now the actual id is composed from all
the match groups specified in that list. If `idNr` is an integer
then it behaves like it used to.

Application for the new behavior would be for instance to have the
flow of different species on different patches in one plot


<a id="org2f87595"></a>

### New type `dynamicslave` in `customRegexp`

This combines the properties of the types `dynamic` and `slave`:
dynamically generated data sets that are added to another plot


<a id="org0f5cd56"></a>

### Additional profiling option `--profile-line-profiler`

Uses the library `line_profiler` for profiling. Only of interest
for developers. Experimental


<a id="orgb29003c"></a>

### Utilities that use templates can be customized with the configuration

The section `Template` in the configuration now allows modifying
the behavior of the templating engine (how templates are processed
and syntax details)


<a id="org6df8b6f"></a>

### `LocalConfigPyFoam` now can be read **before** argument parsing

This allows overruling options before they are set be command line
options. This has to be enabled by the application (it doesn't
make sense for all).

An example is the `pyFoamPrepareCase.py`-utility where the local
configuration file can overrule the default behavior of the
template engine


<a id="orgdedd366"></a>

### `pyFoamConvertToCSV.py` automatically selects the output format with `--automatic-format`

Now if that option is selected and the extension of the output is
`xls` the option `-write-excel-file` doesn't have to be set
anymore


<a id="orgbf5b698"></a>

### `pyFoamConvertToCSV.py` allows adding original data as separate sheets

The input data files now can be added to an excel-file as separate
sheets with the `--add-sheets`-option


<a id="org21ce5bd"></a>

### `pyFoamConvertToCSV.py` has improved naming of columns

Now if there is more than one source file then the columns from
the first source also get a unique prefix.

It is also possible to clean the column names before writing them
to file. The time name can be changed with
`-write-time-name`. Substrings can be replaced with
`--column-name-replace` and simple functions can be applied with
`--column-name-transformation`


<a id="org01ec699"></a>

### `pyFoamConvertToCSV.py` now supports sets-files

The utility now can read these files and determine the field names
from the filename. `--automatic` assumes that files with the
extension `.xy` are of this format


<a id="org7dfbd21"></a>

### `pyFoamPrepareCase.py` can calculate derived values with a script

If a script `derivedParameters.py` is present then it is executed
and values set in that script can be used in the templates as well


<a id="org3bf70ed"></a>

### `pyFoamPrepareCase.py` adds a variable `numberOfProcessors`

If unspecified by the user this variable is automatically \(1\). It
can be used by the templates to distinguish between different cases

The `PrepareCaseJob`-class in `ClusterJob` automatically sets the
values according to the number of processors in the cluster job


<a id="orgcaf1ab2"></a>

### `pyFoamChangeBoundaryName.py` and `pyFoamChangeBoundaryType.py` now support decomposed cases

Both utilities now also modify the boundary files in the
`processorX`-direcories. This behaviour can be switched off from the command line


<a id="orgd671909"></a>

### `pyFoamPrepareCase.py` has possibility for templates after the final stage

Templates with the extension `.finalTemplate` are executed after
the `caseSetup.sh`-script.


<a id="orgca14fba"></a>

### `pyFoamRunParameterVariation` allows adding postfix to cloned cases

The option `--cloned-case-postfix` adds a postfix to the cloned
directory names. This can be used if the results from multiple
variations with the same parameter file should be kept (for
instance when comparing OpenFOAM-versions)


<a id="orgdaf89fa"></a>

### `pyFoamConvertToCSV` now allows setting of default input file format

The option `--default-read-format` now allows setting a different
format than `csv` as the default format for input files


<a id="org3751fe2"></a>

### `pyFoamListCases.py` adds the hostname to the printed information

The utility tries to determine from the pickled data the host the
simulation was run on and prints it (can be switched off with an
option)


<a id="org9698b20"></a>

### `pyFoamPrepareCase.py` allows cloning

The utility now has an option `--clone-case` to clone a new case
before starting instead of working in the specified directory (in
this case the case will be cloned to this directory). The name of
the created directory **can** be constructed from the specified
parameters with the `--automatic-casename`-option


<a id="org7d8fecd"></a>

## Enhancements to the Library


<a id="org5730276"></a>

### `SolutionDirectory` detects multiple regions

Valid regions are sub-directories of `constant` that have a
`polyMesh`-directory


<a id="orge53616f"></a>

### `BoolProxy` now compares like builtin `bool`

Comparison used to fail for types where it was not explicitly
implemented like `None`


<a id="orgd4b78aa"></a>

### `PyFoamApplication`-class now supports `pvpython` for debugging

Now `--interactive-after-exception` also works in the utilities
that use `pvpython`


<a id="orge49a8b4"></a>

### `TemplateFile` now allows more flexible assignments

In the mode where executions are allowed now more flexible
assignments to variables are possible. To be specific:

-   array assignments like

    $$ a["t"] = 2

-   multiple assignments like

    $$ a,b = 2,3


<a id="org290bb1f"></a>

### `ThirdParty`-library `six` upgraded to 1.9.0

This library has been upgraded to the latest released version


<a id="org666561e"></a>

### Additional markup in `RestructuredTextHelper`

There are additional methods `emphasis`, `strong` and `literal`
that wrap their arguments in the appropriate markup

The methods `bulletList`, `enumerateList` and `definitionList`
take lists or dictionaries and mark them as lists


<a id="org70b96ba"></a>

### `SpreadsheetData` can now read files produced by the `sets`-functionObject

If the option `isSampleFile` is set then it is assumed that the
field names are in the filename and there is no header with field
names in the file


<a id="orgcd2d99c"></a>

## Infrastructure


<a id="org76ec865"></a>

### Adaption of Debian packaging to new conventions

By Oliver Borm. The building of Debian packages for Python
libraries has changes. Necessary adaptions were done by Oliver Borm


<a id="org31d20c2"></a>

## Development changes


<a id="orgd9038ed"></a>

### Now uses `pytest` for unittesting

The `nose`-library had problems and all the unit-tests run
out-of-the-box with `pytest`


<a id="orgb583977"></a>

# Version 0.6.4 - 2014-11-24


<a id="org003d25d"></a>

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


<a id="org62af32f"></a>

## Future changes


<a id="org839a772"></a>

### Redundant utilities `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py` unified

These two utilities are almost indistinguishable and will be
unified into one


<a id="orgaca131b"></a>

## Major changes


<a id="org8fcec76"></a>

### Multi-line regular expressions in `customRegexp`

If in `customRegexp` an `expr` is found with `\n` then this
expression is matched over multiple consecutive lines. Types like
`dynamic` work as usual.

This makes it possible to match for instance the output of the
`forces`-function objects


<a id="orgc2967f2"></a>

### Enhancement of `pyFoamPrepare.py`

The utility which was introduced in the last version is becomong
more usable and will be central to all things that set up the case
(for instance a special `ClusterJob`)


<a id="org77fe244"></a>

### Enhancements of the CSV-utilities

These utilities are now more flexible and allow writing and
reading of Excel-files too


<a id="org8604eb9"></a>

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


<a id="org0ed9dae"></a>

## Incompatibilities


<a id="org2eabe5e"></a>

### Option `--silent` removed from `pyFoamPrepareCase.py`

Option has been renamed to `--no-complain`


<a id="orga395f9b"></a>

### Keys in `RunDatabase` with column-names that contain upper-case letters change

SQLite does not support case-sensitive column-names (`s_max` and
`S_max` are the same). To change this the upper case letters in
the column names are replaced by an underscore and the letter
(`S_max` becomes `_s__max`)

This means that old databases might not be read correctly


<a id="org0085a21"></a>

### Change in unique variable names in `pyFoamConvertToCSV.py`

The algorithm to make variable names unique has changed (basically
it uses the part of the filenames that differ) and scripts relying
on these names might fail


<a id="orgff51a8e"></a>

### `PyFoam.IPython`-module renamed to `PyFoam.IPythonHelpers`

The name of the module crashed in certain instances (especially
unit-testing) with the regular `IPython`-library. To avoid these
crashes it has been renamed to `IPythonHelpers`. This raises two
potential problems:

-   scripts that `import` the module have to be adapted to the new name
-   IPython-notebooks created with `pyFoamIPythonNotebook.py` have
    two imports pointing to this module. These notebooks have to be
    adapted to be usable again


<a id="org72f141b"></a>

## Bugfixes


<a id="org6cade50"></a>

### Templates in `pyFoamPrepareCase.py` did not keep permissions

This was a problem for script-templates which were not executable
any more. Fixed


<a id="org67a20e2"></a>

### `pyFoamComparator.py` failed due to circular dependency

This has been fixed by adding an import in `BasicRunner.py`


<a id="orgc1ec398"></a>

### `pyFoamDumpRunDatabaseToCSV.py` fails if Pandas-data is requested

This is now fixed


<a id="org309d908"></a>

### `sort` for list broke code on Python 3

Some calls for `sort` still used the `cmp`-parameter which does
not exist for Python3 anymore. These calls have been replaced with
`key` and `reverse`


<a id="org50d04c4"></a>

### Changing the OF-version does not work in Python 3

Because the output of `subprocess` is now *binary* instead of a
regular string. Fixed


<a id="org9d1b9bd"></a>

### `addData` in `PyFoamDataFrame` extrapolates for invalid values

This was due to incorrect use of the `interpolate`-method


<a id="org8f75a51"></a>

### `--keep-last` did not work for `pyFoamClearCase.py` and parallel cases

This was because there was a problem in the library code and the
utility did not consider the parallel time-steps. Fixed


<a id="org18b337c"></a>

### `pyFoamDumpRunDatabaseToCSV.py` does not add basic run information

Basic run information was not added to the file. Now it is with
the prefix `runInfo//`


<a id="org6e92d1c"></a>

### Restore of `FileBasisBackup` did not work

The logic for checking whether a file was "backupable" was
wrong. This affected the proper restore of files with utilities
for instance for `--write-all`


<a id="org88c5ea5"></a>

### Remove circular dependency in `DataStructures`

According to the bug
<http://sourceforge.net/p/openfoam-extend/ticketspyfoam/219/> it was
not possible to import `DataStructures` because of a circular
dependency with `FoamFileGenerator`. Fixed by moving an import to
the back of the file


<a id="orgadafbf4"></a>

## New features/Utilities


<a id="org79948ab"></a>

### `pyFoamRunParameterVariation.py`

This utility takes a template case and a file specifying the
parameter variation and creates cases with the
`pyFoamPrepareCase.py`-engine, runs a solver on these cases and
collects the data into a database. The database can then be
extracted with `pyFoamDumpRunDatabaseToCSV.py`


<a id="orga991c24"></a>

### `pyFoamBinarySize.py`

Calculates the size of the binaries in an OpenFOAM-installation
separated by compile-option


<a id="org6322319"></a>

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


<a id="org94fec6b"></a>

## Enhancements to Utilities


<a id="orgce5d174"></a>

### `pyFoamChangeBoundaryType.py` allows setting additional values

The option `--additional-values` allows specifying a dictionary
with additional values for the boundary (stuff that is needed by
`mappedWall` etc)


<a id="orge764967"></a>

### `pyFoamPrepareCase.py` now has OF-version and fork as defined variables

This allows to write case-templates that can distinguish between
different OF-versions


<a id="orgc78f053"></a>

### `pyFoamPrepareCase.py` now allows "overloading" another directory

Before doing anything else the contents of different directories
are copied into the current case. This allows for instance to use
tutorial cases as the basis for a case


<a id="orgf5062f5"></a>

### `pyFoamIPythonNotebook.py` adds improvements to the notebook

Additional code added to the generated notebook:

-   Code to change the default size of the plots
-   Distribution-directories in subdirectories `distributions`
    (generated by some `swak`-function objects) added


<a id="orgef968c1"></a>

### `pyFoamListCases.py` more tolerant to faulty `controlDict`

If the `controlDict` is acceptable to OpenFOAM but syntactically
incorrect for PyFoam (for instance because of a missing semicolon)
the utility does not fail anymore (but no data is collected for
that case).


<a id="org9c3d5f9"></a>

### `pyFoamDumpConfiguration.py` prints sections and keys alphabetically

This should make it easier to find items


<a id="org86640e3"></a>

### `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py` read and write Excel-files

Both utilities now allow writing Excel-files

In addition to regular text files the first sheet from `xls`-files
can be read


<a id="orge737cb9"></a>

### Flexible variable filtering in `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py`

Now it is possible to filter for regular expressions

The functionality of the two utilities now is very similar and it
is possible that one of them will be discontinued


<a id="org8ad3af9"></a>

### Columns in `pyFoamJoinCSV.py` and `pyFoamConvertToCSV.py` can be recalculated

The two utilities now can add columns or recalculate columns
based on the existing column values


<a id="org778a4d0"></a>

### Testing for `Numeric` removed from `pyFoamVersion.py`

Testing for the library `Numeric` library removed as it is no
longer supported as a fallback for `numpy`. Test also removed from
`setup.py`


<a id="org9e9cf9b"></a>

## Enhancements to the Library


<a id="org895c395"></a>

### Subclass of `ClusterJob` that support `PrepareCase`

The class `PrepareCaseJob` supports cases that are set up with
`pyFoamPrepareCase.py`. Additional parameters to the constructor are

-   the name of the parameter-file
-   a list with the parameters. The list is composed of
    name/value-pairs


<a id="orgd2920b9"></a>

### Subclass of `ClusterJob` that support `RunParameterVariation`

The class `VariationCaseJob` supports cases that are set up with
`pyFoamRunParameterVariation.py`. Additional parameters to the constructor are

-   the name of the parameter-file
-   the name of the variations-file


<a id="org214f11d"></a>

### `execute` in `PyFoam/Utilities` fails if script is not executable

The function checks if the file exists and is **not**
executable. The program fails in that case


<a id="orgeb59443"></a>

### `foamVersion` uses a separate wrapper class for `tuple`

This ensures that it is printed in a form that is valid in
OF-dictionaries


<a id="org1a1a01a"></a>

### Move calculation of disk usage to `Utilities`

This has until now only been used in `ListCases` but moved to a
separate method/function `diskUsage` in the `Utilities`-module


<a id="orgeaa21e2"></a>

### Enhancement of `--help`

Added the possibility to have an epilog and usage examples with
the `epilog` and  `examples`-keyword arguments for applications.

These and descriptions now have the possibility for line-breaks:
if two line-breaks are encountered in the text a new paragraph is
created


<a id="orge32158f"></a>

### `which`-routine in `Utitlities` uses native Python-routine

For Python-version where `shutil` has a `which`-function this is
used instead of calling an external program


<a id="orga9874b1"></a>

### `FileBasis` now allows file handles instead of the filename

This currently only works for reading, Backups, zipping etc won't
work but it makes algorithms more flexible


<a id="orgf523b19"></a>

### `BlockMesh` doesn't force writing to file anymore

Instead content is stored in memory. Old behaviour is the default
to preserve compatibility with old scripts


<a id="orgcee7e38"></a>

### Additional methods for `BlockMesh`-class

-   **numberVertices:** Adds comments with the vertex numbers to the
    vertices


<a id="orgee9cc94"></a>

### `LineReader` allows keeping spaces on left

Previous behaviour was stripping all spaces from the lines. Now
the left hand spaces can be ket. Old behaviour is still default
for compatibility


<a id="orgdc2cbfd"></a>

### `TemplateFile` now allows writing of assignment-results in file

This allows faster debugging of template-files. This can be
enabled with a switch in the utilities using templates


<a id="orgdac0a22"></a>

### `SolverJob` now allows passing of parameters to the solver

And additional parameter `solverArgs` will now be passed to the
solver (if the solver accepts arguments)


<a id="org0f22196"></a>

### `SpreadsheetData` now allows reading from an Excel file

During construction if an Excel-file is specified and the
`xlrd`-library and `pandas` are installed then the first sheet in
the file is read


<a id="org4015342"></a>

### `SpreadsheetData` allows recalculating columns

Columns can be recalculated using expressions. This includes other
data items. Currently present column names are available as
variables. There is also a variable `data` that can be subscripted
for items that are not valid variable names. A variable `this`
points to the item to be recalculated


<a id="orgca1f60e"></a>

## Known bugs


<a id="orgfc34162"></a>

### Timelines not forgotten for multiple runner calls

This manifests with `pyFoamRunParameterVariation.py`. The custom
timelines are still kept in memory. Not a problem. Just annoying


<a id="org23f752f"></a>

# Version 0.6.3 - 2014-06-23


<a id="orgf8034c1"></a>

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


<a id="org07477c5"></a>

## Major changes


<a id="org328e3ac"></a>

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


<a id="org8a6df25"></a>

## Incompatibilities


<a id="orgc54dd56"></a>

### Change of command interface of `pyFoamSTLUtility.py`

The selection of what is to be done is now selected by subcommands
instead of options. This will break scripts using this


<a id="org6f56424"></a>

### If `0.org` is present `pyFoamCloneCase.py` and `pyFoamPackCase.py` ignore `0`

The reason is that the utilities assume that this directory is
produced from `0.org`


<a id="org5a5719a"></a>

## Bugfixes


<a id="orgfd7cfe9"></a>

### PlotWatcher has long times between updates if pickling takes long

The reason was that it used the same throttling that made sense
for the PlotRunner. Fixed


<a id="org14e3955"></a>

### `pyFoamPVSnapshot.py` fails for newer paraview-versions

Reason is that the class `vtkPythonStdStreamCaptureHelper` does
not support `isatty`


<a id="org6ff7087"></a>

### SamplePlot failed when valueNames are unspecified

Reported in
<https://sourceforge.net/apps/mantisbt/openfoam-extend/view.php?id=208>
and fixed


<a id="org8ab7cea"></a>

### `pyFoamTimelinePlot.py` failed Numpy/Pandas output of vector fields

Vector fields only were added to the data fields if they were the
first in the list. Fixed


<a id="orgcca73de"></a>

### `alternateAxis` ignored for slave

This is now fixed. The alternate values have to be specified in
the master (specifying in the slave gives an error)


<a id="org44a2314"></a>

### `pyFoamCaseReport.py` more stable for binary `boundary`-files

Usually these files are `ascii` (even if the header says
`binary`). In some cases the parsing failed for these. Fixed by
enforcing reading as `ascii`. Can be switched off


<a id="org917fa9a"></a>

### `SpreadsheetData` returns data which breaks certain Pandas-operations

The reason was that if there were duplicate times in the table the
index was non-unique which certain Pandas-operations don't
appreciate. Solved by dropping duplicate times. Can be switched off


<a id="org23fe4e7"></a>

### `pyFoamCloneCase.py` added duplicates to the archive

If things are specified twice they were added twice. Now it is
checked whether the item already exists in the tar-file before
adding them


<a id="org6ff5fcc"></a>

### `nonuniform` of length 3 not correctly printed

The reason was that this was interpreted as a vector and the
numeric prefix was removed. Reported at
<http://sourceforge.net/apps/mantisbt/openfoam-extend/view.php?id=218>

Fixed by introducing an extra parameter to `FoamFileGenerator`


<a id="org1f17340"></a>

## New features/Utilities


<a id="org52435d1"></a>

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


<a id="org4a8e42c"></a>

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


<a id="orgf4a4b34"></a>

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


<a id="org61fbd28"></a>

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


<a id="org7d81761"></a>

## Enhancements to Utilities


<a id="org386c115"></a>

### `pyFoamSampleplot` has option to use index instead of time in filenames

The option `-index-instead-of-filename` switches this on. This
makes it easier to generate movies from the files


<a id="orgc1388cd"></a>

### `pyFoamListCases.py` Allows addition of custom data

The option `--custom-data` now allows the specification of custom
data items. These are read from the `pickledData`-files and
displayed in the table like regular data items


<a id="orgf3ba76b"></a>

### Switch compiler versions

Now all utilities allow switching the compiler version (for
instance from `Gcc47` to `Gcc48`). The relevant options are
`--force-system-compiler`, `--force-openfoam-compiler` and
`--force-compiler`


<a id="org776ef5e"></a>

### `pyFoamVersion.py` reports the installed versions better

Now the location of the installations is reported as well


<a id="org2dc39f1"></a>

### Offscreen rendering can be switched off in `pyFoamPVSnapshot.py`

This is a workaround where the writer produces a segmentation
fault


<a id="org0eb4dab"></a>

### Write 3D-data in `pyFoamPVSnapshot.py`

In addition to writing out bitmaps allows writing out 3D-data (for
importing into other applications). Sources can be selected by name


<a id="org2cf8644"></a>

### Added capabilities to `pyFoamSTLUtility`

The utility can now also:

-   erase selected patches
-   merge selected patches into one


<a id="org33b85bf"></a>

### `pyFoamDecomposer.py` switches off function objects

This now automatically happens for OF-versions that support
it (2.0 and greater). They can be switched on again


<a id="org6e555af"></a>

### `pyFoamCloneCase.py` clones more stuff

Files that are assumed to be used by `pyFoamPrepareCase.py` are
automatically added to the clone. This includes all files (and
directories) with the extensions `.sh`, `.template` and
`.org`. Also IPython notebooks (extension `.ipynb` are added)


<a id="org5f09e8e"></a>

## Enhancements to the Library


<a id="org9301875"></a>

### `BasicRunner` now can print the command line that is actually used

This should help with diagnosing problems with MPI etc.

Can be switched on in some utilities with `--echo-command-prefix`


<a id="org8461a15"></a>

### `ClusterJob` now can live without a machinefile

Using the machine-file now can be switched off for job-schedulers
with a tight integration


<a id="orgcbccb06"></a>

### Enhanced treatment of symlinks during cloning

If a item in the case itself is a symlink then it used to be a
copy of the file the symlink is pointing to. Now it is created as
a symlink to the target the original symlink. If the
`--follow-symlink`-option is used the old behaviour is used
(copying). In this case the option `noForceSymlink` in the
`Cloning`-section of the configuration can be used to change this
behaviour for selected files


<a id="org3dbbb2a"></a>

### `AnalyzedCommon` clears the `analyzed`-directory

The directory is cleared if it exits from a previous run.


<a id="org09cfc42"></a>

### `TimelineDirectory` is more tolerant

Used to fail if incompatible data types were used. Now ignores
them


<a id="org057684a"></a>

### Possibility of a subcommand-interface for utilities

The subclass `SubclassFoamOptionParser` now allows the parsing of
subclasses. The base class for utilities `PyFoamApplication` now
supports this as an option. As an example this is implemented in
`pyFoamSTLUtilities.py`


<a id="org70e65c2"></a>

### `STLUtility` accepts file-handles

The class checks whether arguments are filehandles and in this
case doesn't try to open a file for reading or writing but uses
the handle


<a id="org6c177ef"></a>

### `addClone` in `SolutionDirectory` accepts glob patterns

If no file matching the name is found it is assumed that this is a
glob-pattern and all matching files are added. This affects all
utilities that use that method (especially `pyFoamCloneCase.py`)


<a id="orgedef9ce"></a>

### `execute` in `Utilities` allows specification of working directory and echoing of output

This method now allows the specification of a working
directory. Before executing the command the method changes to the
working directory. Afterwards it changes back to the regular
working directory.

There is also an option `echo` that immediately prints the output
to the screen


<a id="orgf82b9ae"></a>

### `rmtree` and `copytree` more tolerant

`rmtree` now also works if the "tree" is a file.

`copytree` now has a parameter `force` that allows removing the
destination directory if it exists


<a id="org8dada90"></a>

### Enhanced support for booleans in the parser

Strings that are usually interpreted as boolean in OF-dictionaries
(for instance `on`, `yes`, &#x2026;) are now stored as a special type
that allows treating them like 'real' booleans.

For instance an expression `test no;` in a dictionary now allows
things like `if d['test']:` in the script


<a id="orgb1148d6"></a>

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


<a id="org26bdb00"></a>

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


<a id="orgc24b366"></a>

### `pyFoamSamplePlot.py` now more flexible for distributions

Tries to determine the names of the values from the first line in
the files


<a id="orgad91e46"></a>

### `DictProxy` now has a `dict`-like `update`-method

This also allows enforcing string values


<a id="org0b3e2a5"></a>

### `FoamFileGenerator` automatically quotes strings

If strings are unquoted but contain characters that make it
illegal as a word then the string is quoted before output


<a id="orgdb0a996"></a>

### Children of `FileBasis` now can be used with the `with`-statement

This mainly concerns `ParsedParameterFile`


<a id="orgcf3c6ef"></a>

# Version 0.6.2 - 2013-11-03


<a id="orgbba5797"></a>

## Major changes


<a id="org29d7d86"></a>

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


<a id="org2df2350"></a>

## Incompatibilities


<a id="orgfd26b9d"></a>

### Different separator for databases in CSV-files

The class `RunDatabase` (and therefor also the utility
`pyFoamDumpRunDatabaseToCSV.py`) now write as a separator for data
from sub-tables a `//` instead of the space. This especially means
that scripts that rely on a data-item `foo` in `analyzed` might
break because this is now called `analyzed//foo` instead of
`analyzed foo`. On the other hand this makes the names more
consistent and easier to parse as `//` is the saperator for other
levels of dictionaries


<a id="orgdcb1ff3"></a>

### Change of independent variable name in sample data

Instead of `col0` this is now `coord`. This could cause problems
with scripts that use that column name in the resulting
`SpreadsheetData`-object


<a id="org5afc8ef"></a>

## Bugfixes


<a id="org586889d"></a>

### `pyFoamPackCase.py` does not handle symbolic links correctly

Symbolic links were copied as is and did not work correctly
afterwards. This is fixed. If the symbolic link is an absolute
path or points outside the case directory it is replaced with the
file it points to. Otherwise it is preserved as a symbolic link


<a id="org294699e"></a>

### `pyFoamPotentialRunner.py` not working with OpenFOAM 2.0 or newer

These versions require an entry `potentialFlow` in the
`fvSolution`-file instead of the old `SIMPLE`


<a id="org7914291"></a>

### `pyFoamListCase.py` fails with `controlDict` that use preprocessing

Fixed by first trying to read that with preprocessing. Without if
that fails


<a id="org4bcacca"></a>

### Cloning fails in symlink-mode if files are specified twice

Now using a `set` instead of a `list` makes sure that no file is
cloned twice


<a id="org4474c2b"></a>

## Utilities


<a id="org6424e3f"></a>

### `pyFoamPotentialRunner.py` now allows removing of `functions` and `libs`

The utility now allows removing these entries in case that they
don't work with `potentialFoam`


<a id="org38df037"></a>

### The Runner-utilities now have more options for clearing

Some of the options of `pyFoamClearCase.py` for clearing cases
(for instance specifying additional files) have been ported to the
`Runner`-utilities. Also is the `postProcessing`-directory
removed by default


<a id="orgc58deae"></a>

## Library


<a id="orgd220fa3"></a>

### `SolutionDirectory` and `TimeDirectory` are more tolerant

If there are field files and their zipped counterpart than
instead of an error a warning **can** be given


<a id="org269020f"></a>

### `ClusterJob` now handles template files

A new method `templateFile` gets the name of a file which is
constructed from a template of the same name plus the extension
`.template`


<a id="orgc53aa1d"></a>

### Additional parameters in `ClusterJob`

The method `additionalParameters` can return a dictionary with
additional parameters


<a id="org87c3e9a"></a>

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


<a id="org77d40cd"></a>

### `SolverJob` now allows compression of output

The parameter `solverLogCompress` compresses the log-file while
writing it to disc. **Attention:** This may lead to corrupted
log-files if the run crashes


<a id="org09dbf20"></a>

### `PyFoamApplication`-class now allows quick access to data

The dictionary returned by `getData()` now allows access to all
the elements as attributes.


<a id="org11fca3f"></a>

## New features/Utilities


<a id="org5647355"></a>

### Post-run hook that sends mail at the end of run

The hook-module `MailToAddress` sends a mail at the end of a
run. Prerequisite is an SMTP-Server that doesn't need
authentication


<a id="org58e1362"></a>

### New utility `pyFoamCompressCases.py`

This utility goes through cases and compresses single files. The
cases can be searched recursively to.

Purpose of this utility is to shrink cases where
`writeCompression` was not turned on during the run


<a id="orgc8a1e50"></a>

### Paraview-module to read additional data

A new module `PyFoam.Paraview.Data` reads additional data usually
written by OpenFOAM. These are converted to `vtkArray` using the
following functions and can be used in `Programmable filters`:

-   **setSampleData:** reads the data from sampled sets
-   **setTimelineData:** reads data from a timeline directory
-   **setPlotData:** reads pickled plot data using `RedoPlot`


<a id="org410d311"></a>

## Enhancements


<a id="org8c65d40"></a>

### `pyFoamRedoPlot.py` can plot in XKCD-mode

When used with the option `--implementation=xkcd` and version of
`matplotlib` that supports it is installed then plots are done in
the style of the webcomics <http://xkcd.com>


<a id="org9ce7042"></a>

### `pyFoamListCases.py` now displays disk usage in human readable form

If the disk usage of the cases is calculated then it is displayed
in human readable form (as KB, MB, GB or TB) for sizes larger than
one Kilobyte


<a id="orge645728"></a>

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


<a id="org7cd1103"></a>

### `pyFoamFromTemplate.py` automatically chooses template and default values

If an output file `foo` is specified and no template then the
utility looks for a file `foo.template` as a template.

If a file `foo.defaults` is present then this file is read and
used as default parameter values. Other specifications override
these defaults


<a id="orgfcf0e0b"></a>

### `pyFoamDumpRunDatabaseToCSV.py` can disable standard-fields

Additional option `--disable-run-data`


<a id="org9191f51"></a>

### `pyFoamDumpRunDatabaseToCSV.py` prints `pandas`-object

With the `-pandas-print`-option a `DataFrame` is generated and
printed


<a id="org16bcdbb"></a>

### Better debugging with `ipdb`

If the `ipdb`-package (basically `pdb` with `IPython`-additions)
is installed then it is used. This gives additions like
tab-completion


<a id="org45dc6f6"></a>

### Interactive shell after execution for utilities

The option `--interactive-after-execution` drops the user to an
interactive shell where the namespace can be inspected. If present
`IPython` will be used, otherwise the regular shell is used


<a id="orga17f0f9"></a>

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


<a id="orgd41c013"></a>

### Utilities that read quantitative data write Excel files

The utilities `pyDumpRunDatabaseToCSV.py`,
`pyFoamTimelinePlot.py`, `pyFoamSamplePlot.py` and
`pyFoamRedoPlot.py` now have options to write Excel-files


<a id="org4af6a1e"></a>

### Specify additional settings for `GnuPlot` in `customRegexp`

If an item in `customRegexp` has an item `gnuplotCommands` then
it is assumed that this is a list of strings which are executed
before the first plotting. For instance

    gnuplotCommands (
       "set format y '%.2e'"
     );

changes the number format on the y-axis


<a id="org57ba2bb"></a>

### More flexible data specification for `pyFoamSamplePlot.py`

Instead of determining the names of the fields and lines form the
filenames it is now also possible to specify them through options.

The option `--is-distribution` is a shorthand that sets these
options for distribution files


<a id="orgf916f53"></a>

### `pyFoamSamplePlot.py` now allows specification of x-range

The range of the x-axis of the plots can either be set by
automatically scaling to the domains of all the data sets with
`--scale-domain` or by specifying them with `--domain-minimum` or
`--domain-maximum`.

These domains are set for **all** plots


<a id="org9fab04c"></a>

# Version 0.6.1 - 2013-05-24


<a id="org139fdad"></a>

## Major changes


<a id="orgddd0e18"></a>

## Bugfixes


<a id="org55e95de"></a>

### Restoring of `controlDict` after `write`

When activating an on-demand write the `constrolDict` was not
restored because the output-line about the file being read was not
recognized (due to a change in the output in recent
OF-versions). Now a number of different formats is recognized


<a id="org42302ac"></a>

### Custom-plot type `slave` not working if no `master` defined

That plot-type needs a `master`. Fixed to fail if none is defined


<a id="org41afdcd"></a>

### `-list-only` did not correctly parse lists with a numeric prefix

This did affect all utilities that use that option and also calls
with `listOnly` to the library class


<a id="orgb277feb"></a>

## Utilities


<a id="org6976440"></a>

### `pyFoamBuildHelper.py` now allow more than one action

If multiple actions like `--update` and `--build` are specified
they are executed in a sensible order (update before build etc)


<a id="orgb468973"></a>

### Utilities warn if OpenFOAM-version is unset

If the environment variable that determines the OpenFOAM-version
is unset a warning is issued by the utilities


<a id="orgeba72a6"></a>

### `pyFoamUpgradeDictionariesTo20.py` allows single files

If  single file is specified then the action to transform it has
can be specified


<a id="orgdbd9fb9"></a>

### `pyFoamUpgradeDictionariesTo20.py` transforms reaction-schemes

Now knows how to transform "old" reaction files (where the
`reactions`-entry was a list) to the new format (where it is a
dictionary). Only a limited number of reaction types is supported.


<a id="org8575c44"></a>

### `pyFoamUpgradeDictionariesTo20.py` transforms thermophysical data

Now the old form of thermophysical data (lists) is transformed
into the new dictionary-form


<a id="org1c75bdb"></a>

### `pyFoamCloneCase` now allows creating directory that symlinks to the original

Now with the option `--symlink-mode` instead of copying the
directories from the original new directories art created and
populated with symlinks to the files in the original. The depth
until which no symlinks to directories are created can be
specified. This allows the clone to share the configuration files
with the original


<a id="org6fd7dc0"></a>

### `pyFoamClearCase.py` now removes `postProcessing` and allows removal of additional files

The directory `postProcessing` is now automatically removed (can be
switched off with `--keep-postprocessing`). Also with the
`--additional`-option patterns with additional files to remove
can be specified.


<a id="orgcb53b2e"></a>

### Improvements to `pyFoamVersion.py`

-   Now reports the location of the `python`-executable
-   Reports locations of used libraries


<a id="org6a0aaf9"></a>

### Additional files automatically cloned

The files `Allrun`, `Allclean` and `0.org` are automatically
added during cloning as these are often used by the standard-utilities


<a id="orga53001f"></a>

### `pyFoamDisplayBlockMesh.py` uses the same options for template format as `pyFoamFromTemplate.py`

This makes sure that templates are handled consistently and also
allows different delimiters in the `blockMeshDict.template`


<a id="org4ca467e"></a>

## Library


<a id="orgf4d71dd"></a>

### Improvements in syntax of `ParsedParameterFile`

-   Now the new relative scoping that was introduced in OF 2.2 is
    supported


<a id="org30849b4"></a>

### `Utilities`-class now function to find files matching a pattern

Added a function `find` that approxiamtes the `find`-command


<a id="org6e8ab7d"></a>

### VCS ignores more files

Some more patterns have been added that will be ignored in a
VSC-controlled case. All of them concerning files that PyFoam
creates during operation


<a id="org44b801a"></a>

## New features/Utilities


<a id="org5ac96f0"></a>

### New Utility `pyFoamSymlinkToFile.py`

This utility replaces a symlink with a copy of the
file/directories it points to. To be used after a
`pyFoamCloneCase.py` in `--symlink-mode`


<a id="orgf454d98"></a>

# Version 0.6.0 - 2013-03-14


<a id="org5bde096"></a>

## Major changes


<a id="org11c4903"></a>

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


<a id="org3e8deeb"></a>

### New ThirdParty-Libraries

-   **six:** Library that helps supporting Python 2 and Python 3 in
    the same source code. Currently version 1.2 from
    [<https://bitbucket.org/gutworth/six>] is used
-   **pyratemp:** Templating library to support the new templating
    format. Version 0.2.0 from
    [<http://www.simple-is-better.org/template/pyratemp.html>]
    is used


<a id="org916aef9"></a>

### Porting to `Windows`

Port to allow running PyFoam on Windows was done by Bruno Santos
of blueCAPE (bruno.santos@bluecape.com.pt)

Patch was originally posted at
<http://sourceforge.net/apps/mantisbt/openfoam-extend/view.php?id=166>

**Note**: many of PyFoam's features are not yet fully functional on
Windows.


<a id="orgd7c7d8d"></a>

### Experimental port to `pypy`

Sources are executed in `pypy` but it seems there are problems
with `numpy` and also with code like `for l in open(f).readlines()`


<a id="org87ecdda"></a>

## Third-Party


<a id="orgb0a3bde"></a>

### Upgraded `ply` to 3.4

This brings virtually no changes. `README` with copyright
information has been added


<a id="orgb7fdb24"></a>

## Infrastructure


<a id="org4049378"></a>

### Parameters can't be modified in `CTestRun` after initialization

This should help to avoid side-effects


<a id="org8993dcc"></a>

### Treat timeouts in the `MetaServer` right

Due to a previous workaround timeouts when collecting information
about new machines was not treated correctly


<a id="org76f4369"></a>

### Add `execute`-method to `ClusterJob`

This allows the execution of a shell-script in the directory of
the case


<a id="org5b7506a"></a>

### Add possibility to run specific modules before or after the solver

These modules are found in `PyFoam.Infrastructure.RunHooks`. Two
concrete implementations:

-   **`PrintMessageHook`:** to print a text to the terminal
-   **`SendToWebservice`:** encode an URL and send it to a webservice
    (example for `pushover.net` added)

Hooks are automatically instantiated from the configuration data
(examples are hardcoded))


<a id="org3822c98"></a>

### Parameters added to the info about the run

The Runner-classes now have a parameter `parameters`. This data
(usually it would be a dictionary) is added verbatim to the run
info.

Most runner applications now have the possibility to add this
info.

Purpose of this facility is to identify different runs in the
database better.


<a id="org482fbf9"></a>

### Parameter handling in `ClusterJob` extended

Parameter values are now handed to the actual job. Also a
dictionary with parameters can be handed to the constructor and
will be used in the relevant callbacks


<a id="org2b4f02d"></a>

### Run data written alongside `PickledPlots`

During the run whenever the `PickledPlots`-file is written a file
`pickledUnfinishedData` gets written. This has the current solver
data and is similar to `pickledData`.

Also a file `pickledStartData` gets written that has the data that
is available at the start of the run.


<a id="org8178f8b"></a>

### `BasicRunner` collects error and warning texts

The runner collects

-   at every warning the next 20 lines of the output until a total
    of 500 lines is reached (this avoids filling disk and memory if
    the solver produces too many warnings)
-   All output from an error message until the end

And stores them in the application data


<a id="orgd866a75"></a>

## Library


<a id="org6fcc935"></a>

### `TemplateFile` now uses `pyratemp`

The class `TempalteFile` now uses an enhanced templating
engine. The  old implementation is in the class
`TemplateFileOldFormat`


<a id="org7fb7072"></a>

### Clearer error message in Application-classes

If used as classes (not as utilities) these classes print the
class name instead of the calling utilities name


<a id="org8c53d89"></a>

### Output is only colored if it goes to the terminal

Error and warning messages don't decorate the output if it goes to
files or other non-terminal streams


<a id="orgbcceacc"></a>

### `error`-method of application classes now raises an exception

An exception is now raised by `self.error()`. This makes it easier
to handle such errors if the application class is used. The
exception is passed up until there is a "real" application


<a id="org33ca6c1"></a>

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


<a id="org895cd5d"></a>

### `LabledReSTTable` for more flexible table generation

New class in the `RestructuredTextHelper` allows more flexible
generation of tables. Items are added with `column` and `row` and
if these don't exist in the first row/column the table is extended
appropriately


<a id="orgf9218cc"></a>

### Plotting classes now allow setting of `xlabel`

This is implemented for `Gnuplot` and `Matplotlib`. Default for
the label on the x-Axis is now "Time [s]"


<a id="orgd4734b3"></a>

## Utilities


<a id="orge6aebbe"></a>

### `pyFoamFromTemplate.py` with new templating engine

The utility can now use the pyratemp-templating engine which
allows templates with loops, conditions and other  fancy stuff


<a id="orga7c691f"></a>

### `pyFoamSamplePlot.py` allows using the reference data as basis for comparison

Instead of using the x-values from the original data the y-values
of the reference data can be used for comparing (with the
`--use-reference`-option)

Same for `pyFoamTimelimePlot.py`


<a id="org6a84dcf"></a>

### Scaling and offsets are now used in plots of `pyFoamSamplePlot.py`

If scales not equal to \(1\) and offsets not equal to \(0\) are
specified they are used in the `gnuplot`-output


<a id="org42f5ec3"></a>

### `pyFoamPrintData2DStatistics.py` prints relative average error

With the `--relative-average-error`-option


<a id="org8d55e08"></a>

### Enhancements to `pyFoamVersion.py`

-   More tolerant if no library was found
-   Reports the location of the PyFoam-Library
-   Checks whether utility version is consistent the library found


<a id="org33d3f40"></a>

### `pyFoamRunner.py` allows hooks

Hooks can be added at the start and the end of a run


<a id="org63e4e44"></a>

### `pyFoamRedoPlots.py` supports range for plots

Added `-end` and `-start`-option to select a range that should be
plotted.

Currently not working with the Matplotlib-implementation (only gnuplot)


<a id="org8e2b21d"></a>

### `pyFoamDisplayBlockMesh.py` no supports templates

If a file with values is specified then the utility assumes you're
editing a template file and will evaluate it before displaying it


<a id="org619595e"></a>

### `pyFoamCaseReport.py` is tolerant towards binary files

New switch that makes the parser treat files that are declared
`binary` in the header as if they were `ascii`


<a id="org40ec20f"></a>

### `pyFoamSamplePlot.py` and `pyFoamTimelinePlot.py` raise error if no plots are generated

This makes it easier to catch faulty specifications (or empty
timeline-files)


<a id="org054696b"></a>

### `pyFoamSurfacePlot.py` can wait for a key

An option `--wait` has been added that makes the utility wait
before displaying the next picture


<a id="org82587da"></a>

### `pyFoamEchoDictionary.py` is more flexible with binary files

Switch allows forcing it to read a binary File as an ASCII


<a id="org4b4c950"></a>

### All utilities now have a switch that starts the debugger even with syntax-errors

Previously the option `--interactive-debug` only started the
debugger if the error was **no** syntax error. This is still the
default behavior, but can be overruled


<a id="orgfaa2110"></a>

### Utilities now can be killed with `USR1` and will give a traceback

The option `--catch-USR1-signal` now installs a signal-handler
that prints a traceback and finishes the run. If the interactive
debugger is enabled then it goes to the debugger-shell.

Option `--keyboard-interrupt-trace` triggers the same behaviour
for keyboard interrupts with `<Ctrl>-C`


<a id="orgb009f18"></a>

### Switch to switch on **all** debug options

For the purpose of developing a switch `--i-am-a-developer` has
been added.


<a id="org920ad05"></a>

### Plotting utilities now allow specification of x-Axis label

With the option `xlabel` in the `customRegexp`-file the label on
the x-axis of the plot can be changed. Setting `ylabel` and
`y2label` (for the secondary axis) was already possible


<a id="orga86993e"></a>

### Metrics and compare for `pyFoamTimelinePlot.py` and `pyFoamSamplePlot.py` support time ranges

Now the options `--min-time` and `--max-time` are supported by
`--metrics` and `--compare`


<a id="orgd611832"></a>

### `pyFoamDisplayBlockMesh.py` allows graphical selection of blocks and patches

New addition by Marc Immer allows the graphical selection of
blocks and patches and adds them to the `blockMeshDict`


<a id="org80a069e"></a>

### `pyFoamCloneCase.py` and `pyFoamPackCase.py` accept additional parameters

The file `LocalConfigPyFoam` is read by these utilities and if
there is a parameter `addItem` in the section `Cloning` defined
then these files are cloned/packed automatically (no user
specification required)


<a id="org73579dc"></a>

### `pyFoamListCases.py` now calculates estimated end-times

Additional option to print the estimated end times. These can be
wrong if the case did not start from the `startTime` in the
`controlDict`.

Also now allows printing the end and the start-time according to
the `controlDict`


<a id="org1f281b3"></a>

## New features


<a id="org7ac5507"></a>

### Different "phases" for multi-region solvers

Plots of type `phase` in `customRegexp` don't actually plot
anything. The set a phase-name that is used for subsequent values
(for instance to distinguish the different residuals)


<a id="org2ae2760"></a>

### `pyFoamChangeBoundaryType.py` allows selection of region and time

Options `--region` and `--time-directory` added that allow
selecting different `boundary`-files


<a id="org7345bfc"></a>

### New class for storing case data in a sqlite-database and associated utilities

The class `RunDatabase` stores the data from runs. Utility
`pyFoamAddCaseDataToDatabase.py` is one way to populate the
database. `pyFoamDumpRunDatabaseToCSV.py` allows dumping that
data to a file for further processing (in a spreadsheet for
instance)

Database can also be populated using a special post-run hook


<a id="orgbc68abd"></a>

## Bugfixes


<a id="org7b6cb3e"></a>

### Only binary packages of 1.x were found

Pattern had to start with 1 (now every digit is possible))


<a id="orgefce7ad"></a>

### Option group *Regular expressions* was listed twice

No harm done. But fixed


<a id="org065966f"></a>

### `--clear`-option for `pyFoamDecompose.py` not working

Reason was that `rmtree` does not allow wildcards. Fixed


<a id="org5020891"></a>

### `pyFoamDisplayBlockmesh.py` not working with variable substitution

The `DictRedirect` would not convert to float. Fixed. Although it
might happen again for other data types


<a id="org705c8b3"></a>

### Option `--function-object-data` of `pyFoamClearCase.py` not working with directories

The option was only implemented for the list-form of the
`functions` entry in `controlDict`

Now fixed to also work with the dictionary-form


<a id="org8ac13af"></a>

### `nonuniform` of length 0 not correctly printed

Seems like the length was interpreted as the name of the
list. Fixed


<a id="org1697278"></a>

### Building of pseudocases with `pyFoamRunner.py` broken

Only worked if no region was specified (= not at all). Fixed


<a id="orgf3ae7ae"></a>

### `pyFoamRedoPlot.py` did not correctly honor `--end` and `--start`

Plots were over the whole data range. This is now fix (also the
issue that `--end` alone did not work)


<a id="orgb3881fb"></a>

### `WriteParameterFile` does not preserve the order of additions

Contents was "only" set as a dictionary which does not preserve
the order in which entries are added. Replaced with a `DictProxy`


<a id="org58048c5"></a>

### Wrong number of arguments when using `TimelinePlot` in `positions`-mode

Problem that was introduced by changes in the `fields`-mode


<a id="org4d107fe"></a>

### `ClusterJob` uses only `metis` for decomposition

For OpenFOAM-versions 1.6 and higher the automatic decomposition
used is now `scotch`


<a id="org65c60f2"></a>

### `pyFoamSamplePlot.py` and `pyFoamTimelinePlot.py` produced no pictures for regions

As regions have their own subdirectories the `/` from the
directory name was inserted into the filename and if the
subdirectory did not exist `gnuplot` did not create the picture


<a id="org5246b19"></a>

### Barplots in `pyFoamTimelinePlot.py` not working if value is a vector

The base class didn't correctly handle the `(` and `)`. Fixed


<a id="orgaa92ea0"></a>

### Mysterious deadlocks while plotting long logfiles

The problem was that during splitting the timeline data an exception was
raised. This exception was caught by another part of PyFoam. This
left a lock on the data structure locked and the next access to
the structure was held indefinitely. Fixed


<a id="orgbc18344"></a>

### Scanning linear expressions form the block coupled solver failed

As there is a tuple of residuals the scanner did not analyze the
output of the output of the block-coupled solver from `1.6-ext`
correctly. This is now treated as a special case and each residual
is plotted separately (distinguished by a `[x]` with `x` being the
number of the component)


<a id="orgf12ed84"></a>

### `#include` not correctly working with macros in the included file

Macros `$var` were not correctly expanded. Fixed


<a id="org6da2c3a"></a>

### Macros not correctly expanded to strings

When being expanded to string form macros were not correctly
expanded


<a id="org8898d4e"></a>

### `pyFoamPackCase.py` in the working directory produces 'invisible' tar

If the utility was used in the form

    pyFoamPackCase.py .

then an 'invisible' tar `..tgz` was produced. Fixed


<a id="orgdadd08e"></a>

### String at the end of a linear solver output makes parsing fail

Reported in
[<http://www.cfd-online.com/Forums/openfoam-solving/112278-pyfoam-struggles-adopted-solver-post403990.html>]
the string is assumed to be part of the iteration number. Fixed


<a id="org31b2bf5"></a>

### Paraview utilities not working with higher Paraview versions

At least for PV 3.14 and 3.98 the way the version number is
determined has changed and the PV-utilities failed. This has been
fixed but is untested with old versions


<a id="org9ba3bac"></a>

### Camera settings not honored with `pyFoamPVSnapshot.py`

For the first rendered view Paraview automatically resets the
camera. This has now been switched off (so the snapshot is
rendered correctly)


<a id="orge80bb85"></a>

# Version 0.5.7 - 2012-04-13


<a id="orgd893792"></a>

## Parser improvements

-   Problem with nested comments
-   Parse code streams
-   Preserving of comments can be switched off
-   Ignore extra semicolons
-   Allows parsing lists of length 3 and 9 as lists and not as
    vectors and tensors
-   "lookup redirection" in OF-dictionaries now works


<a id="org8b558bd"></a>

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


<a id="orgcb98381"></a>

## New Utilities

-   pyFoamEchoPickledApplicationData to output pickled data
-   pyFoamPrintData2DStatistics.py to output data from comparisons
-   pyFoamBuildHelper.py to build project and its prerequisites (work
    in progress)
-   pyFoamCreateModuleFile.py to create files for
    <http://modules.sourceforge.net/> (by Martin Beaudoin)
-   pyFoamSTLUtility.py to join STL-files


<a id="org0d5ccfb"></a>

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


<a id="org36307ad"></a>

## Removed utilities

-   pyFoamAPoMaFoX.py
-   pyFoamPlotResiduals.py


<a id="orgbca3dce"></a>

## Thirdparty

-   Got rid of Numeric-support in Gnuplot-library


<a id="org7384e0a"></a>

## Other

-   script to generate man-pages for the utilities
-   Paraview3-example probeDisplay.py now renamed to
    probeAndSetDisplay.py and reads sampledSets from controlDict and
    sampleDict


<a id="org3b223b9"></a>

# Older Versions

The changes for older versions can be found on
[the Wiki-page](http://openfoamwiki.net/index.php/Contrib_PyFoam#History)
