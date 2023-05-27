"""
List the files in a given directory with a given suffix.
"""

import glob
import argparse


def main(args):
    """Run the command line program."""
    sreach=f'{args.dir}*{args.suffix}'
    all_file=glob.glob(sreach)
    print('\n'.join(all_file))
    #return '\n'.join(all_file)


if __name__ == '__main__':
    paser = argparse.ArgumentParser(description=__doc__)
    paser.add_argument('dir',type=str,
                       help='Directory')
    paser.add_argument('suffix',type=str,
                       help='File suffix (e.g. py, sh)')
    args=paser.parse_args()
    main(args)
