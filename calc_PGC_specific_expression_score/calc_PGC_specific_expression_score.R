#!/usr/bin/env R

library(tidyverse)

args <- commandArgs(trailingOnly=T)

SSR <- function(x,y){
  return(sum((x-y)^2))
}

pattern.df <- data.frame(
                         PGC_specific = c(rep(0,2),1,0.5,rep(0,2)),
                         cell_type = c('iPSCs','iMeLCs','PGCLCs','pmPGCLCs','TCs','T1LCs')
                         )

cell.info.name <- args[1]
cell.info <- read.table(cell.info.name,header=T)
cell.info <- cell.info[cell.info$class=="vitro",]

gene.info.name <- args[2]
gene.info <- read.table(gene.info.name,header=T)
gene.info$ens_Id <- sub("\\.[0-9]+","",gene.info$ens_Id)
gene.info.cds <- gene.info[gene.info$group == "protein_coding",]

symbol.ens_Id.df <- gene.info.cds[,c('name','ens_Id')]
colnames(symbol.ens_Id.df) <- c('gene','ens_Id')

data.name <- args[3]
data <- read.csv(data.name,header=T,row.names=1,check.names=F)

data <- data[rownames(data) %in% gene.info.cds$name,]
colnames(data) <- gsub('\\-[0-9]','',colnames(data))

data <- data[,as.character(cell.info$cell_Id)]

data.scale <- as.data.frame(t(apply(data, 1, scale)))
colnames(data.scale) <- colnames(data)

data.scale.t <- as.data.frame(t(data.scale))
data.scale.t$cell_Id <- cell.info$cell_Id
data.scale.t$cell_type <- factor(cell.info$cell_type,levels=c('iPSCs','iMeLCs','PGCLCs','pmPGCLCs','TCs','T1LCs'))
data.long <- data.scale.t %>% gather(key=gene,value=zscore,-cell_Id,-cell_type) %>% group_by(cell_type,gene)

data.long.mean <- data.long %>% summarize(mean = mean(zscore))

data.mean <- data.long.mean %>% spread(key=cell_type,value=mean)
data.mean <- data.frame(data.mean)
rownames(data.mean) <- data.mean$gene
data.mean <- data.mean[,2:ncol(data.mean)]

data.mean.rescale <- sweep(data.mean,1,apply(data.mean,1,min))
data.mean.rescale <- sweep(data.mean.rescale,1,apply(data.mean.rescale,1,max),FUN="/")



SSR.res.v <- c()
for(i in 1:nrow(data.mean.rescale)){
  exp.v <- as.numeric(data.mean.rescale[i,])
  SSR.PGC_specific <- SSR(exp.v,pattern.df$PGC_specific)
  SSR.res.v <- c(SSR.res.v,SSR.PGC_specific)
}

res.df <- data.frame(gene = rownames(data.mean.rescale), SSR = SSR.res.v)
res.df <- merge(res.df,symbol.ens_Id.df,by="gene")
res.df$PGC_specific_score <- -log(res.df$SSR,10)


out.name <- args[4]
write.table(res.df,out.name,col.names=T,row.names=F,sep="\t",quote=F)


