from robot_face_eye import change_eyes, neutral,wide,angry,look_down
from robot_face_mouth import move_mouth
from robot_face_eyebrows import move_eyebrows
from classifier_edgetpu import Classifier




seen_items = Classifier(label_file="labels.txt",model_file="minseo_model.tflite",threshold=0.8)

reactions = {"game_pad"            : "sad",
             "remote_controller"   : "neutral",
             "lego_bird"           : "angry",
             "cube"                 : "happy"}

faces = {
	"neutral":{"mouth":0,
		   "right_eye":neutral,
		   "left_eye":neutral,
		   "eyebrows":0},
    
	"angry":{"mouth":45,
		 "right_eye":angry,
		 "left_eye":angry,
		 "eyebrows":150},
    
	"sad":{"mouth":-20, "right_eye":wide, "left_eye":wide, "eyebrows":-150},
    
	"happy":{"mouth":-45, "right_eye":look_down, "left_eye":look_down, "eyebrows":-40}
    }


def set_face(face):
    change_eyes(face["left_eye"], face["right_eye"])
    move_mouth(face["mouth"])
    move_eyebrows(face["eyebrows"])
    
    

    
    
if __name__ == '__main__':
    from time import sleep
    print("neutral")
    set_face(faces["neutral"])
    sleep(1)
    
    print("sad")
    set_face(faces["sad"])
    sleep(1)
    
    print("angry")
    set_face(faces["angry"])
    sleep(1)
    
    print("happy")
    set_face(faces["happy"])
    

    while True:
        sleep(1)
        if seen_items.item != seen_items.last_item:
            item = seen_items.item
            print('name=', item) #[0], 'prob=', round(item[1],2))
            if item in reactions.keys():
                set_face(faces[reactions[item]])
        sleep(1)

    
    
    
    
    