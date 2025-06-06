
---

### `rubin_tap_guide.py`

```python
"""
Rubin TAP + Python Utilities Guide
Author: McAelan Remigio
Based on original material by:** Leanne Guy, Melissa Graham
Last updated: June 6, 2025
Credit: This simplified guide is derived from the original Rubin Science Platform tutorial by Leanne Guy, created in the context of Rubin DP0.1. It aims to reduce complexity and improve clarity for new learners.\n",

This guide introduces the Rubin Science Platform TAP service through:
- ADQL querying (basic and aggregated)
- When to use search() vs submit_job()
- Basic matplotlib histograms
- NaN handling and pandas techniques

Target audience: Astronomy & data science learners with minimal programming experience.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colormaps
from lsst.rsp import get_tap_service

### TAP SERVICE CONNECTION
service = get_tap_service("ssotap")
assert service is not None

### SCHEMA INSPECTION
# Get column metadata from MPCORB table
results = service.search("""
SELECT column_name, datatype, description, unit 
FROM TAP_SCHEMA.columns 
WHERE table_name = 'dp03_catalogs_10yr.MPCORB'
""")
print(results.to_table().to_pandas())

### BASIC QUERY: Range of Object IDs
results = service.search("""
SELECT MIN(ssObjectId), MAX(ssObjectId) 
FROM dp03_catalogs_10yr.MPCORB
""")
print(results.to_table())

### AGGREGATION EXAMPLE
query = """
SELECT COUNT(*) AS total,
       MIN(a) AS min_a,
       MAX(a) AS max_a,
       AVG(e) AS avg_e
FROM dp03_catalogs_10yr.MPCORB
"""

# Recommended for large datasets
job = service.submit_job(query)
job.run()
job.wait(phases=['COMPLETED', 'ERROR'])
assert job.phase == 'COMPLETED'
df = job.fetch_result().to_table().to_pandas()
print(df)

### VISUALIZATION: Histogram of Orbital Elements
# Simulate structure for demo (in real use, you'd pull this from your query)
df = pd.DataFrame({'e': np.random.beta(2, 5, 10000)})

fig, ax = plt.subplots(2, 3, figsize=(10, 6), sharey=False)
ax[0, 0].hist(df['e'], bins=100, log=True)
ax[0, 0].set_xlabel('Eccentricity')
ax[0, 0].set_ylabel('log(Number)')
fig.suptitle('Histograms for Key Orbital Elements')
fig.tight_layout()
plt.show()

### DATA CLEANING: Handling NaNs
# Example: Assume we want to remove rows missing values in 'a' and 'e'
df_cleaned = df.dropna(subset=['e'])  # Copy version
df.dropna(subset=['e'], inplace=True) # In-place version

# Resetting index after row removal
df.reset_index(drop=True, inplace=True)

print('Number of rows after dropping NaNs:', len(df))
