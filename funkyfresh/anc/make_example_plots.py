import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np

from funkyfresh import set_style

theta = np.linspace(0, 360, 3601) * u.degree  # noqa

# Matplotlib default
fig, axis = plt.subplots()
axis.plot(theta, np.sin(theta))
axis.set_xlabel(r'$\theta$ [degrees]')
axis.set_ylabel(r'$\sin(\theta)$')
plt.savefig('matplotlib_default.png')
plt.close(fig)

# FunkyFresh default
set_style(name='AGU', silent=True)
fig, axis = plt.subplots()
axis.plot(theta, np.sin(theta))
axis.set_xlabel(r'$\theta$ [degrees]')
axis.set_ylabel(r'$\sin(\theta)$')
plt.savefig('funkyfresh.png')
plt.close(fig)

# FunkyFresh default with Matplotlib dark
plt.style.use('dark_background')

fig, axis = plt.subplots()
axis.plot(theta, np.sin(theta), color='white')
axis.set_xlabel(r'$\theta$ [degrees]')
axis.set_ylabel(r'$\sin(\theta)$')
plt.savefig('funkyfresh_dark.png')
plt.close(fig)

# presentation mode
set_style(name='AGU', silent=True, presentation=True)
fig, axis = plt.subplots()
axis.plot(theta, np.sin(theta))
axis.set_xlabel(r'${\theta}$ [degrees]')
axis.set_ylabel(r'$\sin(\theta)$')
plt.savefig('funkyfresh_presentation.png')
plt.close(fig)
