
import pandas as pd

# Define required columns and platform-specific rules
REQUIRED_COLUMNS = ['Asset ID', 'Title', 'Platform', 'Delivery Date', 'Runtime', 'Resolution']
PLATFORM_RULES = {
    'Netflix': {'Resolution': ['1920x1080', '3840x2160'], 'Runtime_min': 90},
    'Hulu': {'Resolution': ['1280x720', '1920x1080'], 'Runtime_min': 60}
}

def load_data(file_path):
    return pd.read_csv(file_path)

def check_required_columns(df):
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    return missing

def run_qc_checks(df):
    issues = []

    for index, row in df.iterrows():
        platform = row.get('Platform')
        rules = PLATFORM_RULES.get(platform, {})
        resolution_ok = row.get('Resolution') in rules.get('Resolution', [])
        runtime_ok = row.get('Runtime', 0) >= rules.get('Runtime_min', 0)

        if not resolution_ok:
            issues.append(f"Row {index}: Bad resolution '{row.get('Resolution')}' for {platform}")
        if not runtime_ok:
            issues.append(f"Row {index}: Runtime too short ({row.get('Runtime')} min) for {platform}")

    return issues

def main():
    file_path = 'data/sample_asset_report.csv'
    df = load_data(file_path)

    missing = check_required_columns(df)
    if missing:
        print(f"Missing columns: {missing}")
        return

    issues = run_qc_checks(df)
    if issues:
        print("QC Issues found:")
        for issue in issues:
            print(issue)
    else:
        print("No QC issues found.")

if __name__ == '__main__':
    main()
