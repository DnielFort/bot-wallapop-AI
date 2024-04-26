# bot-wallapop-AI
IMPLEMENTATION OF AI PART

Machine Learning Approach Implementation for Selecting the Best Vehicle Deals

Requirements:
1. Install the following libraries:
   - scikit-learn
   - pandas
   - matplotlib
   - seaborn
   - PyTorch

2. Given the size of the database used, it is advisable to use Google Collab (a cloud-based Python development environment that provides free access to hardware resources such as GPUs and TPUs, allowing for faster intensive computations than on a local machine, which is especially useful for training machine learning models in this project).

Goal:
Optimize vehicle search, integrating relevant information into the car selection system to enhance the notification of new offers previously developed.

It is anticipated to obtain an indicator based on the probability that the price of the vehicle belongs to the first quartile for its brand-vehicle-motorization group, meaning it is part of the cheapest 25% among all vehicles with similar features. To achieve this, a binary variable will be created that associates the value 1 with brand-vehicle-motorization groupings that are below the first quartile in price, and 0 with those above it.

Adding this indicator will allow the user to contextualize the offer they have been alerted to, enabling them to understand how it is priced relative to other offers for the vehicle in question, aiding in the decision of whether or not to engage with the vehicle link on Wallapop.

Phases of AI Implementation:
1. Introductory Framework: 
   - Context
   - Problem
   - Scope and limitations

2. Data
   - Metadata
   - Desired output identification: an indicator with categories from 0 to 10, created from the probability of belonging to the first quartile.

3. Preprocessing: 
   - Data quality improvement.
   - NA handling: random missing imputation using KNN (K-Nearest Neighbors) or MICE (Multiple Imputation by Chained Equations) methods.
   - Outliers handling
   - Feature selection using PCA (Principal Components Analysis)

4. Modeling
   - Split into train (2/3 of the data) and test (1/3).
   - Construction of models: using XGBoost and Random Forest
   - Strategies: data balancing, avoiding overfitting, hyperparameter tuning
   - Model validation
5. Benchmarking: comparative table of metrics: Accuracy, precision, recall, F1, and confusion matrix to select the best-performing model. 
6. Production of the winning model.

Other interesting aspects to determine:

It is worth assessing the utility of using classic unsupervised clustering algorithms (to be determined between K-means or Hierarchical) or advanced clustering (Dbscan or Optics). The idea is to create groups with vehicle characteristics, possibly adding to the Wallapop link of the vehicle and its score from 1 to 10, the cluster it belongs to, adding to the text of the Telegram chat the profiling of the clusters (what characteristics define each group). This addition would provide more information to the user about the type of vehicle in question.



----------
# Tasks: 
API
- [x] Given a new wallapop link, create a new csv file for each product, and if it exists, go to search the file
- [x] Change params.txt .env
- [x] Fix the bug that if there are no elements, it does not crash
- [x] Insert ad limiter in the .env (not yet implemented in the code)
- [x] Set in the .env the time it takes to search for the elements
- [x] When there are no products with that name, send a message notifying the user and delete the previously created csv
- [x] Optimize where to put the driver.quit()
- [x] Optimize the sleeps of the animations in open_web
----------
PART IN CHARGE OF MANAGING THE BOT
- [x] Create a new project independent from the API to control the behavior of the bot
- [x] Create a folder for each new user, with their chatid as the title. Check new users
- [x] Automatically create a links file in each user's folder so that each user can store their links
- [x] Automate the csv file creation system for each user, the files will be stored in their respective folder
- [x] Add a set of instructions
- [x] Set a password for new users
- [x] CURRENT Filter all folder names in users (chatid of each user) and save them as authorized users so they do not have to enter the password with each reset
- [ ] Set up a trial
- [ ] Be able to omit ads from certain users or certain titles
----------
API MODIFICATIONS TO WORK TOGETHER WITH THE BOT
- [x] Modify the main loop to execute buscar_productos() from all the links of all users.
- [x] Edit the csv generation system so that it creates the files in the folder of each user.
- [x] Establish that the first time the products are added to the csv, the user is not notified to avoid flood.
----------
