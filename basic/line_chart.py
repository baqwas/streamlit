#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023-09-27 15:59:39
"""

import numpy as np, pandas as pd, streamlit as st

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
