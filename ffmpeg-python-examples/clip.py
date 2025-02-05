import ffmpeg

input_file = 'zionmixtape.mp4'

# create clip
(
    ffmpeg
    .input(input_file,  ss='00:00:03.0', t='00:00:06.0')
    .output('zioclip.mp4')
    .overwrite_output()
    .run()
)

# Create images 
(
    ffmpeg
    .input(input_file)
    .filter('fps', fps='1/5')
    .output('zioclip-%03d.jpg')
    .overwrite_output()
    .run()
)