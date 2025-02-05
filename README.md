**LOSSLESS COMPRESSION (RUN-LENGTH ENCODING)**
    This is acompression technique to compress images without the loss of any image data.
                                
                                **BEST ENVIRONMENT TO RUN THE REPO**
***This block of of is best to run on colab to recieve a pleasant output***

OPEN CV, Image, Numpy and matplotlib.pyplot are some libraries that were imported

                                  **HOW TO UPLOAD YOUR IMAGE**
The used image in this repo is "batman.jep".
+Get a picture and upload it to FILES in colab.
+Then look for the codes: # Example Usage
                          if __name__ == "__main__":
                              image_path = "/content/batman.jpg"  # Provide the path to a binary image
                              evaluate_rle(image_path)
+replace **"/content/batman.jpg"** with the path pf your picture.

                                    **_OVERVIEW OF THE CODES_**
-The block of code in this repository loads the batman.jpeg image, converted it to grayscale and to binary
-Below this is a function to flatten the 3D batman.jeg image to a 2D image
-After a function is created to compress/encode the image that that has been converted to grayscale
-Another function is created to decode the encoded image to the original for(which is the binary image)

                **IMAGES OF THE RESULTS OF THE RUN-LENGTH ENCODING AFTER RUNNING CODES**
![END-RESULT PICTURES](IMAGES)
