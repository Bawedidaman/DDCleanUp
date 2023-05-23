import paramiko

def execute_command(hostname, username, password, command, command2):
    # Create an SSH client
    client = paramiko.SSHClient()
    # Automatically add the client's hostname and key to the local system's known_hosts file
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the remote host
        client.connect(hostname, username=username, password=password)

        # Execute the command
        stdin, stdout, stderr = client.exec_command(command)
#        stdin, stdout, stderr = client.exec_command(command2)
        

        # Read the output from the command
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')

        # Print the output and error messages
        print('Output:\n', output)
        print('Error:\n', error)

    finally:
        # Close the connection
        client.close()

# Provide the details of the remote Linux client
hostname = 'hostname'
username = 'username'
password = 'password'
command1 = 'cd Jenkins && ls' #rm -rf *'  # Replace with the command you want to execute
command2 = 'ls'
# Call the function to execute the command on the remote Linux client
execute_command(hostname, username, password, command1, command2 )
