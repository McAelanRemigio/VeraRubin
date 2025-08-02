Applying supervised learning and data visualization to better understand what features are most likely to be helpful for later unsupervised classification

        a. (Python Notebook) SupervisedLearningPipeline: Retrieved other columns from diaObject that are useful for classification for matched objects mentioned above (color, amplitude, etc), filtered by number of obversations, and saved results to csv. Also plotted color magnitude diagram and attempted supervised learning with random forest
            -Required CSVs: diaobject_matched_final.csv
            -Output CSVs: variablestar_filtered.csv, variable_star_all_feat.csv

        b. (Python Notebook) FeatureVisualization: to understand distribution (skew, outliers, etc) we made boxplots of all of our features of interest
            -Required CSVs: variablestar_filtered.csv
            -Output CSVs: None
