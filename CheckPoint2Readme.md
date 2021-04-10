# Team 12

## URLs
URL to our website: https://hardwareresources12.herokuapp.com/

URL to backend: https://backendteam12.herokuapp.com/

## Welcome to Team 12's website!

#### User Instructions:

When the user first clicks on our website, they will be taken to a home page where they can decide whether they need to register as a first time user or login as a returning user. Once successfully registered/logged in, the user will be taken to their personal dashboard in which they have three options.

- The first option is to create a new project by clicking on the large new project button. 
- The second option is to log out and return to the home screen. Once logged out, the user cannot access the /dashboard route.
- The last option is to access a pre-existing project by entering the project ID and the correct shared password for double security. 

After successfully entering the project information, the user will be taken to the hardware resources page.
In this section, you can check in/out hardware with the form on the right. There are also datasets to download at the bottom. Click on the name of the dataset to download.

## Known Issues


 - In the hardware check in/out section, we have bars to visualize the availability. That will be functional in checkpoint 3. There is a text version at the top. **However, it does not populate the availability values until the submit button is pressed for the form.** The text version updates once request is submitted. In other word, as soon as you enter the /hardware route, click the submit button on the form, with no requests, just to bring the values to the frontend from the backend.
 - You can only logout from the dashboard, not the hardware page, so navigate back.
 - Some of the cards and alerts are not perfect yet.
 -  Not really an issue, but we used two repos to deploy onto Heroku: one for the backend, one for the frontend.
