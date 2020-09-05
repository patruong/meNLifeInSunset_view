#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 23:39:55 2020

@author: ptruong
"""

import os 

"""
Use this part in assets/images folder 
"""
files = os.listdir() #take the files from assets/image

md_meta_data = []
for i in files:
    md_meta_data.append(i.split(".")[0]+".md")
    
"""
Change all file ext to .jpg USED IN assets/images/fulls folder
"""
    
files = os.listdir() #take the files from assets/image and assets/thumbs
for i in range(len(files)):
    old_name = files[i]
    new_name = files[i].split(".")[0] + ".jpg"
    os.rename(old_name, new_name)

"""
Generate meta data in _images folder
"""

i = 1
for i in range(len(md_meta_data)):
    file_name = md_meta_data[i]
    f = open(file_name, "w")
    f.write("---\n")
    text = " ".join(file_name.split(".")[0].split("_")[1:])
    f.write("title: " + text + "\n")
    f.write("caption: \n")
    f.write("---")
    f.close()
    
