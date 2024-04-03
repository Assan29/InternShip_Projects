from flask import Flask, render_template, request
import joblib
import os
import sklearn

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prediction', methods=['POST'])
def pred():
    review = request.form.get('review')
    data_point = str(review)

    # Load the model
    model = joblib.load(r'logistic_regression_sentiment_analysis_model_balanced.pkl')

    # Perform prediction
    prediction = model.predict([data_point])[0]
    
    # Determine sentiment
    sentiment = 'Negative' if prediction == 0 else 'Positive'
    
    return render_template('output.html', prediction=sentiment, review=review, sentiment=sentiment)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
