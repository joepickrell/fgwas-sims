
f = list.files(pattern = "_wf")

toprint = data.frame(matrix(nrow = length(f), ncol = 7))

for (i in 1:length(f)){
	d = read.table(f[i], as.is = T, head = T)
	tmp = d[2500:7500,]
	tmp = tmp[tmp$a1f > 0.1 & tmp$a1f < 0.9,]
	index = sample(1:nrow(tmp), 1)
	tmp2 = tmp[index,]
	toprint[i,1:5] = tmp2[1,]
	toprint[i,6] = rownames(tmp2[1,])
	toprint[i,7] = f[i]
}

write.table(toprint, file = "causals.txt", quote = F, row.names = F, col.names = F)


