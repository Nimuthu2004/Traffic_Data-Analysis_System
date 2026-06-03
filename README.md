```markdown
# Traffic Data Analysis System

## Overview

This Python-based traffic data analysis tool processes vehicle survey data from multiple CSV files. The system analyzes traffic patterns at two major junctions, computes key statistics, and generates comprehensive reports.

## Author

- **Name:** W.M.Nimuthu Lakdina Fernando
- **Student ID:** 2119779
- **Date:** 2024/12/09

## Project Structure

```
```
.
├── Coursework Code.py
├── Pseudocode.docx
├── result.txt
├── Test results.pdf
├── traffic_data15062024.csv
├── traffic_data16062024.csv
└── traffic_data21062024.csv

```
```

## Features

The program analyzes traffic data and calculates:

- Total vehicle count for each date
- Truck count and percentage of total vehicles
- Electric vehicle count
- Two-wheeled vehicles (Bicycles, Motorcycles, Scooters)
- Northbound buses leaving Elm Avenue/Rabbit Road junction
- Straight-through vehicles (not turning left or right)
- Average bikes per hour
- Speed limit violations
- Vehicle distribution between both junctions
- Scooter percentage at Elm Avenue/Rabbit Road
- Peak traffic hour at Hanley Highway/Westway
- Rain hour count (Light Rain or Heavy Rain conditions)

## Data Format

The CSV files contain the following columns:

| Column | Description |
|--------|-------------|
| JunctionName | Junction location (Elm Avenue/Rabbit Road or Hanley Highway/Westway) |
| Date | Survey date (DD/MM/YYYY) |
| timeOfDay | Time of vehicle passage (HH:MM:SS) |
| travel_Direction_in | Incoming direction |
| travel_Direction_out | Outgoing direction |
| Weather_Conditions | Weather at time of recording |
| JunctionSpeedLimit | Speed limit at junction |
| VehicleSpeed | Recorded vehicle speed |
| VehicleType | Type of vehicle |
| elctricHybrid | Electric/Hybrid status (True/False) |

## How to Use

### Prerequisites
- Python 3.x installed
- CSV files in the same directory as the script

### Running the Program

1. Execute the script:
   ```bash
   python "Coursework Code.py"
   ```

2. Enter the survey date when prompted:
   - Day (dd): 1-31
   - Month (MM): 1-12
   - Year (YYYY): 2000-2024

3. View results displayed in the console

4. Results are automatically saved to `result.txt`

5. To analyze another dataset:
   - Type `Y` (Yes) to continue
   - Type `N` (No) to exit

## Sample Output

```
Data file selected is traffic_data15062024.csv
The total number of vehicles recorded for this date is 1037
The total number of trucks recorded for this date is 109
The total number of electric vehicles for this date is 368
The total number of two-wheeled vehicles for this date is 401
The total number of Busses leaving Elm Avenue/Rabbit Road heading North is 15
The total number of Vehicles through both junctions not turning left or right is 363
The percentage of total vehicles recorded that are trucks for this date is 11%
The average number of Bikes per hour for this date is 7
The total number of Vehicles recorded as over the speed limit for this date is 205
The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is 494
The total number of vehicles recorded through Hanley Highway/Westway junction is 543
11% of vehicles recorded through Elm Avenue/Rabbit Road are scooters
The highest number of vehicles in an hour on Hanley Highway/Westway is 39
The most vehicles through Hanley Highway/Westway were recorded between 18:00 and 19:00
The number of hours of rain for this date is 0
```

## Output File

All results are appended to `result.txt` with each analysis separated by asterisk borders for easy reading.

## Error Handling

- **Input validation:** Ensures dates are within valid ranges and integers are entered
- **File not found:** Handles missing CSV files gracefully with error messages
- **Data type conversion:** Handles potential errors when converting speed values

## Notes

- The script expects CSV files named in the format `traffic_dataDDMMYYYY.csv`
- Vehicle counts exclude header rows
- Rain hours count both "Light Rain" and "Heavy Rain" conditions
- Peak hour analysis is performed specifically for Hanley Highway/Westway junction

## License

This project was developed as part of academic coursework.
