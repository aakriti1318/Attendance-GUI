## Face Recognition + Attendance System 
<p><b> OpenCV </b></p>
<br>
<h4> Steps to be followed for Face Recognition </h4>
<ul>
<li>
Find the faces using the hogg method at the backend which is histogram of oriented gradients 
</li>
<li>
Once the bounding box where the face is present then we apply a word because sometimes images maybe tilted and it is difficult to recognize this kind of images.
</li>
<li>
Then we use dlib lib. 
</li>
<li>
Once the face is centered then we will send this image to neural networks. That give us the encoded features. (distance between eyes, eyes n nose, nose n lips)
</li>
<li>
Differentiate them to find the matches so to do that we can use SVM classifier, KNN, etc.. any classifier.
</li>
</ul>

