from sklearn.svm import SVC
# Binary Relevance
from sklearn.multiclass import OneVsRestClassifier
from sklearn.neighbors import KNeighborsClassifier
# Performance metric
from sklearn.metrics import f1_score
import pickle
from xgboost import XGBClassifier
from sklearn.linear_model import SGDClassifier

from trainModel import Model

model = Model()

def health(xtrain, xtest, ytrain, ytest, folder_name, category):
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(estimator=XGBClassifier(gamma =0.2,max_depth = 4,min_child_weight=1,learning_rate=0.05,eval_metric='mlogloss',use_label_encoder =False))
    # classifier.fit(xtrain_tfidf, ytrain)
    # svc = SVC( kernel='rbf', C=1e9, gamma=1e-07)
    # svc = KNeighborsClassifier(n_neighbors = 5, weights = 'distance',algorithm = 'brute',metric = 'minkowski')
    # svm_clf = OneVsRestClassifier(svc)
    classifier.fit(xtrain, ytrain)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))
    loaded_model = pickle.load(open(filename, 'rb'))

    print("################## Making prediction #################\n")
    svm_pred = classifier.predict(xtest)
    # evaluate performance
    print(f1_score(ytest, svm_pred, average="micro"))


def modelHealth():
    # preprocess text 
    xtrain, xtest, ytrain, ytest , category = model.readAndProcessData("Healthcare.csv", 
                                                                        "healthcare")

    health(xtrain, xtest, ytrain, ytest, category, category)


def computer(xtrain, xtest, ytrain, ytest, folder_name, category):
    
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(estimator=SGDClassifier(eta0 = 100, loss = 'modified_huber', penalty = 'l1'))
    classifier.fit(xtrain, ytrain)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))
    loaded_model = pickle.load(open(filename, 'rb'))

    print("################## Making prediction #################\n")
    sgd_pred = classifier.predict(xtest)
    # evaluate performance
    print(f1_score(ytest, sgd_pred, average="micro"))


def modelComputer():
    # preprocess text 
    xtrain, xtest, ytrain, ytest , category = model.readAndProcessData("computer_and_it.csv", 
                                                                        "computer_and_it")

    computer(xtrain, xtest, ytrain, ytest, category, category)


def education(xtrain, xtest, ytrain, ytest, folder_name, category):
    
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(estimator=SGDClassifier(eta0 = 1, loss = 'hinge', penalty = 'l1'))
    classifier.fit(xtrain, ytrain)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))
    loaded_model = pickle.load(open(filename, 'rb'))

    print("################## Making prediction #################\n")
    sgd_pred = classifier.predict(xtest)
    # evaluate performance
    print(f1_score(ytest, sgd_pred, average="micro"))


def modelEducation():
    # preprocess text 
    xtrain, xtest, ytrain, ytest , category = model.readAndProcessData("Education.csv", 
                                                                        "education")

    computer(xtrain, xtest, ytrain, ytest, category, category)  
    
    
def sales(xtrain, xtest, ytrain, ytest, folder_name, category):
    print("################## Model building started #################\n")
    xgb1 = xgb.XGBClassifier()
    xgb_clf = OneVsRestClassifier(xgb1)
    xgb_clf.fit(xtrain, ytrain)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(xgb_clf, open(f'models/{folder_name}/{category}.sav', 'wb'))
    loaded_model = pickle.load(open(filename, 'rb'))

    print("################## Making prediction #################\n")
    svm_pred = xgb_clf.predict(xtest)
    # evaluate performance
    print(f1_score(ytest, svm_pred, average="micro"))
    
def sales_and_retail():
    # preprocess text 
    xtrain, xtest, ytrain, ytest , category = model.readAndProcessData("sales_and_retail.csv", 
                                                                        "sales_and_retail")

    sales(xtrain, xtest, ytrain, ytest, category, category)

def cleaning_facility(xtrain, xtest, ytrain, ytest, folder_name, category):
    print("################## Model building started #################\n")
    classifier = KNeighborsClassifier(n_neighbors = 5, weights = 'distance',algorithm = 'brute',metric = 'minkowski')

    classifier.fit(xtrain, ytrain)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))
    loaded_model = pickle.load(open(filename, 'rb'))

    print("################## Making prediction #################\n")
    svm_pred = classifier.predict(xtest)
    # evaluate performance
    print(f1_score(ytest, svm_pred, average="micro"))
        


def modelcleaning_facility():
    # preprocess text 
    xtrain, xtest, ytrain, ytest , category = model.readAndProcessData("cleaning_and_facilities.csv", 
                                                                        "cleaning_and_facilities")

    cleaning_facility(xtrain, xtest, ytrain, ytest, category, category)
modelEducation()

modelcleaning_facility()
