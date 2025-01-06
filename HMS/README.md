# The University of Michigan Healthy Minds Survey (HMS) Data Analysis project
### About the HMS
The HMS is an online survey of undergraduate and graduate level students who are above 18 years of age. The survey asks respondents about their demographics, mental health, substance use, body image, abuse, physical health, behaviors, inclusion in the learning environment, resilience, finances, peer support, and athletic history. 

### Areas of Focus
* Mental Health
  * Stigma
  * Respondent mental health
  * Mental health knowledge
* Habits and feelings while in college/university
  * Sense of belonging
  * Exercise
  * Internet usage
* Family
* Academic achievement

### Specific Variables
#### Demographics
* What is the highest level of education completed by your parents, step-parents, or guardians?
    * educ_par1  educ_par2  
        * 1=8th 2 = hs (no degree) 3 = hs degree 4= some college 5 = associates 6 = bach 7 = grad 8 dk
* What is your GPA?
  * gr_A (A - F), gr_none, gr_dk
      * binary 1.0 or 0, gr_none and dk are mutually exclusive (ME)
* Do you belong/see myself as part of campus
  * belong1 (Q2.29)
    * 1 SA - 6 SD

#### Mental Health
* In the past 4 weeks, how many days have you felt that
   emotional or mental difficulties have hurt your
   academic performance?
  * aca_impa
    * 1 = None, 2 - 1-2 days, 3 = 3-5, 4 = >= 6
* Positive Mental Health
  * dieners 1-8 -> positiveMH
    * Create columns that sum the scores in dieners 1-8, and if >= 48 Yes and under No for flourishing -> 1 = flourishing 0 = not flourishing
* Depression
  * phq9 (**Special case**) - dep_any
    *  Create columns that sum the scores in phq9_ 1-9 (subtract a value of 9 because an input of 1 = no days which shouldn't add to the score), and if >= 10 Yes and under No for depressed (major depression or otherwise) -> 0 not depressed 1 = depressed (any type)
* Suicidality - In the past year, did you ever seriously think about attempting suicide?
  * sui_idea
      * 1 = Yes, 0 = No
###### The following 3 variables are randomized, meaning that roughly half of the respondents werent asked the question and their rows probably contain nan values
* In the past 30 days, about how many hours per week on average did you spend exercising? (Include any exercise of moderate or higher intensity) 
    * exerc
      * 1 = <1h, 2 = 1-2h, 3=2-3h, 4=3-4h, 5 = >=5
* Are you lonely? UCSD 3-question scale, added in data cleaning by UMich
  * lonely
    * 0 = No, 1 = Yes, NA = respondent didn't answer all questions
* In the past week, on average, approximately how much time per day have you spent using online spaces not for school or work, such as social media, gaming, etc.
  *   internet_1
    * 1 = none, 2 = <10, 3 = 10-30, 4 = 31-60, 5 = 1-2 hr, 6 = 2-3 hr, 7 = >= 3 hr
###### Two different variables below
* 1 Most people think less of a person who has
received mental health treatment.
2 I would think less of a person who has received
mental health treatment.
  * stig_pcv and stig_per
    * 1 = strong agree, 6 = sd
* In the past 12 months, I needed help for
emotional or mental health problems or
challenges such as feeling sad, blue, anxious or
nervous.
  *  percneed
    * 1 = strong agree, 6 = sd
* Relative to the average person, how knowledgeable are you about
mental illnesses (such as depression and anxiety disorders) and their
treatments?
  * know_sp
    * 1 = well above avg, 5 = well below average

### Goals and Objectives
* How does a person's perception of mental health (ie: stigma) affect their mental health status?
* What is correlation between exercise and depression?
* Probability that someone who experiences suicidal ideation is depressed
* Probability that someone feels either lonely or depressed given that they don't feel a sense of belonging.
* Percentage of depression by family's level of education
* 

### Skills I Hope to Improve
* List/dictionary comprehensions and lambda functions
* Different methods of EDA
* Probabilities

###### Side note!
I tried to use existing statistics and studies to generate random exercise minute values and plot them, however, I don't know how to do so while mapping each value to its respondent, so the data isn't very helpful.

###### What I would do differently if I administered the survey...
I'd include open answer responses (ie; how many minutes per week do you exercise, how many minutes do you socialize, etc.)

## Feel free to leave any suggestions! This is my first ever final portfolio project.