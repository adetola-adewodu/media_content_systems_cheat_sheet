import ffmpeg


# create clip
(
    ffmpeg
    .input('*.jpg', pattern_type='glob', vsync='vfr', pix_fmt='yuv420p')
    # .filter('scale', size='hd1080', force_original_aspect_ratio='increase')
    .output('new-movie-1.mp4')
    .overwrite_output()
    .run()
)