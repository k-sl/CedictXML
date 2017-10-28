# CedictXML

## Description
CedictXML is simple tool written in Python to convert an original [CC-CEDICT](https://www.mdbg.net/chindict/chindict.php?page=cc-cedict) file to a XML dictionary file in the logical [XDXF format](https://github.com/soshial/xdxf_makedict/blob/master/format_standard/xdxf_description.md), which can be used with dictionary software that support this format.

## Screenshot
![Screenshot of XDXF CC-CEDICT openned on GoldenDict 1.5](https://github.com/k-sl/CedictXML/blob/master/images/screenshot.png)

Screenshot of XDXF CC-CEDICT openned on [GoldenDict](https://github.com/goldendict/goldendict) 1.5

## Dependencies
* _pinyin.py_ from the [pycedict](https://github.com/jdillworth/pycedict/) library
* Python packages:
    * [lxml](http://lxml.de/)
    * [tdqm](https://github.com/noamraph/tqdm)

## Usage
(Assuming Python 2.7 and all dependencies are installed and cedictxml.py and pinyin.py are in the same folder:) Run the script on a folder with a CC-CEDICT file (named "cedict_ts.u8") to convert it into an XDXF file with the default filename on the same folder. Optionally use one or several of the arguments below.

### Arguments
* `-i` or `--input-file`
The name (and location if not on the current folder) of the original CC-CEDICT file to be converted. The default is a file named *cedict_ts.u8* on the current folder. E.g.:
```
python cedictxml.py -i NameOfCCedictFile.u8
```

* `-o` or `--output-file`
The name (and location if not on the current folder) of the resulting XDXF file. By default this will be "CC-CEDICT_" follwed by the dictionary version ("1." followed by the release date) followed by ".xdxf". E.g.:
```
python cedictxml.py -o ~/Dictionaries/XDXFFileName.xdxf
```

* `-d` or `--download`
Automatically download the most recent release of CC-CEDICT and convert it into XDXF. Naturally this argument cannot be used with `-i`. E.g.:
```
python cedictxml.py -d
```

The conversion can also be run without any argument to convert a *cedict_ts.u8* into a XDXF file with the default name. E.g.:
```
python cedictxml.py
```

## To Do
See [TODO](https://github.com/k-sl/CedictXML/blob/master/TODO.md)

## Change Log
See [CHANGELOG](https://github.com/k-sl/CedictXML/blob/master/CHANGELOG.md)

## Dictionary Files
A recent CC-CEDICT dictionary in XDXF format can be found [here](https://github.com/k-sl/CedictXML/tree/master/CC-CEDICT.xdxf/).

## Limitations
The XDXF format doesn't recognize transcriptions (such as pinyin). The pinyin transcription will be displayed on every entry, as pronunciation, but the entries are not searchable by pinyin. Hopefully this will be implemented in a future version of XDXF.

The XDXF format doesn't recognize different writing systems (such as traditional and simplified Chinese), as such both versions are always displayed, with no indication of which is which or option to display only one. Both versions are searchable, however. Hopefully this will be implemented in a future version of XDXF.

In the CC-CEDICT format there is no separation of words in expressions (each syllable is separated by a space), as such all entries as treated as only one word.

## Credits and Licenses
CC-CEDICT is licensed under a under a Creative Commons Attribution-Share Alike 3.0 License and is maintained by [MDBG](https://www.mdbg.net/chindict/chindict.php).

_pinyin.py_ (which I'm including in this repository, as the project doesn't seem active anymore) is licensed under a BSD 3-clause license, as part of the [pycedict](https://github.com/jdillworth/pycedict/) library. It is **NOT** in the public domain.

CedictXML is not licensed or copyrighted, it is released into the public domain.
