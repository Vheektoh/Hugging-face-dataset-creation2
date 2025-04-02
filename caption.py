import os
import json

image_dir = "/Users/macbok/Downloads/Telegram Desktop"

#manual caption of each image
manual_captions = {
    "image_1.jpg": "This is Naruto and Sasuke standing against a dreamy twilight sky with a full moon and glowing stars. Naruto on the left, with spiky blond hair and an orange jumpsuit, looks ahead with determination, while Sasuke on the right in a blue outfit glances back with a serious expression.",
    "image_2.jpg": "Naruto with a spiky hair and sasuke with a black hair are standing back-to-back with their arms crossed, symbolizing rivalry and contrast. Naruto in an orange outfit and Sasuke in a blue outfit both wear headbands.",
    "image_3.jpg": "Naruto and SAsuke are in a tense confrontation, gripping each other’s clothing while staring intensely into each other's eyes. Sasuke appears more aggressive than blond haired Naruto.",
    "image_4.jpg": "Sasuke and Naruto confronts each other gripping each other's clothes. Sasuke has a black hair while Naruto has a blond hair.",
    "image_5.jpg": "sasuke and naruto jam fist in combat. sasuke is with a purple shirt while naruto is on an orange and ash sweater.",
    "image_6.jpg": "Sasuke and naruto in battle. sasuke with a lightning like structure on his hand while naruto has a light ball known as a rasengan on his hand.",
    "image_7.jpg": "Asta and Noelle cuddling up under a tree. Asta is the male figure with a black hair band while Noelle is the female figure with a brown boot.",
    "image_8.jpg": "This is an image of Captain Yami.",
    "image_9.jpg": "This is an image of Asta with his white hair and black hair band.",
    "image_10.jpg": "Asta and Noelle kissing. Asta is with the hair band while Noelle has a white hair",
    "image_11.jpg": "Naruto and Sasuke lying exhausted after a tiresome batle with their hands each cut off.",
    "image_12.jpg": "Asta and Noelle on a grassland. Asta is carrying Noelle. Asta is with a brown purse while Noelle is with a red purse",
    "image_13.jpg": "Asta and Noelle both shouting with the background as that of space.",
    "image_14.jpg": "Noelle talking to Asta with a blush on her face.",
    "image_15.jpg": "Noelle carrying Asta on her back.",
    "image_16.jpg": "Noelle and Asta hugging passionately.",
    "image_17.jpg": "Noelle and Asta sitting tired under the moonlight.",
    "image_18.jpg": "Asta and Noelle sitting on a grassy field at night with asta's mouth open.",
    "image_19.jpg": "Noelle standing preety with her feminine features all outlined through her clothes.",
    "image_20.jpg": "Captain yami sitting with his sword and white singlet and his cigarette in his mouth.",
    "image_21.jpg": "Captain yami giving a battle ready stance with his sword in his hands pointing towards something.",
    "image_22.jpg": "Naruto and sasuke lying down exhaisted after an intense battle each with an arm short.",
    "image_23.jpg": "Captain yami with his sword and a black matter behing him.",
    "image_24.jpg": "Captain yami with his sword and a black matter behing him known as dimensional slash.",
    "image_25.jpg": "Asta and captain yami duo ready for a battle. Asta wields his big sword known as demon dweller while captain yami holds his regular sword with both their groimores open.",
    "image_26.jpg": "Captain yami tosses his sword to asta in a battle stance.",
    "image_27.jpg": "Captain yami and asta stand back to back.",
    "image_28.jpg": "Asta and his friend yuno. yuno dresses like a prince and has a green hair.",
    "image_29.jpg": "Asta and yuno stand together on the street. yuno has a black hair here.",
    "image_30.jpg": "A portrait of Yuno and Asta side by side. Yuno has a black hair while Asta has a black hairband.",
    "image_31.jpg": "Yuno and Asta stand side by side with yuno having his fairy on his shoulder.",
    "image_32.jpg": "Asta and Yuno stand back to back.",
    "image_33.jpg": "Naruto and sasuke styand facing each other in the woods. Naruto is smiling while sasuke has a straight face.",
    "image_34.jpg": "Asta and Yuno stand side buy side with asta holding his sword and groimore while yuno has just his groimore.",
    "image_35.jpg": "Asta and yuno stand side by side smiling while looking at each other with a side eye. asta holds his sword on his shoulder while yuno holds his groimore.",
    "image_36.jpg": "Asta in a battle scene looking all angry.",
    "image_37.jpg": "Asta and captain yami standing side by side with their groimores. while asta has a red groimore, captain yami has a purple groimore.",
    "image_38.jpg": "Gojo Satoru with his fingers crossed. behind him is an aura being portrayed by his domain expansion which is his special power.",
    "image_39.jpg": "Gojo satoru pointing at his hands showing the mount fuji guy that he is more powerful. Gojo satoru has a white hair while the mount fuji guy has a cup like opening on his head. also, gojo satoru is wearing a purplr clothe.",
    "image_40.jpg": "Itadori and Todou faces a cursed spirit hanami. itadori is with a purple dress, todou is shirtless and throwing a kick while hanami has a treelike structure coming out of where his eyes are supposed to be.",
    "image_41.jpg": "Okkotsu yuta and geto suguru fighting. yuta is backing the camera while geto is with the purple kimono with yuta's cursed spirit standing behind him.",
    "image_42.jpg": "Okkotsu yuta and geto suguru fighting. yuta is wearing a white shirt with a sword in his hands while his cursed spirit is standing behind him.",
    "image_43.jpg": "Okkotsu yuta.",
    "image_44.jpg": "Sasuke and naruto duo, sasuke is holding a sword.",
    "image_45.jpg": "Gojo satoru standing inbetween hanami and the mount fuji guy.",
    "image_46.jpg": "meliodas with a big battle sword.",
    "image_47.jpg": "meliodas with his big bright yellow hair.",
    "image_48.jpg": "meliodas standing with his yellow hair under a tree in sunrise.",
    "image_49.jpg": "escanor in battle mode with his axe.",
    "image_50.jpg": "escanor with his armour and axe.",
    "image_51.jpg": "Itadori and Todou standing next to each other, with todou standing shirtless while itadori is with his regular purple clothe.",
    "image_52.jpg": "Naruto and sasuke with their rasengan and lightning respectively.",
    "image_53.jpg": "Naruto and sasuke standing head to head with some injuries seen on the glasslike frame.",
    "image_54.jpg": "A portrait of sasuke and naruto both sliced and put next to each other.",
    "image_55.jpg": "A portrait of sasuke and naruto both sliced and put next to each other with an image of them about to throw fists below.",
    "image_56.jpg": "Naruto and sasuke with naruto's arm around sasuke's shoulder and with a smile on naruto's face.",
    
}

# create the json structure
dataset = {'train':[]}

# loop through the images in the directory and add them to the json structure
for filename in os.listdir(image_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # get the caption from the manual_captions dictionary
        caption = manual_captions.get(filename, "No caption available")
        
        # create the image entry
        image_entry = {
            'image': os.path.join(image_dir, filename),
            'caption': caption
        }
        
        # add the image entry to the dataset
        dataset['train'].append(image_entry)
# save the dataset to a json file
with open('dataset.json', 'w') as f:
    json.dump(dataset, f, indent=4)
print("Dataset created successfully!")

# Load the dataset using the datasets library
from datasets import load_dataset, Image, DatasetDict
dataset = load_dataset('json', data_files='dataset.json')
dataset = dataset['train'].cast_column("image", Image())

print(dataset)
print(dataset['train'][0])

#push dataset to huggingface
dataset.push_to_hub('TrikyViktor/Anime-Image-Captioning')
#
# Check if the dataset is pushed successfully
from huggingface_hub import whoami
print(whoami())