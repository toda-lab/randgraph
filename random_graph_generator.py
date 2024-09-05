import random
import math

from argparse import ArgumentParser

def get_option():
    """Gets command-line options."""
    ap = ArgumentParser(description="Random graph generator")
    ap.add_argument(
        "-s", "--seed", type=int, help="Specify random number seed")
    ap.add_argument(
        "-n", "--vertex", type=int, required=True, help="Specify number of vertices")
    ap.add_argument(
        "-d", "--density", type=float, required=True, help="Specify graph density")
    return ap.parse_args()

args       = get_option()
seed       = args.seed
num_verts  = args.vertex
density    = args.density
num_edges  = math.floor(((num_verts*(num_verts-1))/2)*density)

if seed is not None:
    random.seed(seed)

if density < 0 or density >1:
    raise Exception("invalid density")
if num_edges == 0:
    raise Exception("no edge")

all_edges = [(i,j)\
    for i in range(1, num_verts+1)\
        for j in range(i+1, num_verts+1)]

if len(all_edges) < num_edges:
    raise Exception("too many edges!")

random.shuffle(all_edges)
print(f"c seed {seed}")
print(f"c density {density}")
print(f"p {num_verts} {num_edges}")
for u in range(1,num_verts+1):
    print(f"n {u}")
for u,v in sorted(all_edges[:num_edges]):
    print(f"e {u} {v}")
