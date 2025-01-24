```python
def find_median(nums1, nums2):
    m, n = len(nums1), len(nums2)
    p1, p2 = 0, 0

    for _ in range((m + n) // 2 + 1):
        if p1 < m and p2 < n:
          if nums1[p1] <= nums2[p2]:
            current = nums1[p1]
            p1 += 1
          else:
            current = nums2[p2]
            p2 += 1
        elif p1 < m:
          current = nums1[p1]
          p1 += 1
        else:
          current = nums2[p2]
          p2 += 1

    if (m + n) % 2 == 0:
      previous = current
      if p1 < m and p2 < n:
        if nums1[p1] <= nums2[p2]:
          current = nums1[p1]
        else:
          current = nums2[p2]
      elif p1 < m:
        current = nums1[p1]
      else:
        current = nums2[p2]
      return (previous + current) / 2
    else:
      return current
```