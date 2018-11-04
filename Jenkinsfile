def containername

pipeline {
    agent any
    stages {
        stage('Check Docker') {
            steps {
                bat 'docker version'
            }
        }
        stage('remove container') {
            steps {
					bat 'docker rm compiler'		
            }
        }
		stage('start container') {
            steps {
					bat 'docker run -it --name compiler -h compilerhost --r always -p 8000:80 -v K:\Docker\dockervol:c:\dockervol microsoft/windowsservercore:1709'		
            }
        }
        stage('Get In Container') {
            steps{
					bat 'hostname'
            }
			steps{
                script {
                         bat 'docker exec -i compiler powershell -c c:/dockervol/abc.bat'
                }
            }    
        }
    }
}