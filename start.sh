#!/bin/bash
port=${PORT:-8501}
streamlit run dashboard.py --server.port $port --server.address 0.0.0.0
