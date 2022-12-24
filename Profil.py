import matplotlib.pyplot as plt
import astropy.io.fits as astrofits
hdulist = astrofits.open("v523cas60s-001.fit")
hdulist.info()
scidata = hdulist[0].data
print(scidata)


Y_1 = []
X_1 = []
for i in range(645, 690):
    X_1.append(i)
    Y_1.append(scidata[1655][i])
fig_1 = plt.figure()
ax_1 = fig_1.add_subplot(111)
fig_1.set_facecolor('LemonChiffon')
ax_1.set_title('Профиль звезды', color='Maroon', fontweight='bold')
ax_1.set_xlabel('х')
ax_1.set_ylabel('Counts')
ax_1.set_xlim([640, 695])
#ax_1.grid()
ax_1.plot(scidata[1655], color='Maroon', linewidth=1)
ax_1.scatter(X_1, Y_1, color='Maroon', marker='.')

fig_2 = plt.figure()
ax_2 = fig_2.add_subplot(111)
fig_2.set_facecolor('LemonChiffon')
ax_2.set_title('Профиль звезды', color='Indigo', fontweight='bold')
ax_2.set_xlabel('у')
ax_2.set_ylabel('Counts')
X_2 = []
Y_2 = []
for j in range(1635, 1675):
    X_2.append(j)
    Y_2.append(scidata[j][670])
scidata_2_y = []
for k in range(0, len(scidata)):
    scidata_2_y.append(scidata[k][670])
ax_2.set_xlim([1630, 1680])
ax_2.plot(scidata_2_y, color='Indigo', linewidth=1)
ax_2.scatter(X_2, Y_2, color='Indigo', marker='.')
plt.show()