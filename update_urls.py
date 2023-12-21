import re

# Define the pattern to match local image sources
pattern = r'src="image/(.*?)"'

# Define your bucket name and region
bucket_name = "my-bucket"
region = "us-east-1"

# Define the images and their filenames
images = {
    "weather_img": "weather.png",
    "rain_img": "rain.png",
    "wind_img": "wind.png",
    "humidity_img": "humidity.png",
}

# Read the index.html content
with open('index.html', 'r') as file:
    content = file.read()


# Function to replace local paths with S3 URLs
def replace_with_s3_url(match):
    filename = match.group(1)
    return f'src="https://{bucket_name}.s3.amazonaws.com/{filename}"'

updated_content = re.sub(pattern, replace_with_s3_url, content)


# Write the updated content back to index.html
with open('index.html', 'w') as file:
    file.write(updated_content)

