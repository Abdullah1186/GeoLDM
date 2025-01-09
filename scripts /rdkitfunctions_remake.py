from rdkit import Chem
import json
import matplotlib.pyplot as plt
import numpy as np



def rdkitfun(dataset,model):
    # Load JSON file into a Python list
    



    if dataset == 'QM9':
        with open("/root/GeoLdm/databases/qm9_smiles.json", "r") as file:
            DBsmiles= json.load(file)
        
        if model =='Gschnet':
            with open("/root/GeoLdm/databases/48h_smiles.json", "r") as file:
                smiles_list = json.load(file)
            
                
        elif model =='GeoLDM':
            with open("/root/GeoLdm/databases/GeoLDM_smiles.json", "r") as file:
                smiles_list = json.load(file)

        else: 
            smiles_list = None
            DBsmiles = None
            

    if dataset == 'OE62':
        with open("/root/GeoLdm/databases/OE62_full_smiles.json", "r") as file:
                DBsmiles= json.load(file)
                
        if model == 'Gschnet':
            with open("/root/GeoLdm/databases/0E62_20k_1.7_2.3_smiles.json", "r") as file:
                smiles_list = json.load(file) 

            

        else:
            DBsmiles= None 
            smiles_list = None


    def is_valid_smiles(smiles):
        """
        Check if a SMILES string is valid.
        
        Parameters:
            smiles (str): The SMILES string to validate.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        mol = Chem.MolFromSmiles(smiles)
        return mol is not None

    valid=[]
    for i in smiles_list: 
        if is_valid_smiles(i) == True:
            valid.append(i)

    validity = len(valid)/len(smiles_list)

    def compute_uniqueness(valid):
            """ valid: list of SMILES strings."""
            return len(set(valid)) / len(valid)

    unique= set(valid)
    uniqueness=compute_uniqueness(valid)

        

    def compute_novelty(unique):
        num_novel = 0
        novel = []
        for smiles in unique:
            if smiles not in DBsmiles:
                novel.append(smiles)
                num_novel += 1
        return num_novel / len(unique)
    novelty=compute_novelty(unique)


    return novelty, uniqueness, validity


# dataset = input( 
#     """ OE62 or QM9
#     """
# )

# model = input( 
#     """ GeoLDM or Gschnet
#     """
# )


# rdkitfun(dataset,model)