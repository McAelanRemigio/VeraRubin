This folder includes our entire pipeline from data retrieval to machine learning, which was done through the following folders. Please note that the following is NOT the order that files will be found within this github folder and is instead the chronological order that we created these files in (and a 4th folder for all the CSV files used/created within this section)
    1. (Folder) Labeled Data Retrieval: Retrieving classified star data (primarily coordinates) and matching them to objects within RSP's DP1 diaObject catalog
        a. (Python Notebook) VStarQueries-Literature: Querying data from Bersier & Wood (2001) and test queries from Gaia DR3 within the Fornax Region
            -Required CSVs: None
            -Output CSVs: RRLyrae_Bersier_Wood.csv, Cepheid_Bersier_Wood.csv, LPV_Cand_Bersier_Wood.csv
        b. (Python Notebook) VStar_Tables: Combining data from Bersier & Wood (2001), Braga et. al (2022), and Gaia DR3 to create a 
            -Required CSVs: RRLyrae_Bersier_Wood.csv, Cepheid_Bersier_Wood.csv, LPV_Cand_Bersier_Wood.csv, Braga_RRLyrae.csv, Gaia_fornax_rrl.csv, Gaia_fornax_lpv.csv
            -Output CSVs: v_stars.csv
            *Note: We lost the notebook where we originally queried/created the Gaia DR3 csvs that were used here, but it's not very important to the conclusion of this code as we queried Gaia again later
        c. (Python Notebook) AdjustBersierWood: Adjusting coordinates from Bersier & Wood (2001) within v_stars.csv as the ra/dec columns didn't include full precision
            -Required CSVs: v_stars.csv
            -Output CSVs: v_stars_updated.csv
        d. (Python Notebook) VStarQueries-International: Querying data from the International Variable Star Catalog from all 7 regions covered by DP1, matching it to objects within RSP's DP1 diaObject catalog, and saving those matched objects to csv
            -Required CSVs: None
            -Output CSVs: international_catalog.csv
        e. (Python Notebook) GaiaLabelsToRSP: Querying data from Gaia DR3 from within the 7 regions covered by DP1, matching it to objects within RSP's DP1 diaObject catalog, and saving those matched objects to csv
            -Required CSVs: None
            -Output CSVs: gaiadata_dp1.csv
        e. (Python Notebook) DP1Matching: Matching all previously unmatched objects (all stars from fornax within v_stars_updated.csv) with objects from RSP's DP1 diaObject catalog, combining those matched objects with other already matched objects, implemented additional verification method through Simbad, filtered duplicates, and saved to csv
            -Required CSVs: v_stars_updated.csv, international_catalog.csv, gaiadata_dp1.csv
            -Output CSVs: diaobject_matched_final.csv
    2. (Folder) Feature Visualization and Supervised Learning
        a. (Python Notebook) SupervisedLearningPipeline: Retrieved other columns from diaObject that are useful for classification for matched objects mentioned above (color, amplitude, etc), filtered by number of obversations, and saved results to csv. Also plotted color magnitude diagram and attempted supervised learning with random forest
            -Required CSVs: diaobject_matched_final.csv
            -Output CSVs: variablestar_filtered.csv, variable_star_all_feat.csv
        b. (Python Notebook) FeatureVisualization: to understand distribution (skew, outliers, etc) we made boxplots of all of our features of interest
            -Required CSVs: variablestar_filtered.csv
            -Output CSVs: None
    3. (Folder) Unsupervised Learning: Queried Forced Source on DiaObject catalog to get more accurate data, filtered by observations, applied data normalization, performed PCA, applied unsupervised learning, and created graphs to visualize findings.
        a. FSODO_pipeline_labeled: Queried the Forced Source on DiaObject catalog for all unflagged and low error observations for labeled variable stars found in previous steps, calculated summary statistics for these values, and added them to the dataframe. Filtered by number of observations in r and i b ands, applied data normalization, and performed PCA on a subset of columns within the dataframe, and then applied unsupservised learning to the subset. Made color magnitude and distribution of RR Lyrae diagrams.
            -Required CSVs: variable_star_all_feat.csv
            -Output CSVs: None
        b. FSODO_fornax_queries: Queried the Forced Source on DiaObject catalog for all unflagged and low error observations for all diaObjects in the Fornax fitting certain variability requirements, calculated summary statistics for these values, and added them to the dataframe. Added labels to variable stars found in previous steps, filtered by number of observations in r and i b ands, applied data normalization, and performed PCA on a subset of columns within the dataframe, and then applied unsupservised learning to the subset. Made color magnitude and distribution of RR Lyrae diagrams.
            -Required CSVs: variable_star_all_feat.csv
            -Output CSVs: None
    4. (Folder) CSVs: All associated csv files made/used within this folder
        REPLACE WITH ALL CSV NAMES IN ALPHABETICAL ORDER
