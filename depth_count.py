# Reads MDXI01 vcf file and saves tallies if all, only one, half,
# or no reads support, or other, into depth_count txt file.

import sys, string, glob

hdr = open("MDXI01.vcf", 'r')
f1 = open("depth_count.txt", 'w')

hdr_dict = {}

# all the counters for amount each line has reads supporting
none = 0
half = 0
one = 0
full = 0
other = 0

# check vcf cols
for line in hdr.xreadlines():
	items = line.split("\t")
	total = int(items[3])			# total matching reads

	# reads column is empty if total is 0
	if total > 0:
		reads = items[4]

		# count up + and ^ chars in reads and compare to total
		count = reads.count("+") + reads.count("^")

		# compare to total and add to its respective tally
		if count == total:
			full = full + 1
		elif count == 1:
			one = one + 1
		elif count + total == 2*total:
			half = half + 1
		elif count == 0:
			none = none + 1
		else:
			other = other + 1

print full, one, half, none, other
f1.write("\n%d\t%d\t%d\t%d\t%d\n" %(full, one, half, none, other))

f1.close()
