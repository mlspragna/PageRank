import os
import random
import re
import sys
import copy

DAMPING = 0.85
SAMPLES = 10000


def main():
	if len(sys.argv) != 2:
		sys.exit("Usage: python pagerank.py corpus")
	corpus = crawl(sys.argv[1])
	ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
	print(f"PageRank Results from Sampling (n = {SAMPLES})")
	for page in sorted(ranks):
		print(f"  {page}: {ranks[page]:.4f}")
	ranks = iterate_pagerank(corpus, DAMPING)
	print(f"PageRank Results from Iteration")
	for page in sorted(ranks):
		print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
	"""
	Parse a directory of HTML pages and check for links to other pages.
	Return a dictionary where each key is a page, and values are
	a list of all other pages in the corpus that are linked to by the page.
	"""
	pages = dict()

	# Extract all links from HTML files
	for filename in os.listdir(directory):
		if not filename.endswith(".html"):
			continue
		with open(os.path.join(directory, filename)) as f:
			contents = f.read()
			links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
			pages[filename] = set(links) - {filename}

	# Only include links to other pages in the corpus
	for filename in pages:
		pages[filename] = set(
			link for link in pages[filename]
			if link in pages
		)

	return pages


def transition_model(corpus, page, damping_factor):
	probdist={}
	total_pages=len(corpus)
	p1=1/total_pages
	if len(corpus[page])==0:
		for p in corpus.keys():
			probdist[p]=p1
	else:
		d1=1-damping_factor
		p2=d1/total_pages
		p=p2+(damping_factor/len(corpus[page]))
		for i in corpus.keys():
			if i in corpus[page]:
				probdist[i]=p
			else:
				probdist[i]=p2
	return probdist
	"""
	Return a probability distribution over which page to visit next,
	given a current page.

	With probability `damping_factor`, choose a link at random
	linked to by `page`. With probability `1 - damping_factor`, choose
	a link at random chosen from all pages in the corpus.
	"""
	raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
	sample=[]
	pages=list(corpus.keys())
	intial_page=random.choice(pages)
	sample.append(intial_page)
	page=intial_page
	k=n
	n=n-1
	while(n!=0):
		probdist=transition_model(corpus,page,damping_factor)
		page=random.choices(list(probdist.keys()),list(probdist.values()),k=1)[0]
		sample.append(page)
		n=n-1
	pagerank={}
	for i in pages:
		pagerank[i]=sample.count(i)/len(sample)
	return pagerank
	"""
	Return PageRank values for each page by sampling `n` pages
	according to transition model, starting with a page at random.

	Return a dictionary where keys are page names, and values are
	their estimated PageRank value (a value between 0 and 1). All
	PageRank values should sum to 1.
	"""
	raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
	pages=list(corpus.keys())
	N=len(pages)
	intial_prob=1/N
	incoming_links={}
	intial_pagerank={}
	for i in pages:
		if len(list(corpus[i]))==0:
			corpus[i]=set(pages)
	for i in pages:
		intial_pagerank[i]=intial_prob
		incoming_links[i]=[]
		for k,j in corpus.items():
			if i in list(j):
				incoming_links[i].append(k)
	def stop(p1,p2):
		found=False
		for i in pages:
			if abs(p1[i]-p2[i])>0.001:
				found=True
				break
		return found
	count=0
	pagerank1=intial_pagerank
	pagerank=intial_pagerank
	while(stop(pagerank1,pagerank) or count==0):
		pagerank1=copy.deepcopy(pagerank)
		count=1
		for i in pages:
			pagerank[i]=(1-damping_factor)/N
			for j in incoming_links[i]:
				pagerank[i]=pagerank[i]+((damping_factor*pagerank1[j])/len(list(corpus[j])))
	return pagerank1
	"""
	Return PageRank values for each page by iteratively updating
	PageRank values until convergence.

	Return a dictionary where keys are page names, and values are
	their estimated PageRank value (a value between 0 and 1). All
	PageRank values should sum to 1.
	"""

	raise NotImplementedError
def dprint(incoming_links):
	for i,j in incoming_links.items():
		print(i, ":" ,j)

if __name__ == "__main__":
	main()
