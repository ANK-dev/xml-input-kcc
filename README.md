# Batch XML Input for Kindle Comic Converter #

>Allows for a quick generation of XML for Kindle Comic Converter

## Usage ##

This script can generate `ComicInfo.xml` files recursively for use in Kindle
Comic Converter (KCC).

Place this script in the root directory of your comic library. It needs to be
setup in the following manner:

```plain
./XMLInput.py
[./Title A]
    |___[/Volume 01]
    |    |___[/Chapter 001]
    |    |  |___000.png
    |    |  |___001.png
    |    |  |___...
    |    |
    |    |___[/Chapter 002]
    |    |___[/Chapter 003]
    |    |___...
    |
    |___[/Volume 02]
    |    |___[/Chapter 012]
    |    |___[/Chapter 013]
    |    |___...
    |
    |___[/Volume 03]
        |___[/Chapter 018]
        |___[/Chapter 019]
        |___...

[./Title B]
    |___[/Volume 01]
    |   |___[/Chapter 001]
    |   |___[/Chapter 002]
    |   |___...
    |
    |___...
```

Run in a terminal with the following command:

```sh
    py ./XMLInput.py
```

Follow the on-screen prompts for futher instructions.

## Output ##

The output XML files have the following stucture:

```xml
<?xml version="1.0" encoding="utf-8"?>
<ComicInfo
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <Series>Title</Series>
    <Volume>01</Volume>
    <Number>001</Number>
    <Writer>Person A</Writer>
    <Penciller>Person B</Penciller>
    <Inker>Person C</Inker>
    <Colorist>Person D</Colorist>
</ComicInfo>
```

## Credits ##

Made by [ANK-dev](https://github.com/ANK-dev)
