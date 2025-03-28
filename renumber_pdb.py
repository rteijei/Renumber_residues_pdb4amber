from Bio import PDB

wrong_num_pdb = "4omg_8_tleap.pdb"

right_num_pdb ="4omg_8FH.pdb"

new_pdb = "renumbered_tleap2.pdb"

def renumber_chain_A(target_pdb, reference_pdb, output_pdb):
    parser = PDB.PDBParser(QUIET=True)
    io = PDB.PDBIO()

    # Load PDB structures
    ref_structure = parser.get_structure("ref", reference_pdb)
    target_structure = parser.get_structure("target", target_pdb)

    # Extract correct numbering from chain A in reference PDB
    ref_residue_map = {}
    for model in ref_structure:
        for chain in model:
            if chain.id == 'A': #If your initial pdb file doesn't have chains (sometimes pdb4amber deletes the chain ID if there is only one) just comment out this line and the A in line 26
                for index, res in enumerate(chain.get_residues(), start=1):
                    ref_residue_map[index] = res.id[1]  # Map sequential index to correct residue number

    # Extract residues from target PDB (only chain A)
    target_chain = target_structure[0]['A'] #Again, if your pdb file doesn't have chain ID just comment out before ['A'].
    target_residues = list(target_chain.get_residues())

    # Check if the number of residues match
    if len(ref_residue_map) != len(target_residues):
        raise ValueError(f"Residue count mismatch: {len(ref_residue_map)} (ref) vs {len(target_residues)} (target)")

    # Apply new residue numbering
    for new_res_id, res in zip(ref_residue_map.values(), target_residues):
        res.id = (' ', new_res_id, ' ')  # Set new residue number

    # Save the new PDB file
    io.set_structure(target_structure)
    io.save(output_pdb)
    print(f"Renumbered PDB saved as {output_pdb}")

# Example usage
renumber_chain_A(wrong_num_pdb, right_num_pdb, new_pdb)
