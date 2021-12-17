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



# ----------------- matplotlib -----------------

fig, ax = plt.subplots(nrows=2,ncols=2, figsize=(20,10))

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

plt.show()




