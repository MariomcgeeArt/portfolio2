 question 1 How is this project structure different than a Flask (or Node) application? What role are the urls.py and views.py files responsible for?

Django is used for building larger scale applications. The urls handle all of the route urls in your project between apps. The views display front end and also have functionality and can connect with other aspects of your django app.


 question 2 Why do we use 2 separate urls.py files? How do they interact?

 1.one is for project directory, and the others are for all the other apps in your project

 2.The interatction between the root Url file and the apps urls is such that when a user makes a request it looks in the root url file and matches the first part of the request with the correct url pattern/ so for example if you have an app portfolio it will first look in your django app root url.py urlpatterns  to see if there is anything starting with portfolio. When it finds this match it will see that there is more information to be processed which is where the include() comes into play. It now knows that since you have specified to include all of portfolio.urls to send the rest of the process over to the url patterns within the portfolio app. When it arrives it continues to look through the Url patterns within portfolioapp and goes according to what you have set up which might be to render a view etc...


 question 3When is it desirable to split our code over multiple apps? Why would we want to do so?

 1.if you have large features in your project spliting them into apps can be benficital for  organzational and refactoring purposes.