import numpy as np
import pickle
from gaussCurvefit import gaussCurvefit
from singleSlitCurvefit import singleSlitCurvefit
from MeasureIntensity import findIntensity



 
def xfitmaker(AOI=400):
    with open(r'C:\Users\James_admin\Desktop\scripts for focus cam\a.pkl', 'rb') as fin:
        a = pickle.load(fin)
    
    xarray = np.sum(a,0)  
    
    xpos = np.argmax(xarray)
    
    lowerlim = xpos - AOI
    upperlim = xpos + AOI
    
    if xpos - AOI < 0:
        lowerlim = 0
    if xpos + AOI > len(xarray):
        upperlim = len(xarray)
    
    xaxis = np.arange(lowerlim, upperlim,1)
    
    plottedx = xarray[lowerlim:upperlim]
    plottedx = plottedx - np.min(plottedx)
    
    if np.min(plottedx) >= np.argmax(xarray):
        exit('This value is too large, choose a smaller input')
        
    
    if np.max(plottedx) <= np.argmax(xarray):
        exit('This value is too small, choose a larger input')
    
    xmax = np.max(plottedx)
    
    guessx = np.array((xpos,50,xmax))
    
    xfit = gaussCurvefit(xaxis,plottedx,guessx)
    
    # finding intensity of the centroid
    intensity = findIntensity(a)
    xfit = np.concatenate((xfit, np.array([intensity])))

    # parameters = open("xvariables.txt",'w')
    # xarrayfile = open("xarrayfile.txt",'w')
    # xaxisfile = open("xaxisfile.txt",'w')
    

    xaxisfile = "xaxisfile.txt"
    xarrayfile = "xarrayfile.txt"                 
    np.savetxt(xaxisfile,xaxis)
    np.savetxt(xarrayfile,plottedx)
    #parameters.write(str(xfit[0])+'\n'+str(xfit[1])+'\n'+str(xfit[2])+'\n')
    xfit2 = xfit.reshape((len(xfit), 1))
    np.savetxt("xvariables.txt", xfit2, fmt='%.3f')

    # xaxisfile.close()
    # xarrayfile.close()
    # parameters.close()
    fin.close()

def xfitmaker2(AOI=400):    
    with open(r'C:\Users\James_admin\Desktop\scripts for focus cam\a2.pkl', 'rb') as fin:
        a = pickle.load(fin)
    xarray = np.sum(a,0) 
    
    xpos = np.argmax(xarray)
    
    lowerlim = xpos - AOI
    upperlim = xpos + AOI
    
    if xpos - AOI < 0:
        lowerlim = 0
    if xpos + AOI > len(xarray):
        upperlim = len(xarray)
    
    xaxis = np.arange(lowerlim, upperlim,1)
    
    plottedx = xarray[lowerlim:upperlim]
    plottedx = plottedx - np.min(plottedx)
    
    if np.min(plottedx) >= np.argmax(xarray):
        exit('This value is too large, choose a smaller input')
        
    
    if np.max(plottedx) <= np.argmax(xarray):
        exit('This value is too small, choose a larger input')
    
    xmax = np.max(plottedx)
    
    guessx = np.array((xpos,50,xmax))
    
    xfit = gaussCurvefit(xaxis,plottedx,guessx)
    
    # finding intensity of the centroid
    intensity = findIntensity(a)
    xfit = np.concatenate((xfit, np.array([intensity])))

    # parameters = open("xvariables.txt",'w')
    # xarrayfile = open("xarrayfile.txt",'w')
    # xaxisfile = open("xaxisfile.txt",'w')
    xaxisfile = "xaxisfile.txt"
    xarrayfile = "xarrayfile.txt"  
          
    np.savetxt(xaxisfile,xaxis)
    np.savetxt(xarrayfile,plottedx)
    xfit2 = xfit.reshape((len(xfit), 1))
    np.savetxt("xvariables.txt", xfit2, fmt='%.3f')
    # parameters.write(str(format(xfit[0], '.2f'))+'\n'+str(xfit[1])+'\n'+str(xfit[2])+'\n')

    # xaxisfile.close()
    # xarrayfile.close()
    # parameters.close()
    fin.close()
    
def xfitmaker3(AOI=400):          
    with open(r'C:\Users\James_admin\Desktop\scripts for focus cam\a3.pkl', 'rb') as fin:
        a = pickle.load(fin)
    xarray = np.sum(a,0) 
    
    xpos = np.argmax(xarray)
    
    lowerlim = xpos - AOI
    upperlim = xpos + AOI
    
    if xpos - AOI < 0:
        lowerlim = 0
    if xpos + AOI > len(xarray):
        upperlim = len(xarray)
    
    xaxis = np.arange(lowerlim, upperlim,1)
    
    plottedx = xarray[lowerlim:upperlim]
    plottedx = plottedx - np.min(plottedx)
    
    if np.min(plottedx) >= np.argmax(xarray):
        exit('This value is too large, choose a smaller input')
        
    
    if np.max(plottedx) <= np.argmax(xarray):
        exit('This value is too small, choose a larger input')
    
    xmax = np.max(plottedx)
    
    guessx = np.array((xpos,50,xmax))
    
    xfit = gaussCurvefit(xaxis,plottedx,guessx)
    
    # finding intensity of the centroid
    intensity = findIntensity(a)
    xfit = np.concatenate((xfit, np.array([intensity])))

    # parameters = open("xvariables.txt",'w')
    # xarrayfile = open("xarrayfile.txt",'w')
    # xaxisfile = open("xaxisfile.txt",'w')
    xaxisfile = "xaxisfile.txt"
    xarrayfile = "xarrayfile.txt"  
          
    np.savetxt(xaxisfile,xaxis)
    np.savetxt(xarrayfile,plottedx)
    xfit2 = xfit.reshape((len(xfit), 1))
    np.savetxt("xvariables.txt", xfit2, fmt='%.3f')
    # parameters.write(str(format(xfit[0], '.2f'))+'\n'+str(xfit[1])+'\n'+str(xfit[2])+'\n')

    # xaxisfile.close()
    # xarrayfile.close()
    # parameters.close()
    fin.close()
    
def xfitmaker4(AOI=400):    
    with open(r'C:\Users\James_admin\Desktop\scripts for focus cam\a4.pkl', 'rb') as fin:
        a = pickle.load(fin)  
    xarray = np.sum(a,0) 
    
    xpos = np.argmax(xarray)
    
    lowerlim = xpos - AOI
    upperlim = xpos + AOI
    
    if xpos - AOI < 0:
        lowerlim = 0
    if xpos + AOI > len(xarray):
        upperlim = len(xarray)
    
    xaxis = np.arange(lowerlim, upperlim,1)
    
    plottedx = xarray[lowerlim:upperlim]
    plottedx = plottedx - np.min(plottedx)
    
    if np.min(plottedx) >= np.argmax(xarray):
        exit('This value is too large, choose a smaller input')
        
    
    if np.max(plottedx) <= np.argmax(xarray):
        exit('This value is too small, choose a larger input')
    
    xmax = np.max(plottedx)
    
    guessx = np.array((xpos,50,xmax))
    
    xfit = gaussCurvefit(xaxis,plottedx,guessx)
    
    # finding intensity of the centroid
    intensity = findIntensity(a)
    xfit = np.concatenate((xfit, np.array([intensity])))

    # parameters = open("xvariables.txt",'w')
    # xarrayfile = open("xarrayfile.txt",'w')
    # xaxisfile = open("xaxisfile.txt",'w')
    xaxisfile = "xaxisfile.txt"
    xarrayfile = "xarrayfile.txt"  
          
    np.savetxt(xaxisfile,xaxis)
    np.savetxt(xarrayfile,plottedx)
    xfit2 = xfit.reshape((len(xfit), 1))
    np.savetxt("xvariables.txt", xfit2, fmt='%.3f')
    # parameters.write(str(format(xfit[0], '.2f'))+'\n'+str(xfit[1])+'\n'+str(xfit[2])+'\n')

    # xaxisfile.close()
    # xarrayfile.close()
    # parameters.close()
    fin.close()

def xfitmaker5(AOI=400):    
    with open(r'C:\Users\James_admin\Desktop\scripts for focus cam\a5.pkl', 'rb') as fin:
            a = pickle.load(fin)
            
    xarray = np.sum(a,0) 
    
    xpos = np.argmax(xarray)
    
    lowerlim = xpos - AOI
    upperlim = xpos + AOI
    
    if xpos - AOI < 0:
        lowerlim = 0
    if xpos + AOI > len(xarray):
        upperlim = len(xarray)
    
    xaxis = np.arange(lowerlim, upperlim,1)
    
    plottedx = xarray[lowerlim:upperlim]
    plottedx = plottedx - np.min(plottedx)
    
    if np.min(plottedx) >= np.argmax(xarray):
        exit('This value is too large, choose a smaller input')
        
    
    if np.max(plottedx) <= np.argmax(xarray):
        exit('This value is too small, choose a larger input')
    
    xmax = np.max(plottedx)
    
    guessx = np.array((xpos,20,xmax))
    
    xfit = gaussCurvefit(xaxis,plottedx,guessx)
    
    # finding intensity of the centroid
    intensity = findIntensity(a)
    xfit = np.concatenate((xfit, np.array([intensity])))

    # parameters = open("xvariables.txt",'w')
    # xarrayfile = open("xarrayfile.txt",'w')
    # xaxisfile = open("xaxisfile.txt",'w')
    xaxisfile = "xaxisfile.txt"
    xarrayfile = "xarrayfile.txt"  
          
    np.savetxt(xaxisfile,xaxis)
    np.savetxt(xarrayfile,plottedx)
    xfit2 = xfit.reshape((len(xfit), 1))
    np.savetxt("xvariables.txt", xfit2, fmt='%.3f')
    # parameters.write(str(format(xfit[0], '.2f'))+'\n'+str(xfit[1])+'\n'+str(xfit[2])+'\n')

    # xaxisfile.close()
    # xarrayfile.close()
    # parameters.close()
    fin.close()
    


