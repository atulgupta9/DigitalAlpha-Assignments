import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split

spam_dataset = pd.read_csv(r"C:\Users\user\Python Programs\April16\spambase.data.csv")
x = spam_dataset.iloc[:,0:48]
y = spam_dataset.iloc[:,-1]

#splitting the dataset into training and testing
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=42)


x_train_0 = x_train[y_train == 0]
x_train_1 = x_train[y_train == 1]

feature_likelihoods_0 = np.mean(x_train_0,axis=0)/100.0

feature_likelihoods_1 = np.mean(x_train_1,axis=0)/100.0


num_ham_email = float(len(x_train_0))
num_spam_email = float(len(x_train_1))

prob_spam = num_ham_email/(num_ham_email +num_spam_email)
prob_ham = num_spam_email/(num_ham_email +num_spam_email)

log_prob_spam = np.log10(prob_spam)
log_prob_ham = np.log10(prob_ham)

def calculate_log_likelihoods_with_naive_bayes(feature_vector, Class):
    assert len(feature_vector) == 48
    log_likelihood = 0.0 #using log-likelihood to avoid underflow
    if Class==0:
        for feature_index in range(len(feature_vector)):
            if feature_vector[feature_index] == 1: #feature present
                log_likelihood += np.log10(feature_likelihoods_0[feature_index]) 
            elif feature_vector[feature_index] == 0: #feature absent
                log_likelihood += np.log10(1.0 - feature_likelihoods_0[feature_index])
    elif Class==1:
        for feature_index in range(len(feature_vector)):
            if feature_vector[feature_index] == 1: #feature present
                log_likelihood += np.log10(feature_likelihoods_1[feature_index]) 
            elif feature_vector[feature_index] == 0: #feature absent
                log_likelihood += np.log10(1.0 - feature_likelihoods_1[feature_index])
    else:
        raise ValueError("Class takes integer values 0 or 1")
        
    return log_likelihood

def calculate_class_posteriors(feature_vector):
    log_likelihood_class_0 = calculate_log_likelihoods_with_naive_bayes(feature_vector, Class=0)
    log_likelihood_class_1 = calculate_log_likelihoods_with_naive_bayes(feature_vector, Class=1)
    
    log_posterior_class_0 = log_likelihood_class_0 + log_prob_ham
    log_posterior_class_1 = log_likelihood_class_1 + log_prob_spam
    
    return log_posterior_class_0, log_posterior_class_1


def classify_spam(document_vector):
    feature_vector = [int(element>0.0) for element in document_vector]
    log_posterior_class_0, log_posterior_class_1 = calculate_class_posteriors(feature_vector)
    if log_posterior_class_0 > log_posterior_class_1:
        return 0
    else:
        return 1
    

#Predict spam or not on the test set
predictions = []
for email in np.array(x_test):
    predictions.append(classify_spam(email))
    
    

def evaluate_performance(predictions, ground_truth_labels):
    correct_count = 0.0
    for item_index in range(len(predictions)):
        if predictions[item_index] == ground_truth_labels[item_index]:
            correct_count += 1.0
    accuracy = correct_count/len(predictions)
    return accuracy

accuracy_of_naive_bayes = evaluate_performance(predictions, np.array(y_test))
print(accuracy_of_naive_bayes)



