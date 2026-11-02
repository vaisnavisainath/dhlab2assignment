"""
======================================================================
Topic: Extraction of Indian Cultural Elements Using RAG
======================================================================
Author Name(s): Vaisnavi Sainath
Short Description: This file contains the names of Indian flora and 
fauna extracted from Chitra Banerjee Divakaruni's novel 'The Palace 
of Illusions' using a Retrieval-Augmented Generation (RAG) pipeline.
Semester: Monsoon Semester 2026
Affiliation: Humanities and Social Science, IIT(ISM) Dhanbad
======================================================================
"""

# Extracted Flora (Trees, Plants, Flowers, Herbs, Spices, Crops)
# Cleaned from RAG extraction output
flora_RAG_extraction = [
    # Fruits & Trees
    "Mango", "Custard Apple", "Tamarind", "Sakura",
    
    # Flowers & Ornamental Plants
    "Jasmine", "Parijat", "Lotus", "Rose", "Lily", "Tulip", 
    "Marigold", "Poppy", "Orchid", "Daisy", "Sunflower", 
    "Hyacinth", "Pansy", "Carnation", "Iris", "Dahlia", "Honeysuckle",
    
    # Spices, Herbs & Medicinal Plants
    "Chilies", "Ginger", "Turmeric", "Coriander", "Cumin", 
    "Fenugreek", "Basil", "Mint", "Rue", "Sage", "Thyme", 
    "Lavender", "Chamomile"
]

# Extracted Fauna (Mammals, Birds, Reptiles, Amphibians, Fish, Insects)
# Cleaned from RAG extraction output
fauna_RAG_extraction = [
    # Birds & Mammals
    "Peacock", "Birds", "Deer", "Lion", "Elephant", "Tiger", 
    "Mongoose", "Rabbit", "Fox", "Wolf",
    
    # Reptiles & Amphibians
    "Crocodile", "Alligator", "Snake", "Cobra", "Python", 
    "Lizard", "Gecko", "Frog", "Toad",
    
    # Insects & Arachnids
    "Flies", "Insect", "Butterfly", "Bee", "Ant", 
    "Spider", "Scorpion", "Mosquito", "Cicada", 
    "Grasshopper", "Dragonfly"
]

if __name__ == "__main__":
    print(f"Total Flora items extracted: {len(flora_RAG_extraction)}")
    print(f"Total Fauna items extracted: {len(fauna_RAG_extraction)}")