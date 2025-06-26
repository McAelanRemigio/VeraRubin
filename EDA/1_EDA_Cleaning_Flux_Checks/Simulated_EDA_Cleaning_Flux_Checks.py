# libraries, imports, etc
import numpy
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colormaps
import seaborn as sns

print('numpy version: ', numpy.__version__)
print('matplotlib version: ', matplotlib.__version__)

# TAP Service 
from lsst.rsp import get_tap_service, retrieve_query
import lsst.daf.butler as dafButler
import lsst.geom
import lsst.afw.display as afwDisplay

service = get_tap_service("tap")
assert service is not None

# Selected Datasets

#1) DiaObject - core table for preprocessed time-varying object detections
diaobject_query = "SELECT column_name, datatype, description, unit "+\
                 "FROM TAP_SCHEMA.columns "+\
                 "WHERE table_name = 'dp02_dc2_catalogs.DiaObject'"
diaobject_results = service.search(diaobject_query)
diaobject_results_table = diaobject_results.to_table().to_pandas()
print('Number of columns available in the DiaObject catalog: ', len(diaobject_results_table))

#2) DiaSource - individual photometric measurements (light curves) of variables
diasource_query = "SELECT column_name, datatype, description, unit "+\
                 "FROM TAP_SCHEMA.columns "+\
                 "WHERE table_name = 'dp02_dc2_catalogs.DiaSource'"
diasource_results = service.search(diasource_query)
diasource_results_table = diasource_results.to_table().to_pandas()
print('Number of columns available in the DiaSource catalog: ', len(diasource_results_table))

#3) ForcedSource - uniform photometry across bands/images; color and P-L/P-L-C relations 
forcedsource_query = "SELECT column_name, datatype, description, unit "+\
                 "FROM TAP_SCHEMA.columns "+\
                 "WHERE table_name = 'dp02_dc2_catalogs.ForcedSource'"
forcedsource_results = service.search(forcedsource_query)
forcedsource_results_table = forcedsource_results.to_table().to_pandas()
print('Number of columns available in the ForcedSource catalog: ', len(forcedsource_results_table))

#4) Object - static properties; mean position, reference band, color, etc
object_query = "SELECT column_name, datatype, description, unit "+\
                 "FROM TAP_SCHEMA.columns "+\
                 "WHERE table_name = 'dp02_dc2_catalogs.Object'"
object_results = service.search(object_query)
object_results_table = object_results.to_table().to_pandas()
print('Number of columns available in the Object catalog: ', len(object_results_table))

# display table previews
diaobject_results_table
diasource_results_table
forcedsource_results_table
object_results_table

# Counts of observations in each dataset
# 1) DiaObject
diaobject_count_query = "SELECT COUNT(*) FROM dp02_dc2_catalogs.DiaObject"
diaobject_count_result = service.search(diaobject_count_query)
print("Number of observations in DiaObject: ", diaobject_count_result.to_table()[0][0])

# 2) DiaSource
diasource_count_query = "SELECT COUNT(*) FROM dp02_dc2_catalogs.DiaSource"
diasource_count_result = service.search(diasource_count_query)
print("Number of observations in DiaSource: ", diasource_count_result.to_table()[0][0])

# 3) ForcedSource
forcedsource_count_query = "SELECT COUNT(*) FROM dp02_dc2_catalogs.ForcedSource"
forcedsource_count_result = service.search(forcedsource_count_query)
print("Number of observations in ForcedSource: ", forcedsource_count_result.to_table()[0][0])

# 4) Object
object_count_query = "SELECT COUNT(*) FROM dp02_dc2_catalogs.Object"
object_count_result = service.search(object_count_query)
print("Number of observations in Object: ", object_count_result.to_table()[0][0])

# DiaObject sample (pre-processed detections)

# DiaObject g-band
diaobjectG_query = """
SELECT TOP 100000
    decl, diaObjectId, gPSFluxChi2, gPSFluxErrMean, gPSFluxLinearSlope,
    gPSFluxMAD, gPSFluxMax, gPSFluxMean, gPSFluxMeanErr, gPSFluxMin, gPSFluxNdata,
    gPSFluxSigma, gPSFluxStetsonJ
FROM dp02_dc2_catalogs.DiaObject
"""
diaobjectG_df = service.search(diaobjectG_query).to_table().to_pandas()

# DiaObject r-band
diaobjectR_query = """
SELECT TOP 100000
    decl, diaObjectId, rPSFluxChi2, rPSFluxErrMean, rPSFluxLinearSlope,
    rPSFluxMAD, rPSFluxMax, rPSFluxMean, rPSFluxMeanErr, rPSFluxMin, rPSFluxNData,
    rPSFluxSigma, rPSFluxStetsonJ
FROM dp02_dc2_catalogs.DiaObject
"""
diaobjectR_df = service.search(diaobjectR_query).to_table().to_pandas()

# DiaObject i-band
diaobjectI_query = """
SELECT TOP 100000
    decl, diaObjectId, iPSFluxChi2, iPSFluxErrMean, iPSFluxLinearSlope,
    iPSFluxMAD, iPSFluxMax, iPSFluxMean, iPSFluxMeanErr, iPSFluxMin, iPSFluxNData,
    iPSFluxSigma, iPSFluxStetsonJ
FROM dp02_dc2_catalogs.DiaObject
"""
diaobjectI_df = service.search(diaobjectI_query).to_table().to_pandas()

# DiaSource sample (time-domain photometry)
diasource_query = """
SELECT TOP 100000
    coord_dec, coord_ra, decl,
    diaObjectId, diaSourceId, filterName
    forced_PsfFlux_flag, forced_PsfFlux_flag_edge, 
    forced_PsfFlux_flag_noGoodPixels, midPointTai,
    psfFlux_flag, psfFlux_flag_edge, psfFlux_flag_noGoodPixels,
    psFlux, psFluxErr
FROM dp02_dc2_catalogs.DiaSource
"""
diasource_df = service.search(diasource_query).to_table().to_pandas()

# ForcedSource sample (cleaner/consistent photometry)
forcedsource_query = """
SELECT TOP 100000
    objectId, band, psfFlux, psfFluxErr
    psfFlux_flag, psfDiffFlux, psfDiffFluxErr
    psfDiffFlux_flag, coord_ra, coord_dec
FROM dp02_dc2_catalogs.ForcedSource
"""
forcedsource_df = service.search(forcedsource_query).to_table().to_pandas()

# Object sample (reference catalog)

# Object g-band
objectG_query = """
SELECT TOP 100000
    objectId, coord_ra, coord_dec, footprintArea, g_apFlux_flag, 
    g_apFlux_flag_apertureTruncated, g_bdChi2, g_bdFluxDErr, 
    g_calib_astrometry_used, g_calib_photometry_used, g_calibFlux_flag, 
    g_calibFlux_flag_apertureTruncated, g_cModel_flag, g_cModelFlux, g_decl, 
    g_extendedness, g_extendedness_flag, g_i_flag, g_inputCount, g_pixelFlags_bad, 
    g_psfFlux, g_psfFlux_flag, g_psfFluxErr, g_ra

FROM dp02_dc2_catalogs.Object
"""
objectG_df = service.search(objectG_query).to_table().to_pandas()

# Object r-band
objectR_query = """
SELECT TOP 100000
    objectId, coord_ra, coord_dec, footprintArea, r_apFlux_flag, 
    r_apFlux_flag_apertureTruncated, r_bdChi2, r_bdFluxDErr, 
    r_calib_astrometry_used, r_calib_photometry_used, r_calibFlux_flag, 
    r_calibFlux_flag_apertureTruncated, r_cModel_flag, r_cModelFlux, r_decl, 
    r_extendedness, r_extendedness_flag, r_i_flag, r_inputCount, r_pixelFlags_bad, 
    r_psfFlux, r_psfFlux_flag, r_psfFluxErr, r_ra

FROM dp02_dc2_catalogs.Object
"""
objectR_df = service.search(objectR_query).to_table().to_pandas()

# Object i-band 
objectI_query = """
SELECT TOP 100000
    objectId, coord_ra, coord_dec, footprintArea, i_apFlux_flag, 
    i_apFlux_flag_apertureTruncated, i_bdChi2, i_bdFluxDErr, 
    i_calib_astrometry_used, i_calib_photometry_used, i_calibFlux_flag, 
    i_calibFlux_flag_apertureTruncated, i_cModel_flag, i_cModelFlux, i_decl, 
    i_extendedness, i_extendedness_flag, i_i_flag, i_inputCount, i_pixelFlags_bad, 
    i_psfFlux, i_psfFlux_flag, i_psfFluxErr, i_ra

FROM dp02_dc2_catalogs.Object
"""
objectI_df = service.search(objectI_query).to_table().to_pandas()

# Creating csv files

# DiaObject (g, r, and i bands)
diaobjectG_df.to_csv("diaobjectG_sample_relevant.csv", index=False)
diaobjectR_df.to_csv("diaobjectR_sample_relevant.csv", index=False)
diaobjectI_df.to_csv("diaobjectI_sample_relevant.csv", index=False)

# DiaSource
diasource_df.to_csv("diasource_sample_relevant.csv", index=False)

# ForcedSource
forcedsource_df.to_csv("forcedsource_sample_relevant.csv", index=False)

# Object (g, r, and i bands)
objectG_df.to_csv("objectG_sample_relevant.csv", index=False)
objectR_df.to_csv("objectR_sample_relevant.csv", index=False)
objectI_df.to_csv("objectI_sample_relevant.csv", index=False)

# Dropping rows and saving as cleaned csvs

# DiaObject dataframes (g, r, and i bands) 
diaobjectGdf = pd.read_csv("diaobjectG_sample_relevant.csv").dropna()
diaobjectRdf = pd.read_csv("diaobjectR_sample_relevant.csv").dropna()
diaobjectIdf = pd.read_csv("diaobjectI_sample_relevant.csv").dropna()

# DiaSource dataframe 
diasourcedf = pd.read_csv("diasource_sample_relevant.csv").dropna()

# ForcedSource dataframe
forcedsourcedf = pd.read_csv("forcedsource_sample_relevant.csv").dropna()

# Object dataframes (g, r, and i bands)
objectGdf = pd.read_csv("objectG_sample_relevant.csv").dropna()
objectRdf = pd.read_csv("objectR_sample_relevant.csv").dropna()
objectIdf = pd.read_csv("objectI_sample_relevant.csv").dropna()

# Checks
print(diaobjectGdf) 
print(diaobjectRdf) 
print(diaobjectIdf) 
print(diasourcedf) 
print(forcedsourcedf) 
print(objectGdf) 
print(objectRdf) 
print(objectIdf)
print(diaobjectRdf.isna().sum()) # TEST

# Creating csv files again

diaobjectGdf.to_csv("diaobjectG_sample_relevant_cleaned.csv", index = False)
diaobjectRdf.to_csv("diaobjectR_sample_relevant_cleaned.csv", index = False)
diaobjectIdf.to_csv("diaobjectI_sample_relevant_cleaned.csv", index = False)
diasourcedf.to_csv("diasource_sample_relevant_cleaned.csv", index = False)
forcedsourcedf.to_csv("forcedsource_sample_relevant_cleaned.csv", index = False)
objectGdf.to_csv("objectG_sample_relevant_cleaned.csv", index = False)
objectRdf.to_csv("objectR_sample_relevant_cleaned.csv", index = False)
objectIdf.to_csv("objectI_sample_relevant_cleaned.csv", index = False)

print(forcedsourcedf.columns) # CHECKS
print(objectGdf.columns)
print(objectRdf.columns)
print(objectIdf.columns)

# Quantifying flux flags

# We dropped missing values, now filter out flag columns and zero checks for quality improvement

# DiaSource
diasourcedf = diasourcedf[
    (~diasourcedf['psfFlux_flag']) &
    (~diasourcedf['psfFlux_flag_edge']) &
    (~diasourcedf['psfFlux_flag_noGoodPixels']) &
    (diasourcedf['psFlux'] > 0)
]

# Object (g, r, i bands) 
objectGdf = objectGdf[
    (~objectGdf['g_psfFlux_flag']) &
    (objectGdf['g_psfFlux'] > 0)
]

objectRdf = objectRdf[
    (~objectRdf['r_psfFlux_flag']) &
    (objectRdf['r_psfFlux'] > 0)
]

objectIdf = objectIdf[
    (~objectIdf['i_psfFlux_flag']) &
    (objectIdf['i_psfFlux'] > 0)
]

# Pie Chart 

# Note: DiaObject and ForcedSource don't have booleans that behave as quality flags,
# both DiaObject and ForcedSource were skipped to avoid misclassification

# DiaSource 

diasourcedf_full = pd.read_csv("diasource_sample_relevant.csv")
# flag indicator column
diasourcedf_full['is_flagged'] = diasourcedf_full[
    ['psfFlux_flag', 'psfFlux_flag_edge', 'psfFlux_flag_noGoodPixels']
].astype(bool).any(axis=1)

diasourceflag_counts = diasourcedf_full['is_flagged'].value_counts()
print(diasourceflag_counts)

labels = ['Clean', 'Flagged']
sizes = [diasourceflag_counts[False], diasourceflag_counts[True]]
colors = ['lightgreen', 'salmon']

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Clean vs Flagged Detections in DiaSource')
plt.axis('equal')  # circle
plt.show()

# Object G-band 
objectGdf_full = pd.read_csv("objectG_sample_relevant.csv")
# flag indicator column
objectGdf_full['is_flagged'] = objectGdf_full['g_psfFlux_flag'].fillna(False).astype(bool)

objectGflag_counts = objectGdf_full['is_flagged'].value_counts()
print(objectGflag_counts)

labels = ['Clean', 'Flagged']
sizes = [objectGflag_counts[False], objectGflag_counts[True]]
colors = ['lightgreen', 'salmon']

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Clean vs Flagged Detections in Object G-band')
plt.axis('equal')  
plt.show()

# Object R-band 
objectRdf_full = pd.read_csv("objectR_sample_relevant.csv")
# flag indicator column
objectRdf_full['is_flagged'] = objectRdf_full['r_psfFlux_flag'].fillna(False).astype(bool)

objectRflag_counts = objectRdf_full['is_flagged'].value_counts()
print(objectRflag_counts)

labels = ['Clean', 'Flagged']
sizes = [objectRflag_counts[False], objectRflag_counts[True]]
colors = ['lightgreen', 'salmon']

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Clean vs Flagged Detections in Object R-band')
plt.axis('equal')  
plt.show()

# Object I-band 
objectIdf_full = pd.read_csv("objectI_sample_relevant.csv")
# flag indicator column
objectIdf_full['is_flagged'] = objectIdf_full['i_psfFlux_flag'].fillna(False).astype(bool)

objectIflag_counts = objectIdf_full['is_flagged'].value_counts()
print(objectIflag_counts)

labels = ['Clean', 'Flagged']
sizes = [objectIflag_counts[False], objectIflag_counts[True]]
colors = ['lightgreen', 'salmon']

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Clean vs Flagged Detections in Object I-band')
plt.axis('equal')  
plt.show()

# Make csvs files AGAIN

diasourcedf.to_csv("diasource_sample_relevant_flagcleaned.csv", index=False)
objectGdf.to_csv("objectG_sample_relevant_flagcleaned.csv", index=False)
objectRdf.to_csv("objectR_sample_relevant_flagcleaned.csv", index=False)
objectIdf.to_csv("objectI_sample_relevant_flagcleaned.csv", index=False)

# Merging all bands
diaobject_merged = diaobjectGdf[['diaObjectId', 'gPSFluxSigma', 'gPSFluxMean']].merge(
    diaobjectRdf[['diaObjectId', 'rPSFluxSigma', 'rPSFluxMean']], on='diaObjectId').merge(
    diaobjectIdf[['diaObjectId', 'iPSFluxSigma', 'iPSFluxMean']], on='diaObjectId')

diaobject_merged['g_r'] = diaobject_merged['gPSFluxMean'] - diaobject_merged['rPSFluxMean']
diaobject_merged['r_i'] = diaobject_merged['rPSFluxMean'] - diaobject_merged['iPSFluxMean']
diaobject_merged['g_i'] = diaobject_merged['gPSFluxMean'] - diaobject_merged['iPSFluxMean']

# gPSFluxSigma vs rPSFluxSigma

sns.scatterplot(data=diaobject_merged, x='gPSFluxSigma', y='rPSFluxSigma')
plt.xlabel('gPSFluxSigma'); plt.ylabel('rPSFluxSigma')
plt.title('g vs r Variability'); plt.show()

# gPSFluxSigma vs iPSFluxSigma

sns.scatterplot(data=diaobject_merged, x='gPSFluxSigma', y='iPSFluxSigma')
plt.xlabel('gPSFluxSigma'); plt.ylabel('iPSFluxSigma')
plt.title('g vs i Variability'); plt.show()

# rPSFluxSigma vs iPSFluxSigma
sns.scatterplot(data=diaobject_merged, x='rPSFluxSigma', y='iPSFluxSigma')
plt.xlabel('rPSFluxSigma'); plt.ylabel('iPSFluxSigma')
plt.title('r vs i Variability'); plt.show()

# g - r (x) vs gPSFluxSigma (y)
sns.scatterplot(data=diaobject_merged, x='g_r', y='gPSFluxSigma')
plt.xlabel('g - r Color'); plt.ylabel('gPSFluxSigma')
plt.title('Color vs Variability in g'); plt.show()

# r - i (x) vs iPSFluxSigma (y)
sns.scatterplot(data=diaobject_merged, x='r_i', y='iPSFluxSigma')
plt.xlabel('r - i Color'); plt.ylabel('iPSFluxSigma')
plt.title('Color vs Variability in i'); plt.show()

# g - i (x) vs rPSFluxSigma
sns.scatterplot(data=diaobject_merged, x='g_i', y='rPSFluxSigma')
plt.xlabel('g - i Color'); plt.ylabel('rPSFluxSigma')
plt.title('Color vs Variability in r'); plt.show()

# gpsFluxSigma vs count
plt.hist(diaobject_merged['gPSFluxSigma'], bins=50, color='skyblue')
plt.title('Histogram of gPSFluxSigma'); plt.xlabel('gPSFluxSigma'); plt.ylabel('Count')
plt.show()

# rpsFluxSigma vs count
plt.hist(diaobject_merged['rPSFluxSigma'], bins=50, color='skyblue')
plt.title('Histogram of rPSFluxSigma'); plt.xlabel('rPSFluxSigma'); plt.ylabel('Count')
plt.show()

# ipsFluxSigma vs count
plt.hist(diaobject_merged['iPSFluxSigma'], bins=50, color='skyblue')
plt.title('Histogram of iPSFluxSigma'); plt.xlabel('iPSFluxSigma'); plt.ylabel('Count')
plt.show()