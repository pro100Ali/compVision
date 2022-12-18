from PIL import Image, ImageDraw
import face_recognition

image = face_recognition.load_image_file("storedImages/fenix.jpg")

face_landmarks_list = face_recognition.face_landmarks(image)

pil_image = Image.fromarray(image)
for face_landmarks in face_landmarks_list:
    d = ImageDraw.Draw(pil_image, 'RGBA')

    d.polygon(face_landmarks['left_eyebrow'], fill=(150, 0, 0, 64))
    d.polygon(face_landmarks['right_eyebrow'], fill=(150, 0, 0, 64))
    d.line(face_landmarks['left_eyebrow'], fill=(150, 0, 0, 64), width=5)
    d.line(face_landmarks['right_eyebrow'], fill=(150, 0, 0, 64), width=5)

    d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
    d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
    d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

    d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
    d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))

    d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(8, 8, 123, 93), width=10)
    d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(8, 8, 123, 93), width=10)

    pil_image.show()