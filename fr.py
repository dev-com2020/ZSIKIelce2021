import PIL.Image
import PIL.ImageDraw
import face_recognition

image = face_recognition.load_image_file("people.png")

face_locations = face_recognition.face_locations(image)

number_of_faces = len(face_locations)

print("Znalazłem {} twarzy na fotografii".format(number_of_faces))

pil_image = PIL.Image.fromarray(image)

for face_location in face_locations:
    top, right, bottom, left = face_location
    print("Twarz znajduje się w lokalizacji pikseli: \n"
          "Top {}, Left {}, Bottom {}, Right {}".format(top, left, bottom, right))
    draw = PIL.ImageDraw.Draw(pil_image)
    draw.rectangle([left, top, right, bottom], outline='red')
pil_image.show()
