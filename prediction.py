# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.


from recon import reconWrapper
import keypoint
import os

def prediction():

	# OPENPOSE 실행
	keypoint.prediction(img_path = "input/input.png",rect_path = "input/input_rect.txt")

	# PIFU HD 실행
	start_id = -1
	end_id = -1
	input_path = './input'
	out_path = './output'
	ckpt_path = './checkpoints/pifuhd.pt'
	resolution = '256'
	loadSize = '1024'

	cmd = ['--dataroot', input_path, '--results_path', out_path,\
			'--loadSize', loadSize, '--resolution', resolution, '--load_netMR_checkpoint_path', \
			ckpt_path,'--start_id', '%d' % start_id, '--end_id', '%d' % end_id]

	reconWrapper(cmd, True)
	#os.remove("input/input.png")
	#os.remove("input/input_rect.txt")

if __name__ == "__main__":

	prediction()



