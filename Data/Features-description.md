# Descipción de las 68 variables de nuestro dataset

Description of the variables from the SDSS catalog. 
The SDSS is a major astronomical survey that has mapped a significant portion of the sky, 
collecting data on galaxies, quasars, and stars. 

## Positional and Redshift Data
These variables define the object's location in the sky and its distance.

* **ra**: **Right ascension**, one of the two celestial coordinates that specifies the object's position on the sky.
* **dec**: **Declination**, the other celestial coordinate, analogous to latitude on Earth.
* **z**: The **redshift** of the object, derived from its spectrum. This is a measure of how much the light has been stretched due to the expansion of the universe, and it is directly related to the object's distance.
* **zErr**: The statistical **error** associated with the redshift measurement.
* **decErr**: The **error** in the declination measurement.

---

## Magnitude and Flux Measurements
Magnitudes are a logarithmic scale of brightness. A smaller number indicates a brighter object. The prefixes 'dered', 'fiber', 'model', and 'psf' refer to different ways of measuring or correcting the magnitudes. The suffixes 'g', 'i', 'r', 'u', 'z' denote the five photometric filters used in the SDSS.

* **dered_u, dered_g, dered_r, dered_i, dered_z**: **Dereddened magnitudes**. These are the corrected brightnesses of the object after accounting for **extinction** caused by dust within our own Milky Way galaxy. Extinction makes objects appear fainter and redder than they are, so these corrected values are a more accurate representation of the object's true brightness.
* **extinction_u, extinction_g, extinction_r, extinction_i, extinction_z**: The amount of **extinction** (in magnitudes) applied to the raw photometry to get the dereddened values.
* **psfMag_u, psfMag_g, psfMag_r, psfMag_i, psfMag_z**: **Point-spread function (PSF) magnitudes**. These are calculated by fitting the brightness profile of a point source (like a star) to the object. They are most reliable for point-like objects such as stars and quasars.
* **psfMagErr_u, psfMagErr_g, psfMagErr_r, psfMagErr_i, psfMagErr_z**: The **errors** associated with the PSF magnitudes.
* **fiberMag_u, fiberMag_g, fiberMag_r, fiberMag_i, fiberMag_z**: **Fiber magnitudes**. These are the brightnesses measured through the fiber aperture of the spectrograph. They indicate how much light from the object entered the spectrograph.
* **fiberMagErr_u, fiberMagErr_g, fiberMagErr_r, fiberMagErr_i, fiberMagErr_z**: The **errors** associated with the fiber magnitudes.
* **modelMag_u, modelMag_g, modelMag_r, modelMag_i, modelMag_z**: **Model magnitudes**. These are the magnitudes of a galaxy as determined by fitting one of two galaxy models (a de Vaucouleurs profile for elliptical galaxies and an exponential profile for spiral galaxies) to the object's light profile. They are considered the most accurate total magnitudes for galaxies.
* **modelMagErr_u, modelMagErr_g, modelMagErr_r, modelMagErr_i, modelMagErr_z**: The **errors** associated with the model magnitudes.

---

## Morphological and Shape Data
These variables describe the size and shape of the galaxy.

* **expRad_u, expRad_g, expRad_r, expRad_z**: **Exponential scale radius**. The radius of an object assuming it has an exponential light profile, which is typical for disk galaxies and the bulges of spiral galaxies.
* **expRadErr_u, expRadErr_g, expRadErr_r, expRadErr_z**: The **errors** associated with the exponential scale radius.
* **deVRad_g, deVRad_i, deVRad_r, deVRad_z**: **de Vaucouleurs scale radius**. The radius of an object assuming it has a de Vaucouleurs light profile, which is typical for elliptical galaxies.
* **deVRadErr_g, deVRadErr_i, deVRadErr_r, deVRadErr_z**: The **errors** associated with the de Vaucouleurs scale radius.
* **expPhi_u, expPhi_g, expPhi_r, expPhi_i, expPhi_z**: The **position angle** of the exponential light profile model. It describes the orientation of the galaxy on the sky.
* **petroRad_r, petroRadErr_r**: The **Petrosian radius** and its error, which is a standardized way to measure the size of a galaxy. It represents the radius within which a specific fraction of the galaxy's total light is contained. It is measured in the 'r' band.
