#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np, pandas as pd, streamlit as st

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)