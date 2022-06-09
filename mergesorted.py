def sortedMerge(a, b, res, n, m):
    # Concatenate two arrays
    i, j, k = 0, 0, 0
    while (i < n):
        res[k] = a[i]
        i += 1
        k += 1
    while (j < m):
        res[k] = b[j]
        j += 1
        k += 1
  
    # sorting the res array
    res.sort()
  
# Driver code
a = list(map(int, input("Enter the values with spaces between them: ").split()))
b = list(map(int, input("Enter the values with spaces between them: ").split()))
#a = [ 10, 5, 15 ]
#b = [ 20, 3, 2, 12 ]
n = len(a)
m = len(b)
# Final merge list
res = [0 for i in range(n + m)]
sortedMerge(a, b, res, n, m)
print ("Sorted merged list :")
for i in range(n + m):
    print(res[i],end=" ")
