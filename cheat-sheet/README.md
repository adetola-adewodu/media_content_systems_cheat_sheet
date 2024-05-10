# Media Contents Systems Cheat Sheet

We use the following tools to analyze/inspect video and audio: 
- FFMPEG (https://www.ffmpeg.org/): used to transcode and analyze audio and video
- MediaInfo (https://mediaarea.net/en/MediaInfo): Used to analyze audio and video
- Vidchecker: http://www.telestream.net/vidchecker/overview.htm
 
Video Encodings: 
- SD
- HD
- UHD
- 4k

The formats that we are usually convert to:
- DNX HD MXF
- XDCAM HD MXF
 
Preferred Frame Rates:
- 25, 50 for International
- 29.97, 59.94 for US
 
Types of Transcoding: 
- Transcode – Change from one video format to another (MXF to MXF is a basic transcode)
- Rewrap – Change a format from MOV/MXF to MXF (Usually from DNX HD MOV to DNX HD MXF)
- Standards Conversion – Convert from one frame rate to another frame rate
- Frame Rate Conversion
- 23 to 50 for International
- 59 to 50 for International
- 23 to 59 for US
- 50 to 59 for US
  
Frame Rate + Video Format Conversion
- 23 DNX HD MXF, XDCAM MXF to 59.94 XDCAM MXF 
- 50 DNX HD MXF, XDCAM MXF to 59.94 XDCAM MXF
- Time Compression - When you compress time in a video, you are making the duration shorter than real-time. 
- 30 seconds as a percentage of the video
- 45 seconds
- 60 seconds

 
Transcoding Tools: 
FFMPEG
- Create proxies
- Convert file to another format - Rewrap
- Create audio files from video files
- Create clips 
Vantage – Transcode and Rewrap
Amberfin Dark- Transcode and Rewrap
Adobe Media Encoder (Media Encoder) – Transcode and Rewrap
Radiant Grid/Wormhole – Standards Conversion and Time Compression
 
Also, here is an introduction to video engineering on github as well. 
 
https://github.com/adedot/digital_video_introduction
