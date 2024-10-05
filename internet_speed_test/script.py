import speedtest  

st = speedtest.Speedtest()  
st.get_best_server()  
download_speed = st.download() / 1_000_000  # Convert to Mbps  
upload_speed = st.upload() / 1_000_000  # Convert to Mbps  

print(f"Download speed: {download_speed:.2f} Mbps")  
print(f"Upload speed: {upload_speed:.2f} Mbps")