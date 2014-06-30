#
# plot
#


getrange = function(f){
	d = read.table(f, as.is = T)
	d = d[order(d[,1]),]
	return( c(mean(d[6:95]), d[6], d[95]))
}

fs = c("all_0.1_0.1.fs", "all_0.2_0.1.fs", "all_0.3_0.1.fs", "all_0.4_0.1.fs")
ffs = c(0.1, 0.2, 0.3, 0.4)
toplot = data.frame(matrix(nrow = 4, ncol = 5))

for (i in 1:length(fs)){
	t = getrange(fs[i])
	toplot[i,1] = ffs[i]
	toplot[i,2] = 0.01
	toplot[i,3:5] = t

}
print(toplot)

toplot2 = data.frame(matrix(nrow = 4, ncol = 5))

for (i in 1:length(fs)){
        t = getrange(paste0(fs[i], "_noannot"))
        toplot2[i,1] = ffs[i]
        toplot2[i,2] = 0.01
        toplot2[i,3:5] = t

}
print(toplot2)

pdf("plot_baseline_0.1.pdf")
plot(toplot[,1], toplot[,3], pch = 20, xlim = c(0, 0.5), ylim = c(0, 0.6), xlab = "Simulated prop. of causal variants in annotation", ylab= "Estimated prop. of causal variants in annotation")
for (i in 1:nrow(toplot)){
	lines( c(toplot[i,1], toplot[i,1]), c(toplot[i,4], toplot[i,5]))
}

points(toplot2[,1]+0.01, toplot2[,3], pch = 20, xlim = c(0, 0.5), ylim = c(0, 0.6), col = "grey")

for (i in 1:nrow(toplot2)){
        lines( c(toplot2[i,1]+0.01, toplot2[i,1]+0.01), c(toplot2[i,4], toplot2[i,5]), col = "grey")
}
lines(c(-10, 10), c(0.1, 0.1), col = "grey", lty = 2)
text(0.5, 0.09, lab = "Prop. of non-causal SNPs in annotation", adj = c(1, 1), col = "grey", cex = 0.6)
legend("topleft", legend = c("annotation not in model", "annotation in model"), col = c("grey", "black"), bty = "n", pch = c(20, 20))

dev.off()

	

