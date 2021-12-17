# -----------------  improting packages -----------------
import sys 
import matplotlib.pyplot as plt
import numpy as np




# ----------------- Loading the file -----------------
with open(sys.argv[1]) as f:
    content = f.read().splitlines()




# ----------------- Parsing Data -----------------
start_l=[]
end_l  =[]
for i,j in enumerate(content):
    if 'Per MPI rank memory allocation' in j:
        start_l.append(i+2)
#    if 'Loop time of' in j:
    if 'Loop time of' in j or 'colvars: Saving collective variables' in j:
        end_l.append(i-(start_l[-1]))


for i in zip(start_l,end_l):
    print('(StartLine-MaxRow):\t',i)
    
Data = np.loadtxt(fname=sys.argv[1] ,skiprows=start_l[0], max_rows=end_l[0])
#Data = np.loadtxt(fname=sys.argv[1] ,skiprows=start_l[1], max_rows=end_l[1])
#Data = np.loadtxt(fname=sys.argv[1] ,skiprows=start_l[2], max_rows=end_l[2])
print('Matrix size:\t', Data.shape)



# ----------------- Defing quantities -----------------
time = Data[:,1:2]/1000000
temp = Data[:,2:3]
press= Data[:,3:4]
vol  = Data[:,4:5]
dens = Data[:,5:6]

toteng=Data[:,6:7]

xlo  = Data[:,16:17]
xhi  = Data[:,17:18]
ylo  = Data[:,18:19]
yhi  = Data[:,19:20]
zlo  = Data[:,20:21]
zhi  = Data[:,21:22]

ptot = Data[:,22:23]

pxx  = Data[:,23:24]
pyy  = Data[:,24:25]
pzz  = Data[:,25:26]
pxy  = Data[:,26:27]
pxz  = Data[:,27:28]
pyz  = Data[:,28:29]
# ----------------- matplotlib -----------------

fig, ax = plt.subplots(nrows=3,ncols=2, figsize=(20,10))
fig.canvas.set_window_title('Thermodynamics')

ax[0,0].plot(time,temp, label='Temprature')
ax[0,0].axhline(y=np.average(temp), color='r')
ax[0,0].text(0.4, 0.8,size=14, color='w', transform=ax[0,0].transAxes, backgroundcolor='tab:orange', \
             s='average={}\nstd={}'.format(np.round(np.average(temp), decimals=3), np.round(np.std(temp), decimals=3)))
ax[0,0].set_xlabel('Time (ns)')
ax[0,0].set_ylabel('Temprature (K)')
ax[0,0].legend()


ax[0,1].plot(time,press, label='pressure')
ax[0,1].axhline(y=np.average(press), color='r')
ax[0,1].text(0.4, 0.1,size=14, color='w', transform=ax[0,1].transAxes, backgroundcolor='tab:orange', \
             s='average={}\nstd={}'.format(np.round(np.average(press), decimals=3), np.round(np.std(press), decimals=3)))        
ax[0,1].set_xlabel('Time (ns)')
ax[0,1].set_ylabel('pressure (atm)')     
ax[0,1].legend()


ax[1,0].plot(time, vol, label='volume')
ax[1,0].axhline(y=np.average(vol), color='r')
ax[1,0].text(0.4, 0.8,size=14,color='w',transform=ax[1,0].transAxes,backgroundcolor='tab:orange' ,\
             s='average={}\nstd={}'.format(np.round(np.average(vol), decimals=3), np.round(np.std(vol), decimals=3)))
ax[1,0].set_xlabel('Time (ns)')
ax[1,0].set_ylabel('volume (A^3)') 
ax[1,0].legend()

ax[1,1].plot(time,dens, label='Density')
ax[1,1].axhline(y=np.average(dens), color='r')
ax[1,1].text(0.4, 0.1,size=14, color='w', transform=ax[1,1].transAxes,backgroundcolor='tab:orange', \
             s='average={}\nstd={}'.format(np.round(np.average(dens), decimals=3), np.round(np.std(dens), decimals=3)))
ax[1,1].set_xlabel('Time (ns)')
ax[1,1].set_ylabel('Density (gram/cm^3)') 
ax[1,1].legend()

ax[2,0].plot(time,ptot, label='Total Pressure')
ax[2,0].axhline(y=np.average(ptot), color='r')
ax[2,0].text(0.4, 0.1,size=14, color='w', transform=ax[2,0].transAxes,backgroundcolor='tab:orange', \
             s='average={}\nstd={}'.format(np.round(np.average(ptot), decimals=3), np.round(np.std(ptot), decimals=3)))
ax[2,0].set_xlabel('Time (ns)')
ax[2,0].set_ylabel('pressure (atm)') 
ax[2,0].legend()

ax[2,1].plot(time,toteng, label='Total Energy')
ax[2,1].axhline(y=np.average(toteng), color='r')
ax[2,1].text(0.4, 0.1,size=14, color='w', transform=ax[2,1].transAxes,backgroundcolor='tab:orange', \
             s='average={}\nstd={}'.format(np.round(np.average(toteng), decimals=3), np.round(np.std(toteng), decimals=3)))
ax[2,1].set_xlabel('Time (ns)')
ax[2,1].set_ylabel('Total Energy (Kcal/mol)') 
ax[2,1].legend()

# ----------------- matplotlib -----------------

fig, ax = plt.subplots(nrows=3,ncols=2, figsize=(20,10))
fig.canvas.set_window_title('Size of the Box')

ax[0,0].plot(time,xlo, label='Xlo')
ax[0,0].set_xlabel('Time (ns)')
ax[0,0].set_ylabel('X low (A)')
ax[0,0].legend()

ax[0,1].plot(time,xhi, label='Xhi')
ax[0,1].set_xlabel('Time (ns)')
ax[0,1].set_ylabel('X High (A)')
ax[0,1].legend()


ax[1,0].plot(time,ylo, label='Ylo')
ax[1,0].set_xlabel('Time (ns)')
ax[1,0].set_ylabel('Y low (A)')
ax[1,0].legend()

ax[1,1].plot(time,yhi, label='Yhi')
ax[1,1].set_xlabel('Time (ns)')
ax[1,1].set_ylabel('Y High (A)')
ax[1,1].legend()


ax[2,0].plot(time,zlo, label='Zlo')
ax[2,0].set_xlabel('Time (ns)')
ax[2,0].set_ylabel('Z low (A)')
ax[2,0].legend()

ax[2,1].plot(time,zhi, label='Zhi')
ax[2,1].set_xlabel('Time (ns)')
ax[2,1].set_ylabel('Z High (A)')
ax[2,1].legend()


# ----------------- matplotlib -----------------


fig, ax = plt.subplots(nrows=3,ncols=2, figsize=(20,10))
fig.canvas.set_window_title('Pressure')

ax[0,0].plot(time,pxx, label='pxx')
ax[0,0].axhline(y=np.average(pxx), color='r')
ax[0,0].text(0.4, 0.8,size=12, color='w', transform=ax[0,0].transAxes, backgroundcolor='tab:orange', \
             s='average={}\nstd={}'.format(np.round(np.average(pxx), decimals=3), np.round(np.std(pxx), decimals=3)))
ax[0,0].set_xlabel('Time (ns)')
ax[0,0].set_ylabel('PXX (atm)')
ax[0,0].legend()

ax[1,0].plot(time,pyy, label='pyy')
ax[1,0].axhline(y=np.average(pyy), color='r')
ax[1,0].text(0.4, 0.8,size=12, color='w', transform=ax[1,0].transAxes, backgroundcolor='tab:orange', \
             s='average={}\nstd={}'.format(np.round(np.average(pyy), decimals=3), np.round(np.std(pyy), decimals=3)))
ax[1,0].set_xlabel('Time (ns)')
ax[1,0].set_ylabel('PYY (atm)')
ax[1,0].legend()


ax[2,0].plot(time,pzz, label='pzz')
ax[2,0].axhline(y=np.average(pzz), color='r')
ax[2,0].text(0.4, 0.8,size=12, color='w', transform=ax[2,0].transAxes, backgroundcolor='tab:orange', \
             s='average={}\nstd={}'.format(np.round(np.average(pzz), decimals=3), np.round(np.std(pzz), decimals=3)))
ax[2,0].set_xlabel('Time (ns)')
ax[2,0].set_ylabel('PZZ (atm)')
ax[2,0].legend()

ax[0,1].plot(time,pxy, label='pxy')
ax[0,1].axhline(y=np.average(pxy), color='r')
ax[0,1].text(0.4, 0.8,size=14, color='w', transform=ax[0,1].transAxes, backgroundcolor='tab:orange', \
             s='average={}\nstd={}'.format(np.round(np.average(pxy), decimals=3), np.round(np.std(pxy), decimals=3)))
ax[0,1].set_xlabel('Time (ns)')
ax[0,1].set_ylabel('PXY (atm)')
ax[0,1].legend()


ax[1,1].plot(time,pxz, label='pxz')
ax[1,1].axhline(y=np.average(pxz), color='r')
ax[1,1].text(0.4, 0.8,size=14, color='w', transform=ax[1,1].transAxes, backgroundcolor='tab:orange', \
             s='average={}\nstd={}'.format(np.round(np.average(pxz), decimals=3), np.round(np.std(pxz), decimals=3)))
ax[1,1].set_xlabel('Time (ns)')
ax[1,1].set_ylabel('PXZ (atm)')
ax[1,1].legend()

ax[2,1].plot(time,pyz, label='pyz')
ax[2,1].axhline(y=np.average(pyz), color='r')
ax[2,1].text(0.4, 0.8,size=14, color='w', transform=ax[2,1].transAxes, backgroundcolor='tab:orange', \
             s='average={}\nstd={}'.format(np.round(np.average(pyz), decimals=3), np.round(np.std(pyz), decimals=3)))
ax[2,1].set_xlabel('Time (ns)')
ax[2,1].set_ylabel('PYZ (atm)')
ax[2,1].legend()


# ----------------- matplotlib -----------------

fig, ax = plt.subplots(nrows=3,ncols=1, figsize=(20,10))
fig.canvas.set_window_title('Size of the Box')

ax[0].plot(time, (xhi-xlo), label='X Dimension')
ax[0].set_xlabel('Time (ns)')
ax[0].set_ylabel('Size of the Box (A)')
ax[0].legend()

ax[1].plot(time,(yhi-ylo), label='Y Dimension')
ax[1].set_xlabel('Time (ns)')
ax[1].set_ylabel('Size of the Box (A)')
ax[1].legend()


ax[2].plot(time,(zhi-zlo), label='Z Dimension')
ax[2].set_xlabel('Time (ns)')
ax[2].set_ylabel('Size of the Box (A)')
ax[2].legend()

plt.show()

