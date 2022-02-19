if __name__ == '__main__':

    #Create an empty dictionary called pokedex.
    #Add the following key, value pairs to the dictionary:
    # 'Venosaur': ['Grass', 'Poisen'] 
    # 'Charizard': ['Fire', 'Flying']
    # 'Blastoise': ['Water']
    
    pokedex = {
        'Venosaur': ['Grass', 'Poisen'], 
        'Charizard': ['Fire, Flying'],
        'Blastoise': ['Water']
    }   
    #test print
    print(pokedex)
    #Remove 'Blastoise' from the dictionary.

    del pokedex['Blastoise']
    # test print to check removal
    print(pokedex)