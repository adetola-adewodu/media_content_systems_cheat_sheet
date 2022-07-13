Contents Systems Cheat Sheet

We use the following tools to Analyze video and audio: 
•      FFMPEG (https://www.ffmpeg.org/)
o   used to transcode and analyze audio and video
o   https://github.com/FFmpeg/FFmpeg
•      MediaInfo (https://mediaarea.net/en/MediaInfo)
o   Used to analyze audio and video
o   https://github.com/MediaArea/MediaInfo 
•      Vidchecker
 
The formats that we are usually convert to:
•      DNX HD MXF (DCTC)
•      XDCAM HD MXF (DKNOX)
 
Preferred Frame Rates:
25, 50 for International
29.97, 59.94 for US
 
Types of Transcoding: 
•      Transcode – Change from one video format to another (MXF to MXF is a basic transcode)
•      Rewrap – Change a format from MOV/MXF to MXF (Usually from DNX HD MOV to DNX HD MXF)
•      Standards Conversion – Convert from one frame rate to another frame rate
o   Frame Rate Conversion
  23 to 50 for International
  59 to 50 for International
  23 to 59 for US
  50 to 59 for US
o   Frame Rate + Video Format Conversion
•      23 DNX HD MXF, XDCAM MXF to 59.94 XDCAM MXF 
•      50 DNX HD MXF, XDCAM MXF to 59.94 XDCAM MXF
•      Time Compression - When you compress time in a video, you are making the duration shorter than real-time. 
o   30 seconds as a percentage of the video
o   45 seconds
o   60 seconds
  Do not compress 
  Compress segments
 
Transcoding Tools: 
•      FFMPEG
o   Create proxies
o   Convert file to another format - Rewrap
o   Create audio files from video files
o   Create clips 
•      Vantage – Transcode and Rewrap
•      Amberfin Dark- Transcode and Rewrap
•      Adobe Media Encoder (Media Encoder) – Transcode and Rewrap
•      Radiant Grid/Wormhole – Standards Conversion and Time Compression
 
Also, here is an introduction to video engineering on github as well. 
 
https://github.com/adedot/digital_video_introduction
