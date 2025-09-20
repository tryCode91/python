from dotenv import load_dotenv
import os

def load_env(envPath: str = "", env_names: list = []):
    # Path input relative to where it is called
    if envPath == "":
        raise ValueError("envPath must be provided") 
    # Load the .env file from the specified path
    environment = load_dotenv(envPath)
    # Check if the environment variables are loaded correctly
    if environment:    
        missing_keys = []
        for key in env_names:
            value = os.getenv(key)
            if not value:
                missing_keys.append(key)
        
        if missing_keys:
            for key in missing_keys:
                print(f"{key} is missing or empty!")
        else:
            print("Successfully added all environmental variables!")
    else:
        print(f"Failed to load environment variables from path: {envPath}")
