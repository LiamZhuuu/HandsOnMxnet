import os

labels = open('ILSVRC2012_validation_ground_truth.txt', 'r')
imageList =  open('ILSVRC2012_validation_image_list.txt', 'w')

index = 1
for line in labels.readlines():
	label = int(line)
	image_path = 'ILSVRC2012_val_%08d.JPEG' % index
	imageList.write('%d\t%d\t%s\n' % (index, label, image_path))
	
	if index == 1000:
		break
	index += 1