# The University of Michigan Healthy Minds Survey (HMS) Data Analysis project
### About the HMS
The HMS is an online survey of undergraduate and graduate level students who are above 18 years of age. The survey asks respondents about their demographics, mental health, substance use, body image, abuse, physical health, behaviors, inclusion in the learning environment, resilience, finances, peer support, and athletic history. 

### Areas of Focus
* Mental Health

### Specific Variables
#### Demographics
* **educ_par1  educ_par2** 
    * What is the highest level of education completed by your parents, step-parents, or guardians?  
        * 1=8th 2 = hs (no degree) 3 = hs degree 4= some college 5 = associates 6 = bach 7 = grad 8 idk
* **gr_A (A - F), gr_none, gr_dk**
  * What is your GPA?
      * binary 1.0 or 0, gr_none and dk are mutually exclusive (ME)
* **belong1 (Q2.29)**
  * Do you belong/see myself as part of campus
    * 1 SA - 6 SD

#### Mental Health
*  In the past 4 weeks, how many days have you felt that
   emotional or mental difficulties have hurt your
   academic performance?
  *  aca_impa
    * 1 = None, 2 - 1-2 days, 3 = 3-5, 4 = >= 6
* Positive Mental Health
  * diener (**Special case**)
    * Create columns that sum the scores in dieners 1-8, and if >= 48 Yes and under No for flourishing
* Depression
  * phq9 (**Special case**)
    *  Create columns that sum the scores in phq9_ 1-9 (subtract a value of 9 because an input of 1 = no days which shouldn't add to the score), and if >= 10 Yes and under No for depressed (major depression or otherwise)
* Suicidality - In the past year, did you ever seriously think about attempting suicide?
  * sui_idea
      * 1 = Yes, 0 = No
###### The following 3 variables are randomized, meaning that roughly half of the respondents werent asked the question and their rows probably contain nan values
* In the past 30 days, about how many hours per week on average did you spend exercising? (Include any exercise of moderate or higher intensity) 
    * exerc
      * 1 = <1h, 2 = 1-2h, 3=2-3h, 4=3-4h, 5 = >=5
* Sleep (Asks about weekdays and weekends seprately. Average the two out to find the mean over the course of a week. (x hr * 5 + y hr * 2 / 7))
  * sleep
    * 1 = <1h, 2 = 1-2h, 3=2-3h, 4=3-4h, 5 = >=5                                                                                                                                                                     
* In the past week, on average, approximately how much time per day have you spent using online spaces not for school or work, such as social media, gaming, etc.
  *   internet_1
    * 1 = none, 2 = <10, 3 = 10-30, 4 = 31-60, 5 = 1-2 hr, 6 = 2-3 hr, 7 = >= 3 hr
*   1 Most people think less of a person who has
received mental health treatment.
2 I would think less of a person who has received
mental health treatment.
  * stig_pcv and stig_per
    * 1 = strong agree, 6 = sd