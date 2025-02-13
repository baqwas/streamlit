#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023-09-26 15:19:19

Run with: streamlit run basic/table_create.py
"""
import streamlit as st, numpy as np, pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)
# AttributeError: 'AppSession' object has no attribute '_state'
# numpy basic
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

# pandas refinement
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

# static table
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)
