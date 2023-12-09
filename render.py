import os
from lib.colab_util import generate_video_from_obj, set_renderer, video

def render(img, obj, video):

	renderer = set_renderer()
	generate_video_from_obj(obj, img, video, renderer)

if __name__ == "__main__":

	render("test.png", "test.obj", "result.mp4")

