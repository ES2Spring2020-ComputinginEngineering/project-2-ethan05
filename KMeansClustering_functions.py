#Project 2
#Step 4 Functions
#by Ethan Donnelly
#Individual work, spent 9 hours on this assignment

import numpy as np
import statistics as stat

def openckdfile():
    
#openckdfile opens up the data set file for CKD, it has no parameters or return value.
    
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def scale_x(x):
    
#scale_x has one parameter x and is used to scale the x values in the data set to have the min at 0.
#The return value is all the x values in the data set reduced by the min in the data set.
    
    x_scale = []
    for i in range(0,158):
        w = ( (x[i]-3.1) / (17.8-3.1) ) 
        x_scale.append(w)
    return x_scale

def scale_y(y):
    
#scale_y has one parameter y and is used to scale the y values in the data set to have the min at 0.
#The return value is all the y values in the data set reduced by the min in the data set.
    
    y_scale = []
    for i in range(0,158):
        w = ( (y[i]-70) / (490-70) )
        y_scale.append(w)
    return y_scale

def select(K):
    
#select(K) has one parameter K and randomizes a K value. (number of centroids)
    
    return np.random.random((K, 2))

def assign(centroids, hemoglobin, glucose):
    
#assign has three parameters; centroids, hemoglobin, and glucose.
#It assigns data points to the nearest centroid. 
    
    K = centroids.shape[0]
    distances = np.zeros((K, len(hemoglobin)))
    for i in range(K):
        g = centroids[i,1]
        h = centroids[i,0]
        distances[i] = np.sqrt((scale_x(hemoglobin)-h)**2+(scale_y(glucose)-g)**2) 
    assignments = np.argmin(distances, axis = 0)    
    return assignments

def update(K,a,hemoglobin,glucose):
    
#update has four parameters; K, a, hemoglobin, and glucose.
#This function updates the location of the centroid by taking the average of all the data points assigned to it.
    
    L=[]
    M=[]
    N=[]
    for i in range(0,K):
        l=[]
        m=[]
        for j in range(0,158):
            if a[j]==i:
                x=scale_x(hemoglobin)[j]
                y=scale_y(glucose)[j]
                l.append(x)
                m.append(y)
        L.append(l)
        M.append(m)
    for i in range(0,K):
        p=stat.mean(L[i])
        t=stat.mean(M[i])
        N.append(p)
        N.append(t)
    NL=np.array(N)
    N=np.reshape(NL,(K,2))
    return N
    
def iterate(K,hemoglobin,glucose,m):
    
#iterate has four parameters; K, hemoglobin, glucose, and m.
#This function repeats assign and update until a specified number of iterations are completed. 
    
    p=select(K)
    for i in range(0,m):
        a=assign(p,hemoglobin,glucose)
        np=update(K,a,hemoglobin,glucose)
        p=np
    return a,p


def rescale(K,iterate):
    
#rescale has two parameters; K and iterate.
#The function rescales the data so that the centroid points can be graphed with the data from the CKD file.
    
    point=[]
    l=iterate.tolist()
    for i in range(0,K):
        g = l[i][1]
        h = l[i][0]
        RSX=h*14.7+3.1
        RSY=g*420+70
        point.append(RSX)
        point.append(RSY)
    return point
