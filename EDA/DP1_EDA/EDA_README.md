# Exploratory Data Analysis for Variable Star Mapping on Simulated/Real Data

## Overview
This project uses simulated Rubin Observatory data to identify pulsating variable stars, specifically RR Lyrae, Cepheids, and Miras/LPVs and extract their light curve characteristics. These stars act as standard candles for measuring cosmic distances. Ultimately, our goal is to construct 3D spatial maps of the Milky Way and nearby satellite galaxies such as Fornax.

We leverage tools like PSF photometry, variability statistics, and time-series analysis to:
1) Detect candidate variable stars
2) Measure brightness and period
3) Prepare the data for classification and mapping

**EDA Goals**

Exploratory Data Analysis helps us:
1) Understand data quality and structure
2) Explore variability across multiple photometric bands (g, r, i)
3) Filter out false positives (e.g., noise, outliers, low-signal detections)
4) Develop robust inputs for period analysis and machine learning classification

**Data Tables**

We analyze four LSST-style data tables:
1) DIAObject: Time-aggregated object-level variability metrics
2) DIASource: Individual observations used to create light curves
3) Object: Static metadata (e.g., coordinates, average magnitudes)
4) ForcedSource: Flux measurements at known positions, used for color/variability tracking

## Step 1: Data Cleaning - Validation

**Goals**

1) Ensure data integrity
2) Remove missing or flagged data that may distort results

**Tasks**

1) Drop rows with NaN, NA, or zero-valued fluxes
2) Identify and quantify flux flags (e.g., saturation, deblending issues)
3) Pie chart: Ratio of clean vs flagged detections

**Band Comparison**

Pulsating stars behave differently across photometric bands:
1) RR Lyrae: Peak in blue/green band, short period, low metallacity, strong variation in blue bands, [g]
2) Cepheids: peak in visible red bands, intermediate period, good balance of amplitude/stability, [r]
3) Miras: Peak in infrared bands, long period, cool red giants, larger amplitudes in redder bands, [i]

**Variability and Color Analysis Plots**

1) **gPSFluxSigma vs rPSFluxSigma** - Compare blue vs red variability, helps separate RR Lyrae (high in g) from Cepheids (moderate in r)
2) **gPSFluxSigma vs iPSFluxSigma** - Compare blue vs infrared variability, useful to isolate Miras (stronger variation in i) from RR Lyrae
3) **rPSFluxSigma vs iPSFluxSigma** - Compare red vs redder variability, differentiates Cepheids (stronger in r) from Miras (stronger in i)
4) **g - r vs gPSFluxSigma** - Shows how blue-red color correlates with g-band variability, RR Lyrae are usually bluer, with higher variability
5) **r - i vs iPSFluxSigma** - Shows how red–infrared color tracks with i-band variability, great for flagging Miras, which are redder and vary more in i
6) **g - i vs PSFluxSigma** (choose most informative band or all three) - Long baseline color, useful for separating cool vs hot variables, can highlight outliers or transition stars
7) **Histograms of PSFluxSigma in Each Band** - Helps visualize overall variability strength distribution by band (gPSFluxSigma, rPSFluxSigma, iPSFluxSigma)

**Outlier Validation**

High variability metrics don’t always mean true variability. We:
1) Select stars with high Chi², MAD, Stetson J
2) Validate light curves for anomalies or bad data

## Step 2: DIAObject EDA - Variability Metrics

**Key Visualizations**
1) Chi² vs Std Dev (per band): Identifies high-variability candidates
2) Stetson J vs Skew (per band): Looks for asymmetric pulses (e.g., RR Lyrae rise/fall pattern)
3) MAD vs Std Dev Histogram(per band): Compares outlier-robust and sensitive metrics
4) Flux Range Histogram (Max - Min)(per band): Finds large-amplitude stars
5) Chi² vs N Data Points(per band): Validates metric reliability
6) Skew vs Std Dev (per band): Differentiates noise from true variability
7) Stetson J vs Flux Range(per band): Flags high-priority candidates
8) Comparison plots for 1-7

**Core Columns**

gPSFluxChi2, gPSFluxSigma, gPSFluxStetsonJ, gPSFluxMax, gPSFluxMin, gPSFluxMAD, gPSFluxSkew, gPSFluxLinearSlope, gPSFluxNdata

**Summary Table**
| Metric          | Description                               |
| --------------- | ----------------------------------------- |
| Chi², Stetson J | Variability consistency                   |
| Sigma, MAD      | Spread and robustness                     |
| Skew            | Asymmetry of variability                  |
| Max/Min/Range   | Amplitude indicators                      |
| Linear Slope    | Temporal trends (e.g., sawtooth patterns) |
| Ndata           | Confidence indicator for above statistics |


# Step 3: DiaSource EDA - (Light Curves)

We plot raw and smoothed light curves to:
1) Visualize brightness changes over time
2) Prepare for period estimation using models like Lomb-Scargle

**Steps**
1) Plot midPointTai vs psFlux with psFluxErr as error bars
2) Compute and plot rolling mean to visualize periodic patterns

**Why This Matters**
1) Variable stars "pulse" over time—tracking these patterns helps us:
2) Detect variability
3) Estimate period and amplitude
4) Classify stars using astronomy, ML, data science, and statistics

**Object Table**

These are some simple metadata checks to help ensure data consistency and support downstream classification 
1) RA vs Dec scatter plot to verify spatial coverage
2) Histograms for color indices (g - r, r - i)

# Step 4: ForcedSource – Color Checks for Distance Estimation

We use it to:
1) Estimate stellar color (e.g., g - i, r - i)
2) Support Period-Luminosity-Color (PLC) relation modeling
3) Calculate absolute magnitudes and distances
4) Contribute to the 3D galactic map

**Summary**

This EDA lays the foundation for identifying periodic variables and preparing inputs for:
1) Distance estimation
2) Stellar classification
3) Galactic structure modeling

By visualizing variability patterns and cleaning the data, we increase the reliability of our subsequent time-series and ML workflows.
