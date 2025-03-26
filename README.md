# Renumber_residues_pdb4amber
Script for renumbering residues of pdb file after running pdb4amber


When preparing the input for MD simulations with AMBER sometimes your PDB file will not start from the first residue (terminal regions of proteins are flexible and X-ray can't solve the full structure). After running the PDB file through pdb4amber, there will be a renumbering in the residues and if, for example, your file started in residue 16 (SER) now that SER will be considered  as residue 1. This can be confusing especially when the time to analyze results comes, therefore I wrote this script to go back to the original numbering of residues after you have run pdb4amber to prepare your file!
