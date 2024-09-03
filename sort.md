# Sorting


In computer science, sorting is arranging elements in an ordered sequence. Over  
the years, several algorithms were developed to perform sorting on data,  
including merge sort, quick sort, selection sort, or bubble sort. (The other  
meaning of sorting is categorizing; it is grouping elements with similar  
properties.)  

The opposite of sorting, rearranging a sequence of elements in a random or  
meaningless order, is called shuffling.  


Data can be sorted alphabetically or numerically. The sort key specifies the  
criteria used to perform the sort. It is possible to sort objects by multiple  
keys. For instance, when sorting users, the names of the users could be used as  
primary sort key, and their occupation as the secondary sort key.  

## Sorting order

A standard order is called the ascending order: a to z, 0 to 9. The reverse  
order is called the descending order: z to a, 9 to 0. For dates and times,  
ascending means that earlier values precede later ones e.g. 1/1/2020 will sort  
ahead of 1/1/2021.  

## Stable sort

A stable sort is one where the initial order of equal elements is preserved.  
Some sorting algorithms are naturally stable, some are unstable. For instance,  
the merge sort and the bubble sort are stable sorting algorithms. On the other  
hand, heap sort and quick sort are examples of unstable sorting algorithms.  

Consider the following values: 3715*5*93. A stable sorting produces the  
following: 1335*5*79. The ordering of the values 3 and 5 is kept. An unstable  
sorting may produce the following: 133*5*579.  

Python uses the timsort algorithm. It is a hybrid stable sorting algorithm,  
derived from merge sort and insertion sort. It was implemented by Tim Peters in  
2002 for use in the Python programming language.  
