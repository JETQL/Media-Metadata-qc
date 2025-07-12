![Project Banner](https://github.com/JETQL/Media-Metadata-qc/raw/main/Media_Metadata_Banner.png)
# Media Metadata QC and Delivery Performance Dashboard

This project includes:
1. A Python script for **batch quality control (QC)** of asset metadata.
2. A Jupyter Notebook that **visualizes delivery performance** by platform.

## 🔍 QC Script (`qc_script.py`)
- Checks for required fields
- Flags resolution or runtime errors based on delivery platform

## 📊 Dashboard (`visualization.ipynb`)
- Platform-level delivery counts
- Average runtimes
- On-time delivery rates

## 📂 Sample Data
Place data in `data/sample_asset_report.csv` with the following columns:
- `Asset ID`, `Title`, `Platform`, `Delivery Date`, `Runtime`, `Resolution`

## ✅ Setup
```bash
pip install -r requirements.txt
python qc_script.py
```

Then open the Jupyter Notebook to view visualizations.

---

## 🧠 How It Works
- Uses `pandas` to automate QC from delivery reports
- Platform-specific resolution/runtime checks
- Built with easy-to-read visuals using `matplotlib`
