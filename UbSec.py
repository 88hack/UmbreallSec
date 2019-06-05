# coding:utf-8
from lib.core.option import *
import os

if __name__ == '__main__':
    version = 'v0.1'
    progam = u'''
  _    _           _                      _   _    _____
 | |  | |         | |                    | | | |  / ____|
 | |  | |_ __ ___ | |__  _ __ ___  __ _  | | | | | (___   ___  ___
 | |  | | '_ ` _ \| '_ \| '__/ _ \/ _` | | | | |  \___ \ / _ \/ __|
 | |__| | | | | | | |_) | | |  __/ (_| | | | | |  ____) |  __/ (__
  \____/|_| |_| |_|_.__/|_|  \___|\__,_| |_| |_| |_____/ \___|\___|



    {version:%s}
    {author:圣诞}
    ''' % version
    print(progam)

    main(os.path.dirname(os.path.abspath(__file__)))
