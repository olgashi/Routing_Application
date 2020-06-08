import os
from daily_delivery import start_daily_delivery

current_time, total_distance, packages_hash = start_daily_delivery()

print("Welcome to The Western Governors University Parcel Service delivery system")
print("All packages were delivered with a total of " + total_distance + " miles")
print("Please use commands below to perform a specific action or search")

while True:
    command = input("""
    id - look up details for a specific package;
    time - display package status of all packages at a specific time (only accepts am/pm format, for example 8:25 am);
    distance - display total distance for all trucks;
    clear - clear screen;
    exit - to exit;\n >>>\t""")

    if command == 'exit':
        exit()
    elif command == 'clear':
        os.system('cls' if os.name == 'nt' else 'clear')
