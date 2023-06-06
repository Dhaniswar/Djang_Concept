from PIL import Image


def convert_to_thumbnail(source, image_uuid):
    extension = ""
    image_name = ""

    if "." in str(source):
        extension = str(source).split(".")[-1]
        image_name = ".".join(str(source).split('.')[:-1])
    
    destination = f"{image_name}_{image_uuid}.{extension}"

    image = Image.open(source)
    
    SIZE = (500, image.height)
    if image.width < 500:
        SIZE = (image.width, image.height)
    
    print('image size after is => ',SIZE)  # Open image

    image.thumbnail(SIZE)
    print('image size after using thumbnail => ', image.size)  # Open image

    image.save(destination)  # Convert image to webp



def convert_to_webp(source, image_uuid):
    if "." in str(source):
           image_name = ".".join(str(source).split(".")[:-1])   

    destination = f'{image_name}_{image_uuid}.webp'
    image = Image.open(source)
    image.save(destination, format="webp")  # Convert image to webp
   