# Descripción de las 68 variables de nuestro dataset

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

* **expRad_g, expRad_i, expRad_r, expRad_z**: **Exponential scale radius**. The radius of an object assuming it has an exponential light profile, which is typical for disk galaxies and the bulges of spiral galaxies.
* **expRadErr_u, expRadErr_g, expRadErr_r, expRadErr_z**: The **errors** associated with the exponential scale radius.
* **deVRad_g, deVRad_i, deVRad_r, deVRad_z**: **de Vaucouleurs scale radius**. The radius of an object assuming it has a de Vaucouleurs light profile, which is typical for elliptical galaxies.
* **deVRadErr_g, deVRadErr_i, deVRadErr_r, deVRadErr_z**: The **errors** associated with the de Vaucouleurs scale radius.
* **expPhi_u, expPhi_g, expPhi_r, expPhi_i, expPhi_z**: The **position angle** of the exponential light profile model. It describes the orientation of the galaxy on the sky.
* **petroRad_r, petroRadErr_r**: The **Petrosian radius** and its error, which is a standardized way to measure the size of a galaxy. It represents the radius within which a specific fraction of the galaxy's total light is contained. It is measured in the 'r' band.


# How are these values actually measured

The process involves two main steps: 
  - **Photometry**: measuring brightness through filters
  - **Light Profile Fitting**: measuring size and shape

1. How the "Light Profile" Looks and is Measured (Photometry)
The fundamental concept is the Spectral Energy Distribution (SED) of the object, and the SDSS filters sample that SED.

The Object's "Profile" (SED)
- The object's true light profile is its Spectral Energy Distribution (SED), which is indeed a plot of Energy (or Flux Density) versus Wavelength ($\lambda$).

- For a star, the SED looks like a smooth curve, similar to a blackbody, but with absorption or emission lines superimposed.

- For a galaxy, the SED is more complex, as it is the combined light from billions of stars (old and new), gas, and dust.

The SDSS telescope doesn't take a single continuous spectrum; it takes five separate images, each through a unique color filter.

Filter	Peak Wavelength (λ)	Color Sensation
1. u	$\sim355$ nm	Ultraviolet
2. g	$\sim480$ nm	Green
3. r	$\sim620$ nm	Red
4. i	$\sim750$ nm	Near-Infrared
5. z	$\sim890$ nm	Infrared

For a single filter (e.g., the g-band):

- The filter only lets light within a specific wavelength range pass through.

- The CCD detector records the total number of photons that passed through that filter.

- This raw photon count is converted into an instrumental flux and then into a magnitude (like psfMag_g, fiberMag_g, etc.) using calibration standards.

- This process gives you five discrete brightness measurements along the object's full SED. The color of the object is defined by the differences between these magnitudes, e.g., (u−g), (g−r), etc.

2. Deriving the Variables from the Measurements
The measured variables are derived from the image data in two main ways:

  A. Total Brightness (Magnitudes): All magnitude variables (like psfMag, modelMag, dered, etc.) are ways of calculating the object's brightness.

| Variable Name	| Calculation Method	| Purpose |
| :--- | :---: | ---: |
| psfMag	| Calculates the brightness by fitting a model of a Point Spread Function (PSF) to the object's light.	| Best for point sources (stars, quasars) where the observed shape is dominated by the telescope's optics.|
| modelMag	| Calculates the brightness using the best-fit galaxy light profile (either exponential or de Vaucouleurs).	| The recommended magnitude for most galaxies, as it best captures the total light.|
| fiberMag	| Calculates the brightness contained only within the physical aperture (usually 3 arcseconds) of the spectrograph fiber.	| Used to determine if enough light was gathered to measure the redshift.|
| dered_	| This is a correction applied after the raw magnitude is found, using the extinction_ value.	| Corrects for the dimming and reddening caused by dust in our own galaxy to get the object's intrinsic brightness.|


  B. Size and Shape (Morphological Variables): The galaxy's physical light profile—the way its brightness drops from the center to the edge—is modeled to get the size and shape variables.

**Modeling the Light**: The SDSS imaging pipeline attempts to fit two mathematical models to the 2D light distribution of the galaxy in each band:

**The de Vaucouleurs Profile** (Sérsic index n=4): Typical for elliptical galaxies and the bulges of spirals. This fit results in the deVRad (deVRad_r) and associated error.

**The Exponential Profile** (Sérsic index n=1): Typical for spiral galaxy disks. This fit results in the expRad (expRad_r) and associated error.

**Petrosian Radius** (petroRad_r): This is a non-model-dependent way to measure a galaxy's size. It defines a radius where the ratio of the surface brightness at that point to the average surface brightness inside that point reaches a specific, standard value (usually 0.2). This value is standard across astronomy and allows for consistent size and flux comparisons.

**Position Angle** (expPhi_g): This variable, and related ones, are the result of the 2D light profile fitting. It measures the rotation of the fitted ellipse (the galaxy's shape) relative to the north direction, giving its orientation on the sky.

  C. Distance (Redshift): The z and zErr variables are measured using a dedicated spectrograph:

- The light gathered by the fiber (which determines fiberMag) is split into a continuous spectrum.

- Specific spectral lines (like Hydrogen or Oxygen lines) are identified in the spectrum.

- The redshift (z) is calculated by measuring how much the wavelength (λ) of these identified lines has shifted away from their known, rest-frame lab value

- The zErr is the statistical error of this calculation, reflecting the quality and signal-to-noise ratio of the measured spectrum.
