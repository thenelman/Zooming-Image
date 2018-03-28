# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 20:39:45 2018

@author: L NelSoN ManGanGchA
"""
import numpy as np
import matplotlib.pyplot as plt

class Pivot: 
    "class to store the co ordinate of the pivot"
    """pivot row position should lie between [row/2] and [(k*(row-1)+1) - (row/2)]"""
    """pivot column position should lie between [column / 2] and [(k*(column-1)+1) - (column / 2)]"""

    def __init__(self,rw,cl):
        self.rw = rw #row position
        self.cl = cl #col position
        
def imageZoom(im,scale,pivot): # zooms the image by scale times
    """Zooms the RGB image"""
    
    blue_im = im[:,:,0]
    red_im = im[:,:,1]
    green_im = im[:,:,2]
    row, col, dim = im.shape
    zoomed_blue = zoom(blue_im,scale,pivot)
    zoomed_red = zoom(red_im,scale,pivot)
    zoomed_green = zoom(green_im,scale,pivot)
    #recombine the pixels
    zoomedImage = np.array([[[zoomed_blue[i,j],zoomed_red[i,j],zoomed_green[i][j]]for j in range(col)]for i in range(row)])
    return zoomedImage

def zoom(image,scale,pivot): #helper function to zoom the pixels of each color
    row , column = image.shape
    imageList = image.tolist() # convert the numpy.ndarray to a list object
    r = rowOperation(imageList,0,scale)
    i = 0
    while(i  <  len(imageList)-1):
        rowOperation(imageList,i+1,scale)
        colOperation(imageList,i,scale)
        i = i+scale
    startRow = pivot.rw - (row//2)
    endRow = startRow + row
    startCol = pivot.cl - (column//2)
    endCol = startCol + column
    newImage = np.array(imageList,dtype=np.uint8) #convert back to numpy.ndarray
    return newImage[startRow:endRow,startCol:endCol]


def rowOperation(img,index,scale): #perform row operation on "index" row of the list of list "img"
    ind = 0
    while(ind < len(img[index])-1):
        p1 = img[index][ind]
        p2 = img[index][ind+1]
        if( p1 < p2):
            smaller = p1
            larger = p2
        else:
            smaller = p2 
            larger = p1
        OP = (larger - smaller) // scale
        T = smaller + OP
        for i in range(scale - 1):
            ind = ind +1
            img[index].insert(ind,T)
            T = T + OP
        ind = ind + 1;        

def colOperation(img,index,scale): #perform column operation between "index" and "index+1" columns of the list of list "img"
    T = []
    OP_List = []
    l1 = img[index]
    l2 = img[index + 1]
    ind = 0
    while ( ind < len(img[index])):
        Q1 = img[index][ind]
        Q2 = img[index+1][ind]
        if(Q1 < Q2):
            smaller = Q1
            larger = Q2
        else:
            smaller = Q2
            larger = Q1
        OP = (larger - smaller) // scale
        OP_List.append(OP)
        T.append(smaller + OP)
        ind = ind + 1
    
    T_array = np.array(T)
    OP_array = np.array(T)
    
    for i in range( scale - 1 ):
        img.insert(index+1,T_array.tolist())
        T_array = T_array + OP_array

def main():
    #import the image
    ImageFilename = input("Enter image path")
    image = plt.imread(ImageFilename)
    k = int(input("Enter zooming factor")) #zooming factor
    """pivot row position should lie between [row/2] and [(k*(row-1)+1) - (row/2)]"""
    """pivot column position should lie between [column / 2] and [(k*(column-1)+1) - (column / 2)]"""
    rw = int(input("Enter the pivot row position. ")) 
    cl = int(input("Enter the pivot column position. "))
    pivot = Pivot(rw,cl)
    
    #show original image
    plt.imshow(image)
    plt.show()
    
    #Zoom the image by k times
    newImage = imageZoom(image,k,pivot)
    
    #shape of the zoomed image
    #must be of the same size of the original image
    print(newImage.shape)
    
    #show the new zoomed image
    plt.imshow(newImage)
    plt.show()
    
    #save the zoomed image
    newFilename = input("Enter the filename to save the zoomed Image")

    plt.imsave(newFilename,newImage)
    

if __name__ =="__main__":
    main()