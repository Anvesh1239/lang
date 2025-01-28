```python
def findMedianSortedArrays(nums1, nums2):
  m, n = len(nums1), len(nums2)
  p1, p2 = 0, 0

  for _ in range((m + n) // 2 + 1):
    if p1 < m and (p2 >= n or nums1[p1] < nums2[p2]):
      prev = curr
      curr = nums1[p1]
      p1 += 1
    else:
      prev = curr
      curr = nums2[p2]
      p2 += 1

  return (prev + curr) / 2 if (m + n) % 2 == 0 else curr
```