from anonymisation import main_ano

thesaurus_path = "thesaurus.txt"

#string = "Kyiv's mayor said half of the capital was without electricity. The mayor of Lviv said 80% of the city had no electricity so lighting, water and heating supplies were off. City authorities in Vinnytsia in west-central Ukraine were told to stock up on water following damage to a pumping station."
string = "april talked yesterday a lot about ibm"

print(main_ano(string,thesaurus_path))
