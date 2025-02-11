import os
from physcraper import opentree_helpers
from physcraper.treetaxon import TreeTax


json_file = "main.json"

estimated_tree = "turtle_iqtree.tre"
estimated_tree_OTT = "turtle_iqtree_OTT.tre"


#Use the bulk TNRS output to match your existing tree to standard labels
tt = TreeTax(otu_json=json_file, treefrom=estimated_tree)

#Use write out your tree with standard labels
tt.write_labelled(estimated_tree_OTT, label = "^ot:ottTaxonName", norepeats=False)

