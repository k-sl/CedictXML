# CedictXML

## Description
CedictXML is simple tool written in Python to convert an original [CC-CEDICT](https://www.mdbg.net/chindict/chindict.php?page=cc-cedict) file to a XML dictionary file in the logical [XDXF format](https://github.com/soshial/xdxf_makedict/blob/master/format_standard/xdxf_description.md), which can be used with dictionary software that support this format.

## External Dependencies
* [lxml](http://lxml.de/)
* _pinyin.py_ from the [pycedict](https://github.com/jdillworth/pycedict/) library

## Usage
(Assuming Python 2.7 and lxml are installed and cedictxml.py and pinyin.py are in the same folder:) Run the script on a folder with a CC-CEDICT file (named "cedict_ts.u8").

```
python cedictxml.py
```
(or `python2 cedictxml.py`, if Python 3  is the default in your system.)

## To Do
See [TODO](https://github.com/k-sl/CedictXML/blob/master/TODO.md)

## Dictionary Files
A recent CC-CEDICT in XDXF format can be found [here](https://github.com/k-sl/CedictXML/tree/master/CC-CEDICT.xdxf/).

## Credits and Licenses
CC-CEDICT is licensed under a under a Creative Commons Attribution-Share Alike 3.0 License and is maintained by [MDBG](https://www.mdbg.net/chindict/chindict.php).

_pinyin.py_ (which I'm including in this repository, as the project doesn't seem active anymore) is licensed under a BSD 3-clause license, as part of the [pycedict](https://github.com/jdillworth/pycedict/) library. It is **NOT** in the public domain.

CedictXML is not licensed or copyrighted, it is released into the public domain.
