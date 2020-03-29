import os
import platform
import re

def getSubDirectories(item):
    return [f.path for f in os.scandir(item) if f.is_dir()]
    

def setData():
    while True:
        print('\nFound the following series:')
        comic_dict = dict(enumerate(getSubDirectories('.'), 1))
        for key in comic_dict:
            print(f'{key} - {comic_dict[key]}')
        
        while True:
            series_select = input('Type the series number you would like to edit, or "0" to exit: ')
            try:
                series_select = int(series_select)
                if series_select == 0:
                    exit(0)
                elif series_select not in comic_dict:
                    print('\nInvalid number!')
                else:
                    confirm_select = input(f'The selected series is {comic_dict[series_select]}. Is this correct? [Y]ES/[n]o: ')
                    if confirm_select == '' or confirm_select[0] == 'y' or confirm_select[0] == 'Y':
                        break
                    elif confirm_select[0] == 'n' or confirm_select[0] == 'N':
                        continue
                    else:
                        print('\nInvalid option! Try again.')
            except ValueError:
                print('\nInvalid number!')
                

        writer = input('\nSet the [Writer] name, or press "ENTER" key for "none": ')
        penciller = input('Set the [Penciller] name, or press "ENTER" key for "none": ')
        inker = input('Set the [Inker] name, or press "ENTER" key for "none": ')
        colorist = input('Set the [Colorist] name, or press "ENTER" key for "none": ')

        print('\nThe following information has been set:')
        print('=======================================\n')
        print(f'Series: {comic_dict[series_select]}')
        print(f'Writer: {writer}')
        print(f'Penciller: {penciller}')
        print(f'Inker: {inker}')
        print(f'Colorist: {colorist}')

        confirm_select = input('\nBegin renaming process now? [Y]ES/[n]o: ')
        if confirm_select == '' or confirm_select[0] == 'y' or confirm_select[0] == 'Y':
            return comic_dict[series_select], writer, penciller, inker, colorist
        elif confirm_select[0] == 'n' or confirm_select[0] == 'N':
            continue
        else:
            print('Invalid option! Try again.')


def createXML(vol_chapter_dict, comic, writer, penciller, inker, colorist):
    for volume in vol_chapter_dict:
            for chapter in vol_chapter_dict[volume]:
                output = ('<?xml version="1.0" encoding="utf-8"?>'
                            '<ComicInfo'
                                'xmlns:xsd="http://www.w3.org/2001/XMLSchema"'
                                'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                                f'<Series>{comic}</Series>'
                                f'<Volume>{volume}</Volume>'
                                f'<Number>{chapter}</Number>'
                                f'<Writer>{writer}</Writer>'
                                f'<Penciller>{penciller}</Penciller>'
                                f'<Inker>{inker}</Inker>'
                                f'<Colorist>{colorist}</Colorist>'
                            '</ComicInfo>')
                
                library_path = f'./{comic}/Volume {volume}/{comic} - Chapter {chapter}'

                if os.path.exists(library_path):
                    try:
                        f = open(f'{library_path}/ComicInfo.xml', 'w')
                        f.write(output)
                        f.close
                    except OSError:
                        print('ERROR READING/WRITING "ComicInfo.xml" FILE!')
                        exit(1)
                else:
                    print('Path not found! Check that you are running the script\n'
                        'from the root of the comic library and ensure that your\n'
                        'directory tree matches that of the README.md file!')
                    exit(1)


def main():
    print('===== Batch XML Input for Kindle Comic Converter by ANK-dev =====')
    print('                       github.com/ANK-dev')
    
    # Get user data
    comic, writer, penciller, inker, colorist = setData()

    # Get volume and chapter subdirectory list
    volume_list = getSubDirectories(comic)
    chapter_list = [getSubDirectories(volume) for volume in volume_list]

    # Remove file path from lists
    if platform.system() == 'Windows':
        #comic = re.search('(?<=\.\\\\)([\s\S]*)', comic).group()    #Windows path structure (.\\Example\)
        comic = re.search(r'(?<=\.\\)([\s\S]*)', comic).group()    #Windows path structure (.\\Example\)

    else:
        comic = re.search(r'(?<=\./)([\s\S]*)', comic).group()  #Linux/Mac path structure (./Example/)

    volume_list = [re.search(r'([0-9]+)$', volume).group() for volume in volume_list]
    chapter_list = [[re.search(r'([0-9]*)\.?([0-9])$', chapter).group() for chapter in volume] for volume in chapter_list]

    # Create a dictionary that matches each volume (key) to a chapter list (value)
    volume_and_chapter = dict()
    for item in zip(volume_list, chapter_list):
        volume_and_chapter[item[0]] = item[1]

    # Delete previous lists
    del volume_list, chapter_list

    print('\n~~~~~~ Processing... Please Wait ~~~~~~')
    
    # XML Creation
    createXML(volume_and_chapter, comic, writer, penciller, inker, colorist)

    print("\nAll Done! ヽ(o＾▽＾o)ノ")


if __name__ == "__main__":
    main()