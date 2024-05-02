import json
from deepface import DeepFace


# face matching

result = DeepFace.verify(img1_path="modi1.jpeg", img2_path="modi2.png")
print(json.dumps(result, indent=2))


# find face in db

# face analysis
