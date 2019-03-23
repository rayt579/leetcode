import math
class Solution:
    def kClosest(self, points, K):
        distances = [(self.eucl_dist_from_origin(point), point) for point in points]
        distances.sort()
        return [distances[i][1] for i in range(K)]

    def eucl_dist_from_origin(self, point):
        return math.sqrt(math.pow(point[0], 2) + math.pow(point[1],2))

sol = Solution()
print('Expect [-2, 2] : {}'.format(sol.kClosest([[1,3], [-2, 2]], 1)))
