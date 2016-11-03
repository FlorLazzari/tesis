# para agregar variación en el tiempo (animación)
 
# http://www.monash.edu/science
# http://www.callumatkinsononline.com/

# http://www.callumatkinsononline.com/animating-velocity-field-python-ffmpeg/

nsteps = 6304 # number of time-steps to plot
imageprefix = "velocity_"
# consider each time-step
for nt in range (1,nsteps):
  # compute velocity fluctuation
  uf = np.copy(u[nt,:,:])
  vf = np.copy(v[nt,:,:])
  # subtract mean velocity at each y position
  for j in range(0,u.shape[1]):
    uf[j,:] -= um[j]
    vf[j,:] -= vm[j]
  # set figure size in inches
  fig = plt.figure(1,figsize=(9.,3.5))
  plt.clf()
  ax = fig.add_subplot(111, aspect='equal')
  # set contour levels
  levels = np.arange(-5.2,5.2,0.2)
  plt.contourf(x,y,uf[:,:],levels)
  cbar = plt.colorbar()
  cbar.set_label('$u\'^+$', fontsize=18)
  # plot vectors of fluctuating velocity (every 2nd vector) plt.quiver(x[::2],y[::2],uf[::2,::2],vf[::2,::2],units='xy',angles='xy',scale=0.04,width=3, headwidth=5,headlength=8,minlength=0.1)
  # set plot limits and axis titles
  plt.ylim([20,1200])
  plt.xlabel('$x^+$', fontsize=18)
  plt.ylabel('$y^+$',fontsize=18)
  # save plot to image file at a resolution of 300 dpi
  plt.savefig("%s%04d.png" % (imageprefix,nt),dpi=300)




# en la terminal, para compilar el video:

# ffmpeg -i velocity_%04d.png -c:v libx264 -r 15 -pix_fmt yuv420p video.mp4

