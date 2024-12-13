import os
# we really hope that keys are unique

files = [f for f in os.listdir(".") if f.endswith(".bib")]
#files = ["publications-journals.bib", "publications-conferences.bib"]
#"invited" should not be considered, it's empty and creates issues
print(files)

output_file = "publications.bib"
text = ""
for f in files :
    with open(f, "r") as fp :
        text += fp.read()
        text += "\n"
    
    
with open(output_file, "w") as fp :
    fp.write(text)
    
