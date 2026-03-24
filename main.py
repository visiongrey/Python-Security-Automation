import concurrent.futures
import subprocess

def run_scripts(script):
    result = subprocess.run(["python", script])
    if result.returncode == 0:
        print(f"#############\nPASS: {script}\n#############\n")
    else:
        print(f"#############\nFAIL: {script}\n#############\n")

if __name__ == "__main__":    
    scripts = ['parse_fwlogs.py','match_fwrules.py','api_requests.py', 'ssh_executecmd.py']
    with concurrent.futures.ThreadPoolExecutor() as exec:
        exec.map(run_scripts, scripts)

