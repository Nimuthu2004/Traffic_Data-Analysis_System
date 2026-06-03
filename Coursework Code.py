
#Author:     W.M.Nimuthu Lakdina Fernando
#Date:       2024/12/09
#Student ID: 2119779

#Input Validation
def date_input(promt,x,y) :   
  while True :
    try :
        value = int(input(promt))
        if value < x or value > y :
            print(f"Out of range - values must be in the range {x} and {y}.")
        else :
            print("")
            return value
        
    except :
        print("Integer required")

#define file save 
def save_results_to_file(file_name, vehicle_count, truck_count, electric_count, 
                                     twowheeled_count, bus_north, straight_run, truck_ave, bike_ave, 
                                     speedlimit_pass, rabbtiroad_count, westwayroad_count, scooter_ave, max_coun,
                         peak_hour_message, rain_count):

    #file open and assign
    with open(file_name, 'a') as file:
        file.write(f"""
            Data file selected is {f"traffic_data{day:02}{month:02}{year}.csv"}
            The total number of vehicles recorded for this date is {vehicle_count-1}
            The total number of trucks recorded for this date is {truck_count}
            The total number of electric vehicles for this date is {electric_count}
            The total number of two-wheeled vehicles for this date is {twowheeled_count}
            The total number of Busses leaving Elm Avenue/Rabbit Road heading North is {bus_north}
            The total number of Vehicles through both junctions not turning left or right is {straight_run}
            The percentage of total vehicles recorded that are trucks for this date is {truck_ave}%
            The average number of Bikes per hour for this date is {bike_ave}
            The total number of Vehicles recorded as over the speed limit for this date is {speedlimit_pass}
            The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {rabbtiroad_count}
            The total number of vehicles recorded through Hanley Highway/Westway junction is {westwayroad_count}
            {scooter_ave}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters
            The highest number of vehicles in an hour on Hanley Highway/Westway is {max_count}
            The most vehicles through Hanley Highway/Westway were recorded between {peak_hour_message}
            The number of hours of rain for this date is {rain_count}
            
            *************************** 
        """)


#arguments of date_input()
Date = {}  
while True:
    
    day = date_input("\nPlease enter the day of the survey in the format dd: ",1,31)
    month = date_input("Please enter the month of the survey in the format MM: ",1,12)
    year = date_input("Please enter the year of the survey in the format YYYY: ",2000,2024)

    
    date = (day,month,year)
    Date["input"] = date 


#Processed Outcomes
    import csv
    for key, date in Date.items():
        file_name = f"traffic_data{day:02}{month:02}{year}.csv"
        
        try:
            with open(file_name, "r") as file:
                print("\n***************************")
                print(f"Data file selected is {file_name}:")
                print("***************************")

                csv_reader = csv.reader(file)
                rows = list(csv_reader)

                # Logic for processing data
                
                vehicle_count = len(rows)  
                print(f"\nThe total number of vehicles recorded for this date is {vehicle_count-1}")

                truck_count = 0
                for row in rows:
                    
                    if row[8] == "Truck":  
                        truck_count += 1

                print(f"The total number of trucks recorded for this date is {truck_count}.")

                electric_count = 0
                for row in rows:
                    
                    if row[9] == "True":  
                        electric_count += 1

                print(f"The total number of electric vehicles for this date is {electric_count}.")

                twowheeled_count = 0
                for row in rows:
                    
                    if row[8] in ("Bicycle", "Motorcycle", "Scooter"):
                        twowheeled_count += 1

                print(f"The total number of two-wheeled vehicles for this date is {twowheeled_count}.")


                bus_north = 0
                for row in rows:
                    
                    if row[0] == "Elm Avenue/Rabbit Road" and row[4] == "N" and row[8] == "Buss":  
                        bus_north += 1

                print(f"The total number of Busses leaving Elm Avenue/Rabbit Road heading North is {bus_north}.")


                straight_run = 0
                for row in rows:
                    if row[3] == row[4] :
                        straight_run += 1

                print(f"The total number of Vehicles through both junctions not turning left or right is {straight_run}")

                
                truck_ave = truck_count/vehicle_count*100
                truck_ave = round(truck_ave)
                print(f"The total number of electric vehicles for this date is {truck_ave}%.")



                bike_count = 0
                for row in rows:
                    
                    if row[8] == "Bicycle" :
                        bike_count += 1
                        
                bike_ave = bike_count / 24
                bike_ave = round(bike_ave)
                print(f"the average number of Bikes per hour for this date is {bike_ave}.")


                speedlimit_pass = 0
                for row in rows:
                    try:
                        speed_limit = float(row[6])
                        recorded_speed = float(row[7])
                        
                        if recorded_speed > speed_limit:
                            speedlimit_pass += 1
                    except :
                        continue
                print(f"\nThe total number of Vehicles recorded as over the speed limit for this date is {speedlimit_pass}.")


                rabbtiroad_count = 0
                for row in rows:
                    if row[0] == "Elm Avenue/Rabbit Road":
                        rabbtiroad_count += 1

                print(f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {rabbtiroad_count}.")

                westwayroad_count = 0
                for row in rows:
                    if row[0] == "Hanley Highway/Westway":
                        westwayroad_count += 1

                print(f"The total number of vehicles recorded through Hanley Highway/Westway junction is {westwayroad_count}.")


                scooter_count = 0
                for row in rows:
                    if row[0] == "Elm Avenue/Rabbit Road" and row[8] == "Scooter" :
                        scooter_count += 1
                scooter_ave =  scooter_count / rabbtiroad_count * 100
                scooter_ave = round(scooter_ave)
                print(f"{scooter_ave}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.")


                hourly_westwayroad_count = {}  
                for row in rows: 
                    if row[0] == "Hanley Highway/Westway":
                        time = row[2].split(":")[0] 
                        hourly_westwayroad_count[time] = hourly_westwayroad_count.get(time, 0) + 1


                max_hour = max(hourly_westwayroad_count, key=hourly_westwayroad_count.get)
                max_count = hourly_westwayroad_count[max_hour]
                print(f"\nThe highest number of vehicles in an hour on Hanley Highway/Westway is {max_count}.")


                peak_hour_count = max(hourly_westwayroad_count.values(), default=0)
                peak_hours = [hour for hour, count in hourly_westwayroad_count.items() if count == peak_hour_count]
                peak_hour_message = f"Between {peak_hours[0]}:00 and {int(peak_hours[0]) + 1}:00"
                print(f"The most vehicles through Hanley Highway/Westway were recorded between {peak_hour_message}.")

                 
                rain_count = 0
                for row in rows:
                    if row[5] in ("Light Rain","Heavy Rain") :
                        rain_count += 1
                print(f"The number of hours of rain for this date is {rain_count}.")


                # Save results to the file
                save_results_to_file("result.txt", vehicle_count, truck_count, electric_count, 
                                     twowheeled_count, bus_north, straight_run, truck_ave, bike_ave, 
                                     speedlimit_pass, rabbtiroad_count, westwayroad_count, scooter_ave, max_count,
                                     peak_hour_message, rain_count)                




        except FileNotFoundError :
            print(f"\nFile {file_name} does not exist.")

#Validation logic

    choice = input("\nTo load another dataset:\nYes : type 'Y'\nNo  : type 'N'\nchoice : ")
    
    if choice.upper().strip() == 'N':  
        print("End of run.")
        break
    elif choice.upper().strip() != 'Y': 
        print("Invalid choice.End of run.")
        break


        







