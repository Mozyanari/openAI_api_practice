from openai import OpenAI
import os
import base64

os.environ["OPENAI_API_KEY"] = "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"
client = OpenAI()

# with open("/home/mozyanari/ダウンロード/PXL_20231216_020121369.jpg", "rb") as image_file:# 画像ファイルを開く
#     # Base64にエンコード
#     encoded_string = base64.b64encode(image_file.read())
    
    # Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
# バスマジックリン
# image_path_1 = "/home/mozyanari/ダウンロード/PXL_20231216_020121369.jpg"

# カップラーメン
# image_path_1 = "/home/mozyanari/ダウンロード/PXL_20231218_144619062.jpg"
# image_path_2 = "/home/mozyanari/ダウンロード/PXL_20231218_144609606.jpg"
# image_path_3 = "/home/mozyanari/ダウンロード/PXL_20231218_144606289.jpg"

# ペットボトル
# image_path_1 = "/home/mozyanari/ダウンロード/PXL_20231218_141855015.jpg"
# image_path_2 = "/home/mozyanari/ダウンロード/PXL_20231218_141848613.jpg"
# image_path_3 = "/home/mozyanari/ダウンロード/PXL_20231218_141840749.jpg"

# オロナミンCドリンク
# image_path_1 = "/home/mozyanari/ダウンロード/PXL_20231218_141955107.jpg"
# image_path_2 = "/home/mozyanari/ダウンロード/PXL_20231218_141951230.jpg"
# image_path_3 = "/home/mozyanari/ダウンロード/PXL_20231218_141958872.jpg"

# インスタントコーヒー
# image_path_1 = "/home/mozyanari/ダウンロード/PXL_20231218_142107744.jpg"
# image_path_2 = "/home/mozyanari/ダウンロード/PXL_20231218_142111971.jpg"
# image_path_3 = "/home/mozyanari/ダウンロード/PXL_20231218_142115295.jpg"

# キズパワーパッド
# image_path_1 = "/home/mozyanari/ダウンロード/PXL_20231218_153459828.jpg"
# image_path_2 = "/home/mozyanari/ダウンロード/PXL_20231218_153502607.jpg"
# image_path_3 = "/home/mozyanari/ダウンロード/PXL_20231218_153506570.jpg"

# チューブ
image_path_1 = "/home/mozyanari/ダウンロード/PXL_20231201_062246090.jpg"


# Getting the base64 string
base64_image_1 = encode_image(image_path_1)
# base64_image_2 = encode_image(image_path_2)
# base64_image_3 = encode_image(image_path_3)
    

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            # "role" : "system",
            # "content": """I will now show you the product images.Please classify the image into the following categories.
            # ・PET bottles・Fabric products・Blister pack・box・Pouches, bags・Cans, bottles・Shrink packaging・Others not applicable to the above""",
            
            "role": "user",
            "content": [
                {"type": "text", "text": """I will now show you the product images.Please classify the image into the following categories.
                 ・PET bottles・Fabric products・Blister pack・box・Pouches, bags・Cans, bottles・Shrink packaging・Others not applicable to the above"""},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image_1}"
                    },
                    # "type": "image_url",
                    # "image_url": {
                    #     "url": f"data:image/jpeg;base64,{base64_image_2}"
                    # },
                    # "type": "image_url",
                    # "image_url": {
                    #     "url": f"data:image/jpeg;base64,{base64_image_3}"
                    # },
                },
            ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0])