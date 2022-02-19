import winrm
import paramiko
"""
protocol = winrm.protocol.protocol(endpoint="http://2022:5985//wsman",
                                   transport="ntlm",
                                   username="",
                                   password="",
                                   server_cert_verification="ignore",)
shell=protocol.openshell()
command=protocol.run_command(shell,"ipconfig")
output,error,status=protocol.get_command_output(shell,command)
print(status)
print(error)
print(output)
"""

"""
ssh =paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="",username="",password="",port=)
sftp_client=ssh.open_sftp()
sftp_client.get("remote filepath","local filepath")
print(sftp_client.getcwd())
sftp_client.close()

sftp_client=ssh.open_sftp()
sftp_client.put("local filepath","remote filepath")
print(sftp_client.getcwd())
sftp_client.close()
"""


