#!/usr/bin/env python
import os
import argparse
import numpy as np
import pandas as pd
from matplotlib import cm
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

parser = argparse.ArgumentParser()
parser.add_argument('data')
parser.add_argument('--method', default='single')
parser.add_argument('--metric', default='euclidean')
parser.add_argument('--threshold', type=float)
args = parser.parse_args()

data = pd.read_table(args.data, index_col=0)
hcluster = linkage(data, method=args.method, metric=args.metric)

fig = plt.figure()

# ax1 for dendrogram
ax1 = fig.add_axes([0.2, 0.1, 0.3, 0.8])
dendro = dendrogram(hcluster, color_threshold=args.threshold, no_labels=True, orientation='right', labels=data.index)
ax1.axvline(args.threshold, linestyle='--', linewidth=2, color='gray')
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_position(('outward', 4))
ax1.xaxis.set_ticks_position('top')
ax1.xaxis.set_label_position('top')
ax1.set_xticks(np.arange(0.2, 1.4, 0.2))
ax1.set_xticklabels(np.arange(0.2, 1.4, 0.2), weight='bold')
ax1.set_xlabel('Distance', fontsize='x-small', weight='bold')
ax1.tick_params(labelsize='x-small', bottom='off', left='off', right='off', direction='out', width=1, pad=5)

# rearrange data according the clustering results
data = data.ix[dendro['ivl']]

# ax2 for heat map
ax2 = fig.add_axes([0.5, 0.1, 0.3, 0.8])
im = ax2.imshow(data, vmin=0, vmax=0.1, cmap=cm.jet, origin='lower', interpolation='nearest')
for i in xrange(len(data.columns)):
    ax2.axvline(i + 0.5, linewidth=0.5, color='k')
for i in xrange(len(data.index)):
    ax2.axhline(i + 0.5, linewidth=0.5, color='k')
ax2.yaxis.set_label_position('right')
ax2.yaxis.set_ticks_position('right')
ax2.set_xticks(np.arange(len(data.columns)))
ax2.set_xticklabels(data.columns, rotation=90, weight='bold')
ax2.set_yticks(np.arange(len(data.index)))
ax2.set_yticklabels(data.index, weight='bold')
ax2.tick_params(labelsize=3, top='off', bottom='off', left='off', right='off')
ax2.set_xlabel('Glomerulus Identity', fontsize='large', weight='bold')
ax2.set_ylabel('LN Identity', fontsize='large', weight='bold')
plt.axis('tight')

# ax3 for color bar
ax3 = fig.add_axes([0.5, 0.91, 0.3, 0.015])
ax3.xaxis.set_ticks_position('top')
cb = fig.colorbar(im, cax=ax3, orientation='horizental')
cb.set_ticks(np.arange(0, 0.15, 0.025))
cb.ax.set_xticklabels(['0', '2.5', '5', '7.5', '10 %'], weight='bold')
ax3.tick_params(labelsize='x-small', direction='out', width=1)

root = os.path.splitext(os.path.basename(args.data))[0]
plt.savefig('{0}_{1}_{2}_hcluster.png'.format(root, args.method, args.metric), dpi=300)
plt.close(fig)
