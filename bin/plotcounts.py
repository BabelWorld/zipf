"""
plot
"""

import pandas as pd
import argparse


def main(args):
    """Run the command line program."""
    input_csv = args.infile
    df = pd.read_csv(input_csv, header=None,
                    names=('word', 'word_frequency'))
    df['rank'] = df['word_frequency'].rank(ascending=False,
                                            method='max')
    df['inverse_rank'] = 1 / df['rank']
    scatplot = df.plot.scatter(x='word_frequency',
                                y='rank',
                                figsize=[12, 6],
                                grid=True,
                                xlim=args.xlim)
    fig = scatplot.get_figure()
    fig.savefig(args.outfile)


if __name__ == '__main__':
    parser=argparse.ArgumentParser(__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Input file name')
    parser.add_argument('-x','--xlim',
                        type=int, default=12,
                        help='arix x limit')
    parser.add_argument('-y','--ylim',
                        type=int,default=6,
                        help='arix y limit')
    parser.add_argument('-o', '--outfile',
                        type=str, default='plotcounts.png',
                        help='Output file')
    args = parser.parse_args()
    main(args)
