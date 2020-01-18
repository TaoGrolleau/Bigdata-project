#Site miroir de lyon2
chooseCRANmirror()
29

#Intall packages
install.packages("igraph")
install.packahes("igraphdata")
install.packages("here")

#Libraries
library(igraph)
library(igraphdata)

setwd("c:/Users/taogr/PycharmProjects/Bigdata")
relativepath <- "/data_files/graph_authors.txt"
path <- paste(getwd(), relativepath, sep="")

g <- read.graph(path, format = "ncol")
sg <- induced.subgraph(g, 1:12, "create_from_scratch")
deg <- degree(g)
plot(g, layout=layout.fruchterman.reingold, vertex.size=deg*3, edge.label=E(g)$weight, edge.width = E(g)$weight * 2,
     margin = -0.2)

vcount(g)
ecount(g)
closeness(g)
