from os.path import join
import numpy as np
import scipy.sparse as sp
from utils import settings
from global_.prepare_local_data import IDF_THRESHOLD
from time import sleep
local_na_dir = join(settings.DATA_DIR, 'local', 'graph-1')


def encode_labels(labels):
    classes = set(labels)
    classes_dict = {c: i for i, c in enumerate(classes)}
    return list(map(lambda x: classes_dict[x], labels))


def load_local_data(path=local_na_dir, name='cheng_cheng'):
    # Load local paper network dataset
    print('Loading {} dataset...'.format(name), 'path=', path)

    idx_features_labels = np.genfromtxt(join(path, "{}_pubs_content.txt".format(name)), dtype=np.dtype(str))
    features = np.array(idx_features_labels[:, 1:-1], dtype=np.float32)  # sparse?
    
    #print(idx_features_labels)
    labels = encode_labels(idx_features_labels[:, -1])
    print("-----------------------------------------1")
    print(labels, "labels")
    # build graph
    idx = np.array(idx_features_labels[:, 0], dtype=np.str)
    idx_map = {j: i for i, j in enumerate(idx)}
    edges_unordered = np.genfromtxt(join(path, "{}_pubs_network.txt".format(name)), dtype=np.dtype(str))
    edges = np.array(list(map(idx_map.get, edges_unordered.flatten())),
                     dtype=np.int32).reshape(edges_unordered.shape)
    if edges.shape == (2,):
        edges = np.array([[0,1],[1,0]])
    adj = sp.coo_matrix((np.ones(edges.shape[0]), (edges[:, 0], edges[:, 1])),
                        shape=(features.shape[0], features.shape[0]), dtype=np.float32)

    # build symmetric adjacency matrix
    adj = adj + adj.T.multiply(adj.T > adj) - adj.multiply(adj.T > adj)

    print('Dataset has {} nodes, {} edges, {} features.'.format(adj.shape[0], edges.shape[0], features.shape[1]))

    return adj, features, labels


if __name__ == '__main__':
    load_local_data(name='zhigang_zeng')
