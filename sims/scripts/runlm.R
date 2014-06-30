
a = commandArgs(T)

infile = a[1]
legendfile = a[2]
phenofile = a[3]
outfile = a[4]
index = a[5]

tmp = strsplit(infile, split = "[.]")[[1]]
print(tmp)
chrom = tmp[length(tmp)-6]
print(chrom)

d = read.table(infile, as.is = T)
tmp = strsplit(infile, split = "[.]")[[1]]
s = read.table(legendfile, as.is = T, head = T)
p = read.table(phenofile, as.is = T)
geno = data.frame(matrix(nrow = nrow(d), ncol = ncol(d)/2))
for (i in 1:(ncol(d)/2)){
	print (i)
	geno[,i] = d[,(i*2-1)] + d[,(i*2)]
}

toprint= data.frame(matrix(nrow = nrow(s), ncol = 8))
colnames(toprint) = c("SNPID", "CHR", "POS","F", "Z", "SE", "N", "SEGNUMBER")
for (i in 1:nrow(geno)){
	print(i)
	g = as.numeric(geno[i,])

	l = lm(p[,3] ~ g)
	c = summary(l)$coef
	print(c)
	m = NA
	se = NA
	Z = NA
	if (nrow(c) > 1){
		m = c[2,1]
		se = c[2,2]
		Z = m/se
	}
	f = sum(g)/(2*ncol(geno))
	toprint[i,] = c(s[i,1], chrom, s[i,2], f, Z, se, "5000", index)
}

write.table(toprint, file = outfile, quote = F, row.names = F)
