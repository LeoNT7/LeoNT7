from PIL import Image, ImageSequence

def change_background_to_black(input_path, output_path):
    with Image.open(input_path) as img:
        frames = []
        for frame in ImageSequence.Iterator(img):
            frame = frame.convert("RGBA")
            # Create a black background
            black_bg = Image.new("RGBA", frame.size, "black")
            # Composite the frame with the black background
            frame = Image.alpha_composite(black_bg, frame)
            frames.append(frame)

        # Save the modified frames as a new GIF
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            duration=img.info["duration"],
            loop=img.info["loop"]
        )

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: change_background.py <input_path> <output_path>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    change_background_to_black(input_path, output_path)
