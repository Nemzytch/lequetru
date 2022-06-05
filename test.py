import os
import sys

#add bes.exe to path


fileToAdd = 'BES_1.7.8/BES.exe'
variableName = 'PATH'

#add file to path
os.environ[variableName] = f'{os.environ[variableName]};{fileToAdd}'

