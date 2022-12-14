# Anonymisation

## Usage 
Language is complex and nuanced. This service attempts to balance removing sensitive information, while leaving non-sensitive information intact. 

`test_ano.py` gives an example usage. 

`thesaurus.txt` is a custom dictionary of words you can enter that the service will remove. For example, if you have a client called abc_enterprises and you notice the service does not remove it, you can add the name to this text file to ensure it's removed. 


A possible workflow would be;

 1. Create a python file and import `from anonymisation import main_ano`
 2. Add your own code to read your data and iterate over it 
 3. For each piece of text (this could be a message, an email etc) run `main_ano(string,thesaurus_path)` and save the output