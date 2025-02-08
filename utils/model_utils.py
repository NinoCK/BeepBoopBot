import subprocess

def get_available_models():
    try:
        output = subprocess.check_output(['ollama', 'list'], encoding='utf-8')
        return [line.strip().split()[0] for line in output.strip().split('\n') if line]
    except Exception as e:
        print(f"Error getting model list: {e}")
        return []
