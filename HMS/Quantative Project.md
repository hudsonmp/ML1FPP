# Converting `exercise` and `internet_usage` into numeric variables

### `Exercise`
* For each 1, it should track to a normal distribution curve with minutes ranging from 0-59

Because there wasn't much readily available on the distribution of exercise minutes for students who exercise under 1 hour weekly, I took the zero_exercise proportion and multiplied it by the number of respondents who selected '1'. Then, since most exercise data sets are right-skewed and the average number of minutes is 19, I created a logarithmic histogram (thanks ChatGPT!!) with the mean and std that reflected this.
