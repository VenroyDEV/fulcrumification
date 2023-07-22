import audio 
import select_file_tk
def readable_format():
   millisecond_duration = select_file_tk.get_file_info(select_file_tk.select_file())
   seconds_duration =  millisecond_duration /1000
   seconds = seconds_duration % 60
   minutes_duration = seconds_duration // 60

   print(f"{int(minutes_duration)}:{int(seconds)}")  

if __name__ == "__main__":
   audio.process_video()