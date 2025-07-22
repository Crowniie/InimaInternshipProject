import json
class JSONManager:
    def readJSON(self, file_path):
        import json
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"File {file_path} not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {file_path}.")
            return None