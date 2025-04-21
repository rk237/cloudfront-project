# cloudfront-project
#this is a hands-on project implementing the concepts of content delivery network using cloudfront in aws. This project involves hosting a static website on s3 which contains a button to redirect to a to-do list application which hosted on ec2 instance.
Pre-requiste:
# Run below commands in your linux ec2 instance
sudo apt get update -y
pip install python3 -y
pip install python3-flask

# Step by Step instructions 

1. Create a s3 bucket with static website hosting enabled.
2. Go to cloudfront and create a new distribution
   a. Click on create distribution
   b. Fill up the details
     1. origin domain : select the s3 bucket where your index.html file for static content is kept
     2. Select Origin Access Type as Legacy Access setting or Origin Access Control Settings. I have selected Legacy access setting , created a new OAI and checked the option to update bucket policy. Leave the rest of settings as default. You can select the edge locations where you want the cdn to be accessible.
   3. Click on create distribution and your cloud front distribution with s3 as origin1 will be created.

3. Add ec2 as second origin in cloudfront
   a. ec2 instance should have a public ip
   b. Flask should be running on port 80
   c. Go to origins in cloudfront and click on "Add Origin"
   d. In Origin domain, paste your ec2 public dns i.e. "ec2-xx.xx.xx.xx.region.compute.amazonaws.com"
   e. Set the origin name as per your choice
   f. Keep the other values as default or you can configure your protocol as HTTP or HTTPS based on your ec2 app
   g. Click "Create Origin"

4. Add a behaior for  /todo
   a. Go to behaiors tab in cloudfront distribution -> Click "Create Behavior"
   b. Set : Path Pattern : /todo*
   c. Origin : Select the new ec2 origin created in previous step
   d. Viewer protocol policy : Redirect HTTP to HTTPS
   e. Aloowed Methods : GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE
   f. Enable caching based on cookies or headers if needed

5. Click "Create Behavior"
6. Now test your website once distribution is updated. It might take few minutes.
7. Copy the distribution domain name in your browser to check if it is accessible or not. You will get something like this
   <img width="292" alt="image" src="https://github.com/user-attachments/assets/a748cf36-134f-48a9-be53-31133c67dce2" />

8. Now click on "Go to To-Do List" and you will be redirected to your to-do list app hosted on your ec2 instance.
   <img width="307" alt="image" src="https://github.com/user-attachments/assets/6272e8ad-b6ce-4dc8-a59f-7b1568a3c79e" />


**INFRASTRUCTURE DIAGRAM **

![Infrastructure Diagram](https://github.com/user-attachments/assets/1ababd3a-eee6-4bb3-87ac-7960619c741c)



