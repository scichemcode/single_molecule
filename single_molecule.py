import MDAnalysis as mda
import os
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Get single molecule from crystal .gro files')
    parser.add_argument('--gro_file', type=str,required=True,
                        help='Input gro file')
    parser.add_argument('--output_file', type=str, required=False, help='The name of the output file')

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    # Parse command-line arguments
    args = parse_arguments()

u=mda.Universe(args.gro_file)
residue=u.residues[0]
residue.atoms.write(args.output_file)
