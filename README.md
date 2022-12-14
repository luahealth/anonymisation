# Anonymisation

This is a python based service for redacting sensitive information from text.   

## Setup / Install 
### Prerequisites  
* Python 3.8 or 3.9  

### Installation  
1. [Optional] Setup and activate a virtual environment 
2. Install the required packages by running `pip -r requirements`


## Usage 

`test_ano.py` gives an example usage. 

`thesaurus.txt` is a custom dictionary of words you can enter that the service will remove. For example, if you have a client called abc_enterprises and you notice the service does not remove it, you can add the name to this text file to ensure it's removed. 


A possible workflow would be;

 1. Create a python file and import `from anonymisation import main_ano`
 2. Add your own code to read your data and iterate over it 
 3. For each piece of text (this could be a message, an email etc) run `main_ano(string,thesaurus_path)` and save the output
