#Site miroir de lyon2
chooseCRANmirror()
29

#Intall packages
#igraph
#igraphdata

#Libraries
library(igraph)
library(igraphdata)

g <- read.graph("c:/Users/taogr/PycharmProjects/Bigdata/data_files/graph_authors.txt", format = "ncol")
sg <- induced.subgraph(g, 1:12, "create_from_scratch")
deg <- degree(g)
plot(g, layout=layout.fruchterman.reingold, vertex.size=deg*3)

vcount(g)
ecount(g)
closeness(g)
