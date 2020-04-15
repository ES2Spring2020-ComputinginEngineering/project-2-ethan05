Running my code is relatively simple. For parts 2 and 3, make sure the CKD file is on the desktop. For part 4, make sure the driver and function code as well as the CKD file are all in the same folder on the desktop. The part 4 code will not pull the file if it is not in the same folder as the driver and function code.

The nearest neighbor classification file in my repository is code that takes a data set and compares a randomly generated point and compares the point to the data set. Depending on the distance of that random point to other points, it determines if that randomly generated point is a 1(yes) for CKD or 0(no) for CKD. The kmeans clustering functions file is code that has all of the functions for the kmean clustering driver. The driver will run on its own as long as the functions code is in the same folder without altering the functions. Those two files work together to create centroids in the graph of the CKD data based on how many centroids the user wants to create. The CKD file has all of the raw data needed for the initial scatter plots to compare the new data to. In order to obtain the results in my report, change k to 1, 2, and 3 in the driver file and run code multiple times to obtain similar data.

Here are the functions and their uses in the clustering algorithm:

scale_x has one parameter x and is used to scale the x values in the data set to have the min at 0. The return value is all the x values in the data set reduced by the min in the data set.

scale_y has one parameter y and is used to scale the y values in the data set to have the min at 0. The return value is all the y values in the data set reduced by the min in the data set.

select(K) has one parameter K and randomizes a K value. (number of centroids) It returns a random K value.
assign has three parameters; centroids, hemoglobin, and glucose. It assigns data points to the nearest centroid and returns these assignments.

update has four parameters; K, a, hemoglobin, and glucose. This function updates the location of the centroid by taking the average of all the data points assigned to it. It returns the new centroid based on all the assigned points to that centroid (the averages of those points).

iterate has four parameters; K, hemoglobin, glucose, and m. This function repeats assign and update until a specified number of iterations are completed. It returns the last assignment and update.

rescale has two parameters; K and iterate. The function rescales the data so that the centroid points can be graphed with the data from the CKD file. It returns the new centroid points scaled.

