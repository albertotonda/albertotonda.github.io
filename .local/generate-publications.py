# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 13:02:26 2024

This script employs the 'academic' python module to automatically generate
hugoblox-compatible pages from bibtex. I wrote this because the module does not
log properly when ran from command line, and I need to understand what is going on

@author: Alberto
"""
import logging
import os

from academic.import_bibtex import import_bibtex

logging.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s",
    level=logging.INFO,
    datefmt="%I:%M:%S%p",
)
#log = logging.getLogger(__name__)
log = logging.getLogger()

formatter = logging.Formatter("[%(levelname)s %(asctime)s] %(message)s",
                                  "%Y-%m-%d %H:%M:%S")
fh = logging.handlers.RotatingFileHandler("log.log",
                         mode='a',
                         maxBytes=100*1024*1024,
                         backupCount=2,
                         encoding=None,
                         delay=0)

fh.setFormatter(formatter)
fh.setLevel(logging.INFO)
log.addHandler(fh)

#log.propagate = True

if __name__ == "__main__" :
    
    bibtex_file = "publications.bib"
    output_folder = "content/publication/"
    work_locally = False
    
    # change working directory (the script has some issues if the target
    # directory is not exactly "content/publication" from working directory)
    # comment for local experiments
    if not work_locally :
        os.chdir("../")
        bibtex_file = ".local/" + bibtex_file
    
    #if not os.path.exists(output_folder) :
    #    os.makedirs(output_folder)
        
    import_bibtex(
        bibtex_file,
        pub_dir=output_folder,
        overwrite=True,
                  )