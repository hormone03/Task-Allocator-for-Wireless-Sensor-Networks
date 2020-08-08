
# coding: utf-8

# In[6]:


#To block unnecessary tensoflow warnings
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")


# In[7]:


#importing libraries
import networkx as nx 
import pylab
import matplotlib.pyplot as plt 
from __future__ import print_function
import copy
from random import randint, random, randrange, choice
from functools import reduce
import logging
import numpy as np
logging.getLogger(__name__).addHandler(logging.NullHandler())
import numpy
import time
import networkx as nx


# In[8]:


# total processor
total_cores = 10
#total task 
total_tasks=10
low_percent=0.75

# Gets the index of maximum element in a list. If a conflict occurs, the index of the first largest is returned
def maxl(l): return l.index(reduce(lambda x,y: max(x,y), l))

# Gets the index of minimum element in a list. If a conflict occurs, the index of the first smallest is returned
def minl(l): return l.index(reduce(lambda x,y: min(x,y), l))


# In[9]:


def draw_graph(graph, labels=None, graph_layout='shell',
               node_size=1600, node_color='green', node_alpha=0.3,
               node_text_size=12,
               edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):

    # create networkx graph
    G=nx.Graph()

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # these are different layouts for the network you may try
    # shell seems to work best
    if graph_layout == 'spring':
        graph_pos=nx.spring_layout(G)
    elif graph_layout == 'spectral':
        graph_pos=nx.spectral_layout(G)
    elif graph_layout == 'random':
        graph_pos=nx.random_layout(G)
    else:
        graph_pos=nx.shell_layout(G)

    # draw graph
    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, 
                           alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font)

    if labels is None:
        labels = range(len(graph))

    edge_labels = dict(zip(graph, labels))
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, 
                                 label_pos=edge_text_pos)
    
    pylab.savefig('graph.eps')

    # show graph
    plt.show()

if(total_cores==3):
    #graphPlot= [(0,1), (0,2), (1,0)  (1, 2), (2,0), (2,1)]
    graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
elif(total_cores ==5):
    graphPlot= [(0,1), (0,2), (1,0), (1,4),  (2,0), (2,3), (3,2), (3,4), (4,1), (4,3)]
    graph = {0: [1, 2], 1: [0, 4], 2: [0, 3], 3: [2, 4], 4: [1, 3]}
elif(total_cores ==10): 
    graphPlot = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9),(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
    graph = {0: [1, 4], 1: [0, 5, 6, 7], 2: [4, 5], 3: [6, 7], 4: [0, 2, 5, 8], 5:[1, 2, 4, 5, 9], 6:[1, 3], 7:[1, 3], 8:[4, 9], 9:[5, 8]}
elif(total_cores ==15):
    graphPlot = [(0, 1),(1, 5), (1, 7), (4, 5), (4, 8),(0,10), (5,11), (12,10), (7,13), (9,14), (1, 6), (3, 7), (5, 9),(2, 4), (0, 4), (2, 5),(14,5),(11,13),(12,2), (3, 6), (8, 9)]
    graph = {0: [1, 4, 10], 1: [0, 5, 6, 7], 2: [4, 5, 12], 3: [6, 7], 4: [0, 2, 4, 5, 8], 5:[1, 2, 4, 5, 9, 11, 14], 6:[1, 3], 7:[1, 3, 13], 8:[4, 9], 9:[5, 8, 14], 10:[0, 12], 11:[5, 13], 12:[2, 10], 13:[7, 11], 14:[5, 9]}
elif(total_cores ==20):
    graphPlot = [(0, 1),(1, 5), (19,4), (19,3), (1, 7), (4, 5), (15,6), (8,16), (9,17), (9,18), (10,19), (4, 8),(0,10), (5,11), (12,10), (7,13), (9,14), (1, 6), (3, 7), (5, 9),(2, 4), (0, 4), (2, 5),(14,5),(11,13),(12,2), (3, 6), (8, 9)]
    graph = {0: [1, 4, 10], 1: [0, 5, 6, 7], 2: [4, 5, 12], 3: [7, 6, 19], 4: [0, 2, 5, 8, 19], 5:[1, 2, 4, 9, 11, 14], 6:[1, 3, 15], 7:[1, 3, 13], 8:[4, 9, 16], 9:[5, 8, 17, 14, 18], 10:[0, 12, 19], 11:[5, 13], 12:[10, 12, 15], 13:[11, 7], 14:[5, 9], 15:[6, 12], 16:[8], 17:[9], 18:[9], 19:[3, 4, 10]}
elif(total_cores ==25):
    graphPlot = [(0, 1),(1, 5), (1, 22), (12,15), (15, 21), (15,23), (15, 24), (20,2), (20,4), (19,3), (1, 7), (4, 5), (15,6), (8,16), (9,17), (9,18), (10,19), (10,20), (4, 8),(0,10), (5,11), (12,10), 
    (7,13), (9,14), (1, 6), (3, 7), (5, 9),(2, 4), (0, 4), (2, 5),(14,5),(11,13),(12,2), (3, 6), (8, 9)]
    graph = {0: [1, 4, 10], 1: [0, 5, 6, 7, 22], 2: [4, 5, 12, 20], 3: [6, 7, 19], 4: [0, 2, 5, 8, 20], 5:[1, 2, 4, 5, 11, 14], 6:[1, 3, 15], 7:[1, 3, 13], 8:[4, 9, 16], 9:[5, 8, 9, 14, 17, 18], 10:[0, 12, 19, 20], 11:[5, 13], 12:[2, 10, 15], 13:[7, 11], 14:[9], 15:[6, 12, 21, 23, 24], 16:[8], 17:[9], 18:[9], 19:[3, 10], 
             20:[2, 4, 5, 10], 21:[15], 22:[1], 23:[15], 24:[15]}
elif(total_cores ==30):
    graphPlot = [(0, 1),(1, 5), (1, 22), (12,15), (15, 21), (15,23), (15, 24), (15, 25), (15, 26), (15, 27), (15, 28), (15,29), (20,2), (20,4), (19,3), (1, 7), (4, 5), (15,6), (8,16), (9,17), (9,18), 
    (10,19), (10,20), (4, 8),(0,10), (5,11), (12,10), (7,13), (9,14), (1, 6), (3, 7), (5, 9),(2, 4), (0, 4), (2, 5),(14,5),(11,13),(12,2), (3, 6), (8, 9)]
    graph = {0: [1, 4, 10], 1: [0, 5, 6, 7, 22], 2: [4, 5, 12, 20], 3: [6, 7, 19], 4: [0, 2, 5, 8, 20], 5:[1, 2, 4, 5, 11, 14], 6:[1, 3, 15], 7:[1, 3, 13], 8:[4, 9, 16], 9:[5, 8, 9, 14, 17, 18], 10:[0, 12, 19, 20], 11:[5, 13], 12:[2, 10, 15], 13:[7, 11], 14:[9], 15:[6, 12, 21, 23, 24, 25, 26, 27, 28 ,29], 16:[8], 17:[9], 18:[9], 19:[3, 10], 
            20:[2, 4, 5, 10], 21:[15], 22:[1], 23:[15], 24:[15], 25:[15], 26:[15], 27:[15], 28:[15], 29:[15]}
elif(total_cores ==35):
    graphPlot = [(0, 1), (1, 5), (1, 22), (12,15), (15, 21), (15,23), (15, 24), (15, 25), (15, 26), (15, 27), (15, 28), (15,29), (20,2), (20, 30), (20,31), (20,32), (20, 33), (20,34), (20,4), 
    (19,3), (1, 7), (4, 5), (15,6), (8,16), (9,17), (9,18), (10,19), (10,20), (4, 8),(0,10), (5,11), (12,10), (7,13), (9,14), (1, 6), (3, 7), (5, 9),(2, 4), (0, 4), (2, 5),(14,5),(11,13),(12,2), (3, 6), (8, 9)]
    graph = {0: [1, 4, 10], 1: [0, 5, 6, 7, 22], 2: [4, 5, 12, 20], 3: [6, 7, 19], 4: [0, 2, 5, 8, 20], 5:[1, 2, 4, 5, 11, 14], 6:[1, 3, 15], 7:[1, 3, 13], 8:[4, 9, 16], 9:[5, 8, 9, 14, 17, 18], 10:[0, 12, 19, 20], 11:[5, 13], 12:[2, 10, 15], 13:[7, 11], 14:[9], 15:[6, 12, 21, 23, 24, 25, 26, 27, 28 ,29], 16:[8], 17:[9], 18:[9], 19:[3, 10], 
             20:[2, 4, 5, 10, 30, 31, 32, 33, 34], 21:[15], 22:[1], 23:[15], 24:[15], 25:[15], 26:[15], 27:[15], 28:[15], 29:[15], 30:[20], 31:[20], 32:[20], 33:[20], 34:[20]}
elif(total_cores ==40):
    graphPlot = [(0, 1), (1, 5), (1, 22), (12,15), (15, 21), (15,23), (15, 24), (15, 25), (15, 26), (15, 27), (15, 28), (15,29), (20,2), (20, 30), (20,31), (20,32), (20, 33), (20,34), (20,4), (19,3), (1, 7), (4, 5), 
    (15,6), (8,16), (9,17), (9,18), (10,19), (10,20), (4, 8),(0,10), (5,11), (12,10), (7,13), (9,14), (9,35), (9,36), (9,37), (9,38), (9,39), (1, 6), (3, 7), (5, 9),(2, 4), (0, 4), (2, 5),(14,5),(11,13),(12,2), (3, 6), (8, 9)]
    graph = {0: [1, 4, 10], 1: [0, 5, 6, 7, 22], 2: [4, 5, 12, 20], 3: [6, 7, 19], 4: [0, 2, 5, 8, 20], 5:[1, 2, 4, 5, 11, 14], 6:[1, 3, 15], 7:[1, 3, 13], 8:[4, 9, 16], 9:[5, 8, 9, 14, 17, 18, 35, 36, 37, 38, 39], 10:[0, 12, 19, 20], 11:[5, 13], 12:[2, 10, 15], 13:[7, 11], 14:[9], 15:[6, 12, 21, 23, 24, 25, 26, 27, 28 ,29], 16:[8], 17:[9], 18:[9], 19:[3, 10], 
            20:[2, 4, 5, 10, 30, 31, 32, 33, 34], 21:[15], 22:[1], 23:[15], 24:[15], 25:[15], 26:[15], 27:[15], 28:[15], 29:[15], 30:[20], 31:[20], 32:[20], 33:[20], 34:[20], 35:[9], 36:[9], 37:[9], 38:[9], 39:[9]}
    
else:
    print("Total number nodes is exceeded")


#labels = map(chr, range(65, 65+len(graph)))

draw_graph(graphPlot)



# In[153]:


#initial = False
#taskNumber = 50
#for i in range(taskNumber):
    #if not initial:
        #locSec = [0 for _ in range(taskNumber)]
    #locSec[i] = randint(1, 5)
    #initial=True
    
    


# In[154]:


if(total_tasks==5):
    DAG = {0: [1, 2], 1: [3], 2: [3], 3: [4]}
    reverseDAG = {0: [], 1: [0], 2: [0], 3: [1, 2], 4: [3]}
    commLoad = [300663, 279679, 324338, 285456, 275612]
    bitSize = [813, 729, 849, 849, 811]
    taskSec = [4, 1, 2, 1, 1]
    locSec = [4, 5, 1, 2, 1]
    
    
elif(total_tasks==10):
    DAG = {0: [1], 1: [2, 3], 2: [4], 3: [4], 4: [5, 6], 5: [7], 6: [7, 8], 7: [8], 8: [9]}
    commLoad = [300450, 300421, 293478, 301903, 317801, 318894, 296052, 308573, 270461, 305481]
    bitSize = [817, 765, 790, 825, 745, 831, 787, 728, 770, 841]
    taskSec = [2, 4, 3, 3, 2, 2, 3, 2, 3, 3]
    locSec = [2, 3, 4, 3, 2, 2, 3, 2, 3, 3]
    
    
    
elif(total_tasks==15):
    DAG = {0: [1, 2], 1: [3, 4], 2: [4, 5], 3: [6, 8], 4: [6, 7], 5: [7, 10], 6: [8, 9], 7: [9, 10], 8: [11], 9: [11, 12],
         10: [12], 11: [13], 12: [13], 13: [14]}
    commLoad = [283247, 275178, 311034, 304905, 308996, 317387, 315415, 329991, 271790, 317749, 328641, 270849, 302770, 324337, 312747]
    bitSize = [732, 731, 794, 856, 849, 774, 799, 778, 727, 837, 859, 853, 734, 759, 748]
    taskSec = [2, 3, 4, 2, 3, 5, 3, 5, 5, 3, 4, 5, 4, 3, 1]
    locSec = [2, 4, 4, 5, 2, 5, 5, 2, 4, 3, 5, 5, 2, 1, 4]
    
    
    
elif(total_tasks==20):
    DAG = {0: [1, 2, 3], 1: [4], 2: [5], 3: [5], 4: [6, 8], 5: [6, 7, 12], 6: [8, 9], 7: [12, 13], 8: [10, 11], 9: [11, 12],
         10: [11, 14], 11: [14, 15, 17], 12: [15, 16, 18], 13: [16], 14: [17], 15: [17, 18], 16: [18], 17: [19], 18: [19] }
    commLoad = [301809, 299232, 281190, 305189, 326141, 315721, 276833, 325420, 276989, 282391, 277964, 328784, 295351, 326589, 
                270415, 308932, 282721, 278083, 301958, 294057]
    bitSize = [768, 736, 802, 734, 856, 786, 733, 732, 847, 847, 741, 788, 754, 841, 741, 836, 873, 857, 737, 766]
    taskSec = [3, 4, 2, 2, 4, 4, 3, 4, 2, 4, 4, 1, 2, 5, 1, 1, 4, 4, 1, 3]
    locSec = [2, 4, 5, 3, 2, 1, 1, 1, 5, 5, 1, 5, 3, 5, 1, 1, 5, 2, 5, 2]
    
    
    
elif(total_tasks==25):
    DAG = {0: [1, 2, 3, 4], 1: [5, 8], 2: [5, 6], 3: [6, 7], 4: [7, 11], 5: [8, 9, 12, 16], 6: [9, 10, 17], 7: [10, 11], 8: [12], 9: [13],
         10: [14, 18], 11: [15], 12: [16, 19], 13: [16, 17], 14: [17, 18, 23], 15: [18, 21], 16: [19], 17: [20], 18: [21], 19: [22],
         20: [22, 23], 21: [23], 22: [24], 23: [24]}
    commLoad = [312759, 306149, 323178, 329321, 282925, 275910, 327210, 319575, 299613, 270650, 278040, 298535, 284741, 
                292530, 289878, 289646, 286427, 325215, 328697, 276442, 270465, 299748, 321620, 304265, 314654]
    bitSize = [799, 726, 819, 812, 733, 875, 758, 763, 735, 867, 748, 875, 738, 845, 770, 841, 786, 869, 809, 726, 
               836, 849, 756, 799, 870]
    taskSec = [4, 3, 5, 1, 5, 4, 3, 2, 4, 5, 2, 1, 1, 4, 1, 1, 4, 4, 1, 4, 5, 3, 5, 2, 3]
    locSec = [4, 1, 3, 1, 3, 3, 2, 1, 4, 1, 1, 1, 3, 5, 1, 4, 5, 1, 4, 5, 5, 4, 1, 2, 3]
    
    
    
elif(total_tasks==30):
    DAG = {0: [1, 2, 3, 7], 1: [4, 5, 6], 2: [6, 7], 3: [7, 8, 9, 13], 4: [10, 11], 5: [11, 12], 6: [12, 21], 7: [13], 8: [14, 18], 9: [14, 15, 22],
         10: [19], 11: [16], 12: [17], 13: [18, 21], 14: [18, 22], 15: [19], 16: [20], 17: [20, 21], 18: [21, 22], 19: [22, 27],
         20: [23, 24, 26], 21: [24], 22: [25], 23: [26], 24: [26], 25: [27, 28], 26: [28], 27: [28], 28: [29]}
    commLoad = [303772, 271868, 274544, 293075, 290501, 303683, 318747, 284140, 312114, 322298, 298665, 276534, 282817,
                289946, 324401, 282806, 310960, 305510, 304520, 274420, 329961, 326454, 274130, 303333, 293052, 301791, 302249, 317438, 295238, 319157]
    bitSize = [801,863,842,742,840,739,814,864,768,866,839,762,739,810,804,873,858,768,772,833,738,737,722,836,842,854,766,847,775,762]
    taskSec = [1,1,1,5,2,1,2,3,3,4,4,1,3,5,5,2,5,2,1,5,2,5,3,4,5,2,2,2,4,2]
    locSec = [3,4,3,5,2,4,2,5,1,1,3,4,2,5,2,4,1,3,4,5,4,1,2,5,4,1,5,2,2,5]
    
    
    
elif(total_tasks==35):
    DAG = {0: [1, 2, 3, 4], 1: [2, 5], 2: [3, 5, 6, 7], 3: [4, 7], 4: [7, 8], 5: [9, 13], 6: [7,10], 7: [10, 11], 8: [11, 12], 9: [13, 14],
         10: [14, 15], 11: [15, 16], 12: [16, 17, 21], 13: [18, 19], 14: [19], 15: [19, 20, 24], 16: [20, 21, 25], 17: [21, 22, 26], 18: [23, 27], 19: [23, 24, 28],
         20: [24, 25, 29], 21: [25, 26, 30], 22: [26], 23: [27, 28], 24: [28, 29, 32], 25: [29, 30, 33], 26: [30], 27: [31], 28: [31, 32, 34], 29: [32, 33],
         30: [33], 31: [34], 32: [34], 33: [34]}
    commLoad = [320100, 314300, 294724, 329462, 292746, 288946, 328709, 322350, 316878, 329608, 327042, 326802, 304186, 302687, 319281,
                314382, 279916, 283839, 324541, 322528, 311955, 273521, 311622, 320387, 315962, 271325, 286972, 293323,
                329109, 286062, 318966, 315698, 327696, 287375, 309412]
    bitSize = [720,799,843,785,793,725,872,728,742,826,864,749,744,782,778,830,764,759,778,852,784,803,849,737,
               783,834,782,839,829,777,859,778,734,724,804]
    taskSec = [5,2,5,2,5,2,4,2,1,4,2,4,5,4,1,1,3,5,5,1,2,5,3,5,5,3,3,3,5,5,3,5,5,1,3]
    locSec = [2,4,4,1,4,4,2,2,1,1,2,1,1,2,4,4,4,3,5,1,4,1,3,1,4,1,1,2,5,5,3,5,1,1,3]
    
    
    
elif(total_tasks==40):
    DAG = {0: [1, 2, 3, 4, 5], 1: [6, 10], 2: [6, 7], 3: [7, 8], 4: [8, 9], 5: [9], 6: [10, 11], 7: [11, 12, 17], 8: [12, 13, 18], 9: [13, 14, 19],
         10: [15, 16], 11: [16, 17], 12: [17, 18], 13: [18, 19, 25], 14: [19, 20, 26], 15: [21, 22], 16: [22, 23], 17: [23, 24, 29], 18: [24, 25], 19: [25, 26, 31],
         20: [26, 32], 21: [27], 22: [27, 28], 23: [28, 29], 24: [29, 30, 34], 25: [30, 31, 35], 26: [31, 32, 36], 27: [33], 28: [33, 34], 29: [34],
         30: [34, 35], 31: [35, 36, 38], 32: [36], 33: [34, 37], 34: [35, 37, 39], 35: [38, 39], 36: [38], 37: [39], 38: [39]}
    commLoad = [306645, 298435, 326764, 294164, 279415, 315824, 278422, 297223, 277057, 319375, 319197, 273976, 294204, 
                270454, 292704, 312430, 324214, 275627, 301779, 277254, 314559, 303017, 299395, 312321, 315543, 294045, 301705, 
                324586, 298840, 309313, 308021, 308470, 282969, 302783, 294242, 325226, 308897, 285089, 300602, 305872]
    bitSize = [875,771,843,876,869,835,822,787,820,722,732,880,753,876,741,723,761,785,863,739,785,779,846,751,801,
               755,872,777,877,769,798,754,838,782,844,793,737,793,865,794]
    taskSec = [2,3,3,2,3,4,3,1,2,3,2,5,1,3,5,5,1,3,4,1,3,4,5,2,1,4,5,3,4,5,4,3,4,5,4,2,2,3,1,2]
    locSec = [1,5,1,2,2,5,2,3,1,2,2,1,1,4,1,5,4,4,4,2,5,3,3,4,2,3,1,3,2,4,2,1,1,5,5,5,1,3,3,2]
    
    
    
elif(total_tasks==45):
    DAG = {0: [1, 2, 3], 1: [2, 4, 5, 6], 2: [3, 6, 7, 12], 3: [7, 8, 9, 13, 14], 4: [5, 10], 5: [6, 10, 11, 15], 6: [11, 12, 16], 7: [12, 13, 17], 8: [13, 14, 18], 9: [14, 19],
         10: [15], 11: [15, 16], 12: [16, 17], 13: [17, 18, 22], 14: [18, 19, 23], 15: [25, 20], 16: [20, 21, 27], 17: [21, 22, 28], 18: [22, 23, 29], 19: [23, 24, 31],
         20: [26, 27, 33], 21: [27, 28, 34], 22: [28, 29, 35], 23: [30, 31, 37], 24: [31], 25: [26, 32], 26: [32, 33], 27: [33, 34], 28: [34, 35], 29: [30, 35, 36],
         30: [36, 37], 31: [37], 32: [38], 33: [34, 38, 39], 34: [35, 39, 40, 43], 35: [36, 40, 41], 36: [37, 41, 42], 37: [42], 38: [39, 44], 39: [43],
         40: [41, 43], 41: [42, 43], 42: [44], 43: [44]}
    commLoad = [276270, 279323, 275187, 316835, 287483, 294789, 311204, 302790, 290765, 327319, 276019, 292220, 284217, 
                299817, 329988, 271729, 326826, 289206, 299929, 294516, 322587, 323577, 308478, 291064, 301815, 325367, 316907,
                289404, 290868, 270232, 300456, 280318, 278391, 301980, 279405, 327565, 300344, 310848, 279103, 327293, 
                314572, 308674, 277095, 272365, 286807]
    bitSize = [832,740,764,777,835,746,852,830,729,746,869,835,824,811,870,803,770,811,811,864,753,773,792,816,
               864,756,790,822,834,720,807,752,731,790,772,865,786,799,814,755,835,794,798,772,740]
    taskSec = [4,2,4,3,2,1,3,1,4,3,3,5,5,3,3,4,1,5,1,3,3,5,5,1,5,5,3,5, 2,4,2,5,5,5,3,5,5,3,4,4,2,5,4,1,4]
    locSec = [3,2,4,2,2,1,4,3,4,2,5,2,2,4,5,2,3,3,4,2,3,5,5,1,2,3,3,5,3,3,5,3,2,1,1,3,4,1,5,2,2,3,4,5,2]
   

    
elif(total_tasks==50):
    DAG = {0: [1, 2, 3, 4, 10], 1: [2, 5, 6, 7, 11], 2: [3, 7, 8], 3: [4, 8, 9, 14], 4: [9, 10, 15, 21], 5: [11, 16], 6: [11, 12, 17], 7: [12, 13, 18], 8: [13, 14], 9: [14, 15, 20],
         10: [21, 27], 11: [16, 17], 12: [17, 18, 23], 13: [18, 19, 24], 14: [19, 20, 25], 15: [20, 21, 26], 16: [17, 22, 28], 17: [22, 23, 24], 18: [23, 24, 30], 19: [24, 25, 31],
         20: [25, 26, 32], 21: [26, 27, 33], 22: [28, 29], 23: [29, 30, 33], 24: [30, 31, 36], 25: [31, 32, 37], 26: [32, 33, 38, 39], 27: [33, 40], 28: [29, 34], 29: [34, 35],
         30: [35, 36], 31: [36, 37], 32: [37, 38], 33: [39, 40, 46], 34: [35, 41], 35: [36, 42], 36: [37, 42, 43], 37: [38, 43, 44], 38: [39, 44, 45], 39: [45, 46],
         40: [46], 41: [42, 47], 42: [43, 47], 43: [44, 47, 49], 44: [45, 48, 49], 45: [46, 48], 46: [48], 47: [49], 48: [49]}
    commLoad = [304179, 287807, 276080, 304779, 276723, 270859, 288910, 307422, 282297, 321430, 287672, 322701, 306691, 
                325138, 323844, 309175, 286125, 270902, 327209, 307074, 310036, 291561, 286002, 305638, 278970, 274229,
                313131, 297216, 328069, 315147, 277511, 301830, 307842, 324304, 271263, 314018, 319416, 302772, 290777, 
                316972, 329709, 308716, 300357, 323190, 287143, 324958, 282379, 278272, 287392, 323484]
    bitSize = [780,744,821,723,824,752,823,874,777,753,859,775,845,804,750,799,859,764,760,840,786,854,845,844,
               753,820,852,756,786,856,871,857,749,816,830,836,855,737,853,789,720,793,739,809,823,779,790,793,806,739]
    taskSec = [2,5,1,1,1,1,1,4,4,5,3,3,1,3,3,2,3,2,1,5,1,5,3,1,1,2,1,4,3,1,4,2,4,2,4,4,2,4,4,5,3,4,3,3,3,3,3,4,1,2]
    locSec = [4,5,5,5,1,5,5,4,3,5,4,3,2,3,5,1,2,1,5,3,5,4,5,3,4,3,4,2,5,4,2,2,2,4,5,1,1,4,5,3,2,2,5,4,4,3,1,1,4,1]
    
else:
    print("Number of tasks is exceeded")
   
    
    


# In[155]:


#sorting
def reverse_dict(d):
     #Reverses direction of dependence dict
    #>>> d = {'a': (1, 2), 'b': (2, 3), 'c':()}
    #>>> reverse_dict(d)
    #{1: ('a',), 2: ('a', 'b'), 3: ('b',)}
   
    result = {}
    for key in d:
        for val in d[key]:
            result[val] = result.get(val, tuple()) + (key, )
            
    for val in result.values():
        val = [list(val)]
        
       
    return result


# In[156]:


def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.__contains__(start):
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


# In[157]:



def get_core_for_task(low_percent):
    if random() < low_percent:
        return randrange(0, int(total_cores / 2))
    else:
        return randrange(int(total_cores / 2), total_cores)


# In[158]:


def create_individual(DAG, low_percent):
    #individual is a single possible solution for all the task
    """
    Create a member of the population.
    """
    schedule = [-1 for _ in range(total_tasks)] #just initializing the schedule
    for i in range(total_tasks):
        schedule[i] = get_core_for_task(low_percent) 

    return schedule # assign processor to the tasks 


# In[159]:


def create_population(DAG, population_size):
    #population is a collection of n solutions for all the tasks
    """
    Create a number of individuals (i.e. a population).
    tasks: data structure holding tasks
    count: the number of individuals in the population....remove
    """
    return [create_individual(DAG, low_percent) for _ in range(population_size)]


# In[160]:


def scheduleExecutionTime(DAG, individual):
    myNew_dag = copy.deepcopy(DAG)
    reversedDAG = reverse_dict(myNew_dag)
    confidentialityLevel=[1, 2, 3, 4, 5]
    #locationSecurityLevel=[1, 2, 3, 4, 5]
    theta=[3.08E-6, 3.58E-6, 4.15E-6, 4.63E-6, 5.21E-6] #WCCT values from the paper
    T_p = [0 for _ in range(len(individual))] #currentProcessorTime -> taskFinishTime after processing
                                              #Must wait for all predecessor and take max(pre_t)
    T_c = [0 for _ in range(len(individual))]
    f_j = 133E6  #from the paper
    bandwidth=250000
    t_delay=0
    l_i=0
    
    #No predecessor for source TAsk, T_P[0] = t_st + taskProcessingTime
    computationLoad_0 = commLoad[0] #randint(270000, 330000) #[300KCC ± 10%] 
    T_p[0] = 0 + computationLoad_0/f_j
    for key in reversedDAG:
        processorOfKey = individual[key]
        t_c = [0 for _ in range(len(reversedDAG[key]))]
        for val in reversedDAG[key]:
            processorOfVal = individual[val]
            if(processorOfKey != processorOfVal):
                bits_l_sender = bitSize[key] #randint(720,880) #[800bits ± 10%] Communication load
                ########## Security realted within this "#####"
                taskSecurityLevel = taskSec[key] #choice(confidentialityLevel)
                locationSeclevel = locSec[key] #choice(locationSecurityLevel)
                securityLevel=max(taskSecurityLevel,locationSeclevel)
                securityLevelIndex = confidentialityLevel.index(securityLevel)
                WCCT=theta[securityLevelIndex]
                WCET = l_i + (WCCT*bits_l_sender)  #eq1 of Sec
                t_en = WCET
                ################# End Security Realted
                c_st = T_p[val] #+ t_en #finishTimeofPredecessor i.e Val
                st_cw = time.time()
                path = find_shortest_path(graph, processorOfKey, processorOfVal)
                ft_cf = time.time()
                timeHubs = ft_cf - st_cw
                t_delay = max(timeHubs, t_delay)
                t_cmm = bits_l_sender/bandwidth + t_delay
                valIndex = (reversedDAG[key]).index(val)
                #add decriptionTime
                t_de = WCET
                c_ft  = c_st + t_cmm #+ t_de
                t_c[valIndex] = c_ft
            else:
                #no ecription,comm and decription
                c_st = T_p[val] #finishTimeofPredecessor i.e Val
                t_cmm = 0
                valIndex = (reversedDAG[key]).index(val)
                c_ft = c_st + t_cmm
                t_c[valIndex] = c_ft
        LT = max(t_c) #max time from All predecesors 
        t_st = max(LT, T_p[key]) #maxValue between current processor time and highest pred_comm
        executionTime = (commLoad[key])/f_j  #(randint(270000, 330000))/f_j
        t_ft = c_ft + executionTime
        T_p[key] = t_ft
    SL = max(T_p)
    
    return SL
 


# In[161]:


def networkLiTime(DAG, individual):
    l_i=0
    confidentialityLevel=[1, 2, 3, 4, 5]
    #locationSecurityLevel=[1, 2, 3, 4 ,5]
    theta=[3.08E-6, 3.58E-6, 4.15E-6, 4.63E-6, 5.21E-6] #WCCT values from the paper
    E_encription = [0 for _ in range(total_cores)] #initialize encription energy
    E_decription = [0 for _ in range(total_cores)] #initialize decription energy
    new_dag = copy.deepcopy(DAG) 
    
    CHROMOSOME= []
    #initialization
    E_computation = [0 for _ in range(total_cores)]
    E_transmission = [0 for _ in range(total_cores)]
    E_receiving = [0 for _ in range(total_cores)]
    e_t= 0.344E-6 #from table 3.3 in your publication
    e_r= 0.246E-6 #from table 3.3 in your publication
    freeSpacePermitivity =  8.85E-12 #constant
    d = 25  #from the paper
    f_j = 133E6  #from the paper
    AveragePowerConsumption = 200E-3 # averagePower used for each task on node(i), from the paper
    #Note that key is the senderNode, val are the rcver or dep.
    for key in new_dag: 
        sender_node=individual[key]
        computationLoad = commLoad[key]
        t_i = computationLoad/f_j #processingTime
        E_computation[sender_node] += (AveragePowerConsumption * t_i)
        bits_l_sender = bitSize[key] #randint(720,880) #[800bits ± 10%] Communication load
        for val in new_dag[key]:
            receiver_processor=individual[val]
            #check if the task is not performed by the same processor
            if individual[key] != individual[val]:
                ########################################################
                taskSecurityLevel = taskSec[key] #choice(confidentialityLevel) #select security level randomly for each task to be sent
                locationSeclevel = locSec[key] #choice(locationSecurityLevel)
                securityLevel=max(taskSecurityLevel,locationSeclevel)
                securityLevelIndex = confidentialityLevel.index(securityLevel) #this will return the index of the securityLevel above
                WCCT=theta[securityLevelIndex] #worst case computation time that falls into the index
                WCET = l_i + (WCCT*bits_l_sender)  #eq1 of SecurotyPublication
                #Energy consumed by the encripting node Eq 7 of Sec
                E_encription[sender_node] += (WCET*(AveragePowerConsumption/f_j))
                ########################################################
                #add E_transmission sender node Eq 4 ITAS
                E_transmission[sender_node] += ((e_t + freeSpacePermitivity * d * d ) * bits_l_sender)
                path = find_shortest_path(graph, individual[key], individual[val])
                if path:
                    for index in range(1, (len(path)-1)): #last node doesn't transmit -> -1
                        node=path[index]
                        #add transmission energy to relayNode
                        E_transmission[node] += ((e_t + freeSpacePermitivity * d * d ) * bits_l_sender)
                    for index in range(1, len(path)):
                        node=path[index]
                        E_receiving[node] += (e_r * bits_l_sender)
                        if (index + 1) % (len(path)) ==0: 
                            E_decription[node] += (WCET*(AveragePowerConsumption/f_j))
    ########
    CHROMOSOME.append(E_computation)
    CHROMOSOME.append(E_transmission)
    CHROMOSOME.append(E_receiving)
    ########################################################
    CHROMOSOME.append(E_decription)
    CHROMOSOME.append(E_encription)
    ########################################################
    
    E_total_parNode=[sum(i) for i in zip(*CHROMOSOME)]
    
    Residual_parNode=[2000  for _ in range(total_cores)]
    NL_C_i=[x/y for x, y in zip(Residual_parNode, E_total_parNode) if y !=0] 
    NL_C = min(NL_C_i)
   
    return NL_C, E_total_parNode
 


# In[162]:


def get_individual_fitness(DAG, individual):
    """
    Determine the fitness of an individual. 
    """
    
    new_dag = copy.deepcopy(DAG)
    NL_C, E_total_parNode = networkLiTime(new_dag, individual)
    SL = scheduleExecutionTime(new_dag, individual)
    
    if SL > NL_C:
        alpha = NL_C/(NL_C + SL)
        fitness = NL_C - (alpha * SL) 
    else:
        fitness= NL_C - SL
    

    return fitness, NL_C, SL, E_total_parNode


# In[163]:


# Original
def get_population_fitness(DAG, population):
    scores = list()
    NL_Cs = list()
    SLs = list()
    for individual in population:
        fitness, NL_C, SL, E_total_parNode = get_individual_fitness(DAG, individual)
        scores.append(fitness)
        NL_Cs.append(NL_C)
        SLs.append(SL)
    scores=[float(i)/max(scores) for i in scores]
    return scores, NL_Cs, SLs, E_total_parNode


# In[164]:


def crossover(father, mother):
    gene_size = len(father)
    #m: 0 means father and 1 for mother in the gene_pool
    #m: 0 and 1 are not the real gene, just for pool sake
    gene_pool = [0 for _ in range(gene_size)]
    goal = gene_size / 2
    changed = 0
    while changed < goal:
        position = randint(0, (gene_size - 1))
        # we are taking this gene from mama
        if gene_pool[position] == 0:
            changed += 1
            gene_pool[position] = 1

    return [mother[index] if gene_pool[index] == 1 else father[index] for index in range(gene_size)]



# In[165]:


def evolve(population, populationFitness, retain=0.2, random_select=0.05, mutate=0.15):
    graded = []
    for idx, individual in enumerate(population):
        # individual_score, _ = get_individual_fitness(tasks, individual, dag_task)
        graded.append((individual, populationFitness[idx]))

    graded.sort(key=lambda tup: tup[1], reverse=True)
    retain_length = int(len(graded) * retain)
    parents = []
    nextGenration = []
    #m: Note that graded contain two columns [individual  fitness]
    for item in graded[:retain_length]:
        parents.append(item[0])
        
    nextGenration.extend(parents) #randomly additional 10% to replace poor chromosome
    # randomly add other individuals to
    # promote genetic diversity
    #for item in graded[retain_length:]:
        #if random() < random_select:
            #parents.append(item[0])
    p=0  
    for item in population[(int(len(graded) * 0.9)):]:
        p +=1
        graded[(len(graded)-p)]= create_individual(DAG, low_percent)
        
            
    # crossover parents to create children
    parents_length = len(parents)
    desired_length = len(population) - parents_length
    children = []
    while len(children) < desired_length:
        fatherIndex = randint(0, (parents_length - 1))
        motherIndex = randint(0, (parents_length - 1))
        if fatherIndex != motherIndex:
            father = parents[fatherIndex]
            mother = parents[motherIndex]
            child = crossover(father, mother)
            children.append(child)
    nextGenration.extend(children)
    
    
    # mutation
    for individual in nextGenration:
        if random() < mutate:
            position = randrange(0, len(individual))
            individual[position] = get_core_for_task(0.75)
    
    return nextGenration


# In[166]:


#pp = create_population(DAG_5, 10)
#scores, NL_Cs, SLs = get_population_fitness(DAG_5, pp)
#NextGeneration, initial_Population, populationFitness = evolve(pp, scores, retain=0.2, random_select=0.05, mutate=0.15)


# In[167]:


#print(scores)


# In[168]:


#print(initial_Population)


# In[169]:


#print(NextGeneration)


# In[170]:


def main():
    algStartTime=time.time()
    fitness_mean_history = list()
    fitness_min_history = list()
    fitness_max_history = list()
    population_size = 200
    tot_generations = 70
    
    population = create_population(DAG, population_size) 
    scores, NL_Cs, SLs, E_total_parNode = get_population_fitness(DAG, population)
    
    

    # fitness_history = [grade(tasks, population), ]
    fitness_max_history.append( max(scores) )
    fitness_min_history.append( min(scores) )
    fitness_mean_history.append( sum(scores)/len(scores) )
    

    best = None
    m=0
    for i in range(tot_generations):
        population = evolve(population, scores)
        scores, NL_Cs, SLs, E_total_parNode = get_population_fitness(DAG, population)
        bestScore = max(scores)
        fitness_max_history.append( max(scores) )
        fitness_min_history.append( min(scores) )
        fitness_mean_history.append( sum(scores)/len(scores) )
        bestSolution = population[ scores.index(bestScore) ] #index is a keyword
        networkLifeTime = NL_Cs[ scores.index(bestScore) ]
        scheduleExecutionTime = SLs[ scores.index(bestScore) ]
        m += 1
        if((i+1)%tot_generations ==0):
            print(bestSolution)
            print("Network lifetime = " + str(networkLifeTime))
            print("Schedule execution = " + str(scheduleExecutionTime))
            #print("Energy consumed per node = " + str(E_total_parNode))
            

    algEndTime=time.time()
    algorithmTime = algEndTime - algStartTime
    print("Algorithm runtime = " + str(algorithmTime))
 
 
    #plt.plot(fitness_mean_history)
    #plt.title("Mean Progress of Algorithm Training")
    #plt.show()
    
    

    
if __name__ == '__main__':
    main()
    
    

