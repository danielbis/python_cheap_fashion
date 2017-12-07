T$hirt README


Daniel Bis
Sam Maloney
Steven Centeno 




Overview:

We all aspire to look as fashionable and trendy as the celebrities dominating the media, however, very few of us have the funds to cover ourselves in the same over-priced designer couture they're sporting in the pictures. The goal of our Cheap Fashion application, is to provide our users with budget-friendly, look-alike alternatives to the name brand, or limited-edition clothing items that are simply unattainable for those of us without a seven-figure net worth. We've started by focusing on the artists' shirts, and designed a site where users are presented with a grid of nine fashionable male celebrities popular in todays culture, and upon selecting one of the celebrities, our site brings you to a new page, with three of the celebrities wearing different shirts which we have matches for. Upon selecting your favorite of the celebrity's shirt, you are provided with a series of close matches (along with their price, and a url where it can be directly purchased from), determined by machine learning and neural networking, sorted by how closely they match, with the closest match first.


Implementation: 

We used Google’s Inception v3 model (https://arxiv.org/pdf/1409.4842.pdf) to process the images and extract their features. Inception is designed to label images among 1000 categories. We used it, but instead of passing our input through the final layer, we extract the features from the last pooling layer (pool3:0). It gives us a 2048 dimensional vector of most signifiant features. After that we cluster the images into multidimensional space using K-Means Clustering and find the nearest neighbors, which are essentially our most similar pictures.  

After that we populated SQL with the data about the matches: prices, url, titles and paths to the jpeg files. We created a simple FLASK based web application that serves as a demo for our project. 

One of the challenges that we encountered was gathering the data, since we did not have any experience with web-scrapping and Machine Learning requires a large amount of data. Furthermore, data obtained varied in size and needed processing. Data processing appears to be a very important part of machine learning as we learnt that big variance in backgrounds and models wearing t-shirts affected our results, but more on that in the 'Room for improvement’ section. 

Changes to project - post status update 2:

Rather than picking the top-ten male billboard artists, it made more sense to hand-pick popular artists that are known for their sense of style. We've selected
   A$AP Rocky
   Chris Brown
   Jade Smith
   Jerry Lorenzo
   Justin Bieber
   Kanye West
   Russel Westbrook
   Travis Scott
   Vic Mensa

When pivoting to hand-picked artists, it also made more sense to select the photos of the artists and their shirts, rather than scraping their instagram pages and find matches for the three most recent photos of the artists wearing a shirt. By selecting out photos, we were able to improve the quality of the photos and attempt to get photos where the shirt is plainly visible and not obstructed by other elements in the photo's surrounding. In doing this, we are able to get results most similar to the original worn by the artist. 

Rather than sticking with a console-based application, we've decided to create an HTML-based graphical interface, in order tp improve user-friendliness




Websites Scraped for matches:

   Zappos
   Zummies
   Asos
   Shop.css
   Zalando




Room for improvement:

We are generally getting a low percentage of similarity between the original and the match results. This is primarily due to the fact that we did not train the machine learning program for t-shirts, but used pre-trained Inception v3 Architecture. Inception v3 was made by Google Research Team. It is designed to label pictures into one of thousand categories. Not specifically for comparing t-shirts. We could retrain the model, but that required much larger dataset that we did not have. 

Another way to improve the accuracy would be to use different, preferably smaller architecture, preferably using auto encoders, as latest research proves that these work very well in similar problems. 
We were unable to scrap enough images or find a useable data set. Additionally, the program is doing k-means clustering for the entire image, not just specifically the t-shirts in the photo. This is a result of the variation in background and context of the shirt from photos from various sources we scraped. 



Contributions:

T Shirt Scrapers
   Daniel Bis  
   Steven Centeno

Scrape output parsing
   Daniel Bis

Image Collection
   Daniel Bis
   Sam Maloney

Image resizing & Renaming
   Daniel Bis

T$hirt Web Application (Flask, SQLAlchemy, Jinja2 HTML templating) 
   Daniel Bis
   Sam Maloney
   
Clustering & Classifying Images
   Steven Centeno
   Daniel Bis

Status Reports & README
   Sam Maloney
   Daniel Bis



List of libraries used:

Scrapy
Annoy
nltk
Datetime
Keras
Absolute_import
Division
Print_function 
Os
Re
Sys
Json
Flask
Tarfile
Instagram_Scraper
Glob
Psutil
Defaultdict
Numpy
Urllib
Tensorflow
AnnoyIndex
Ngrams
Spatial
Codecs
Random

Sources:

http://douglasduhaime.com/posts/identifying-similar-images-with-tensorflow.html
https://www.tensorflow.org/tutorials/image_recognition
https://stackoverflow.com/questions/34809795/tensorflow-return-similar-images
Rethinking the Inception Architecture for Computer Vision, (Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jonathon Shlens, Zbigniew Wojna), https://arxiv.org/abs/1512.00567 
