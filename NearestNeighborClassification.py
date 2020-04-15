#Project 2 
#Part 2
#by Ethan Donnelly
#Individual work and 6 hours spent on this assignment.

#Imports
import numpy as np
import matplotlib.pyplot as plt
from random import random

#Function List
def shortest_distance(x1,y1):
    
#shprtest_distance has two parameters X1 and y1.
#The function finds the shortest length 
    
    length=[]
    for i in range(0,158):
        z = np.sqrt( (x1-x[i]) **2 + (y1-y[i]) **2)
        length.append(z)
    return p[length.index(min(length))]

def scale_x(x):
    
#scale_x has the parameter x.
#The function scales all the x data points down so the min value starts at 0.
    
    x_scale = []
    for i in range(0,158):
        w = ( (x[i]-3.1) / (17.8-3.1) ) 
        x_scale.append(w)
    return x_scale

def scale_y(y):
    
#scale_y has the parameter y.
#The function scales all the y data points down so the min value starts at 0.
    
    y_scale = []
    for i in range(0,158):
        w = ( (y[i]-70) / (490-70) )
        y_scale.append(w)
    return y_scale

def color(Class):
    
#color has one parameter, Class.
#It assigns data points with the class 1 to be blue and points with the class 0 to be red.
    
    color_list=[]
    for i in range(0,158):
        if Class[i]==1:
            color= 'blue'
            color_list.append(color)
        else:
            color= 'red'
            color_list.append(color)
    return color_list

def createTestCase():
    
#createTestCase has no parameters.
#It creates a random data point within the bounds given in the data set.
    
    rndm = []
    new_Blood_Glucose=random()
    x1 = new_Blood_Glucose
    rndm.append(x1)
    new_Hemoglobin = random()
    y1 = new_Hemoglobin
    rndm.append(y1)
    return rndm

def DistanceArray(newpoint):
    
#DistanceArray has one parameter, newpoint. 
#It finds the length between the new point and origin on new graph by scaling the new point by the same scale that the data set was scaled by.
    
    length=[]
    for i in range(0,158):
       z=np.sqrt((newpoint[0] - scale_x(hemoglobin)[i]) **2 + (newpoint[1]-scale_y(glucose)[i]) **2)
       length.append(z)
    return(length)

def nearestNeighborClassifier(newpoint):
    Array=np.array(DistanceArray(newpoint))
#go over to numpy use argmin
#convert list to array then use argmin to find index
    
#nearestNeighborClassifier has one parameter, newpoint.
#This function finds the closest point to the new point and classifies the new point as 0 or 1 depending on the classification of the nearest point.

    k=np.argmin(Array)
    return classification[k] #classification at index

def newcolor(newpoint):
    
#newcolor has one parameter, newpoint.
#It makes the new data point blue if it is classified as 1 or red if it is 0.
    
    newclass=nearestNeighborClassifier(newpoint)
    color_list=[]
    if newclass==1:
        color='blue'
        color_list.append(color)
    else:
        color= 'red'
        color_list.append(color)
    return color_list   

def graphtestcase(newpoint):
    
#graphtestcase has one parameter, newpoint.
#It plots the newly generated point with its correct color on the graph of the given data set graph.
    
    plt.scatter(scale_x(hemoglobin) , scale_y(glucose) , s=1, color=color(classification))
    plt.scatter(newpoint[0],newpoint[1],s=100, color=newcolor(newpoint))
    plt.xlabel('Blood Glucose Random')
    plt.ylabel('Hemoglobin')
    plt.title('Chronic Kidney Disease chart w/ Test Point', fontdict=None, loc='center')


 
#Main Script

def openckdfile():
    
#openckdfile opens up the data set file for CKD, it has no parameters or return value.
    
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

glucose, hemoglobin, classification = openckdfile()

new = createTestCase()

print(graphtestcase(new))

#PART 3 BELOW


def kNearestNeighborClassifier(k,newpoint):
    
#kNearestNeighborClassifier has two parameters; k and newpoint.
#Depending on the nearest point, it classifies the newpoint as 1 or 0.
    
    l=DistanceArray(newpoint)
    sorted_indices = np.argsort(l)
    k_indices = sorted_indices[:k]
    g=0
    for i in range(0,k):
        g+=classification[k_indices[i]]     
    if g>(k/2):
        return 1
    else:
        return 0

def k_newcolor(k,newpoint): 
    
#k_newcolor has two parameters; k and newpoint.
#depending on the class of the new point, it will assign red for 0 and  for blue.
    
    newclass=kNearestNeighborClassifier(k,newpoint)
    color_list=[]
    if newclass==1:
        color='blue'
        color_list.append(color)
    else:
        color= 'red'
        color_list.append(color)
    return color_list   

def graphktestcase(k,newpoint):
    
#graphktestcase has two parameters; k and newpoint.
#It graphs the new test point on the plot with the original data from the set.
    
    plt.scatter(scale_x(hemoglobin) , scale_y(glucose) , s=1, color=color(classification))
    plt.scatter(newpoint[0],newpoint[1],s=100, color=k_newcolor(k,newpoint))
    plt.xlabel('Blood Glucose Random')
    plt.ylabel('Hemoglobin')
    plt.title('Chronic Kidney Disease chart w/ Test Point', fontdict=None, loc='center')


k = 3

print(kNearestNeighborClassifier(k,new))

print(graphktestcase(k,new))
