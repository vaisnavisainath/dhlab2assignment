"""
======================================================================
Topic: Indic Language Stop Words for Natural Language Processing
======================================================================
Author Name(s): Vaisnavi Sainath
Short Description: This file contains sample stop-word lists for 
Bhojpuri language. These words may be used during text preprocessing 
in Natural Language Processing (NLP).
Semester: Monsoon Semester 2026
Affiliation: Humanities and Social Science, IIT(ISM) Dhanbad
Note:
This list contains common Bhojpuri pronouns, postpositions, 
conjunctions, auxiliaries, and particles.
======================================================================
"""

# Language: Bhojpuri
# Script: Devanagari

bhojpuri_stopwords = [
    # Conjunctions & Connectors
    "अउर", "आ", "बाकिर", "लेकिन", "चाहे", "त", "तबे", "जवना", "तब", "काहेकी",
    "मने", "काहे", "यद्यपि", "तथापि",
    
    # Pronouns & Demonstratives
    "हम", "हमार", "हमनी", "हमनीके", "तू", "तोहार", "रउआ", "रउरे", "ऊ", "ओकर",
    "ओह", "एह", "ई", "एकर", "इन्हन", "ओन्हन", "केहू", "काहें", "का", "कवन",
    "जे", "जौन", "जेकर", "जेकरा", "अपने", "सभे", "केकर", "केकरा", "के",
    
    # Postpositions & Case Markers
    "में", "पे", "पर", "से", "ले", "खातिर", "बदे", "ला", "लग", "तीर",
    "संगे", "साथे", "बिना", "बावत", "लगभग",
    
    # Auxiliary Verbs & Copulas
    "बा", "बाटे", "बाड़ी", "बाड़न", "बाड़ें", "रहल", "रहे", "रहलन", "होखे", "होई",
    "गइल", "भइल", "कइल", "दिहल", "लिहल", "आइल", "नाहीं", "ना", "मत", "निखे",
    "बारी", "बाटन", "हवे", "ह", "हउवे", "पड़ी", "चाहहीं",
    
    # Adverbs, Adjectives & Particles
    "यहाँ", "हियाँ", "उहाँ", "हुवाँ", "कहाँ", "कहवाँ", "जहाँ", "जहवाँ", "अब", "कब",
    "जब", "एतने", "ओतने", "कतने", "बहुते", "तनिक", "खाली", "भी", "ओहू", "एहू",
    "ठीक", "कइसे", "अइसे", "ओइ्से", "कस", "जस", "तस", "पाछे", "आगू", "भीतर",
    "बाहर", "ऊपर", "नीचे", "दूर", "नियर", "बेसी", "कमी", "सब", "कुल", "सगरो",
    "धरि", "तलक", "एने", "ओने", "सेने", "केने"
]

if __name__ == "__main__":
    print(f"Total Bhojpuri stop words loaded: {len(bhojpuri_stopwords)}")