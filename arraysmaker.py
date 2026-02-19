import numpy as np
from gaussCurvefit import gaussCurvefit
from singleSlitCurvefit import singleSlitCurvefit

 


def yfitmaker(AOI=400):
    import pickle
    with open(r'C:\Users\James_admin\Desktop\scripts for focus cam\a.pkl', 'rb') as fin:
            a = pickle.load(fin)
            
    yarray = np.sum(a,1)

    
    ypos = np.argmax(yarray)
    
    lowerlim = ypos - AOI
    upperlim = ypos + AOI
    
    if ypos - AOI < 0:
        lowerlim = 0
    if ypos + AOI > len(yarray):
        upperlim = len(yarray)
    
    yaxis = np.arange(lowerlim, upperlim,1)
    
    plottedy = yarray[lowerlim:upperlim]
    plottedy = plottedy - np.min(plottedy)

    if np.min(plottedy) >= np.argmax(yarray):
        exit('This value is too large, choose a smaller input')
        
    
    if np.max(plottedy) <= np.argmax(yarray):
        exit('This value is too small, choose a larger input')
    
    ymax = np.max(plottedy)
    
    guessy = np.array((ypos,20,ymax))
    
    yfit = gaussCurvefit(yaxis,plottedy,guessy)

    parameters = open("variables.txt",'w')
    yarrayfile = open("yarrayfile.txt",'w')
    yaxisfile = open("yaxisfile.txt",'w')
                     
    np.savetxt(yaxisfile,yaxis)
    np.savetxt(yarrayfile,plottedy)
    parameters.write(str(yfit[0])+'\n'+str(yfit[1])+'\n'+str(yfit[2])+'\n')

    
    yaxisfile.close()
    yarrayfile.close()
    parameters.close()
    fin.close()
 
def yfitmaker2(AOI=400):
     import pickle
     with open(r'C:\Users\James_admin\Desktop\scripts for focus cam\a2.pkl', 'rb') as fin:
         a = pickle.load(fin)
     yarray = np.sum(a,1)

    
     ypos = np.argmax(yarray)
    
    
     lowerlim = ypos - AOI
     upperlim = ypos + AOI
    
     if ypos - AOI < 0:
         lowerlim = 0
     if ypos + AOI > len(yarray):
         upperlim = len(yarray)
    
     yaxis = np.arange(lowerlim, upperlim,1)
    
     plottedy = yarray[lowerlim:upperlim]
     plottedy = plottedy - np.min(plottedy)

     if np.min(plottedy) >= np.argmax(yarray):
         exit('This value is too large, choose a smaller input')
        
    
     if np.max(plottedy) <= np.argmax(yarray):
         exit('This value is too small, choose a larger input')
    
     ymax = np.max(plottedy)
    
     guessy = np.array((ypos,20,ymax))
    
     yfit = gaussCurvefit(yaxis,plottedy,guessy)

     parameters = open("variables.txt",'w')
     yarrayfile = open("yarrayfile.txt",'w')
     yaxisfile = open("yaxisfile.txt",'w')
                     
     np.savetxt(yaxisfile,yaxis)
     np.savetxt(yarrayfile,plottedy)
     parameters.write(str(yfit[0])+'\n'+str(yfit[1])+'\n'+str(yfit[2])+'\n')

    
     yaxisfile.close()
     yarrayfile.close()
     parameters.close()
     fin.close()
    
            
def yfitmaker3(AOI=400):
    import pickle
    with open(r'C:\Users\James_admin\Desktop\scripts for focus cam\a3.pkl', 'rb') as fin:
        a = pickle.load(fin)
    yarray = np.sum(a,1)

    
    ypos = np.argmax(yarray)
    
    lowerlim = ypos - AOI
    upperlim = ypos + AOI
    
    if ypos - AOI < 0:
        lowerlim = 0
    if ypos + AOI > len(yarray):
        upperlim = len(yarray)
    
    yaxis = np.arange(lowerlim, upperlim,1)
    
    plottedy = yarray[lowerlim:upperlim]
    plottedy = plottedy - np.min(plottedy)

    if np.min(plottedy) >= np.argmax(yarray):
        exit('This value is too large, choose a smaller input')
        
    
    if np.max(plottedy) <= np.argmax(yarray):
        exit('This value is too small, choose a larger input')
    
    ymax = np.max(plottedy)
    
    guessy = np.array((ypos,50,ymax))
    
    yfit = gaussCurvefit(yaxis,plottedy,guessy)

    parameters = open("variables.txt",'w')
    yarrayfile = open("yarrayfile.txt",'w')
    yaxisfile = open("yaxisfile.txt",'w')
                     
    np.savetxt(yaxisfile,yaxis)
    np.savetxt(yarrayfile,plottedy)
    parameters.write(str(yfit[0])+'\n'+str(yfit[1])+'\n'+str(yfit[2])+'\n')

    
    yaxisfile.close()
    yarrayfile.close()
    parameters.close()
    fin.close()
    
def yfitmaker4(AOI=400):
     import pickle
     with open(r'C:\Users\James_admin\Desktop\scripts for focus cam\a4.pkl','rb') as fin:
         a = pickle.load(fin)
     yarray = np.sum(a,1)

    
     ypos = np.argmax(yarray)
    
     lowerlim = ypos - AOI
     upperlim = ypos + AOI
    
     if ypos - AOI < 0:
         lowerlim = 0
     if ypos + AOI > len(yarray):
         upperlim = len(yarray)
    
     yaxis = np.arange(lowerlim, upperlim,1)
    
     plottedy = yarray[lowerlim:upperlim]
     plottedy = plottedy - np.min(plottedy)

     if np.min(plottedy) >= np.argmax(yarray):
         exit('This value is too large, choose a smaller input')
        
    
     if np.max(plottedy) <= np.argmax(yarray):
         exit('This value is too small, choose a larger input')
    
     ymax = np.max(plottedy)
    
     guessy = np.array((ypos,20,ymax))
    
     yfit = gaussCurvefit(yaxis,plottedy,guessy)

     parameters = open("variables.txt",'w')
     yarrayfile = open("yarrayfile.txt",'w')
     yaxisfile = open("yaxisfile.txt",'w')
                     
     np.savetxt(yaxisfile,yaxis)
     np.savetxt(yarrayfile,plottedy)
     parameters.write(str(yfit[0])+'\n'+str(yfit[1])+'\n'+str(yfit[2])+'\n')

    
     yaxisfile.close()
     yarrayfile.close()
     parameters.close()
     fin.close()
    
def yfitmaker5(AOI=400):
    import pickle
    with open(r'C:\Users\James_admin\Desktop\scripts for focus cam\a5.pkl', 'rb') as fin:
        a = pickle.load(fin)
            
    yarray = np.sum(a,1)

    
    ypos = np.argmax(yarray)
    
    lowerlim = ypos - AOI
    upperlim = ypos + AOI
    
    if ypos - AOI < 0:
        lowerlim = 0
    if ypos + AOI > len(yarray):
        upperlim = len(yarray)
    
    yaxis = np.arange(lowerlim, upperlim,1)
    
    plottedy = yarray[lowerlim:upperlim]
    plottedy = plottedy - np.min(plottedy)

    if np.min(plottedy) >= np.argmax(yarray):
        exit('This value is too large, choose a smaller input')
        
    
    if np.max(plottedy) <= np.argmax(yarray):
        exit('This value is too small, choose a larger input')
    
    ymax = np.max(plottedy)
    
    guessy = np.array((ypos,50,ymax))
    
    yfit = gaussCurvefit(yaxis,plottedy,guessy)

    parameters = open("variables.txt",'w')
    yarrayfile = open("yarrayfile.txt",'w')
    yaxisfile = open("yaxisfile.txt",'w')
                     
    np.savetxt(yaxisfile,yaxis)
    np.savetxt(yarrayfile,plottedy)
    parameters.write(str(yfit[0])+'\n'+str(yfit[1])+'\n'+str(yfit[2])+'\n')

    
    yaxisfile.close()
    yarrayfile.close()
    parameters.close()
    fin.close()



