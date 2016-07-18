#DICE coefficient plot

#Ben Puccio
#2016-06-08
#
#
#
#

##MAKE PLOTS USING NUMPY AND MATPLOTLIB
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#read each dice numpy array
ss = np.load('/home/bpuccio/dice/IBSR_dice_3dSkullStrip.npy')
fs = np.load('/home/bpuccio/dice/IBSR_dice_FS.npy')
bet = np.load('/home/bpuccio/dice/IBSR_dice_BET.npy')
beast = np.load('/home/bpuccio/dice/IBSR_dice_BEaSTlib.npy')
beastN = np.load('/home/bpuccio/dice/IBSR_dice_BEaSTNFBS.npy')

#print avg dice
sd_mean = np.mean(ss)
sd_std = np.std(ss)
sd_mean_r = round(sd_mean, 3)
sd_std_r = round(sd_std, 3)
print('3dSkullStrip',sd_mean_r,sd_std_r)
fsd_mean = np.mean(fs)
fsd_std = np.std(fs)
fsd_mean_r = round(fsd_mean, 3)
fsd_std_r = round(fsd_std, 3)
print('FreeSurfer',fsd_mean_r,fsd_std_r)
betd_mean = np.mean(bet)
betd_std = np.std(bet)
betd_mean_r = round(betd_mean, 3)
betd_std_r = round(betd_std, 3)
print('BET',betd_mean_r,betd_std_r)
beastd_mean = np.mean(beast)
beastd_std = np.std(beast)
beastd_mean_r = round(beastd_mean, 3)
beastd_std_r = round(beastd_std, 3)
print('BEaST',beastd_mean_r,beastd_std_r)
beastNd_mean = np.mean(beastN)
beastNd_std = np.std(beastN)
beastNd_mean_r = round(beastNd_mean, 3)
beastNd_std_r = round(beastNd_std, 3)
print('BEaST w/ NFBS',beastNd_mean_r,beastNd_std_r)

#make boxplot
data2 = [bet, ss, fs, beast, beastN]
names = ['BET','3dSkullStrip','FreeSurfer','BEaST','BEaST w/ NFBS']
sns.set_style("whitegrid")
box_plot=sns.boxplot(data=data2, palette="Set3", notch=True)
plt.xticks(np.arange(5),names)
plt.xlabel('Skull-Stripping Methods')
plt.ylabel('Dice Similarity Coefficients')
plt.title('IBSR')
plt.savefig('boxplot_IBSR2.png')

