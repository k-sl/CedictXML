# CedictXML

## Description
CedictXML is simple tool written in Python to convert an original [CC-CEDICT](https://www.mdbg.net/chindict/chindict.php?page=cc-cedict) file to a XML dictionary file in the logical [XDXF format](https://github.com/soshial/xdxf_makedict/blob/master/format_standard/xdxf_description.md), which can be used with dictionary software that support this format.

## External Dependencies
* [lxml](http://lxml.de/)
* _pinyin.py_ from the [pycedict](https://github.com/jdillworth/pycedict/) library

## Dictionary Files
A recent CC-CEDICT in XDXF format can be found [here](https://github.com/k-sl/CedictXML/tree/master/CC-CEDICT.xdxf).

## Credits and Licenses
CC-CEDICT is licensed under a under a Creative Commons Attribution-Share Alike 3.0 License and is maintained by [MDBG](https://www.mdbg.net/chindict/chindict.php).

_pinyin.py_ (which I'm including in this repository, as the project doesn't seem active anymore) is licensed under a BSD 3-clause license, as part of the [pycedict](https://github.com/jdillworth/pycedict/) library.

CedictXML is not licensed or copyrighted, it is released into the public domain.
