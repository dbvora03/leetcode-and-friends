class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        denom = (coordinates[1][0] - coordinates[0][0])
        if denom == 0:
            slope = float("Inf")
        else:
            slope = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        
        for i in range(len(coordinates) - 1):
            point_b = coordinates[i + 1]
            point_a = coordinates[i]
            this_denom = (point_b[0] - point_a[0])
            
            if this_denom == 0:
                this_slope = float("Inf")
            else:
                this_slope = (point_b[1] - point_a[1]) / (point_b[0] - point_a[0])
            
            if this_slope != slope:
                return False
        
        return True