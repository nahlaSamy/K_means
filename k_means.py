import math


class K_Mean:
    


    def __init__(self, data_set, centroid1=[3, 4], centroid2=[8, 5], way=1):
        self.way = way
        self.points = data_set
        self.centroid1 = centroid1
        self.centroid2 = centroid2
        self.driver_code()


    def euclidian_distance(self, x1, x2, y1, y2):
        return math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))


    def manhattan_distance(self, x1, x2, y1, y2):
        return abs(x1 - x2) + abs(y1 - y2)


    # way=1 means Euclidian distance formula
    # way=2 means Manhattan distance formula

    def iteration(self, m1, m2):
        m1_distance = []
        m2_distance = []
        cluster = []
        points = self.points

        for i in range(len(self.points)):
            if self.way == 1:
                m1_distance.append(round(self.euclidian_distance(points[i][0], m1[0], points[i][1], m1[1]), 2))
                m2_distance.append(round(self.euclidian_distance(points[i][0], m2[0], points[i][1], m2[1]), 2))

                if m1_distance[i] < m2_distance[i]:
                    cluster.append(1)
                else:
                    cluster.append(2)


            elif self.way == 2:
                m1_distance.append(self.manhattan_distance(points[i][0], m1[0], points[i][1], m1[1]))
                m2_distance.append(self.manhattan_distance(points[i][0], m2[0], points[i][1], m2[1]))

                if m1_distance[i] < m2_distance[i]:
                    cluster.append(1)
                else:
                    cluster.append(2)
            
        # Print Table
        print("Points | M1 Distance | M2 Distance | Cluster")
        for i in range(len(self.points)):
            print(points[i], " ", m1_distance[i]," ", m2_distance[i], " ", cluster[i])
        
        return m1_distance, m2_distance, cluster


    def calculate_new_centroids(self, iteration):
        points = self.points
        cluster = iteration[2]
        m1_count = 0
        m2_count = 0
        m1_x_sum = 0
        m1_y_sum = 0
        m2_x_sum = 0
        m2_y_sum = 0


        for i in range(len(points)):
            if cluster[i] == 1:
                m1_count += 1
                m1_x_sum += points[i][0]
                m1_y_sum += points[i][1]

            elif cluster[i] == 2:
                m2_count += 1
                m2_x_sum += points[i][0]
                m2_y_sum += points[i][1]
        
        new_m1 = [round(m1_x_sum/m1_count, 2), round(m1_y_sum/m1_count, 2)]
        new_m2 = [round(m2_x_sum/m2_count, 2), round(m2_y_sum/m2_count, 2)]

        return new_m1, new_m2
    

    def driver_code(self):
        i = 0
        while True:
            i+=1

            new_points = self.calculate_new_centroids(self.iteration(self.centroid1, self.centroid2)) 
            if new_points[0] == self.centroid1 and new_points[1] == self.centroid2:
                break
            else:
                self.centroid1 = new_points[0]
                self.centroid2 = new_points[1]
                self.iteration(self.centroid1, self.centroid2)
            
                    
