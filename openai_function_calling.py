from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "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"

client = OpenAI()

# Step 1: 呼び出す関数を定義
functions = [
    {
        "type": "function",
        "function": {
            "name": "robot_arm_power_on", #関数の名前
            "description": "Power on robot arm. This function is must required before operation.", #関数の説明
        },
    },
    {
        "type": "function",
        "function": {
            "name": "robot_arm_power_off", #関数の名前
            "description": "Turn off robot arm. This function is must required before operation.", #関数の説明
        },
    },
    
    {
        "type": "function",
        "function": {
            "name": "robot_arm_get_angles", #関数の名前
            "description": "Get the joint angles of mycobot. The return value is a float and is returned as a python list type, and since mycobot has 6 axes, 6 values are stored. For example, if the first axis is 10 degrees, the second axis is 20 degrees, the third axis is 30 degrees, the fourth axis is 40 degrees, the fifth axis is 50 degrees, and the sixth axis is 60 degrees, then [10,20, 30,40,50,60]", #関数の説明
        },
    },
    {
        "type": "function",
        "function": {
            "name": "robot_arm_get_arm_angle", #関数の名前
            "description": "Get the angle of the specified joint of mycobot.", #関数の説明
            "parameters": {
                "type": "object",
                "properties": { #関数の引数の説明
                    "id": { #引数
                        "type": "number", #引数のデータ型を指定　ここでは文字列型
                        "description": "You can enter the number of the joint angle you want to obtain, from 1 to 6.", #引数の説明を例を用いて説明
                    },
                },
                "required": ["id"], #引数が必須なのかを指定　ここでは一つしかないので必須とする
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "robot_arm_set_arm_angle", #関数の名前
            "description": "Moves the specified joint to the specified angle at the specified speed", #関数の説明
            "parameters": {
                "type": "object",
                "properties": { #関数の引数の説明
                    "id": { #引数
                        "type": "number", #引数のデータ型を指定　ここでは文字列型
                        "description": "You can enter the number of the joint angle you want to specify, from 1 to 6.", #引数の説明を例を用いて説明
                    },
                    "degree": { #引数
                        "type": "number", #引数のデータ型を指定　ここでは文字列型
                        "description": "You can enter the desired joint angle from -170 degrees to 170 degrees.", #引数の説明を例を用いて説明
                    },
                    "speed": { #引数
                        "type": "number", #引数のデータ型を指定　ここでは文字列型
                        "description": "You can enter the desired joint movement speed from 0 to 100.", #引数の説明を例を用いて説明
                    },
                    
                },
                "required": ["id,degree,speed"], #引数が必須なのかを指定　ここでは一つしかないので必須とする
            },
        },
    }
]

messages = [{"role": "system", "content": "You are an assistant who will teach you the API of the robot arm. The robot arm is a 6-axis robot arm. Before it moves, you must run the power_on function to start the robot arm. Also, after the operation is finished, it is necessary to use the power_off function to terminate the robot arm."},
            {"role": "user", "content": "Turn on robot, next set the angle of the second joint to 30 degrees."}]
response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=messages,
    # functions=functions,
    tools=functions,
    tool_choice="auto",
)

print(response)

response_message = response.choices[0].message
tool_calls = response_message.tool_calls
print(tool_calls)

if tool_calls:
     messages.append(response_message)
     
for tool_call in tool_calls:
    function_name = tool_call.function.name
    messages.append(
        {
            "tool_call_id": tool_call.id,
            "role": "tool",
            "name": function_name,
        }
    )  # extend conversation with function response
    second_response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
    )

print(second_response)