#Project 2
#Step 4 Driver 
#by Ethan Donnelly
#Individual work, spent about 30 minutes on this code.


from part4functions import *
import matplotlib.pyplot as plt

glucose, hemoglobin, classification = openckdfile()

#k values were changed for different graphs
k=2
m=10

centroids = select(k)
assignments = assign(centroids, hemoglobin, glucose)
final_a, final_p = iterate(k,hemoglobin,glucose,m)

point=(rescale(k,final_p))
print(final_a)
print(classification)
plt.figure()
plt.plot((hemoglobin[classification==1]),(glucose[classification==1]), "k.", label = "Class 1")
plt.plot((hemoglobin[classification==0]),(glucose[classification==0]), "r.", label = "Class 0")
plt.scatter(point[0::2],point[1::2], s=100)
plt.xlabel("Hemoglobin")
plt.ylabel("Glucose")
plt.legend()
plt.show()
