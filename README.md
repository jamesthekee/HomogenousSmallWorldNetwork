Algorithm used to generate Homogeneous Small World Networks of even degree. This is similar to Watts-Strogatz,
except the produced graph has a homogeneous degree distribution.

It is constructed by random link rewiring from a regular network such that the degree of each node remains unchanged. 
In particular the algorithm proceeds as so:
1. Generate regular network of degree K
2. Randomly select edges A-B, C-D s.t A,B,C,D are all distinct nodes.
3. If the current graph has
   1. an edge A-D or B-C and (A-C or B-D) reselect A,B,C,D by returning to step 2
   2. an edge A-D or B-C but not (A-C or B-D) rewire to AC, BD
   3. Otherwise rewire to AD, BC
4. Continues for PE steps, where E is the number of edges in the network and P characterizes the randomness of the network. 

When P > 1 the network topology is essentially random

## References

Here are some papers using this algorithm.

1. Santos et al. Epidemic spreading and cooperation dynamics on homogeneous small-world networks. Phys. Rev. E 72, 056128 (2005).
2. Zhang et al. Effects of behavioral response and vaccination policy on epidemic spreading - an approach based on evolutionary-game dynamics. Sci Rep 4, 5666 (2015).
3. Lü et al. The small world yields the most effective information spreading. New J. Phys. 13, 123005 (2011).
