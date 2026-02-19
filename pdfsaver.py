#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 18:35:44 2021

@author: vincentsmedile
"""
import matplotlib.pyplot as plt
import numpy as np
import pickle
from matplotlib.backends.backend_pdf import PdfPages

def allpdfmaker():
    with open('/Users/vincentsmedile/Documents/OneDrive - The Pennsylvania State University/McEntaffer Group Stuff/scripts for focus cam/a.pkl', 'rb') as fin:
        a1 = pickle.load(fin)
    yarray1 = np.sum(a1,1)
    ypos1 = np.argmax(yarray1)
    yaxis1 = np.linspace(ypos1-100,ypos1+100,200)
    plottedy1 = yarray1[ypos1-100:ypos1+100]
    plottedy1 = plottedy1 - np.min(plottedy1)
        
    xarray1 = np.sum(a1,0)
    xpos1 = np.argmax(xarray1)
    xaxis1 = np.linspace(xpos1-100,xpos1+100,200)
    plottedx1 = xarray1[xpos1-100:xpos1+100]
    plottedx1 = plottedx1 - np.min(plottedx1) 
        
    with open('/Users/vincentsmedile/Documents/OneDrive - The Pennsylvania State University/McEntaffer Group Stuff/scripts for focus cam/a2.pkl', 'rb') as fin:
        a2 = pickle.load(fin)
        
    yarray2 = np.sum(a2,1)
    ypos2 = np.argmax(yarray2)
    yaxis2 = np.linspace(ypos2-100,ypos2+100,200)
    plottedy2 = yarray2[ypos2-100:ypos2+100]
    plottedy2 = plottedy2 - np.min(plottedy2) 
        
    xarray2 = np.sum(a2,0)
    xpos2 = np.argmax(xarray2)
    xaxis2 = np.linspace(xpos2-100,xpos2+100,200)
    plottedx2 = xarray2[xpos2-100:xpos2+100]
    plottedx2 = plottedx2 - np.min(plottedx2) 
        
    with open('/Users/vincentsmedile/Documents/OneDrive - The Pennsylvania State University/McEntaffer Group Stuff/scripts for focus cam/a3.pkl', 'rb') as fin:
        a3 = pickle.load(fin)
        
    yarray3 = np.sum(a3,1)
    ypos3 = np.argmax(yarray3)
    yaxis3 = np.linspace(ypos3-100,ypos3+100,200)
    plottedy3 = yarray3[ypos3-100:ypos3+100]
    plottedy3 = plottedy3 - np.min(plottedy3)

    xarray3 = np.sum(a3,0)
    xpos3 = np.argmax(xarray3)
    xaxis3 = np.linspace(xpos3-100,xpos3+100,200)
    plottedx3 = xarray3[xpos3-100:xpos3+100]
    plottedx3 = plottedx3 - np.min(plottedx3) 
    
    with open('/Users/vincentsmedile/Documents/OneDrive - The Pennsylvania State University/McEntaffer Group Stuff/scripts for focus cam/a4.pkl', 'rb') as fin:
        a4 = pickle.load(fin)
        
    yarray4 = np.sum(a4,1)
    ypos4 = np.argmax(yarray4)
    yaxis4 = np.linspace(ypos4-100,ypos4+100,200)
    plottedy4 = yarray4[ypos4-100:ypos4+100]
    plottedy4= plottedy4 - np.min(plottedy4)   
 
    xarray4 = np.sum(a4,0)
    xpos4 = np.argmax(xarray4)
    xaxis4 = np.linspace(xpos4-100,xpos4+100,200)
    plottedx4 = xarray4[xpos4-100:xpos4+100]
    plottedx4 = plottedx4 - np.min(plottedx4)  
    
    with open('/Users/vincentsmedile/Documents/OneDrive - The Pennsylvania State University/McEntaffer Group Stuff/scripts for focus cam/a5.pkl', 'rb') as fin:
        a5 = pickle.load(fin)
    plt.imshow(a5)
    yarray5 = np.sum(a5,1)
    ypos5 = np.argmax(yarray5)
    yaxis5 = np.linspace(ypos5-100,ypos5+100,200)
    plottedy5 = yarray5[ypos5+100:ypos5+100]
    plottedy5 = plottedy5 - np.min(plottedy5)
        
    xarray5 = np.sum(a5,0)
    xpos5 = np.argmax(xarray5)
    xaxis5 = np.linspace(xpos5-100,xpos5+100,200)
    plottedx5 = xarray5[xpos5+100:xpos5+100]
    plottedx5 = plottedx5 - np.min(plottedx5)
        
    with PdfPages('allfigures.pdf') as pdf:
    # saves the current figure into a pdf page
        plt.plot(yaxis1,plottedy1)
        pdf.savefig()
        plt.plot(xaxis1,plottedx1)
        pdf.savefig()
        plt.imshow(a1)
        pdf.savefig()
                
        plt.plot(yaxis2,plottedy2)
        pdf.savefig()
        plt.plot(xaxis2,plottedx2)
        pdf.savefig()
        plt.imshow(a2)
        pdf.savefig()
                
        plt.plot(yaxis3,plottedy3)
        pdf.savefig()
        plt.plot(xaxis3,plottedx3)
        pdf.savefig()
        plt.imshow(a3)
        pdf.savefig()
                
        plt.plot(yaxis4,plottedy4)
        pdf.savefig()
        plt.plot(xaxis4,plottedx4)
        pdf.savefig()
        plt.imshow(a4)
        pdf.savefig()
                
        plt.plot(yaxis5,plottedy5)
        pdf.savefig()
        plt.plot(xaxis5,plottedx5)
        pdf.savefig()
        plt.imshow(a5)
        pdf.savefig()
                
        pdf.close()

def singlecampdfmaker(camera):
    if camera == 1:
        with open('/Users/vincentsmedile/Documents/OneDrive - The Pennsylvania State University/McEntaffer Group Stuff/scripts for focus cam/a.pkl', 'rb') as fin:
            a1 = pickle.load(fin)
    
        yarray1 = np.sum(a1,1)
        ypos1 = np.argmax(yarray1)
        yaxis1 = np.linspace(ypos1-100,ypos1+100,200)
        plottedy1 = yarray1[ypos1-100:ypos1+100]
        plottedy1 = plottedy1 - np.min(plottedy1)
        
        xarray1 = np.sum(a1,0)
        xpos1 = np.argmax(xarray1)
        xaxis1 = np.linspace(xpos1-100,xpos1+100,200)
        plottedx1 = xarray1[xpos1-100:xpos1+100]
        plottedx1 = plottedx1 - np.min(plottedx1) 
        
        with PdfPages('camera1data.pdf') as pdf:
            plt.plot(yaxis1,plottedy1)
            pdf.savefig()
            plt.plot(xaxis1,plottedx1)
            pdf.savefig()
            plt.imshow(a1)
            pdf.savefig()
            pdf.close
    if camera == 2:
        with open('/Users/vincentsmedile/Documents/OneDrive - The Pennsylvania State University/McEntaffer Group Stuff/scripts for focus cam/a2.pkl', 'rb') as fin:
            a2 = pickle.load(fin)
    
        yarray2 = np.sum(a2,1)
        ypos2 = np.argmax(yarray2)
        yaxis2 = np.linspace(ypos2-100,ypos2+100,200)
        plottedy2 = yarray2[ypos2-100:ypos2+100]
        plottedy2 = plottedy2 - np.min(plottedy2) 
        
        xarray2 = np.sum(a2,0)
        xpos2 = np.argmax(xarray2)
        xaxis2 = np.linspace(xpos2-100,xpos2+100,200)
        plottedx2 = xarray2[xpos2-100:xpos2+100]
        plottedx2 = plottedx2 - np.min(plottedx2) 
        
        with PdfPages('camera2data.pdf') as pdf:
            plt.plot(yaxis2,plottedy2)
            pdf.savefig()
            plt.plot(xaxis2,plottedx2)
            pdf.savefig()
            plt.imshow(a2)
            pdf.savefig()
            pdf.close()
    if camera == 3:
        with open('/Users/vincentsmedile/Documents/OneDrive - The Pennsylvania State University/McEntaffer Group Stuff/scripts for focus cam/a3.pkl', 'rb') as fin:
            a3 = pickle.load(fin)
        
        yarray3 = np.sum(a3,1)
        ypos3 = np.argmax(yarray3)
        yaxis3 = np.linspace(ypos3-100,ypos3+100,200)
        plottedy3 = yarray3[ypos3-100:ypos3+100]
        plottedy3 = plottedy3 - np.min(plottedy3)

        xarray3 = np.sum(a3,0)
        xpos3 = np.argmax(xarray3)
        xaxis3 = np.linspace(xpos3-100,xpos3+100,200)
        plottedx3 = xarray3[xpos3-100:xpos3+100]
        plottedx3 = plottedx3 - np.min(plottedx3)   
        
        with PdfPages('camera3data.pdf') as pdf:
            plt.plot(yaxis3,plottedy3)
            pdf.savefig()
            plt.plot(xaxis3,plottedx3)
            pdf.savefig()
            plt.imshow(a3)
            pdf.savefig()
            pdf.close()
    if camera == 4:
        with open('/Users/vincentsmedile/Documents/OneDrive - The Pennsylvania State University/McEntaffer Group Stuff/scripts for focus cam/a4.pkl', 'rb') as fin:
            a4 = pickle.load(fin)
            
        yarray4 = np.sum(a4,1)
        ypos4 = np.argmax(yarray4)
        yaxis4 = np.linspace(ypos4-100,ypos4+100,200)
        plottedy4 = yarray4[ypos4-100:ypos4+100]
        plottedy4= plottedy4 - np.min(plottedy4)   
 
        xarray4 = np.sum(a4,0)
        xpos4 = np.argmax(xarray4)
        xaxis4 = np.linspace(xpos4-100,xpos4+100,200)
        plottedx4 = xarray4[xpos4-100:xpos4+100]
        plottedx4 = plottedx4 - np.min(plottedx4)        
        
        with PdfPages('camera4data.pdf') as pdf:
            plt.plot(yaxis4,plottedy4)
            pdf.savefig()
            plt.plot(xaxis4,plottedx4)
            pdf.savefig()
            plt.imshow(a4)
            pdf.savefig()
            pdf.close()
            
    if camera == 5:
        with open('/Users/vincentsmedile/Documents/OneDrive - The Pennsylvania State University/McEntaffer Group Stuff/scripts for focus cam/a5.pkl', 'rb') as fin:
            a5 = pickle.load(fin)
            
        yarray5 = np.sum(a5,1)
        ypos5 = np.argmax(yarray5)
        yaxis5 = np.linspace(ypos5-100,ypos5+100,200)
        plottedy5 = yarray5[ypos5+100:ypos5+100]
        plottedy5 = plottedy5 - np.min(plottedy5)
        
        xarray5 = np.sum(a5,0)
        xpos5 = np.argmax(xarray5)
        xaxis5 = np.linspace(xpos5-100,xpos5+100,200)
        plottedx5 = xarray5[xpos5+100:xpos5+100]
        plottedx5 = plottedx5 - np.min(plottedx5)
        
        with PdfPages('camera5data.pdf') as pdf:
            plt.plot(yaxis5,plottedy5)
            pdf.savefig()
            plt.plot(xaxis5,plottedx5)
            pdf.savefig()
            plt.imshow(a5)
            pdf.savefig()
            pdf.close()


allpdfmaker()
