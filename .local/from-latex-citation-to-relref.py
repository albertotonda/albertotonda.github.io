# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 20:29:54 2024

Analyze text, find citation in Latex style, replace it with local reference to
the publication page.

@author: Alberto
"""

import os
import re as regex

if __name__ == "__main__" :
    
    target_file = "../content/research/white-box-machine-learning/index.md"
    
    # read a file, then save a copy
    text = ""
    with open(target_file, "r") as fp :
        text += fp.read()
        
    with open(target_file + ".backup", "w") as fp :
        fp.write(text)
    
    print(text)
    
    # scan the file, find all matches for the regex of a citation,
    # where each match might contain multiple keys
    regex_citation = r"~\\cite{([\w|,]+)}"
    matches = regex.findall(regex_citation, text)
    print(matches)
    
    # get the citation keys
    citation_keys = []
    for m in matches :
        citation_keys.extend(m.split(","))
    print(citation_keys)
    
    # convert the citation keys to the relative reference
    from_citation_key_to_relref = {}
    for ck in citation_keys :
        # split citation key, knowing that the format is <letters><year><letters>
        m = regex.match("([a-z|A-Z]+)([0-9]+)([a-z|A-Z]+)", ck)
        address = "/publication/" + m.group(1) + "-" + m.group(2) + "-" + m.group(3) + "/index.md" 
        relref = "[[" + ck + "]]" + r'({{<relref "' + address + r'" >}})'
        from_citation_key_to_relref[ck] = relref
        print(relref)
        
    # now that we have everything, we re-match the citations, and then we convert
    # them to one or more relrefs
    regex_citation = r"(~\\cite{([\w|,]+)})"
    matches = regex.findall(regex_citation, text)
    
    # now, matches have two parts: one that we have to replace, and the second
    # with all the citation keys
    for replace_this, cks in matches :
        cks = cks.split(",")
        replacement_text = ""
        for i, ck in enumerate(cks) :
            if i > 0 :
                replacement_text += ","
            replacement_text += " "
            replacement_text += from_citation_key_to_relref[ck]
        
        text = text.replace(replace_this, replacement_text)
        
    print(text)
    with open(target_file, "w") as fp :
        fp.write(text)