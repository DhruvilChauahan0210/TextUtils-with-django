# TextUtils

Welcome to **TextUtils**, a Django-based web application that provides a variety of text analysis utilities. This project allows users to manipulate and analyze text with the following features:

1. Remove Punctuations
2. Convert to Uppercase
3. Convert to Lowercase
4. Remove New Lines
5. Remove Extra Spaces
6. Count Number of Characters

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with this project, follow these steps:

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/TextUtils.git
   cd TextUtils
   ```

2. **Create a virtual environment:**

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Run the migrations:**

   ```sh
   python manage.py migrate
   ```

5. **Start the development server:**

   ```sh
   python manage.py runserver
   ```

## Usage

Once the server is running, open your web browser and go to `http://127.0.0.1:8000/`. You will see the homepage of TextUtils.

### Analyzing Text

1. **Enter your text**: In the text area provided, enter the text you want to analyze or manipulate.
2. **Select the operations**: Choose one or more operations you want to perform on the text (e.g., remove punctuations, convert to uppercase).
3. **Submit**: Click the "Analyze" button to see the result.

## Features

### Remove Punctuations

This feature removes all punctuation marks from the input text.

### Convert to Uppercase

This feature converts all characters in the input text to uppercase.

### Convert to Lowercase

This feature converts all characters in the input text to lowercase.

### Remove New Lines

This feature removes all newline characters from the input text.

### Remove Extra Spaces

This feature removes any extra spaces from the input text, leaving only single spaces between words.

### Count Number of Characters

This feature counts and displays the total number of characters in the input text.

## Contributing

We welcome contributions to enhance the functionality of TextUtils. To contribute:

1. **Fork the repository**
2. **Create a new branch** (`git checkout -b feature/your-feature-name`)
3. **Commit your changes** (`git commit -m 'Add some feature'`)
4. **Push to the branch** (`git push origin feature/your-feature-name`)
5. **Open a pull request**

Please ensure your code adheres to the existing code style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Thank you for using TextUtils! If you have any questions or feedback, feel free to open an issue in the repository.
