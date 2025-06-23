# Candidate Variable Star Detection (CVSD) for Pulsating Stars Identification on Simulated/Real Data

## Overview

Following Exploratory Data Analysis (EDA), this phase focuses on quantifying stellar variablity to identify strong candidate variable stars. Our targets: RR Lyrae, Cepheids, and Miras/LPVs show distinct light curve behaviors that can be captured through time-series statistical analysis of flux changes.

We will calculate variablity statistics across bands over time and select most dynamically changing stars, then filter the dataset for high priority sources where we will perform period estimation, classification, and spatial mapping.

**CVSD Goals**

VD helps us:
1) Quantify time-domain variability across multiple metrics
2) Differentiate true variability from noise or bad signals
3) Generate a list of most variable stars for further study
4) Prepare clean and statistically-supported inputs for period-finding and classification

**Data Inputs**

DIASource: time-series flux measurements
DIAObject: summary statistics 
Using objectId, fluxes, uncertainties, time indicies, and photometric bands g, r, i

## Step 1: Variability Metrics 

**Goals**

1) To detect pulsating stars
2) Calculate multiple statistical measure to capture different aspects of variability

**Tasks**

1) Reduced Chi-Square χ^2 Interpretations - quantify deviation from constant brightness, normalized by photometric errors (high values mean inconsistent variability with noise)
2) Welch-Stetson I (I_WS) - detect correlated deviations in sequential flux measurements since pulsating stars show correlated excursions (a high I_WS suggests periodiciy or outburst-like behabvior, use a single band approximation for time-ordered data in a filter)
3) Standard Deviation Thresholds - measure how much observed flux scatter exceeds expected photometric noise (stars with high ratios are likely true variables)

## Step 2: Composite Variability Index 

**Goals**

Combine the multiple metrics in Step 1 to form a unified variability index scorew for ranking candidate variable stars

**Tasks**

2) Normalizing each metric using z-score and/or min-max scaling
3) Compute a composite score (VarIndex = α * Norm(χ^2) + β * Norm(I_WS)) where α = β = 1 (but tunable for downstream performance), and a high score indicates high variability across both statistical frameworks

## Step 3: Top-N Candidate Selection

**Goals** 

We select the top N% most variable stars based on the composite index (e.g., top 5% or 10%). This step helps:
1) Reduce dimensionality and focus on likely candidates
2) Improve period detection success rates
3) Enhance classification and distance estimation accuracy

**Outputs**

1) Variability Catalog containing:
2) objectId
3) Raw and normalized values of χ², I_WS, Std Threshold
4) Composite Variability Index
5) Variability rank or percentile
6) Photometric band used

**Tasks**

1) Histograms of χ², I_WS, and Std Thresholds, understand metric distributions and set thresholds
2) Scatter plots (e.g., χ² vs I_WS), identify clusters and outliers; spot classes of variability
3) Composite Index vs Magnitude, validate brightness-dependence of detected variability
4) Cumulative plot of top N% candidates, justifies threshold selection based on index curve

**Next Steps**

After identifying top variable candidates, we:
1) Extract their time-series data (light curves)
2) Apply period-finding algorithms (e.g., Lomb-Scargle)
3) Classify variability type (RR Lyrae, Cepheid, Mira)
4) Use PLC relations to estimate distances

**Summary**

By combining multiple variability statistics into a normalized score, we isolate the candidate stars in our sample for future classification and mapping.
