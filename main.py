#Copyright Desgyz. Minecraft Modpack Server Patcher

import wget
import os
import zipfile
import filecmp
import shutil

def update():
    print("Downloading Update")
    wget.download('<zip>', 'update.zip')

    try:
        shutil.rmtree(dir+'\config')
    except:
        print("Continuing")
    try:
        shutil.rmtree(dir+'\mods')
    except:
        print("Continuing")
    try:
        shutil.rmtree(dir+'\jarmods')
    except:
        print("Continuing")

    with zipfile.ZipFile('update.zip') as myzip:
        myzip.extractall(dir)
        myzip.close()

    os.remove('svn.txt')
    os.remove('update.zip')

    os.rename('svnnew.txt', 'svn.txt')
    print("Update Complete")

def compare():
    wget.download('<svn.txt>', 'svnnew.txt')

    compare = filecmp.cmp('svnnew.txt', 'svn.txt', shallow="true")

    if compare:
        print('No need for updating.')
        os.remove('svnnew.txt')
    else:
        update()

def config():
    if os.path.exists('config.txt'):
        print("Found Modpack Directory")
        with open("config.txt", "rb") as myfile:
            dir = myfile.read()
    else:
        print('Example: D:\Windows\Games\AT Launcher\Instances\Custom')
        dir = raw_input("The absolute directory where the modpack is held?")
        with open("config.txt", "a") as myfile:
            myfile.write(dir)

    if os.path.exists('svn.txt'):
        print("Starting")
        compare()
    else:
        wget.download('<svn.txt>', 'svn.txt')
        update()

config()
    os.rename('svnnew.txt', 'svn.txt')
    print("Update Complete")
