import os
import sys

'''
this file keeps tracks of paths and sets the paths required for jarvis
'''
root_dir = os.getcwd()
sys.path.insert(1, root_dir + '\\software_AI\\computer-vision')
sys.path.insert(1, root_dir + '\\software_AI\\nlp')
sys.path.insert(1, root_dir + '\\software_Non_AI')
asset_path = root_dir + '\\assets\\'
asset_sounds = asset_path + 'sounds\\'
# return asset_path
