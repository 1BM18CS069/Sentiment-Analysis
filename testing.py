from textblob import TextBlob
testingsent=input( "Enter your paragraph ")
testimonial = TextBlob(testingsent)

if( testimonial.sentiment.polarity > 0):
    print("Happy")
elif(testimonial.sentiment.polarity==0):
    print("Neutral")
elif(testimonial.sentiment.polarity<0):
    print("Sad")
