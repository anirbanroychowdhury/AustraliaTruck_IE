# AustraliaTruck_IE

Problem Statement: We aim to create a product that can act as an early warning system in detecting fatigu/sleepiness. We will be acheiving this by using live video streaming over HTTPS and analyzing that video stream using OpenCV to detect changes in facial features. Examples of features that we will be looking for include yawning, number of eye blink per 24fps, etc. By using OpenCV's built in libraries for Harr Cascade we can easily build these feature detection. We are also assuming that each user will have a mobile phone with front facing camera at his disposal; preferably mounted on a mount at appropriate height level, for the camera to have a clear view of the users face. 

Tech Stack:

Django: We will be using django as our primary framework. Not only does it has an easy integration with web-developing technologies such as HTML5, CSS3, Javascipt and their associate farmeworks. It also remove a huge amount of developer burden during our backend developement phase; as a lot of the work is automated through built in features. An added bonus of using Django is that since OpenCV is primaraly a python library, we have native support and won't need to look for other solutions.

HTML5: A markup language used for structuring and presenting content on the World Wide Web. It is the fifth and last major HTML version that is a World Wide Web Consortium (W3C) recommendation. Will be used in our product to create the page structure for our webapp.

CSS3: It is a style sheet language used for describing the presentation of a document written in a markup language such as HTML. Through using CSS and HTML in tandem we can ensure that our webapp will be responsive on a multitude of devices.

JavaScript: It is a programming language that conforms to the ECMAScript specification. JavaScript is high-level, often just-in-time compiled, and multi-paradigm. It allows our webapp to be dynamic helping us add interactive elements to our webpage. 

OpenCV: It is a library of programming functions mainly aimed at real-time computer vision. Through using the built in functions we can quickly design a lot of the feature extractiona and analysis that is required for this project.
