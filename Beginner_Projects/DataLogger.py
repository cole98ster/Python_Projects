print ('Data Logger - Time, Distance, Speed')

print("Do you have an existing file containing time and distance data? (Y/N)")
response = input().strip().lower()

# prepare lists
time = []
distance = []

if response == 'y':
    filename = input("Enter the filename (with extension like data_log.csv): ").strip()
    import csv
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if not row:
                    continue
                
                row = [cell.strip() for cell in row]
                try:
                    t = int(row[0])
                    d = float(row[1])
                except (ValueError, IndexError):
                    continue
                time.append(t)
                distance.append(d)
        nums_data_points = len(time)
        if nums_data_points == 0:
            print(f"No valid data rows found in {filename}. Please check the file format.")
            exit()
        print(f"Loaded {nums_data_points} data points from {filename}.")
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
        exit()

else:
    try:
        nums_data_points = int(input("How many data points do you want to log?").strip())
        if nums_data_points <= 0:
            print("Please enter a positive integer for data points.")
            exit()
    except ValueError:
        print("Please enter a valid integer for number of data points.")
        exit()

    for i in range(nums_data_points):
        try:
            t = int(input("Enter the time duration for running data in seconds: ").strip())
            d = float(input("Enter the distance in meters: ").strip())
        except ValueError:
            print("Please enter valid numeric values for time and distance.")
            exit()
        time.append(t)
        distance.append(d)


outputfilename = input("Enter the filename to save the data to (e.g., data_log): ").strip()
if not outputfilename.lower().endswith('.csv'):
    outputfilename += ".csv"
min_distance = float('inf')
max_distance = float('-inf') 
min_speed = float('inf')
max_speed = float('-inf') 
average_distance = 0
average_speed = 0
average_time = 0
try:
    for i in range (nums_data_points):
        time_val = int(time[i])
        distance_val = float(distance[i])
        speed = distance_val / time_val if time_val > 0 else 0
        average_speed += speed
        average_distance += distance_val
        average_time += time_val
        if distance_val < min_distance:
            min_distance = distance_val
        if distance_val > max_distance:
            max_distance = distance_val
        if speed < min_speed:
            min_speed = speed
        if speed > max_speed:
            max_speed = speed
        print(f"Data Point {i+1}: Time = {time_val} s, Distance = {distance_val} m, Speed = {speed:.2f} m/s")
    average_distance /= nums_data_points
    average_speed /= nums_data_points
    average_time /= nums_data_points
    
    
    with open (outputfilename, 'w') as file:
        file.write("Data Point,Time (s),Distance (m),Speed (m/s)\n")
        for i in range(nums_data_points):
            speed = distance[i] / time[i] if time[i] > 0 else 0
            file.write(f"{i+1},{time[i]},{distance[i]},{speed:.2f}\n")
        file.write(f"\nMin Distance (m),{min_distance}\n")
        file.write(f"Max Distance (m),{max_distance}\n")
        file.write(f"Average Time (s),{average_time}\n")
        file.write(f"Average Distance (m),{average_distance}\n")
        file.write(f"Min Speed (m/s),{min_speed}\n")
        file.write(f"Max Speed (m/s),{max_speed}\n")
        file.write(f"Average Speed (m/s),{average_speed}\n")
    
        
        
        

    
except ValueError:
    print("Please enter valid numeric values for time and distance.")
