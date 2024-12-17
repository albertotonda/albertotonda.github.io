# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:26:26 2024

Remove all publication directories, except the ones that contain a pdf

@author: Alberto
"""
import os
import shutil

if __name__ == "__main__" :
    
    target_folder = "../content/publication"
    
    dirs = [os.path.join(target_folder, f) for f in os.listdir(target_folder) 
            if os.path.isdir(os.path.join(target_folder, f))]
    
    print("Found a total of %d directories" % len(dirs))
    
    for d in dirs :
        
        # check inside of directory
        other_files = [
            f for f in os.listdir(d) 
            if f.endswith(".pdf") 
            or f.endswith(".png") 
            or f.endswith(".jpg")
            ]
        
        if len(other_files) > 0 :
            print("Found a PDF in folder \"%s\"!" % d)
        else :
            # remove the directory
            shutil.rmtree(d, ignore_errors=True)