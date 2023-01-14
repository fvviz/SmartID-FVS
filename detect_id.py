import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
model = load_model("ID_detector.model")
cap = cv2.VideoCapture(0)
x, y, w, h =  400, 30, 600,600


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    roi = frame[y:y + h, x:x + w]
    roi = cv2.cvtColor(roi,cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (224, 224))
    roi = img_to_array(roi)
    roi  = roi.reshape(1,224,224,3)
    roi = preprocess_input(roi)
    predictions = model.predict(roi)
    max_index = np.argmax(predictions[0])
    cats = ('not wearing ID', 'wearing ID')
    prediction_cat = cats[max_index]
    predict_percent = predictions[0][max_index] * 100
    cv2.putText(frame, f"{prediction_cat} {round(predict_percent, 2)}%", (int(x + 100), int(y)),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('smartId', frame)
    if cv2.waitKey(10) == ord('q'):  # wait until 'q' key is pressed
        break

cap.release()
cap.destroyAllWindows()

