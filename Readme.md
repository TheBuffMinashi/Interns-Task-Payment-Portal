# Payment Portal Project

This is the repository for the payment portal project using Django, Django REST framework, MySQL, and Stripe. The payment portal allows users to pay via PayPal and debit/credit cards and uses Stripe for payment processing.

## Contributing

To contribute to this project:

1. Fork this repository and create a new branch for your changes.
2. Implement the payment portal following the task definition provided.
3. Write tests to ensure the payment portal is functioning correctly.
4. Submit a pull request with your changes for review.

Make sure to follow best practices for coding, testing, and documentation. Include clear and concise documentation on how to use the payment portal and its API.

Happy coding!


## For running the Project !!!

1. Make sure that you have proper vpn or dns for using docker 
2. Run `docker compose up` for running the project
3. Then you can use the swagger provided in `http://localhost:8000` for accessing the provided API which in this case
is creating payment


### Notice that for customized APIs using Stripe we need front end for processing to check out please see the below link
https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements
