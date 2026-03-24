import paramiko

def ssh_linuxcmd(host, port, user, pswd, cmmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, port=port, username=user, password=pswd, timeout=10)
        sd_in, sd_out, sd_err = ssh.exec_command(cmmd)
        cmd_out = "".join(sd_out.read().decode())
        print(f"Output: {cmd_out}")
    
    except Exception as e:
        print(f"Exception caught is {e}")


if __name__ == "__main__":
    host = "bandit.labs.overthewire.org"
    port = "2220"
    user = "bandit0"
    pswd = "bandit0"
    cmmd = "cat /etc/hosts"
    ssh_linuxcmd(host, port, user, pswd, cmmd)