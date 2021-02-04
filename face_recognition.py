# Step 1: find the faces using the hogg method at the backend which is histogram
# of oriented gradients 
# Step 2: Once the bounding box where the face is present then we apply a word 
# because sometimes images maybe tilted and it is difficult to recognize 
# this kind of images. 
# Step 3: Then we use dlib lib. 
# Step 4: Once the face is centered then we will send this image to neural networks. That give us 
# the encoded features. (distance between eyes, eyes n nose, nose n lips)
# Step 5: Differentiate them to find the matches so to do that we can use SVM classifier, KNN, etc.. any classifier.

