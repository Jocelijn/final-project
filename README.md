# final-project

1. Creating a webcrawler;
2. Converting result into an adjacency matrix;
3. Computing a pagerank using the adjacency matrix;
4. Cool interface

For step 2.
Converting url dictionary into matrix form (ones and zeros) [preferably list of lists].

Given:

Dictionary (webcrawler output); 

[the following ordered links]:list containing all webpages checked/all possible links)




Dictionary: {'http://www.uu.nl': [list of links]}

'http://www.uu.nl' is the row of the matrix
it has an assigned number (i.e. which row it is, given by the order in [the following ordered links])

create a list Lijst (this will be a row of the matrix) with the same length as [the following ordered links] (all 0s?)
check [list of links] for [the following ordered links]:
if element n in [the following ordered links] is in [list of links] then element n in Lijst=1. Otherwise=0

check the next webpage
