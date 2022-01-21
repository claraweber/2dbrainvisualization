# global imports
import matplotlib.colors as mcolors
from vedo import Volume
from vedo import embedWindow, show, colorMap
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

##############################
# set path to MNI or template image:
filepathmni152 = './MNI152_T1_1mm_brain.nii.gz'

# set path to overlay image (can be more than one)
filepath2 = './overlay.nii.gz'

# name contrast
opt = 'contrast'


mni152 = nib.load('/Users/claraweber/Desktop/brainrender/skeleton_bin.nii.gz').get_fdata()
im2 = nib.load('/Users/claraweber/Desktop/brainrender/mdev_RD44.nii.gz').get_fdata()

# activate for troubleshoot purposes
#type(im3)
#im3.shape
#np.unique(im3)

#create single slice -> 8 evenly sliced MNI images with overlay
fig, axs = plt.subplots(8, sharex=True, sharey=True)
im1=im1*-1

#mask overlayed images to make zero voxels transparent
mni152 = np.ma.masked_where(im1 ==0, im1)
masked_overlay = np.ma.masked_where(im2 ==0, im2)

#def show_slices(slices):
#   """ Function to display row of image slices """
#   fig, axes = plt.subplots(1, len(slices))
#   for i, slice in enumerate(slices):
#       axes[i].imshow(slice.T, cmap="gray", origin="lower")
#plt.figure(figsize=(8,8), dpi=100)
axs[0].imshow(mni152[:, :, 50], cmap=plt.cm.Greys)
axs[1].imshow(mni152[:, :, 60], cmap=plt.cm.Greys)
axs[2].imshow(mni152[:, :, 70], cmap=plt.cm.Greys)
axs[3].imshow(mni152[:, :, 80], cmap=plt.cm.Greys)
axs[4].imshow(mni152[:, :, 90], cmap=plt.cm.Greys)
axs[5].imshow(mni152[:, :, 100], cmap=plt.cm.Greys)
axs[6].imshow(mni152[:, :, 110], cmap=plt.cm.Greys)
axs[7].imshow(mni152[:, :, 120], cmap=plt.cm.Greys)

#add overlay 1
axs[0].imshow(masked_overlay[:, :, 50], cmap=plt.cm.tab20c)
axs[1].imshow(masked_overlay[:, :, 60], cmap=plt.cm.tab20c)
axs[2].imshow(masked_overlay[:, :, 70], cmap=plt.cm.tab20c)
axs[3].imshow(masked_overlay[:, :, 80], cmap=plt.cm.tab20c)
axs[4].imshow(masked_overlay[:, :, 90], cmap=plt.cm.tab20c)
axs[5].imshow(masked_overlay[:, :, 100], cmap=plt.cm.tab20c)
axs[6].imshow(masked_overlay[:, :, 110], cmap=plt.cm.tab20c)
axs[7].imshow(masked_overlay[:, :, 120], cmap=plt.cm.tab20c)


#plt.suptitle("Center slices for EPI image")
for ax in axs.flat:
    ax.axis('off')
plt.subplots_adjust(left=4, right=5, top=5, bottom=4, hspace=0.1, wspace=0.1)
plt.tight_layout(pad=0.05)
plt.savefig(opt, bbox_inches='tight', dpi=2000)
