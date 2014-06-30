
a = commandArgs(T)
stem = a[1]
d = read.table(paste0(stem, ".hap"), as.is = T)
d2 = read.table(paste0(stem, ".legend"), as.is = T, head = T)
f = apply(d, 1, mean)
d2$a1f = f

write.table(d2, file = paste0(stem, ".legend_wf"), quote = F, row.names = F)

