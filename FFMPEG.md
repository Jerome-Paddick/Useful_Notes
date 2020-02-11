FFMPEG
---

    Video Transcoder

### Command Line

    -i          input
    -ss         timestamp
    -y          overwrites file
    -vframes    number of frames to copy
    -vf         video filter (fps=1/60)
    
Outputs Every 
ffmpeg -i rtp://@192.168.0.1:4321 -y -vf fps=1/60 "out.jpg" -hide_banner



ffmpeg -i rtp://@192.168.0.1:4321 -y -vframes 1 out.png
ffmpeg -i rtp://@192.168.0.1:4321 -y -vframes 1 out.png