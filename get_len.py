import re




D={}
for line in open("aws_pseudohap.fa"):
	i=line.strip().split()
	if line[0]==">":
		c=i[0].strip(">")
                D[c]=[]
		continue
	D[c].extend(line.strip())

contig_N = 0
total_seq_len = 0
for tig in D:
    contig_N+=1
    seq = "".join(D[tig]) 
    print tig, len(seq)
