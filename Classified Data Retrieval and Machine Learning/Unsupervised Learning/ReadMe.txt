Querying Forced Source on DiaObject catalog to get more accurate data, filtering by observations, applying data normalization, performing PCA, applying unsupervised learning, and creating graphs to visualize findings

        a. FSODO_pipeline_labeled: Queried the Forced Source on DiaObject catalog for all unflagged and low error observations for labeled variable stars found in previous steps, calculated summary statistics for these values, and added them to the dataframe. Filtered by number of observations in r and i b ands, applied data normalization, and performed PCA on a subset of columns within the dataframe, and then applied unsupservised learning to the subset. Made color magnitude and distribution of RR Lyrae diagrams.
            -Required CSVs: variable_star_all_feat.csv
            -Output CSVs: None

        b. FSODO_fornax_queries: Queried the Forced Source on DiaObject catalog for all unflagged and low error observations for all diaObjects in the Fornax fitting certain variability requirements, calculated summary statistics for these values, and added them to the dataframe. Added labels to variable stars found in previous steps, filtered by number of observations in r and i b ands, applied data normalization, and performed PCA on a subset of columns within the dataframe, and then applied unsupservised learning to the subset. Made color magnitude and distribution of RR Lyrae diagrams.
            -Required CSVs: variable_star_all_feat.csv
            -Output CSVs: None
