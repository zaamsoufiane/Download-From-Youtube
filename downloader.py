from pytube import YouTube
import os
y = input('Enter the link of the video \n')
try :
    yt = YouTube(y)
except:
    print('good bye')
    exit()
forma = input('1- For Video || 2- For MP3 \n')

if forma == '1':
    
    
 
    

    try:
        video = yt.streams.get_highest_resolution().download("E:\Python\Download videos & mp4\downloads")
        
        print('success')
        
    except:
        print('error')
        exit()

elif forma == '2':
    try:
        audio = yt.streams.filter(only_audio=True).first()
       
        out_file = audio.download(output_path="E:\Python\Download videos & mp4\music")
  
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print('success')
    except:
        print('error')
        exit()
else : 
    print('good by')
