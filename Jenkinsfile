pipeline {
    agent any
    parameters {
        string(name: 'username', defaultValue: '', description: 'Git username')
        password(name: 'password', defaultValue: '', description: 'Git password')
        string(name: 'arg1', defaultValue: '', description: 'First argument for Python script')
        string(name: 'arg2', defaultValue: '', description: 'Second argument for Python script')
        string(name: 'arg3', defaultValue: '', description: 'Third argument for Python script')
    }
    stages {
        stage ('Edit CSV file') {
            steps {
                // Run the Python script that edits the CSV file with the given arguments
                sh "python edit_data.py ${params.arg1} ${params.arg2} ${params.arg3}"
            }
        }
        stage ('Push changes to Git') {
            steps {
                // Configure Git user name and email
                sh "git config user.name ${params.username}"
                sh "git config user.email ${params.username}@example.com"
                // Add and commit the edited CSV file
                sh "git add data.csv"
                sh "git commit -m 'Edited CSV file with Jenkins job'"
                // Push the changes to the same branch with the given username and password
                sh "git push https://${params.username}:${params.password}@${env.GIT_URL}"
            }
        }
    }
}
