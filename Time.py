import time

current_time = time.strftime("%H:%M:%S")
print(current_time)
if(current_time >= "06:00:00" and current_time <= "12:00:00"):
 print("Good morning")
elif(current_time >= "12:00:00" and current_time <= "18:00:00"):
 print("Good afternoon")
elif(current_time >= "18:00:00" and current_time <= "24:00:00"):
 print("Good evening")
