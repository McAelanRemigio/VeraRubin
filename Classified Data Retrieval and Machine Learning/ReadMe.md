### 📊 Classified Data Retrieval & Machine Learning

This folder includes our entire pipeline from data retrieval of classified variable stars (RRLyrae, Cepheid, and LPV) captured by the 7 fields in Rubin DP1 to machine learning approaches to help identify candidate variable stars, which was done through the following folders. 

**Search Tools**: Vizier, Gaia DR3 Catalogs, TAP Service

**Python Libraries Used**: Pandas, Numpy, scikit-learn, matplotlib, lsst.rsp, astropy

**Acknowledgements**: This project uses data from [Bersier & Wood (2001)](https://iopscience.iop.org/article/10.1086/338315/fulltext/) and [Braga et al. (2022)](https://academic.oup.com/mnras/article/517/4/5368/6764730?login=true#supplementary-data)

*Please note that the following is NOT the order that files will be found within this github folder and is instead the chronological order that we created these files in (and a 4th folder for all the CSV files used/created within this section).*

#### Description of Contents:
1. **(Folder) Labeled Data Retrieval**: Retrieving classified star data (primarily coordinates) and matching them to objects within RSP's DP1 diaObject catalog

    a. **VStarQueries-Literature.ipynb**: Querying data from Bersier & Wood (2001) and test queries from Gaia DR3 within the Fornax Region
   
       - Required CSVs: None
       - Output CSVs: RRLyrae_Bersier_Wood.csv, Cepheid_Bersier_Wood.csv, LPV_Cand_Bersier_Wood.csv
   
    b. **VStar_Tables.ipynb**: Combining data from Bersier & Wood (2001), Braga et. al (2022), and Gaia DR3 to create a central catalog for classified variables found in Fornax

       - Required CSVs: RRLyrae_Bersier_Wood.csv, Cepheid_Bersier_Wood.csv, LPV_Cand_Bersier_Wood.csv, Braga_RRLyrae.csv, Gaia_fornax_rrl.csv, Gaia_fornax_lpv.csv
       - Output CSVs: v_stars.csv
       **Note: We lost the notebook where we originally queried/created the Gaia DR3 csvs that were used here, but it's not very important to the conclusion of this code as we queried Gaia catalogs again later**
   
    c. **AdjustBersierWood.ipynb**: Adjusting coordinates from Bersier & Wood (2001) within v_stars.csv as the ra/dec columns didn't include full precision
   
       - Required CSVs: v_stars.csv
       - Output CSVs: v_stars_updated.csv
   
    d. **VStarQueries-International.ipynb**: Querying data from the International Variable Star Catalog from all 7 regions covered by DP1, matching it to objects within RSP's DP1 diaObject catalog, and saving those matched objects to csv
   
       - Required CSVs: None
       - Output CSVs: international_catalog.csv
   
    e. **GaiaLabelsToRSP.ipynb**: Querying data from Gaia DR3 from within the 7 regions covered by DP1, matching it to objects within RSP's DP1 diaObject catalog, and saving those matched objects to csv
   
       - Required CSVs: None
       - Output CSVs: gaiadata_dp1.csv
   
    f. **DP1Matching.ipynb**: Matching all previously unmatched objects (all stars from fornax within v_stars_updated.csv) with objects from RSP's DP1 diaObject catalog, combining those matched objects with other already matched objects, implemented additional verification method through Simbad, filtered duplicates, and saved to csv
   
       - Required CSVs: v_stars_updated.csv, international_catalog.csv, gaiadata_dp1.csv
       - Output CSVs: diaobject_matched_final.csv

2. **(Folder) Feature Visualization and Supervised Learning**: Applying supervised learning and data visualization to better understand what features are most likely to be helpful for classification & clustering of candidate variables

    a. **SupervisedLearningPipeline.ipynb**: Retrieved other columns from diaObject that are useful for classification for matched objects mentioned above (color, amplitude, etc), filtered by number of obversations, and saved results to csv. Also         plotted color magnitude diagram and attempted supervised learning with Random Forest algorithm.
   
    *Note: Our attempt at supervised learning was somewhat constrained due to lack of sufficient labeled training data (especially Cepheid variables. We aim to attempt various supervised learning approaches, especially with access to more classified variable star data in the future and in DP2*
   
        - Required CSVs: diaobject_matched_final.csv
        - Output CSVs: variablestar_filtered.csv, variable_star_all_feat.csv
   
   b. **FeatureVisualization.ipynb**: To understand distribution (skew, outliers, etc), we made boxplots of all of our features of interest (amplitude, variability stats, photometry measurements, etc.)

       - Required CSVs: variablestar_filtered.csv
       - Output CSVs: None
   
3. **(Folder) Unsupervised Learning**: Querying Forced Source on DiaObject catalog to get more accurate data, filtering by observations, applying data normalization, performing PCA, applying unsupervised learning, and creating graphs to visualize findings

    a. **FSODO_pipeline_labeled.ipynb**: Queried the Forced Source on DiaObject catalog for all unflagged and low error observations for labeled variable stars found in previous steps, calculated summary statistics for these values, and added them to the dataframe. Filtered by number of observations in r and i b ands, applied data normalization, and performed PCA on a subset of columns within the dataframe, and then applied unsupservised learning to the subset. Made color magnitude and distribution of RR Lyrae diagrams.
   
       - Required CSVs: variable_star_all_feat.csv
       - Output CSVs: None
   b. **FSODO_fornax_queries.ipynb**: Queried the Forced Source on DiaObject catalog for all unflagged and low error observations for all diaObjects in the Fornax fitting certain variability requirements, calculated summary statistics for these values, and added them to the dataframe. Added labels to variable stars found in previous steps, filtered by number of observations in r and i b ands, applied data normalization, and performed PCA on a subset of columns within the dataframe, and then applied unsupservised learning to the subset. Made color magnitude and distribution of RR Lyrae diagrams.
   
       - Required CSVs: variable_star_all_feat.csv
       - Output CSVs: None

4. **(Folder) Other Files**: Any other files that don't fit the chronological progression used to group other files

    a. **lightcurve_filtering.ipynb**: A generic notebook that was used at multiple different times during research to create different subsets from CSVs (filtering in different ways each time) and to search gaia for associated period values. This notebook is mainly used to create subsets of data to be used by Tahlia's periodogram/lightcurve analysis code (which is why we wanted periods to verify the code's accuracy)
   
       - Required CSVs: Subject to change, depends on what csv file we were using at the time
       - Output CSVs: Also subject to change, named different things at different times

6. **(Folder) CSVs**: All associated csv files made/used within this folder
        REPLACE WITH ALL CSV NAMES IN ALPHABETICAL ORDER
