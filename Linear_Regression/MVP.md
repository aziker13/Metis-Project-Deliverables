Due to the lack of data to evaluate transfer fees for the top 500 players (regardless of position) across 2 seasons, along with the fact that no feature
was producing significant correlation to the target, as no performance feature can encapsulate play across all positions across a pitch, and no characteristic such as
nationality, age, or club, was enough to lift the model.
I have decided to pivot slightly, and I am looking to instead perform 2 regression on ~500 players who play in the
offensive role and score goals, and ~500 players who play in the midfield and bring value through passing. 


![Screenshot from 2021-09-29 00-17-26](https://user-images.githubusercontent.com/87049486/135221269-829c531d-9334-400b-8ccf-fc5f2dbab4ca.png)


![Screenshot from 2021-09-29 00-17-07](https://user-images.githubusercontent.com/87049486/135221351-e65bae61-ec82-4b15-bb95-4d6ce350bd74.png)

I will only be looking at one season of performance along with their transfer value at the end of that season.  I
have successfully obtained the data for both groups, and after cleaning I have ~800 usable datapoints, as passing statistics
were unavailable for players outside of the top 5 European league, which limited the number of players I would be able to evaluate in the midfield.

My next step is to run 2 linear regressions using features specific to each group to gain better insight into the interactions between performance and transfer values
unique to the 2 position groups
