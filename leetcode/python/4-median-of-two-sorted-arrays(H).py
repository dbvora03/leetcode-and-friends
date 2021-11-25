class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        
        if len(A) > len(B):
            A, B = B, A
        
        totalSize = len(A) + len(B)
        halfSize = totalSize // 2
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # Partition for A
            j = halfSize - i - 2 # Partition for B
            
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            # Check if we have a corrent partition
            if Aleft <= Bright and Bleft <= Aright:
                if totalSize % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
            