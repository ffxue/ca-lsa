# About Content Analysis by LSA

The Content Analysis by Latent Semantic Analysis (LSA) is a quick and free software library for measuring the semantic similarity between a set of keywords and a set of documents (in English) for content analysis purpose.

# How to cite

  A working paper to be submitted soon.

# How to use

First, please convert the documents to a text file. All the words in a document should appear in one line, with all symbols (e.g., commas, periods, and quotes) removed. See the "txt/docs-20180703.txt" file for a sample.

Then, you can define a list of keywords, see the "txt/cat-20180630.txt" for a sample. In case there are synonymous terms or alternative words, please append them to the same line of keywords using a semi-colon (;) as the delimiter.

# Install

* Download the pre-trained vector model of [fasttext](//fasttext.cc/docs/en/english-vectors.html)
* Install Anaconda 3
* Open the Anaconda console terminal

    conda install nltk
    
    conda install gensim

* Change the settings of the three files (Lines 8, 10, and 12)

    cd [path_to_file]
    
    python lsa.py > sample_output.txt

# How to contribute

# License

LGPL-3.0

# Acknowledgements

This work was a part of the PhD thesis of Dr. Ye ([Google Scholar](//scholar.google.com.hk/citations?user=SnMNF3QAAAAJ&hl=en)).
 
