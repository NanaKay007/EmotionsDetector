# emoman
am emo

Hey everyone! I'm Navdeep, and I hope you all are doing well! In my life, I have noticed some people have hard times reading emotions in all sorts of places. Some have a hard time with reading body language, and some have a hard time reading language in texts. This project is meant to solve the latter of the two, since facial recognition is much more of a reality than it seems alternative resources. It seems like there is not enough research on text-based emotions, weirdly enough.

I know that some students with autism have a hard time expressing emotions and/or detecting them. This project can help those students slowly condition themselves to understand what "standard responses" to certain emotions can be or look like.

To run this, you really only need one of the nn-...h5 (probably pick the most-recent one) files, the out.csv file, and the simpleModel.py file. You may need to install some packages here and there, but once you have those, you're set!

Thanks for checking this out :)

List of emotions (new classification scheme):

negative (17,703) Positive (13,569) neutral (7,978) List of emotions (old classification scheme):

worry (9438) neutral (7978) happiness (5860) sadness (5841) love (3734) surprise (2134) fun (1749) relief (1489) hate (1300) anger (947) empty (758) enthusiasm (737) boredom (177)

SUBMISSION README:

Team Name emomen Team Members - All Swarthmore College Navdeep Maini Xihao Luo Nana Kweku Anikuabe Bill Dengler

Project Description See above :)

Protoype Summary We were able to create a model using keras and sci-kit learn in-order to classify multiple phrases/sentences. Our model does not do the "easier" thing and stick to simpler classifications such as, "positive, neutral, and negative." Our model tries to solve a harder problem. It is not perfect, but it does predict some phrases correctly :) The back-end for this project is in Flask, and the front-end makes use of Ajax/JQuery. One of our biggest problems was trying to get past CORS/cross-scripting requests, but Ajax/JQuery saved the day!

Live URLs superIndex.html

Presentation Stay tuned to our presentation!

Next Steps It is already working quite a bit! But, something that would strengthen our model is to train it on even more data with more emotion/sentiment labels. This would lead to a more robust model that consists of numerous words.

License This repository includes an unlicense statement though you may want to choose a different license.
