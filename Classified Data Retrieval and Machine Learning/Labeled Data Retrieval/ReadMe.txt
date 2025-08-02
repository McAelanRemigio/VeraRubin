Retrieving classified star data (primarily coordinates) and matching them to objects within RSP's DP1 diaObject catalog

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

        f. (Python Notebook) DP1Matching: Matching all previously unmatched objects (all stars from fornax within v_stars_updated.csv) with objects from RSP's DP1 diaObject catalog, combining those matched objects with other already matched objects, implemented additional verification method through Simbad, filtered duplicates, and saved to csv
            -Required CSVs: v_stars_updated.csv, international_catalog.csv, gaiadata_dp1.csv
            -Output CSVs: diaobject_matched_final.csv
