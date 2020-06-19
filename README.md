# Numpy arrays and Pandas DataFrames to Igor Waves

This include a  package that is designed to convert Numpy arrays into Igor Waves:

**Package:**	igorwriter

**GitHub:**		[t-onoz/igorwriter](https://github.com/t-onoz/igorwriter)

## Installation

(Just run the next cell if you are on Mac in Jupyter Notebook)

```markdown
%pip install igorwriter
```
The package allows easy saving from Numpy arrays to Igor Waves.
Read literature in GitHub repository...

An __*.ibw*__ file is an Igor Wave (only one wave).

An __*.itx*__ file is a collection of Igor Waves.

I suggest using __*.itx*__ for saving full DataFrames

## Saving Pandas DataFrames

Extra function if you wane to save Pandas DataFrame as Igor Waves:

**Function:**	&emsp;save_pd( df [ , name = None , as_ibw = False] )

**Args:**
- df:	 Name of pd.DataFrame to be saved 
- name:   Name that you want to give the file and prefix of each wave name (default = None)
- as_ibw: If true the files are saved as_ibw if false files are saved as .itx (default = False)

The function can be found at: [pandas2Igor](https://github.com/GarethJMoore/Panads_to_Igor/blob/master/pandas2Igor.py)

It can simply be copied and run in notebook before saving a Pandas dataframe as Igor file.

## Example:

First import all packages needed.

```markdown
import numpy as np
import pandas as pd
from igorwriter import IgorWave5 
```
First we create a DataFrame with two columns.
```markdown
data = {'col1': [1, 2, 3, 4, 5, 6], 'col2': [3, 4, 5, 6, 7, 8]}
MyDataFrame = pd.DataFrame(data)
MyDataFrame.head()
```
To save it as one .itx file that contain both columns:
```markdown
save_pd(MyDataFrame, 'Sample1')
```
That when clicked on opens Igor and loads waves: Sample1_col1, Sample1_col2

To save two .ibw files:

Sample1_col1.ibw and Sample1_col2.ibw
```markdown
save_pd(MyDataFrame, 'Sample1', as_ibw = True)
```
