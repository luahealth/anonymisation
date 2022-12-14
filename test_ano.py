from anonymisation import main_ano

#path to the thesaurus file, with concepts 
thesaurus_path = "thesaurus.txt"

string = "april talked yesterday a lot about ibm"

print(main_ano(string,thesaurus_path))
