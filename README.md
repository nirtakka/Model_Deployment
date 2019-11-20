# Model_Deployment
Model Deployment Repository

Author:<br>
Nirta Ika Yunita & Samuel Natamihardja

<br>
API description:
German Credit Scoring, this API call returning prediction if an individual going likely to be default in their installment terms based on set of information.

* **URL**: http://samuelnatami.pythonanywhere.com/api  


* **Method**: `POST`
	
* **Parameters**
	
	* **Body**: 
		* duration_in_month: loan duration in month
		* credit_amount: loan amount
		* unemployed: is the customer jobless? 
		* installment_as_income_perc: installment rate of disposable income in percentage
		* present_res_since:  how long the customers stay in their residence is in year
		* age: age of the customer
		* credits_this_bank: number of existing credits at this bank
		* people_under_maintenance: number of liabilities
		* foreign_worker_yes: is the customer a foreign worker?
			example:
			```python
				{
					"duration_in_month": 6,
					"credit_amount": 1169,
					"unemployed": 0,
					"installment_as_income_perc": 4,
					"present_res_since": 4, 
					"age":67,
					"credits_this_bank": 2,
					"people_under_maintenance":1,
					"foreign_worker_yes:1
				}
			```
* **Success Response**
	* Code: 200
		* Content:
			* Default: prediction result -> 1: default, 0: not default
