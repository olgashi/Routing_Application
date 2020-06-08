import os
from daily_delivery import start_daily_delivery
from src.utils.user_interface import user_input
from src.utils.user_interface import display_package_details
from src.utils.time_utils import display_result_time_command


current_time, total_distance, packages_hash = start_daily_delivery()

print("Welcome to The Western Governors University Parcel Service delivery system")
print("Please use commands below to perform a specific action or search")


while True:
    command = user_input()
    if command.lower() == 'exit':
        exit()
    elif command.lower() == 'clear':
        os.system('cls' if os.name == 'nt' else 'clear')
    elif command.lower() == 'id':
        package_id = input('Please enter a package ID: ')
        display_package_details(package_id, packages_hash)
    elif command.lower() == 'time':
        provided_time = input('Please enter time in am/pm format, for example 8:25 AM: ')
        display_result_time_command(provided_time.strip(), packages_hash)
    elif command.lower() == 'distance':
        print("All packages were delivered with a total of " + total_distance + " miles")
    else:
        print("Unable to recognize the command. Please try again.")
