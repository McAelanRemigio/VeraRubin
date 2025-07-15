# Conclusion: Exploratory Data Analysis of Rubin DP1 for Variable Star Classification

This exploratory analysis established a strong foundation for identifying variable stars using the Rubin DP1 dataset. It integrated flux reliability checks, variability metrics, morphological indicators, and color behavior focusing on RR Lyrae, Cepheids, and Miras.

## Flux Quality and Reliability
```DiaObject``` Table: (≥99% usable). No flux checks. 

```Object``` Table: Very clean (≥99% usable). Ideal for color-magnitude diagrams and morphology.

```DiaSource``` Table: Noisier (~75% usable). Crucial for time-series and variability studies. Requires careful flag filtering.


## Color 
Color-Magnitude Diagrams show a clear stellar sequence with outliers linked to flux issues.

```PSF``` vs. ```CModel Flux``` helps separate point vs. extended sources.

```Chi²``` vs. ```Flux Error``` exposes problematic fits (e.g., chi² ≈ 1e-38).

```Extendedness``` is helpful when combined with color or flux ratios.

## Variability Analysis and Light Curve Behavior

Metrics like ```psfFluxSigma```, ```StetsonJ```, and ```MAD``` reliably indicate variability. 

**RR Lyrae**: Blue stars with strong g-band variability. 

**Cepheids**: Intermediate color, peak in r-band. 

**Miras**: Very red, strongest variability in i-band. 

Variability distributions are skewed, meaning most stars are stable, with a long tail of variable sources.

## Time Series Behavior
Light curves show clear periodicity in high-variability stars, enhanced by smoothing.

Stars with ≥20 observations are suitable for period analysis (e.g., Lomb-Scargle).

Time gaps and flux jumps reveal irregular sampling and artifacts, reinforcing the need for quality flags.

## Next Steps Ready 

Cleaned, grouped, and validated data now support: 

Period estimation 

Feature extraction 

Machine learning classification of variable stars


# RELEVANT COLUMNS

## DiaObject (g, r, i bands)

```diaObjectId```, ```ra```, ```dec```: Identification & sky position

```psfFluxSigma```: Core variability metric

```psfFluxMAD```: amplitude estimator

```psfFluxLinearSlope```: Long-term trend detector

```psfFluxMax```, ```psfFluxMin```: Amplitude range

```psfFluxMean```, ```psfFluxMeanErr```: Central flux and uncertainty

```psfFluxErrMean```: Measurement noise

```psfFluxNdata```: Number of observations for filtering

```psfFluxStetsonJ```: Correlation-based variability indicator

**Used for variability characterization, outlier rejection, and feature engineering**

## Object (g, r, i bands)
```objectId```, ```coord_ra```, ```coord_dec```: Identification & sky position

```psfFlux```, ```psfFluxErr```, ```psfFlux_flag```: Photometry + quality control

```cModelFlux```, ```cModel_flag```: Flux comparison

```bdChi2```, ```bdFluxDErr```: Model fitting quality (e.g., BD Chi² vs. flux error)

```extendedness```, ```extendedness_flag```: Point vs. extended source separation

```calib_photometry_used```, ```calib_astrometry_used```: Checks for reliable calibration

```pixelFlags_bad```: Used to exclude contaminated detections

**Used for classification, flux comparisons (PSF vs. CModel), CMD construction (e.g., g - r vs. r), Quality filtering (flags, chi², bad pixels)**

## DiaSource
```diaObjectId```,```diaSourceId```, ```coord_ra```, ```coord_dec```, ```dec```: Identification and position

```psfFlux```, ```psfFluxErr```: Light curve data

```psfFlux_flag```, ```psfFlux_flag_edge```, ```psfFlux_flag_noGoodPixels```: Quality control for variability

```midPointMjdTai```: Timestamp for light curve plotting


**Used for light curve construction and cleaning, filtering out poor detections, and tracking cadence and gaps**

# NOT DIRECTLY RELEVANT COLUMNS

## Object / DiaSource

```g/r/i_apFlux_flag```, ```*_flag_apertureTruncated```: Aperture photometry not used 

```g/r/i_i_flag```: unclear on what these would be used to check

```inputCount```: Not used

```footprintArea```: Not helpful

```g/r/i_calibFlux_flag```: Redundant with psfFlux_flag

```g/r/i_dec```, ```g/r/i_ra```: Redundant with coord_dec, coord_ra

```forced_PsfFlux_*```: Not relevant unless you're using ForcedSource light curves specifically


