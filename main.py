import cv2

def create_photo_collage(image1_path, image2_path, output_path):
    # Load the images
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # Resize images to the same dimensions (adjust as needed)
    image1 = cv2.resize(image1, (500, 300))
    image2 = cv2.resize(image2, (500, 300))

    # Create a new blank image to hold the collage
    collage = cv2.vconcat([image1, image2])

    # Save the collage
    cv2.imwrite(output_path, collage)

    # Display the collage (optional)
    cv2.imshow('Photo Collage', collage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Paths to input images
    image1_path = "1.jpg"
    image2_path = "2.jpg"

    # Path of output 
    output_path = "photo_collage.jpg"

    # Create the photo collage
    create_photo_collage(image1_path, image2_path, output_path)
