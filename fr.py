import PIL.Image
import PIL.ImageDraw
import face_recognition

image = face_recognition.load_image_file("people.png")

face_locations = face_recognition.face_locations(image)

number_of_faces = len(face_locations)

print("Znalazłem {} twarzy na fotografii".format(number_of_faces))