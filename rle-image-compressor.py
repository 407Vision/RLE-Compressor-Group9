from PIL import Image
import numpy as np

# Step 1: Load and Preprocess the Image
def load_binary_image(image_path):
    """Load an image and convert it to binary (black and white)."""
    image = Image.open(image_path).convert('L')  # Convert to grayscale
    binary_image = image.point(lambda x: 0 if x < 128 else 1, '1')
    return np.array(binary_image)

# Step 2: Run-Length Encoding (RLE)
def rle_encode(binary_image):
    """Encode a binary image using Run-Length Encoding (RLE)."""
    flat_image = binary_image.flatten()
    encoded = []
    count = 1

    for i in range(1, len(flat_image)):
        if flat_image[i] == flat_image[i - 1]:
            count += 1
        else:
            encoded.append((flat_image[i - 1], count))
            count = 1

    encoded.append((flat_image[-1], count))  # Append the last run
    return encoded


# Step 3: Run-Length Decoding
def rle_decode(encoded, shape):
    """Decode RLE-compressed data back into the original binary image."""
    decoded = []
    for value, count in encoded:
        decoded.extend([value] * count)
    return np.array(decoded).reshape(shape)


# Step 4: Evaluation
def evaluate_rle(image_path):
    """Load an image, compress it using RLE, and evaluate the results."""
    binary_image = load_binary_image(image_path)
    encoded = rle_encode(binary_image)
    decoded_image = rle_decode(encoded, binary_image.shape)

    # Compare sizes
    original_size = binary_image.size
    compressed_size = len(encoded)

    print("Original Size (pixels):", original_size)
    print("Compressed Size (RLE entries):", compressed_size)
    print("Compression Ratio:", round(original_size / compressed_size, 2))

    # Verify reconstruction
    assert np.array_equal(binary_image, decoded_image), "Decompressed image does not match the original!"
    print("Decompression successful: The images match!")

# Example Usage
if __name__ == "__main__":
    image_path = "/content/example_binary_image.jpg"  # Provide the path to a binary image
    evaluate_rle(image_path)
