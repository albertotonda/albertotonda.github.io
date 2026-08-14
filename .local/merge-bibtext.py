import os
# we really hope that keys are unique

output_file = "publications.bib"
files = [f for f in os.listdir(".") if f.endswith(".bib") and f != output_file]
#files = ["publications-journals.bib", "publications-conferences.bib"]
#"invited" should not be considered, it's empty and creates issues
print(files)

text = ""
for f in files :
    print("Now reading file \"%s\"..." % f)
    with open(f, "r", encoding='utf-8') as fp :
        text += fp.read()
        text += "\n"
    
print("Now writing file \"%s\"..." % output_file)
with open(output_file, "w", encoding='utf-8') as fp :
    fp.write(text)
    
