from select_file import *


if __name__ == "__main__":
   millisecond_duration = get_file_info(select_file())
   seconds_duration =  millisecond_duration /1000
   seconds = seconds_duration % 60
   minutes_duration = seconds_duration // 60

   print(f"{int(minutes_duration)}:{int(seconds)}")