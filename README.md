# Hand_written_recognition
 # Handwritten Digit Recognition

## 📄 Project Overview
This project is a **Handwritten Digit Recognition** application built using a deep learning model. Users can upload or draw an image of a digit, and the application predicts the digit using a pre-trained neural network.

## 🛠 Features
- Predict digits from uploaded images or drawings.
- Uses a Convolutional Neural Network (CNN) for digit recognition.
- Streamlit web app for a simple and interactive user interface.

## 🧰 Technologies Used
- **Python**
- **TensorFlow/Keras**: Model training and prediction.
- **OpenCV**: Image processing.
- **NumPy**: Data manipulation.
- **Streamlit**: Web app interface.
- **Ngrok**: Hosting the app locally for remote access.

## 🚀 How to Run the Project
1. **Clone the repository**:
   ```bash
   git clone https://github.com/LornaGathoni1/Hand_written_recognition.git
Navigate to the project directory:

cd Hand_written_recognition

Install dependencies:

pip install -r requirements.txt

Run the Streamlit app:

    streamlit run app.py

    Access the app:
        If using ngrok, follow instructions to set up a public link.
        Otherwise, visit http://localhost:8501 in your browser.

📂 Project Structure

Hand_written_recognition/
├── app.py                        # Streamlit app
├── hand_written_digit_recognition_model.keras  # Pre-trained model
├── images/                       # Sample images for testing
│   ├── 1.png
│   ├── 4.png
│   ├── ...
├── requirements.txt              # List of dependencies
└── README.md                     # Project documentation

🖌 Using the Drawing Feature

    Open the app.
    Use the drawing pad to draw a digit.
    Submit the drawing and view the predicted digit.

📊 Dataset Used

The model is trained on the MNIST dataset, a collection of 70,000 handwritten digits (0-9).

📸 Screenshots

Here are some screenshots of the app in action:
![Screenshot 2024-12-18 221640](https://github.com/user-attachments/assets/fe08a962-da27-4f6c-8f7f-aa332288d5a0)
![Screenshot 2024-12-18 221925](https://github.com/user-attachments/assets/6915c3a3-7223-4f9e-b1e2-eba48ee84b04)
![Screenshot 2024-12-18 222058](https://github.com/user-attachments/assets/6f3d970f-043e-4439-8d9c-6476f17e1eb9)




🤝 Contributions

Contributions are welcome! Feel free to fork the repository and submit a pull request.
📜 License

This project is licensed under the MIT License.

