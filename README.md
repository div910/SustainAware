# SustainAware
## Let's EcoEngage Ourselves!

SustainAware is an AI-driven application designed to promote and encourage sustainable practices among individuals, communities, and industries. By leveraging artificial intelligence, personalized recommendations, and gamification elements, SustainAware aims to incentivize sustainable behavior and reduce ecological footprints.

### Features
- GreenScore: A GreenScore of every individual is calculated based on the sustainable practices they follow taken as user input in the website. This gamification elementis integrated into the website to motivate users and make the sustainability journey more enjoyable.
- Social Engagement: SustainAware provides a platform for users to share their sustainable activities and achievements with others in the form of blogs, fostering a sense of community and inspiration. Based on the response they get on their blog in the form of likes, they get points and their GreenScore increases. 
- Image Classification: People can upload the image of an item and 'Recycle Wizard' in the website would classify what type of recycle product the given item is.
- Marketplace section: SustainAware utilizes AI algorithms to provide users with tailored recommendations of the sustainable brands they can invest in based on their interests, location, and preferences.

In conclusion, SustainAware is a powerful and user-friendly website designed to promote sustainable practices and encourage individuals to make a positive impact on the environment. Together, we can make a positive impact on the environment and create a better world for generations to come. Join us on this journey and be part of the sustainability movement with SustainAware!

### Instuructions To Run Project

Run the below mentioned commands, make sure your system has docker installed in it

- sudo docker build -t sustainaware .
- sudo docker run -it --network=host sustainaware:latest /bin/bash
- /usr/local/python3.8/bin/python3.8 sustainaware_backend/manage.py runserver
