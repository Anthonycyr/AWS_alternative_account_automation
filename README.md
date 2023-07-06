# AWS_alternative_account_automation

This repository contains a Python script that uses the Boto3 library to update AWS accounts with alternate contact information.

## Prerequisites

- Python 3.x
- Boto3 library
- pandas library

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/Anthonycyr/AWS_alternative_account_automation.git
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place the input CSV file (e.g., `data.csv`) in the same directory as the Python script. Important that the .csv file use this stucture:AccountId,Security,Operations,Billing (fakedata.csv for example).

2. Update the filename in the script to match the actual name of your input file:

   ```python
   dataframe = pd.read_csv('./data.csv')
   ```

3. Run the script:

   ```
   python3 main.py
   ```

4. The script will read the input CSV file, melt the data, sort it by AccountId, and save the result in a new CSV file called `melted_data.csv`. Additionally, it will update each AWS account with the provided alternate contact information.

## Configuration

Ensure that you have valid AWS credentials configured on your system. Boto3 will use these credentials for authentication.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

